# Effekten per sone — og årsoppløsningens rekkevidde

> **Deponert arbeidsdokument.** Skrevet under arbeidet med `psrtype-samfyring` og
> `kapregister`, og deponert her uendret bortsett fra at lokale filstier er erstattet
> med relative navn, og bortsett fra de daterte rettelsene som er merket i teksten. Utsagn om publiseringsstatus, åpne løkker og «ingen DOI» gjelder
> skrivetidspunktet, ikke i dag. Tallene er dem manuskriptene viser til.


Kjørt 2026-09-13. **Ingen commit, ingen push.** Kode: `effekt_per_sone.py`, `a73_mot_a75.py`.
Sjekksummer for depotet: `SHA256SUMS`.

---

## 0 — En feil i min egen parsing, funnet under dette arbeidet

**Alle ENTSO-E-seriene har `curveType A03`** — trappekurve, der en manglende posisjon betyr at
forrige verdi holder, ikke at data mangler. Målt: 12 412 av 12 412 tidsserier i FI 2021, og hull
i posisjonene i 4 125 av 6 521 perioder i GB 2021.

> **Rettet ved deponering:** GB-tallet over dekker ikke hele 2021. Globet var
> `GB-2021-0[12]-*.xml` avkortet til de førti første filstiene — 30 innholdsfiler fra januar og
> februar. Tallet reproduserer for den delmengden. Over full dekning er GB 2021
> **14 278 av 23 403** perioder. Se `utskrift/a03-revisjon.txt` og `kode/a03_revisjon.py`.
> FI-tallet, 12 412 av 12 412 tidsserier, gjelder alle 365 døgn og står.

**Parseren jeg skrev 12.09 (`a73_mot_a75.py`) summerte bare de punktene som står oppført.** Den
underrapporterte derfor energi i hver serie med hull. Feilen er rettet; den naive versjonen er
beholdt som `a73_mot_a75_FEIL-naiv.py` for etterprøving.

Feilen er **ikke ensartet** — den avhenger av hvor glisen serien er:

| Enhet | naiv | A03-korrekt | |
|---|---:|---:|---:|
| Alholmens B2, FI 2021 | 633,4 | **664,2** | +4,9 % |
| Seinäjoki B1, FI 2021 | 498,9 | 534,8 | +7,2 % |
| Keljonlahti B1, FI 2021 | 432,1 | 529,5 | **+22,6 %** |

**Kontrollen som avgjorde det:** Finland-arbeidets egen `parse_a73.py` fra 11.09 ga 664,18 GWh
for Alholmens B2 i 2021. Den A03-korrekte reberegningen gir **664,2**. Den eldre parseren var
riktig hele tiden; den jeg skrev i går var ikke.

### Hva som flytter seg i det publiserte

| Publisert tall | Var | Blir | Konklusjon |
|---|---:|---:|---|
| Amer 9-avstemming (`psrtype-samfyring`) | −0,040 % | **−0,251 %** | **står** — uten Amer 9 fortsatt −22,4 % |
| Połaniec, R mot hele produksjonen | 1,005 | **1,006** | står |
| Połaniec, R på biomasseblokken | 0,999 | **1,000** | står |
| Lynemouth snitt/topp (`kapregister`) | 72,3–87,1 % | **73,1–88,2 %** | står, overlapp fortsatt **0** |
| øvrige 150 `B10`-enheter, maks | 34,1 % | **34,3 %** | står, faktor 2,12 → **2,13** |
| Lynemouth brukstid | 79,9 % | **80,9 %** | står (Cruachan 6,1 → 7,4 %) |
| NL karbonintensitet, basis | 552,40 | **551,38** | |
| NL-effekten | −34,64 / −6,27 % | **−34,53 / −6,26 %** | står |

**Ingen konklusjon faller.** Men konsistenstesten endrer seg i sine sekundære rader og bør
rettes i en v1.3:

- **Par med A73 > A75: ni → seks.** De to spanske radene faller ut helt — A03-korreksjonen løfter
  spansk A75 mer enn A73, så kolonnene ikke lenger overstiges.
- **GB `B10` faller fra «annen akse» til støy** (vedvarenhet 64,8 % → 56,3 %, under terskelen).
- **Støygulvet: maksimum 57,0 % → 54,7 %.** Terskelen 57,0 % som står i README-en er utledet av
  den naive kjøringen og er nå konservativ, men ikke lenger «det målte maksimum».
- **Amer 9 er fortsatt eneste treff**, og entydigheten er uendret.

Rettelsen gjør testen renere, ikke svakere. **Den bør publiseres som v1.3 med egen merknad.**

---

## 1 — Effekten per sone

**Basis:** A75 for sonen og året, summert time for time med A03-ekspansjon. Faktorsett:
codecarbons `carbon_intensity_per_source.json` — kull og torv 995, gass 743, olje 816,
«fossil» 635, kjerne 29, sol 48, vind/vann 26, **biomasse og avfall 0** gCO₂eq/kWh.

**Korreksjonen** flytter dokumentert biomasse-elektrisitet fra kildekoden til `B01`.

| Sone | A75 total | CI som den står | korrigert | Δ g/kWh | Δ % | flyttet | andel av kildekolonnen |
|---|---:|---:|---:|---:|---:|---:|---:|
| **NL 2023** | 108 789,1 | **551,38** | 516,85 | **−34,53** | **−6,26 %** | 3 775,3 | 31,52 % av `B05` |
| **FI 2021** | 63 732,3 | **185,58** | 180,73 | **−4,85** | **−2,61 %** | 310,8 | 8,76 % av `B08` |
| **CZ 2023** | 71 553,9 | **433,74** | 432,32 … 428,15 | **−1,42 … −5,59** | **−0,33 … −1,29 %** | 102–402 | 0,41–1,60 % av `B02` |
| **PL 2023** | 153 259,9 | **713,71** | 712,08 | **−1,64** | **−0,23 %** | 252,0 | 0,39 % av `B05` |

### Belegget per sone

**NL — CBS**, *Hernieuwbare energie in Nederland 2023* (2024), tabell 8.3.2, raden `2023*`:
**elektriciteit 13 591 TJ = 3 775,3 GWh** fra medfyrt biomasse. Andelen av A75s kullkolonne blir
**31,52 %**, mot CBS' egne **31 % av den totale energiinnsatsen** i *kolencentrales* — to
uavhengige størrelser som treffer hverandre.

**PL — Enea**, ESG-rapport for 2023: «Produkcja z OZE (**współspalanie** biomasy) [GWh] 309 →
**252**». Ren måling, ingen omregning.

**FI — Alholmens Kraft**, `Ympäristöraportti 2021`, brenselsfordeling for AK 2, ordrett:

| Brensel | MWh | Andel |
|---|---:|---:|
| Turve | 597 784 | 32,07 % |
| **Puu** | **871 819** | **46,78 %** |
| Hiili | 205 838 | 11,04 % |
| REF | 165 610 | 8,89 % |
| Öljy | 12 143 | 0,65 % |
| Peltomassa | 148 | 0,01 % |

A73 fører **664,2 GWh** under `Fossil Peat` for AK 2 i 2021. Flyttet: **46,79 %** (puu +
peltomassa) = **310,8 GWh**.

**FI-tallet bærer den uavklarte tilordningen, og det skal stå.** Tre forbehold:

1. **46,78 % er brenselets andel, ikke elektrisitetens.** Å fordele utbyttet proporsjonalt med
   brenselsenergien *er* energimetoden — én av seks allokeringsmetoder, og valget mellom dem er
   eksplisitt utenfor rammen i `psrtype-samfyring/PREREG-v1.md` §4.
2. **REF på 8,89 % er holdt utenfor.** Avfallsbrensel er delvis biogent; å regne det som null
   ville økt korreksjonen. Estimatet er derfor konservativt.
3. **Bare Alholmens har en datert brenselsfordeling.** De fire andre finske `B08`-enhetene i A73
   — Seinäjoki B1, Keljonlahti B1, Toppila B2, Haapavesi B1 — har ingen. **FI-tallet er et gulv
   for ett anlegg, ikke sonens korreksjon.**

**CZ — ČEZ**, `Výroční finanční zpráva 2023`: 309 000 t biomasse ved Hodonín, 256 000 t ved
Poříčí. **Begge anlegg ligger under A73s 100 MW-terskel per genereringsenhet**, så dette er
**utelukkende A75-nivå** — det finnes ingen enhetsdata å rette. Omregningen bruker IPCC 2006
Vol 2 tabell 1.2, `Wood/Wood Waste` NCV 15,6 (7,90–31,0) TJ/Gg, og el-virkningsgrad 15–30 % som
er **en antakelse uten kilde**. Tabellen viser Hodonín alene; Poříčí ligger i `B05` og ville lagt
til i samme størrelsesorden.

---

## 2 — Hva en årlig brenselsandel retter, og hva den ikke retter

**Årssnittet rettes eksakt.** Er den flyttede mengden riktig, er den korrigerte årlige
karbonintensiteten riktig. Det følger av konstruksjonen: Δ = −(EF_kilde − 0) · X / G_år.

**Timesignalet rettes ikke.** En årlig andel `f` pålegger hver time korreksjonen

> Δ(t) = −EF_kilde · f · g_kilde(t) / G(t)

som varierer med hvor mye av timens produksjon som kommer fra kildetypen. Målt:

| Sone | Δ år | min | p05 | median | p95 | maks | timer uten korreksjon |
|---|---:|---:|---:|---:|---:|---:|---:|
| **NL 2023** | −34,53 | **−147,10** | −76,61 | −32,66 | −0,00 | 0,00 | **10,9 %** |
| **FI 2021** | −4,85 | −10,32 | −8,32 | −4,42 | −1,08 | −0,74 | 0,0 % |
| **CZ 2023** (høy) | −5,59 | −8,41 | −7,27 | −5,62 | −3,18 | −2,00 | 0,0 % |
| **PL 2023** | −1,64 | −2,42 | −2,12 | −1,65 | −1,17 | −0,72 | 0,0 % |

**I Nederland spenner den pålagte timekorreksjonen fra −147,10 til null**, og **10,9 % av årets
timer får ingen korreksjon i det hele tatt** fordi kullkolonnen er tom da. Et enkelt årstall er
altså ikke én korreksjon — det er en korreksjon som allerede varierer med en faktor fire mellom
p05 og årssnittet.

### Restfeilen, tallfestet

Den virkelige samfyringsandelen varierer time for time. Kaller vi den `f(t)`, er restfeilen etter
en årlig andel

> Δ_rest(t) = −EF_kilde · (f(t) − f) · g_kilde(t) / G(t)

**Den energiveide årsmiddelverdien er null per konstruksjon** — årssnittet er fortsatt riktig.
Det som står igjen er en tidsfeil, og den skalerer lineært med hvor mye `f(t)` varierer:

| Sone | std(Δ(t)) | std / \|Δ år\| | restfeil ved ±25 % variasjon i `f(t)` | ved ±50 % |
|---|---:|---:|---:|---:|
| **NL 2023** | **25,45** | **0,74** | **± 6,36 g/kWh** | **± 12,73 g/kWh** |
| **FI 2021** | 2,14 | 0,44 | ± 0,54 | ± 1,07 |
| **CZ 2023** | 1,24 | 0,22 | ± 0,31 | ± 0,62 |
| **PL 2023** | 0,30 | 0,18 | ± 0,07 | ± 0,15 |

*Rettet 2026-11-06 (v1.0.1): CZ-raden var regnet ved 252 GWh i stedet for øvre grense 402 GWh; verdiene over er fra `cz_std.txt` i MS-2 v1.2 (10.5281/zenodo.24016061).*

**Tabellen over timekorreksjonen *er* tabellen over restfeil per enhet relativ variasjon.** Det
krever ingen ny antakelse: varierer samfyringsandelen med ±50 % relativt gjennom året, er
restfeilen i Nederland ett standardavvik på **±12,73 gCO₂eq/kWh** — over en tredel av selve
korreksjonen.

**Og variasjonen i `f(t)` er ikke målt av noen.** Det er hele poenget: en årlig andel er det RED-II
faktisk gir ([LITTERATUR-FORSLAG.md](LITTERATUR-FORSLAG.md) §4 — massebalanse «over an
appropriate period of time», offentliggjøring «on an annual basis» per brenselsleverandør), og
den lukker nivåfeilen, ikke tidsfeilen.

---

## 3 — Hva forslaget da kan hevde

**Det retter:** den årlige karbonintensiteten per sone, eksakt, for et dokumentert anlegg.
I Nederland **−34,5 gCO₂eq/kWh, −6,3 %**. Det retter også kapasitetsregisteret, som er
årsbasert av natur.

**Det retter ikke:** timesignalet, som er det dynamiske utslippsfaktorer er til for. Restfeilen
er null i årsmiddel og har standardavvik **0,74 × korreksjonen** i Nederland — altså er
tidsfeilen av samme størrelsesorden som selve korreksjonen når samfyringsandelen varierer
merkbart.

**Det er forslagets egen begrensning, og den er tallfestet her framfor av en fagfelle.**
Å be om timesoppløsning ville lukket den, men det følger ikke av RED-II og kan ikke antas.
Å be om årsoppløsning er billig, belagt og virker — for nivået.
