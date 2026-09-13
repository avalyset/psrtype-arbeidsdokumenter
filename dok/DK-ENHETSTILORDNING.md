# DK — bokfører A75 hele enheten under hovedbrenselet, som i Finland?

> **Deponert arbeidsdokument.** Skrevet under arbeidet med `psrtype-samfyring` og
> `kapregister`, og deponert her uendret bortsett fra at lokale filstier er erstattet
> med relative navn. Utsagn om publiseringsstatus, åpne løkker og «ingen DOI» gjelder
> skrivetidspunktet, ikke i dag. Tallene er dem manuskriptene viser til.


**12.09.2026.** Alt regnet fra materiale som alt lå på disk. Ingen nye kilder hentet.

---

## 1 · A73 finnes ikke for Danmark

Bekreftet i `kapregister/adr/0001-datapunktvalg.md`: `NoMatchingDataError` for DK1, DK2 og
landsdomenet `10Y1001A1001A65H`, også på **2018-02-27** — dagen `electricitymaps-contrib#1161`
lastet ned per-enhet-data. Positiv kontroll samme dag og samme kall: **FR 151 enheter, NL 41**.

**Enhetstesten som beviste den finske mekanismen kan ikke kjøres på Danmark.** Testen må gå på
sonenivå.

---

## 2 · Brukstidstesten — den avgjør ingenting for DK2

Registrerte DK2-kullenheter i 14.1.B: **Asnæsværket 787 MW + Amagerværket 479 MW = 1 266 MW.**

| År | A75 `Fossil Hard coal` GWh | Brukstid som hel produksjon | Brukstid hvis kolonnen var en 30 %-andel |
|---|---:|---:|---:|
| 2021 | 1 238,5 | 11,2 % | 37,2 % |
| 2022 | 963,9 | 8,7 % | 29,0 % |
| 2023 | 1 079,3 | 9,7 % | 32,4 % |
| 2024 | 1 005,0 | 9,0 % | 30,1 % |
| 2025 | 731,9 | 6,6 % | 22,0 % |

**Begge lesninger er fysisk mulige.** Ingen brukstid nærmer seg 100 %.

**Testen som felte den finske torvandels-lesningen felles ikke noe her.** Den virket i Finland
fordi torvenhetene kjøres hardt — 31–49 % brukstid — slik at en tredobling ble umulig. DK2s
kullenheter kjøres på 7–11 %, og tåler en tredobling uten å bryte fysikken.

**Det skal stå. Testen ble kjørt før noe ble tolket, og den ga ingen dom.**

---

## 3 · Men avkoblingen avgjør det

Energinet `DeclarationProduction`, DK2, `FuelAllocationMethod = Total`, fra `mek-*.csv` på disk.
Kontroll: `Production_MWh` er identisk under `125%`, `200%` og `Total` — allokeringsuavhengig,
som målt i runde to.

| År | **A75 kull** | **Energinet kull** | Forhold | Energinet tre+halm | Energinet avfall | Energinet sum termisk |
|---|---:|---:|---:|---:|---:|---:|
| 2019 | 875,1 | 567,9 | 1,54 | 2 219,2 | 741,2 | 3 528,3 |
| 2020 | 810,2 | 148,8 | 5,4 | 2 218,4 | 728,8 | 3 096,0 |
| 2021 | 1 238,5 | **1,4** | **885** | 4 069,8 | 697,3 | 4 768,5 |
| 2022 | 963,9 | 127,1 | 7,6 | 3 181,0 | 762,4 | 4 070,5 |
| 2023 | 1 079,3 | **0,3** | **3 598** | 3 151,7 | 695,3 | 3 847,3 |
| 2024 | 1 005,0 | **0,0** | **∞** | 3 096,7 | 774,5 | 3 871,3 |

**A75s kullkolonne er fullstendig avkoblet fra faktisk kullforbrenning.** Energinets kulltall
faller fra 567,9 til 0,0 mellom 2019 og 2024. A75s kolonne ligger på 810–1 238 GWh gjennom hele
perioden, uten spor av fallet.

### Og den er en stabil andel av noe annet

| År | A75 kull som andel av Energinets **samlede termiske** produksjon |
|---|---:|
| 2019 | 24,8 % |
| 2020 | 26,2 % |
| 2021 | 26,0 % |
| 2022 | 23,7 % |
| 2023 | 28,1 % |
| 2024 | 26,0 % |

**23,7–28,1 % i seks år, med et gjennomsnitt på 25,8 % og et spenn på 4,4 prosentpoeng.**

En kolonne som var kulltilordnet ville fulgt Energinets kull ned til null. En kolonne som var
*hele* den termiske produksjonen ville ligget på 100 %. **Denne ligger stabilt på omtrent en
fjerdedel — som er den andelen to av DK2s termiske enheter kan forventes å levere.**

**Lesningen som passer: A75s `Fossil Hard coal` for DK2 er Asnæs' og Amagers samlede produksjon,
ført under enhetenes registrerte hovedbrensel.** Det er den finske mekanismen.

**Forbehold, uttrykkelig:** dette er en slutning fra stabilitet og størrelsesorden, ikke en
måling per enhet. **Uten A73 for Danmark finnes det ingen dansk motpart til Alholmens-testen.**
Andelen på ~26 % er ikke uavhengig verifisert mot Asnæs' og Amagers egen produksjon — de tallene
ligger ikke på disk, og oppdraget forbød nye kilder.

---

## 4 · Massebevaringen holder under begge lesninger

| År | A75(kull+bio) | Eng(kull+tre+halm) | **Forhold** | A75(k+b+avfall) | Eng(alt termisk) | **Forhold** |
|---|---:|---:|---:|---:|---:|---:|
| 2019 | 3 111,5 | 2 787,1 | **1,116** | 3 664,7 | 3 528,3 | 1,039 |
| 2020 | 2 580,5 | 2 367,2 | **1,090** | 3 110,1 | 3 096,0 | 1,005 |
| 2021 | 4 345,8 | 4 071,2 | **1,067** | 4 879,5 | 4 768,5 | 1,023 |
| 2022 | 3 317,1 | 3 308,1 | **1,003** | 3 863,1 | 4 070,5 | 0,949 |
| 2023 | 3 304,7 | 3 152,0 | **1,048** | 3 634,3 | 3 847,3 | 0,945 |
| 2024 | 3 316,0 | 3 096,8 | **1,071** | 3 660,1 | 3 871,3 | 0,945 |

**Den publiserte serien 1,00–1,12 reproduseres eksakt** — 1,003 til 1,116 over seks år.

Utvides begge sider med avfall, ligger forholdet på **0,945–1,039**, altså innenfor ±6 % og
fortsatt bevart.

**Massebevaringen er robust mot presiseringen.** Grunnen er strukturell: mekanismen flytter
produksjon **mellom etiketter innenfor det termiske settet**. Summen over settet er den samme
uansett hvilken etikett den enkelte enheten bærer. **Det er nettopp derfor massebevaring er det
riktige diagnostiske kriteriet** — den er upåvirket av hvilken av de to lesningene som stemmer,
og den fanger likevel at fordelingen er forskjøvet.

---

## 5 · Dom

**Hel-enhets-tilordning er bekreftet for DK2 — ved avkobling, ikke ved enhetsmåling.**

**DK og FI er samme mekanisme, ikke to akser.** Forrige rundes ramme var for forsiktig:

| | DK2 | FI |
|---|---|---|
| Enheten er registrert som | `Fossil Hard coal` | `Fossil Peat` |
| Enheten brenner faktisk | tre og halm (kull = 0,0 fra 2024) | tre og torv i blanding |
| A75 fører | hele produksjonen under kull | hele produksjonen under torv |
| Bevist ved | **avkobling** — kolonnen følger ikke kullet ned | **enhetsmåling** — A73 664,2 mot 190 tilordnet |
| Hva som mangler | A73 finnes ikke for DK | anleggsvis produksjon for 3 av 4 enheter |

Forskjellen er ikke mekanisme, men **grad**: i DK er hovedbrenselet helt borte, i FI er det redusert
til en tredjedel. **Kapregisters typeendringskriterium fanger bare symptomet** — at etiketten ikke
er oppdatert — ikke at hele produksjonen følger med etiketten.

---

## 6 · Berører det det publiserte?

**Nei. Verken repoet, README-en, ADR-ene eller Zenodo-posten trenger rettelse.**

Grunnen står i selve preregistreringen. `PREREG-v1.md` §6 og `README.md`, ordrett og identisk:

> «**Generering.** Registeret er kapasitet. Ingen MWh utledes av det.»

**kapregister måler 14.1.B — hvilken etikett en enhet bærer — og utleder aldri en mengde.**
Funnet her handler om hvordan A75 bokfører mengder. De to rører ikke hverandre.

Gjennomgått: **14 treff på `A75`, `generering`, `MWh`, `GWh` eller `TWh`** i alt publisert utenom
datasettene. Alle er enten metodeavgrensninger, sitatet fra #1161, eller Unnewehr-referansen.
Den ene som berører A75 direkte, `adr/0001` «Vurdert og valgt bort»:

> «**A75 (aggregert generering per type).** Gir ingen enhetsoppløsning. Den bærer *virkningen* av
> feilklassifisering, men kan ikke peke på et anlegg.»

**Den setningen blir sannere av dette funnet, ikke mindre sann.** Virkningen er større enn antatt
— det er ikke bare at en feil etikett teller feil, det er at hele enhetens produksjon følger
etiketten.

**DOI-en `10.5281/zenodo.22722722` står. Ingenting skal trekkes eller rettes.**

Det som derimot bør skrives, når det skrives: **en preregistrering for produksjonsaksen** — og
den dekker nå **begge** land, ikke bare Finland. Det endrer omfanget av det arbeidet, og det er
Eiriks avgjørelse.
