# -*- coding: utf-8 -*-
"""Reviderer A03-tellingen: hvor mange tidsserier er trappekurve, og hvor mange
perioder har hull i posisjonene.

curveType A03 betyr at en manglende posisjon i en Period ikke er manglende data —
verdien fra forrige oppgitte posisjon HOLDER til neste oppgitte posisjon. En parser
som bare summerer de punktene som staar oppfoert, underrapporterer derfor energi i
hver serie med hull, og ikke ensartet.

Hull-kriteriet her er det samme som i den foerste tellingen: posisjonene er ikke
sammenhengende 1..n. Det fanger ikke en avkuttet hale (posisjon 1..n der n er
mindre enn antall intervaller i perioden); den telles separat.

Raadata foelger ikke med i dette datasettet. Sett ARBEIDSROT til katalogen som
inneholder a75-avvik/ og finland/, eller kjoer fra den katalogen.
"""
import os, glob, pathlib, datetime as dt
import xml.etree.ElementTree as ET
from collections import Counter

ROT = pathlib.Path(os.environ.get("ARBEIDSROT", "."))
OPPL = {'PT15M': 15, 'PT30M': 30, 'PT60M': 60, 'P1D': 1440}


def _tid(s):
    return dt.datetime.strptime(s, '%Y-%m-%dT%H:%MZ')


def revider(moenster, navn):
    ct = Counter(); perioder = 0; hull = 0; hale = 0; filer = 0
    for f in sorted(glob.glob(str(ROT / moenster))):
        try:
            rot = ET.parse(f).getroot()
        except ET.ParseError:
            continue
        if 'Acknowledgement' in rot.tag:
            continue
        filer += 1
        ns = {'g': rot.tag.split('}')[0].strip('{')}
        for ts in rot.findall('.//g:TimeSeries', ns):
            ct[ts.findtext('g:curveType', None, ns)] += 1
            for per in ts.findall('g:Period', ns):
                perioder += 1
                pos = sorted(int(p.findtext('g:position', '1', ns))
                             for p in per.findall('g:Point', ns))
                if not pos:
                    continue
                if pos != list(range(1, max(pos) + 1)):
                    hull += 1
                ti = per.find('g:timeInterval', ns)
                mins = OPPL.get(per.findtext('g:resolution', None, ns) or 'PT60M', 60)
                n = max(1, round((_tid(ti.findtext('g:end', None, ns))
                                  - _tid(ti.findtext('g:start', None, ns))
                                  ).total_seconds() / 60 / mins))
                if max(pos) < n:
                    hale += 1
    print(f"{navn:<22} filer {filer:4d}  curveType {dict(ct)}  "
          f"perioder {perioder}, hull i posisjonene {hull}, avkuttet hale {hale}")


if __name__ == '__main__':
    revider('finland/anlegg/a73-raw/FI-2021-*.xml', 'A73 FI 2021')
    revider('a75-avvik/a73-gb-dkca/GB-2021-*.xml', 'A73 GB 2021')
    revider('a75-avvik/a75-plnlcz-2023/NL-2023-*.xml', 'A75 NL 2023')
