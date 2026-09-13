# -*- coding: utf-8 -*-
"""A73 mot A75 per sone og psrType, paa NOEYAKTIG de samme timene.

A73 dekker bare genereringsenheter >= 100 MW, saa A73 <= A75 er normalen og ikke
et funn. Funnet er kolonner der A73-summen OVERSTIGER A75 — da maa minst en
A73-enhet ligge i en annen A75-kolonne.

Begge sider reduseres til (psrType, dato, time) -> MWh, og sammenligningen
bruker bare timer som finnes paa BEGGE sider for den psrType-en. Det fjerner
A75s hull, som ellers gir falske overskudd (ES B14 mangler 63 % av timene).
"""
import glob, datetime as dt
import xml.etree.ElementTree as ET
from collections import defaultdict

KODE={'B01':'Biomass','B02':'Lignite','B03':'Coal-derived gas','B04':'Fossil Gas',
 'B05':'Fossil Hard coal','B06':'Fossil Oil','B07':'Oil shale','B08':'Fossil Peat',
 'B09':'Geothermal','B10':'Hydro Pumped','B11':'Hydro RoR','B12':'Hydro Reservoir',
 'B13':'Marine','B14':'Nuclear','B15':'Other renewable','B16':'Solar','B17':'Waste',
 'B18':'Wind Offshore','B19':'Wind Onshore','B20':'Other','B25':'Energy storage'}
OPPL={'PT15M':15,'PT30M':30,'PT60M':60}

def _tid(s): return dt.datetime.strptime(s.replace('Z','+0000'), '%Y-%m-%dT%H:%M%z')

def les(katalog, prefiks, aar=None):
    """-> time[(psr,dato,time)]=MWh ; enhet[(psr,eic,dato,time)]=MWh ; navn ; nfil"""
    time_=defaultdict(float); enhet=defaultdict(float); navn={}; nfil=0
    for f in sorted(glob.glob(f"{katalog}/{prefiks}-*.xml")):
        try: rot=ET.parse(f).getroot()
        except Exception: continue
        if 'Acknowledgement' in rot.tag: continue
        nfil+=1
        ns={'g':rot.tag.split('}')[0].strip('{')}
        for ts in rot.findall('.//g:TimeSeries',ns):
            if ts.find('g:inBiddingZone_Domain.mRID',ns) is None: continue
            p=ts.find('.//g:MktPSRType',ns)
            if p is None: continue
            psr=p.findtext('g:psrType',None,ns)
            pr=p.find('.//g:PowerSystemResources',ns)
            eic=pr.findtext('g:mRID',None,ns) if pr is not None else None
            if eic: navn[eic]=pr.findtext('g:name',None,ns)
            for per in ts.findall('g:Period',ns):
                start=_tid(per.findtext('.//g:start',None,ns))
                mins=OPPL.get(per.findtext('g:resolution',None,ns) or 'PT60M',60)
                for pkt in per.findall('g:Point',ns):
                    q=pkt.findtext('g:quantity',None,ns)
                    if q is None: continue
                    pos=int(pkt.findtext('g:position','1',ns))
                    t=start+dt.timedelta(minutes=mins*(pos-1))
                    if aar and t.year not in aar: continue
                    n=(psr, t.date(), t.hour)
                    e=float(q)*mins/60.0
                    time_[n]+=e
                    if eic: enhet[(psr,eic,t.date(),t.hour)]+=e
    return time_, enhet, navn, nfil

def slots(time_):
    s=defaultdict(set)
    for (psr,d,h) in time_: s[psr].add((d,h))
    return s

def test(t73, t75):
    """-> psr -> (A73-sum, A75-sum, antall felles timer)"""
    s73, s75 = slots(t73), slots(t75)
    ut={}
    for psr in set(s73)|set(s75):
        felles = s73.get(psr,set()) & s75.get(psr,set())
        if not felles: 
            ut[psr]=(0.0, 0.0, 0); continue
        a=sum(v for (p,d,h),v in t73.items() if p==psr and (d,h) in felles)
        b=sum(v for (p,d,h),v in t75.items() if p==psr and (d,h) in felles)
        ut[psr]=(a,b,len(felles))
    return ut
