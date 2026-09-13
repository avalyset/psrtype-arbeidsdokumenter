# -*- coding: utf-8 -*-
"""Reproduserer Unnewehr m.fl. (2022) ligning (1) paa deres egne publiserte mellomfiler.

EF(a) = CO2_el(a) / G(a),  CO2_el = VERIFIED_EMISSIONS_2018 - 2 x ALLOCATION_2018
Plausibilitetsbaand fra deres tabell 4 (NREL).  Ingen ny metode.
"""
import csv, pathlib
from collections import defaultdict

import os
# Rotkatalog for raadata. Raadata foelger ikke med i dette datasettet — de er
# re-hentbare fra ENTSO-Es API. Sett ARBEIDSROT til katalogen som inneholder
# a75-avvik/ og finland/, eller kjoer fra den katalogen.
ROT = pathlib.Path(os.environ.get("ARBEIDSROT", "."))
# Unnewehr m.fl. sine egne publiserte mellomfiler. Hentes fra deres repo/Zenodo-post.
U = ROT/"a75-avvik/unnewehr"
G = pathlib.Path(os.environ.get("UNNEWEHR_GEN", str(U/"gen_data_2018.csv")))
BAND = {'gas':(300,1000), 'hard_coal':(675,1700), 'lignite':(675,1700), 'other_fossil':(300,1700)}

def aarssum():
    with open(G, encoding='utf-8') as f:
        r = csv.reader(f); hdr = next(r)
        eics = hdr[1:]; s = [0.0]*len(eics)
        for row in r:
            for i, v in enumerate(row[1:]):
                if v: s[i] += float(v)
    return dict(zip(eics, s))

def enhetsdata():
    d = {}
    for r in csv.DictReader(open(U/"input/unit_data_2018.csv", encoding='utf-8')):
        d[r['']] = dict(navn=r['PowerSystemResourceName'], land=r['MapCode'],
                        typ=r['ProductionTypeName'], mw=float(r['InstalledGenCapacity'] or 0),
                        pu=r['ProductionUnitEIC'])
    return d

def eutl():
    rows = list(csv.reader(open(U/"input/bootom_up_method/verified_emissions_2018_en.csv",
                                encoding='utf-8', errors='replace'), delimiter=';'))
    hdr = rows[13]; ix = {k: i for i, k in enumerate(hdr)}
    # Headeren er forskjoevet i kolonne 1-2 (to navnefelt). Noekkelen er kolonne 3,
    # INSTALLATION_IDENTIFIER; verifisert ved at 428 av 428 match-noekler treffer der.
    KEY = 3
    def tall(x):
        x = (x or '').strip()
        if x in ('', '-1', 'Excluded'): return None
        try: return float(x)
        except ValueError: return None
    d = {}
    for r in rows[14:]:
        if len(r) < len(hdr): continue
        k = (r[0].strip(), r[KEY].strip())
        d[k] = dict(navn=r[1].strip() or r[2].strip(),
                    akt=r[ix['MAIN_ACTIVITY_TYPE_CODE']].strip(),
                    ver=tall(r[ix['VERIFIED_EMISSIONS_2018']]),
                    alloc=tall(r[ix['ALLOCATION_2018']]))
    return d

def kjor():
    gen = aarssum(); ud = enhetsdata(); eu = eutl()
    match = list(csv.DictReader(open(U/"input/matching_ENTSOE_EU_ETS.csv", encoding='utf-8')))
    pr = defaultdict(lambda: dict(g=0.0, enh=[], typer=set(), land=set(), mw=0.0))
    for m in match:
        eg = m['eic_g']; k = (m['EUTL_countrycode'].strip(), m['EUTL_ID'].strip())
        u = ud.get(eg)
        if u is None: continue
        p = pr[k]
        p['g'] += gen.get(eg, 0.0); p['enh'].append((eg, u['navn'])); p['typer'].add(u['typ'])
        p['land'].add(u['land']); p['mw'] += u['mw']
    ut = []
    for k, p in pr.items():
        e = eu.get(k)
        if e is None or e['ver'] is None: continue
        alloc = e['alloc'] or 0.0
        co2_el = e['ver'] - 2*alloc
        ef = (co2_el*1000.0/p['g']) if p['g'] > 0 else None     # tonn->g / MWh->kWh
        typ = sorted(p['typer'])[0] if len(p['typer']) == 1 else '+'.join(sorted(p['typer']))
        b = BAND.get(typ)
        dom = None
        if ef is None or b is None: dom = 'ikke testbar'
        elif ef < b[0]: dom = 'UNDER'
        elif ef > b[1]: dom = 'OVER'
        else: dom = 'innenfor'
        ut.append(dict(eutl=k, navn=e['navn'], akt=e['akt'], land=sorted(p['land'])[0] if p['land'] else '?',
                       typ=typ, mw=p['mw'], gwh=p['g']/1000, ver=e['ver'], alloc=alloc,
                       co2_el=co2_el, ef=ef, dom=dom, n_enh=len(p['enh']),
                       enheter=[n for _, n in p['enh']]))
    return ut
