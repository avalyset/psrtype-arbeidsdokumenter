# -*- coding: utf-8 -*-
"""Endelig konsistenstest A73 mot A75. Tre kriterier, alle maalt foer bruk.

 K1 kildekolonne: A73-summen overstiger A75-kolonnen for samme psrType.
 K2 vedvarenhet : A73 > 1,02 x A75 i mer enn 54,7 % av timene. Terskelen er
                  maksimum blant 124 par uten mistanke (median 0,0 %).
 K3 tilskrivning: NOEYAKTIG EN (enhet, maalkolonne) lukker 90-110 % av et
                  eksisterende gap i maalkolonnen og lander innenfor 2 %.
                  Uten unikhet er tilskrivningen ikke identifisert.
"""
import sys, pathlib, statistics
from collections import defaultdict
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from a73_mot_a75 import les, KODE

import os
# Rotkatalog for raadata. Raadata foelger ikke med i dette datasettet — de er
# re-hentbare fra ENTSO-Es API. Sett ARBEIDSROT til katalogen som inneholder
# a75-avvik/ og finland/, eller kjoer fra den katalogen.
ROT = pathlib.Path(os.environ.get("ARBEIDSROT", "."))
H=ROT; A=H/"a75-avvik"
VEDV_TERSKEL=0.547; LUKKE=(0.90,1.10); LANDING=0.02
SONER=[('FI 2021-2024',[H/"finland/anlegg/a73-raw"],'FI',A/"a75-soner",'FI',(2021,2022,2023,2024)),
 ('PL 2023',[A/"a73-plnlcz-sensus"],'PL',A/"a75-plnlcz-2023",'PL',(2023,)),
 ('NL 2023',[A/"a73-plnlcz-sensus"],'NL',A/"a75-plnlcz-2023",'NL',(2023,)),
 ('CZ 2023',[A/"a73-plnlcz-sensus"],'CZ',A/"a75-plnlcz-2023",'CZ',(2023,)),
 ('ES 2023',[A/"a73-es-sensus"],'ES',A/"a75-soner",'ES',(2023,)),
 ('DK-CA 2023',[A/"a73-gb-dkca"],'DK-CA',A/"a75-soner",'DK-CA',(2023,)),
 ('DK-CA 2019+21',[A/"a73-aatte-prove"],'DK-CA',A/"a75-soner",'DK-CA',(2019,2021)),
 ('GB 2021',[A/"a73-gb-dkca"],'GB',A/"a75-soner",'GB',(2021,)),
 ('AT 2023',[A/"a73-soner"],'AT',A/"a75-soner",'AT',(2023,)),
 ('BE 2023',[A/"a73-soner"],'BE',A/"a75-soner",'BE',(2023,)),
 ('IT 2023',[A/"a73-soner"],'IT',A/"a75-soner",'IT',(2023,)),
 ('PT 2023',[A/"a73-soner"],'PT',A/"a75-soner",'PT',(2023,))]

def sone(kat,pre,k75,p75,aar):
    t73=defaultdict(float); e73=defaultdict(float); n73={}; f73=0
    for k in kat:
        a,b,c,f=les(str(k),pre,aar)
        for kk,v in a.items(): t73[kk]+=v
        for kk,v in b.items(): e73[kk]+=v
        n73.update(c); f73+=f
    t75,_,_,f75=les(str(k75),p75,aar)
    A73=defaultdict(float); A75=defaultdict(float); ENH=defaultdict(float)
    for (p,d,h),v in t73.items(): A73[p]+=v
    for (p,d,h),v in t75.items(): A75[p]+=v
    for (p,e,d,h),v in e73.items(): ENH[(p,e)]+=v
    timer=defaultdict(set)
    for (p,d,h) in t73: timer[p].add((d,h))
    for (p,d,h) in t75: timer[p].add((d,h))
    vedv={}
    for p,T in timer.items():
        vedv[p]=sum(1 for (d,h) in T if t73.get((p,d,h),0.)>1.02*t75.get((p,d,h),0.))/len(T)
    return A73,A75,ENH,n73,vedv,timer,f73,f75

def tilskriv(A73,A75,ENH,n73,psr):
    par=[]
    for (p,e),u in ((k,v) for k,v in ENH.items() if k[0]==psr):
        if A73[psr]-u > A75[psr]: continue
        for q in A75:
            if q==psr or A75[q]<=0: continue
            gap=A75[q]-A73.get(q,0.0)
            if gap<=0: continue
            l=u/gap; land=(A73.get(q,0.0)+u)/A75[q]-1
            if LUKKE[0]<=l<=LUKKE[1] and abs(land)<=LANDING:
                par.append((n73.get(e) or e, u, q, gap, l, land))
    return par

if __name__=="__main__":
    alle=[]; rene=[]
    for et,kat,pre,k75,p75,aar in SONER:
        A73,A75,ENH,n73,vedv,timer,f73,f75 = sone(kat,pre,k75,p75,aar)
        for p in sorted(set(A73)|set(A75)):
            if A75.get(p,0)<=0: continue
            r=A73.get(p,0)/A75[p]
            rad=dict(sone=et,psr=p,a=A73.get(p,0),b=A75[p],r=r,v=vedv.get(p,0),t=len(timer.get(p,())))
            alle.append(rad)
            if r<=1.0: rene.append(rad); continue
            rad['par']=tilskriv(A73,A75,ENH,n73,p)
    v=[x['v'] for x in rene]
    print(f"STØY: {len(rene)} par med A73 <= A75.  vedvarenhet median {statistics.median(v):.1%},"
          f" 90-pst {sorted(v)[int(.9*len(v))]:.1%}, MAKS {max(v):.1%}  -> terskel {VEDV_TERSKEL:.1%}")
    print(f"Totalt {len(alle)} (sone, psrType)-par testet.\n")
    print(f"{'sone':<15}{'psrType':<22}{'A73 GWh':>11}{'A75 GWh':>11}{'ratio':>8}{'vedv':>8}  K2  K3  dom")
    for x in sorted([y for y in alle if y['r']>1.0], key=lambda z:-z['r']):
        par=x.get('par',[])
        k2 = x['v']>VEDV_TERSKEL
        k3 = len(par)==1
        dom = 'TREFF' if (k2 and k3) else ('A75-defekt' if k2 else 'støy')
        print(f"  {x['sone']:<13}{x['psr']+' '+KODE[x['psr']]:<22}{x['a']/1000:11,.1f}{x['b']/1000:11,.1f}"
              f"{x['r']:8.3f}{x['v']:8.1%}  {'ja' if k2 else 'nei':<4}{(str(len(par))+' par'):<5} {dom}")
        for nm,u,q,gap,l,land in par[:3]:
            print(f"        {nm} {u/1000:,.1f} GWh -> {q} {KODE[q]}: gap {gap/1000:,.1f}, lukker {l:.1%}, lander {land:+.3%}")
