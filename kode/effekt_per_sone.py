# -*- coding: utf-8 -*-
"""Karbonintensitet per sone, aarlig og time for time, foer og etter brenselskorreksjon.

Aarssnittet rettes eksakt av en aarlig brenselsandel. Timesignalet gjoer det ikke:
korreksjonen per time skalerer med kildetypens andel den timen, og den andelen
varierer. Skriptet tallfester begge deler.
"""
import sys, pathlib, statistics
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from a73_mot_a75 import les, KODE

EF = {'B01':0,'B02':995,'B03':995,'B04':743,'B05':995,'B06':816,'B07':995,'B08':995,
      'B09':38,'B10':26,'B11':26,'B12':26,'B13':26,'B14':29,'B15':26,'B16':48,
      'B17':0,'B18':26,'B19':26,'B20':635,'B25':0}
import os
# Rotkatalog for raadata. Raadata foelger ikke med i dette datasettet — de er
# re-hentbare fra ENTSO-Es API. Sett ARBEIDSROT til katalogen som inneholder
# a75-avvik/ og finland/, eller kjoer fra den katalogen.
ROT = pathlib.Path(os.environ.get("ARBEIDSROT", "."))
A = ROT/"a75-avvik"

def last(kat, pre, aar):
    t,_,_,n = les(str(A/kat), pre, aar)
    time_=defaultdict(dict); tot=defaultdict(float)
    for (p,d,h),v in t.items():
        time_[(d,h)][p]=time_[(d,h)].get(p,0.0)+v; tot[p]+=v
    return time_, dict(tot), n

def ci(mix): 
    g=sum(mix.values())
    return (sum(v*EF.get(p,635) for p,v in mix.items())/g, g) if g>0 else (0.0,0.0)

def analyser(navn, kat, pre, aar, kilde, X, kildetekst):
    time_, tot, n = last(kat,pre,aar)
    base, G = ci(tot)
    m = dict(tot); m[kilde]=m[kilde]-X*1000; m['B01']=m.get('B01',0.0)+X*1000
    korr, _ = ci(m)
    f = X*1000/tot[kilde]                      # aarlig andel av kildetypen
    d_aar = korr-base
    # timevis: korreksjonen den timen, gitt konstant aarlig andel f
    dt=[]
    for (d,h),mix in time_.items():
        g=sum(mix.values())
        if g<=0: continue
        dt.append(-(EF[kilde]-EF['B01'])*f*mix.get(kilde,0.0)/g)
    dt.sort()
    return dict(navn=navn, dok=n, timer=len(dt), G=G/1000, base=base, korr=korr,
                d_aar=d_aar, d_pst=100*d_aar/base, X=X, f=f, kilde=kilde,
                src_tot=tot[kilde]/1000, kildetekst=kildetekst,
                t_min=dt[0], t_p05=dt[int(.05*len(dt))], t_med=statistics.median(dt),
                t_p95=dt[int(.95*len(dt))], t_max=dt[-1],
                t_null=sum(1 for x in dt if x>-0.01)/len(dt),
                t_over=sum(1 for x in dt if x < d_aar)/len(dt))
