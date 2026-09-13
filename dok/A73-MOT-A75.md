# A73 mot A75 — konsistenstest per sone

> **Deponert arbeidsdokument.** Skrevet under arbeidet med `psrtype-samfyring` og
> `kapregister`, og deponert her uendret bortsett fra at lokale filstier er erstattet
> med relative navn. Utsagn om publiseringsstatus, åpne løkker og «ingen DOI» gjelder
> skrivetidspunktet, ikke i dag. Tallene er dem manuskriptene viser til.


Kjørt 2026-09-12. **Ingen endring i `psrtype-samfyring`.** Ingen commit, ingen push.

Rådata og sjekksummer: `MANIFEST-A73-MOT-A75.md`. Kode: `a73_mot_a75.py`,
`a73_mot_a75_endelig.py`. Rå utskrift: `a73-mot-a75-dom.txt`.

---

## Premisset holdt ikke: A75 måtte hentes

A73-siden lå komplett på disk. **A75 lå bare for PL, NL og CZ 2023** — 36 månedsdokumenter.
For FI, ES, DK, GB, AT, BE, IT og PT fantes ingen A75. Testen kunne ikke kjøres uten, så
A75 ble hentet for de manglende sonene: **185 månedsdokumenter**, `a75-soner/`. Det er samme
kilde og samme endepunkt som før, og det er den eneste hentingen i denne kjøringen.

---

## Metoden

Per sone, år og `psrType`: summer A73 over alle enheter og alle timer, og sammenlign med A75s
kolonne for samme type.

A73 dekker bare genereringsenheter på 100 MW eller mer, så **A73 ≤ A75 er normalen og ikke et
funn**. Funnet er kolonner der A73-summen **overstiger** A75 — da må minst én A73-enhet ligge i
en annen A75-kolonne.

Begge sider reduseres til `(psrType, dato, time) → MWh`. **A75 utelater timer med null**, så
manglende timer leses som null på begge sider; årssummen er sammenligningen.

### Tre kriterier, alle fastsatt før dommen

**K1 — kildekolonne.** A73-summen overstiger A75-kolonnen.

**K2 — vedvarenhet.** A73 > 1,02 × A75 i mer enn **57,0 %** av timene. Terskelen er ikke valgt,
den er **målt**: maksimum blant de 121 parene der A73 ≤ A75 og det altså ikke er noe å finne.
Fordelingen der er median **0,0 %**, 90-persentil **6,1 %**, maksimum **57,0 %**. To par ligger
over 50 %, ingen over 90 %.

**K3 — tilskrivning, og den skal være entydig.** Nøyaktig **én** (enhet, målkolonne) skal lukke
90–110 % av et *eksisterende* gap i målkolonnen og lande innenfor 2 %.

Kravet om entydighet er ikke pynt. Uten det «forklarer» **sju** Bełchatów-enheter det samme
gapet på 2 100 GWh i PLs gasskolonne, fordi de alle er rundt 2 000 GWh. Et gap som mange
enheter passer like godt i, er ikke tilskrevet noen av dem.

Kravet om at gapet skal være *eksisterende* er heller ikke pynt. Uten det «avstemmer» Solina H1
på 68 GWh inn i en brunkullkolonne på 31 473 GWh med 0,775 % avvik — enhver liten enhet gjør
det i en stor kolonne.

### Hva som ikke er et funn

- **Enheter under 100 MW.** De forklarer alltid A73 < A75.
- **A73 er ufullstendig per enhet og time** selv når dokumentet finnes. Tsjekkisk kjernekraft
  gir A73/A75 = 0,801 med alle seks enheter til stede. Testen er ensidig og tåler det.
- **Tidsforskyvning.** Testet: for PL `B02` er middelavviket 2,70 % ved lag 0, 6,95 % ved −1 t
  og 6,97 % ved +1 t. **Rasteret er justert riktig.**

---

## Referansetilfellet: Amer 9

Reproduseres før noe annet teller.

| | GWh 2023 |
|---|---:|
| A73 `B05` (Maasvlakte 3, Eemshaven A, Eemshaven B, NLROTTETH__1) | 9 241,7 |
| A73 `Amer 9`, ført `B01 Biomass` | 2 650,6 |
| **sum** | **11 892,4** |
| A75 `B05 Fossil Hard coal` | **11 897,1** |
| **avvik** | **−0,040 %** |
| uten Amer 9 | −22,32 % |

Gapet i A75s kullkolonne er **2 655,4 GWh**. Amer 9 er **2 650,6 GWh** og lukker **99,8 %** av
det. **Metoden reproduserer referansetilfellet.**

---

## Resultatet

**130 (sone, psrType)-par testet** over tolv sone-år: FI 2021–2024, PL 2023, NL 2023, CZ 2023,
ES 2023, DK kontrollområde 2023 og 2019+2021, GB 1.1.–31.5.2021, AT, BE, IT og PT 2023.

**Ni par har A73 > A75. Ett består alle tre kriteriene.**

| Sone | psrType | A73 GWh | A75 GWh | ratio | vedvarenhet | K2 | K3 | dom |
|---|---|---:|---:|---:|---:|:--|:--|---|
| **NL 2023** | **B01 Biomass** | **2 650,6** | **190,6** | **13,904** | **70,3 %** | ja | **1 par** | **TREFF** |
| ES 2023 | B14 Nuclear | 50 788,4 | 19 980,3 | 2,542 | 88,9 % | ja | 0 | A75-defekt |
| ES 2023 | B05 Fossil Hard coal | 3 733,6 | 2 174,2 | 1,717 | 80,3 % | ja | 0 | A75-defekt |
| PL 2023 | B12 Hydro Reservoir | 176,7 | 133,3 | 1,325 | 38,3 % | nei | 0 | støy |
| DK-CA 2023 | B04 Fossil Gas | 2 527,8 | 1 934,7 | 1,307 | 70,4 % | ja | 0 | **uforklart** |
| GB 2021 | B10 Hydro Pumped | 871,0 | 764,4 | 1,139 | 64,8 % | ja | 0 | forklart, se under |
| NL 2023 | B14 Nuclear | 3 579,4 | 3 500,7 | 1,022 | 22,4 % | nei | 0 | støy |
| PL 2023 | B02 Lignite | 31 649,1 | 31 473,1 | 1,006 | 41,9 % | nei | 8 | støy |
| FI 2021-2024 | B14 Nuclear | 105 532,2 | 105 389,7 | 1,001 | 10,5 % | nei | 0 | støy |

**Svaret på spørsmålet er derfor: Amer 9 står alene.** Ingen annen enhet i de tolv sone-årene
viser en tilskrivbar uenighet mellom A73 og A75. Det skal stå som det.

### ES er en datafeil i A75, ikke en feilplassering

Timeverdier for spansk kjernekraft 15. juni 2023, A75 mot A73:

```
time   A73        A75            time   A73        A75
  0   5 043,7      —              12   5 016,7    1 255,0
  5   3 987,2    1 259,0          15   5 010,1    3 754,0
  7   5 033,7    1 258,0          18   5 014,1    2 505,0
 10   5 022,9    1 255,0          21   5 064,1    5 074,0
 11   5 021,3    1 254,0          22   5 112,0    5 125,0
```

A73 ligger stabilt på ~5 000 MW, som stemmer med spansk kjernekraft. **A75 hopper mellom 1 254
og 5 125 MW og mangler sju av døgnets 24 timer.** Ingen enkelt enhet forklarer noe her, og
avviket er en publiseringsfeil i A75, ikke en tilordning.

### DK kontrollområde står uforklart

A75 for kontrollområdet er **ikke** defekt — den er lik DK1 + DK2 på alle typer:

| type | A75 DK-CA | A75 DK1 + DK2 |
|---|---:|---:|
| B19 Wind Onshore | 10 827,2 | 10 826,4 |
| B18 Wind Offshore | 8 453,6 | 8 452,5 |
| B01 Biomass | 3 764,8 | 3 763,3 |
| B05 Fossil Hard coal | 3 329,7 | 3 328,1 |
| **B04 Fossil Gas** | **1 934,7** | **1 933,7** |

Overskuddet på **593,1 GWh** i gasskolonnen er reelt og vedvarende (70,4 % av timene), men lar
seg ikke tilskrive én enhet. De fire danske gassenhetene i A73 er Avedøreværket 1 (843,6 GWh) og
2 (1 235,8), Skærbækværket 3 (260,1) og Silkeborgværket (188,2). Å flytte Avedøre 2 til
biomassekolonnen lukker ikke gapet der — DK har for mye biomasse under terskelen. **Uavklart.**

---

## Det testen fant på veien: Lynemouth

GB `B10 Hydro Pumped` ble flagget av K1 og K2, men fant ingen målkolonne — fordi A73 og A75 er
**enige**. Uenigheten er mellom ENTSO-E og det britiske registeret.

Tre enheter bærer `B10 Hydro Pumped Storage` i A73 sammen med Cruachan. Over de samme 2 519
timene:

| | GWh | MW i 14.1.B | brukstid | timer med produksjon |
|---|---:|---:|---:|---:|
| `LNMTH-1/-2/-3` | **803,5** | 399 | **79,9 %** | 2 519 av 2 519 |
| `CRUA-1…-4` | 67,5 | 440 | **6,1 %** | 987 av 2 519 |
| `DRAXX` (biomasse) | 4 281,2 | 3 885 | 43,7 % | 2 508 av 2 519 |

**To anlegg i samme produksjonstype, med tretten ganger forskjell i brukstid.** 79,9 % over fem
måneder er termisk grunnlast, ikke pumpekraft.

ENTSO-Es eget kapasitetsregister (14.1.B) fører `48WSTN0000LNMTHP` — `LNMTH`, 399 MW — som
**`Hydro Pumped Storage`** i alle fire årganger på disk: **2017, 2018, 2019 og 2025**.

Elexons offentlige BM-enhetsregister, slått opp på **samme EIC**:

```json
{"nationalGridBmUnit": "LNMTH-1", "elexonBmUnit": "E_LYNE1",
 "eic": "48W00000LNMTH-1R", "fuelType": "BIOMASS",
 "bmUnitName": "LYNEMOUTH GENERATOR 1",
 "leadPartyName": "EP UK INVESTMENTS LIMITED",
 "generationCapacity": "140.000", "gspGroupName": "Northern"}
```

Samme for `LNMTH-2` (`E_LYNE2`, GENERATOR 2) og `LNMTH-3` (`E_LYNE3`, GENERATOR 3), begge
`BIOMASS`. **Kontroll:** samme register fører `48W000000CRUA-16` som `fuelType` **`PS`**
(Drax Pumped Storage Limited) — registeret skiller de to, og har 18 `BIOMASS` mot 16 `PS` blant
3 071 enheter.

**Lynemouth — en biomassekonvertering på 399 MW — er ført som pumpekraftverk i ENTSO-E, i minst
åtte årganger, i både A73 og kapasitetsregisteret.** Koblingen er gjort på EIC, ikke på navn.

Dette er ikke samfyring og ikke en A73/A75-uenighet. Det er en tredje feiltype: **riktig enhet,
feil produksjonstype, konsistent på tvers av ENTSO-Es egne produkter**, og i strid med det
nasjonale registeret.

---

## Hva dette betyr

**For spørsmålet som ble stilt:** A73 og A75 er i hovedsak avledet av samme tilordning. Ett
tilfelle — Amer 9 — bærer en tilordning den andre ikke deler. **Ingen flere finnes i de tolv
sone-årene.** Amer 9 er enkeltstående, og det skal stå slik i `psrtype-samfyring`.

**For funnets ramme:** Lynemouth viser at feil produksjonstype ikke alltid er en
flerbrenselssak. Her er anlegget enbrensel og etiketten likevel gal, i en kategori som ikke
engang er termisk. Det hører i etikettaksen — `kapregister`,
[10.5281/zenodo.22722722](https://doi.org/10.5281/zenodo.22722722) — ikke i
`psrtype-samfyring`.

**To løse tråder, ført som uavklart:** DKs gasskolonne (593,1 GWh, vedvarende, utilskrevet) og
ESs A75-publisering (kjernekraft og steinkull, sannsynlig publiseringsfeil, ikke undersøkt
videre her).
