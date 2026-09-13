# DK-kull — A75 mot Energinet

> **Deponert arbeidsdokument.** Skrevet under arbeidet med `psrtype-samfyring` og
> `kapregister`, og deponert her uendret bortsett fra at lokale filstier er erstattet
> med relative navn. Utsagn om publiseringsstatus, åpne løkker og «ingen DOI» gjelder
> skrivetidspunktet, ikke i dag. Tallene er dem manuskriptene viser til.


**Dato:** 2026-09-11 · Recon. Ingen commit, ingen push, ingen ADR.
Utvider `TSO-KARTLEGGING.md`, erstatter den ikke.

---

## Utfallet: avviket er **ikke** daterbart i denne runden

Spørsmålet var når A75 og Energinet begynte å sprike, og om A75-kolonnen står flat mens
Energinets faller. **Det kan ikke besvares nå**, av to uavhengige grunner:

1. **A75 for DK finnes bare for 2025 lokalt.** det lokale v2-DK/FI-materialet har `DK1_generation_2025.csv`
   og `DK2_generation_2025.csv` og ingenting for 2021–2024. Bare FI ble hentet for fem år.
   En femårs A75-serie for DK krever nye ENTSO-E-kall, som grensene for denne runden forbyr.
2. **Energinet strupet oss.** Femårsserien ble avbrutt av vedvarende HTTP 429
   («Rate limit is exceeded. Try again in 31 seconds»). Jeg stoppet framfor å fortsette å
   prøve — gjentatt overskridelse av kvoter er nettopp det åpne-data-vilkår advarer mot.

Det som **er** etablert står under.

---

## A75 2025, målt lokalt

| Sone | `Fossil Hard coal` | Andel av miks | Total generering |
|---|---:|---:|---:|
| **DK1** | **0,9389 TWh** | **4,02 %** | 23,3584 TWh |
| **DK2** | **0,7319 TWh** | **7,07 %** | 10,3477 TWh |

Begge reproduserer `DK-TILLEGG.md` eksakt (0,939 TWh og 7,07 %), som er en uavhengig
bekreftelse av både MASTER og metoden.

**Varighetsvekting er påkrevd, ikke valgfritt.** Filene har blandet oppløsning — DK2 har
25 660 kvartersintervaller og 2 340 timesintervaller, pluss ett på 75 og ett på 210 minutter.
Et første forsøk med fast timesteg ga **~2× for høyt** og ville reprodusert ingenting.
Summen av intervaller dekker 8 758 av årets 8 760 timer, altså 100 % dekning.

---

## Energinet 2025 — bekreftet komplett

**DK2 `Coal` for hele 2025: nøyaktig 3 rader, alle `Production_MWh = 0.0`**, alle på timen
`2024-12-31T23:00:00Z`, skilt bare av `FuelAllocationMethod` (125 %, 200 %, Total).
Spørringen traff **ikke** 20 000-taket, så resultatet er komplett for året.

**DK1 `Coal` i 2025 finnes derimot:** 20 000 rader returnert (taket truffet), fordelt
mars–desember, 18 392 med verdi ulik null. DK1 har altså fortsatt kull i 2025.

### Motsigelsen, presist formulert

| Sone | A75 2025 | Energinet 2025 | Forhold |
|---|---:|---:|---|
| DK1 | 0,9389 TWh | kull finnes (mengde ikke ferdig målt) | begge kilder enige om at kull finnes |
| **DK2** | **0,7319 TWh** | **0,0000 TWh, komplett** | **motsigelse** |

---

## Fem-årsserien: hva som rakk å bli målt før strupingen

Tallene under er **nedre grenser**, ikke totaler. Alle årene 2021–2024 traff 20 000-taket,
så radene er avkuttet. **De skal ikke siteres som årssummer.**

| Sone | År | Rader returnert | Derav MWh ≠ 0 | Sum MWh (alloc=Total) | Status |
|---|---|---:|---:|---:|---|
| DK2 | 2021 | 20 000 | 10 980 | ≥ 789,55 | avkuttet |
| DK2 | 2022 | 20 000 | 16 268 | ≥ 70 700,07 | avkuttet |
| DK2 | 2023 | 20 000 | 15 374 | ≥ 144,42 | avkuttet |
| DK2 | 2024 | 20 000 | 5 358 | ≥ 7,67 | avkuttet |
| **DK2** | **2025** | **3** | **0** | **0,00** | **komplett** |

Retningen er likevel entydig: DK2 hadde betydelig kull i 2022, avtagende gjennom 2023–2024,
og null i 2025. **Nullen er fersk.** Det er den eneste dateringen runden gir, og den er grov.

---

## Hva utfallet betyr for hypotesen

Den opprinnelige hypotesen — at A75 fører en varig feilklassifisering av konverterte blokker —
er **ikke testet** av dette. Uten A75 for 2021–2024 kan jeg ikke se om A75-kolonnen står flat
mens Energinets faller.

Det som står igjen er svakere og mer presist: **DK2s kull i Energinet falt til null i løpet av
2023–2025, mens A75 fortsatt fører 0,73 TWh i 2025.** Det er forenlig med et etterslep i
klassifisering av nylig konverterte blokker, men også med at de to kildene måler ulike ting.
Begge forklaringene overlever, og runden skiller dem ikke.

**Det som ville avgjort det** er A75 `Fossil Hard coal` for DK2 i 2021–2024. Står den flat rundt
0,7–0,8 TWh mens Energinet faller fra ~70 GWh til null, er etterslepet reelt og daterbart.
Faller begge sammen, er det ulik måling. Det krever ett ENTSO-E-uttrekk på fire år for én sone.

---

## To målefeller, ført for neste runde

**Fast tidssteg på A75-CSV gir ~2× feil.** Filene har blandet oppløsning. Varighetsvekting er
eneste riktige form, og den reproduserer MASTER eksakt.

**Energinets 429 ser ut som tomt svar**, og strupingen bygger seg opp: 8 sekunders pacing var
ikke nok, og en backoff-løkke på 35 sekunder holdt oss i sperren. Neste runde bør ligge på
minst 30 sekunder mellom kall, eller hente rådataene som fil i stedet for gjennom API-et.

---

# Steg 2 — A75 DK2 2021–2024 hentet · 11.09.2026

48 månedskall, **48/48 vellykket, null feil, null omforsøk**. P1M-grense respektert,
UTC-grenser, 5 s mellom kall. Rådata som `dk2-<år>-<måned>.csv` i arbeidskatalogen.

## Serien

| År | A75 `Fossil Hard coal` | Andel av DK2-miks | Total A75 | Energinet `Coal` |
|---|---:|---:|---:|---:|
| 2021 | **1,2385 TWh** | 11,59 % | 10,6841 TWh | ikke målt (strupet) |
| 2022 | **0,9639 TWh** | 9,32 % | 10,3441 TWh | ikke målt (strupet) |
| 2023 | **1,0793 TWh** | 10,11 % | 10,6795 TWh | ikke målt (strupet) |
| 2024 | **1,0050 TWh** | 9,43 % | 10,6555 TWh | ikke målt (strupet) |
| **2025** | **0,7319 TWh** | **7,07 %** | 10,3477 TWh | **0,0000 TWh** (komplett) |

## Kontroller — alle passerer

| År | Rader | Forventet | Duplikater | Målt oppløsning |
|---|---:|---:|---:|---|
| 2021 | 8 760 | 8 760 | **0** | 60 min |
| 2022 | 8 760 | 8 760 | **0** | 60 min |
| 2023 | 8 760 | 8 760 | **0** | 60 min |
| 2024 | 8 784 | 8 784 | **0** | 60 min |

**Oppløsningen er målt fra tidsstempeldeltaene, ikke antatt.** 60 minutter gjennomgående i alle
fire år — DK2 skifter først til 15 min i 2025. Totalsummen 10,34–10,68 TWh ligger på DK2s kjente
årsproduksjon rundt 10 TWh. Samme åtte kolonner alle fire år.

**DST er håndtert riktig av kilden.** Ved tilbakestillingen 2021-10-31 opptrer den gjentatte
timen som `02:00+02:00` og `02:00+01:00` — skilt av offset, ikke kollapset. Null duplikate
UTC-stempler i alle fire år.

## To fellegroper i selve filformatet

**Én av 48 filer har to header-rader.** `dk2-2021-10.csv` kom tilbake med MultiIndex
(`Biomass/Actual Aggregated`, `Biomass/Actual Consumption`, …) mens de 47 andre har flat header.
Leses den flatt, blir andre header-rad en datarad med NaT-indeks. Det ga først 8 761 rader mot
forventet 8 760.

**Og den fila har `Actual Consumption`-kolonner.** Summeres de inn i totalen, blir
generasjonsmiksen feil. Kolonnevalget må derfor filtrere på **både** typenavn og
`Actual Aggregated`. Uten det ville totalen for 2021 vært oppblåst og andelen for lav.

## Hvilken lesning serien støtter

**A75-kolonnen står flat.** 1,24 → 0,96 → 1,08 → 1,01 → 0,73 TWh. Ingen kollaps, bare en mild
nedgang på 24 % over fem år, og andelen holder seg på 7–12 % hele veien.

**Energinet faller til null.** DK2 hadde kull i 2022 (≥ 70,7 GWh, nedre grense fra avkuttet
spørring) og har **eksakt null i 2025**, verifisert komplett.

Det peker mot **FLAT A75 mens Energinet faller** — altså etterslepende klassifisering. Men
**serien alene avgjør det ikke**, og grunnen er at Energinet-kolonnen bare er målt for ett år.
For 2021–2024 har jeg nedre grenser fra avkuttede spørringer, ikke årssummer. Uten dem kan jeg
ikke vise fallet år for år, bare endepunktet.

Det som **er** avgjort: A75-siden er ikke i bevegelse. Hypotesen om at begge faller sammen —
«ingen feilklassifisering, bare ulik måling» — er **uforenlig med disse tallene**, for A75 viser
ingen nedgang som kan matche Energinets fall til null. Den lesningen er dermed svekket.

Det som gjenstår for å lukke saken er Energinet DK2 `Coal` per år 2021–2024 som ekte årssummer.
Det krever kvartals- eller månedsvis paginering med minst 30 sekunders pacing, eller nedlasting
av rådatafil framfor API-kall.

**Datering:** avviket er minst fem år gammelt på A75-siden, og har ikke oppstått — det har
vedvart. Dersom Energinets kull var vesentlig i 2021–2022, begynte spriket å vokse da
Energinets tall falt, ikke da A75 endret seg. A75 har ikke endret seg.

---

# Steg 3 — allokeringsspørsmålet lukket · 11.09.2026

Kun disk. Ingen nye API-kall mot Energinet.

**Forbehold om kildegrunnlaget:** råsvarene fra dagens Energinet-runder ble **ikke lagret** —
jeg printet resultater og lagret bare aggregater, og de to jobbene som skulle skrive JSON ble
drept underveis. Det som finnes er loggutskriftene med feltverdier, et lagret DK1-uttrekk på
20 rader for én time, og `DK-TILLEGG.md`. Dommen under hviler på det, ikke på fullstendige
rådata.

## 1 — hvilken allokeringsnøkkel ga 0,0000?

Spørringen bak nullen var `{"PriceArea":["DK2"],"ProductionType":["Coal"]}` — **uten**
`FuelAllocationMethod`- og `DeliveryType`-filter. Den returnerte `total: 3`, under taket, altså
komplett. De tre radene ordrett fra loggen:

```
2024-12-31T23:00:00  DK2  Coal  MWh=0.0  alloc=125%   deliv=Grid
2024-12-31T23:00:00  DK2  Coal  MWh=0.0  alloc=200%   deliv=Grid
2024-12-31T23:00:00  DK2  Coal  MWh=0.0  alloc=Total  deliv=Grid
```

**Nullen er målt på tre nøkler, ikke én.** `All` og `OwnConsumption` forekommer ikke — og siden
spørringen var ufiltrert, betyr fraværet at slike rader **ikke finnes**, ikke at de ble filtrert
bort.

DK1-kontrollen for samme år viser at `Coal` i dette datasettet bærer nøyaktig de samme tre
nøklene og bare `Grid`: `{'125%': 6667, '200%': 6667, 'Total': 6666}`, `deliv` = Grid i alle
20 000 rader. **DK2-nullen er altså målt på nøyaktig de nøklene som bærer DK1s kull.**

## 2 — 2022, der vi vet det var kull

**Rådataene for 2022 er ikke lagret**, og nye kall er utelukket. Det som kan fastslås fra
loggen: summen på **70 700,07 MWh** ble regnet over rader med `FuelAllocationMethod == "Total"`,
fra en **ufiltrert** spørring. 2022-kullet ligger dermed under `Total` — **samme nøkkel som
leser 0,0 i 2025.**

Det utelukker versjonen av B der kullet flyttet seg til en nøkkel vi ikke så på.

## 3 — systemgrensen: allokering rører ikke mengden

Dette er det som avgjør saken, og det står i data vi alt har.

`dp.json` — DK1, timen 2025-01-14T23:00, 20 rader, alle fire allokeringsnøkler og begge
leveringstyper til stede (`125%` 7, `200%` 7, `All` 5, `Total` 1; `Grid` 19, `OwnConsumption` 1).
Gruppert på (time, område, type, leveringstype) gir det **12 grupper, og null der
`Production_MWh` skiller seg mellom allokeringsnøkler:**

| Type | 125 % | 200 % | Total |
|---|---:|---:|---:|
| BioGas | 41,7631 | 41,7631 | 41,7631 |
| Straw | 37,2059 | 37,2059 | — |
| Wood | 338,5787 | 338,5787 | — |
| FossilGas | 8,1593 | 8,1593 | — |
| **Coal** | **0,4450** | **0,4450** | — |

Samtidig endrer `CO2PerkWh` seg kraftig: Coal 628,90 under 125 % mot 1083,08 under 200 %.

**Konklusjonen er entydig: `FuelAllocationMethod` allokerer utslippsintensiteten mellom el og
varme, ikke produksjonsmengden.** `Production_MWh` er allokeringsinvariant. En allokering kan
derfor ikke skyve kullets elproduksjon over på varmesiden og få mengden til å lese null — feltet
rører ikke mengden.

Begge datasett måler produksjon per budsone per time. Energinets metadata, ordrett: «Declaration
of production per bidding zone (Price area) per hour», med forbeholdet «Only declaration of
production, not to be used for green accounting purposes». `CO2Emis` er derimot forbruksbasert
og importjustert — den er **ikke** sammenlignbar med A75, men det er ikke den vi bruker.

## 4 — dom: **A**, med én presisering

**B er utelukket.** Nullen henger ikke på én nøkkel: den ufiltrerte spørringen returnerte alle
tre radene som finnes, alle null, og `Production_MWh` er allokeringsinvariant, så null under én
nøkkel er null under alle. 2022-kullet ligger under `Total`, samme nøkkel som leser null i 2025.

**C er utelukket for allokering og leveringstype.** Allokeringen rører ikke mengden, og det finnes
ingen `OwnConsumption`-rad som kunne skjult kull utenfor `Grid`. Begge kilder er produksjonsbaserte
per budsone per time.

**A står: A75 bærer 0,73–1,24 TWh kull per år for DK2 som Energinet ikke ser.**

Presiseringen er hvor forskjellen sitter. Den er **ikke** i systemgrense, allokering eller filter —
den er i **anleggstilordning**. Energinets deklarasjon bygger på faktisk brenselsforbruk i GJ, så
en blokk konvertert fra kull til trepellets flytter seg til `Wood`. A75s psrType følger enhetens
registrering, som ikke nødvendigvis er oppdatert. `DK-TILLEGG.md` fører at Energinets termiske
DK2-flåte er **70,28 % `Wood` og 19,24 % `Waste`** — forenlig med nettopp det.

**Det ene som ikke kan utelukkes fra disk** er om A75 `Fossil Hard coal` og Energinet `Coal`
bruker samme anleggstilordning. Det er selve hypotesen, og den kan ikke testes med de to
seriene alene — den krever enhetsnivå på begge sider. Men alle alternative forklaringer som
kunne vært avvist mot disk, er nå avvist.

**MASTER skal ikke rettes.** Motsigelsen står, og den er nå bedre belagt enn før: ikke en
artefakt av filter, nøkkel eller systemgrense.

---

# Steg 4 — Energinet-kolonnen fylt · 11.09.2026

Rådata i `energinet-raw/` i arbeidskatalogen, fire CSV-filer, én per år, skrevet til disk
før parsing. Manifest med sha256 i samme katalog. **Energinet-hullet er lukket.**

## Tabellen

| År | A75 TWh | Andel | Energinet TWh | A75 / Energinet |
|---|---:|---:|---:|---:|
| 2021 | 1,2385 | 11,59 % | **0,001353** | 915× |
| 2022 | 0,9639 | 9,32 % | **0,127106** | 8× |
| 2023 | 1,0793 | 10,11 % | **0,000275** | 3931× |
| 2024 | 1,0050 | 9,43 % | **0,000014** | 70548× |
| 2025 | 0,7319 | 7,07 % | **0,000000** | ∞ |

## Hvilken lesning: **ingen av de tre, som formulert**

De tre alternativene forutsatte alle at Energinet og A75 lå nær hverandre på et tidspunkt.
**Det gjorde de aldri.**

- **«Energinet faller mot null mens A75 står flat»** — halvveis riktig. A75 står flat. Men
  Energinet *falt ikke*; den lå allerede på **0,0014 TWh i 2021**, altså praktisk talt null fem
  år tilbake.
- **«Energinet følger A75 til et år og faller etter»** — nei. Den følger A75 i intet år.
- **«Energinet ligger nær A75 hele veien, 2025 er ettårig»** — nei. Forskjellen er 915× i 2021
  og 70 548× i 2024.

**Den riktige lesningen er en fjerde: avviket er strukturelt og minst fem år gammelt.** A75
fører 0,96–1,24 TWh kull for DK2 hvert eneste år mens Energinet fører mellom 14 MWh og
127 GWh. Selv i 2022 — kriseåret der dansk kull faktisk ble kjørt, og Energinet viser
**0,127 TWh** — er A75 **7,6 ganger høyere**.

## Hva det gjør med hypotesen

**Etterslepende klassifisering av nylig konverterte blokker er svekket.** Et etterslep ville
vist A75 og Energinet i takt fram til konverteringen, og deretter sprik. Her spriker de fra
første målte år. Blokkene var enten konvertert før 2021, eller A75s kullkolonne for DK2 har
aldri sporet dem.

**2022-toppen er det mest talende punktet.** Da kull faktisk ble fyrt i DK2, steg Energinet fra
0,0014 til 0,127 TWh — en faktor 94. A75 steg ikke; den *falt* fra 1,24 til 0,96 TWh. De to
seriene beveger seg ikke bare på ulikt nivå, de beveger seg **i motsatt retning** i det ene året
der kullet er utvilsomt reelt.

Det er ikke forenlig med at de måler samme fysiske størrelse med ulik forsinkelse. Det peker mot
at A75s `Fossil Hard coal` for DK2 bærer noe annet enn det Energinet kaller `Coal` — vedvarende,
ikke midlertidig.

## Kontroller

| År | Rader | Distinkte timer | Forventet | Stemmer |
|---|---:|---:|---:|---|
| 2021 | 26 280 | 8 760 | 8 760 | ja |
| 2022 | 26 280 | 8 760 | 8 760 | ja |
| 2023 | 26 280 | 8 760 | 8 760 | ja |
| 2024 | 26 352 | 8 784 | 8 784 | ja |

Rader = timer × 3 allokeringsnøkler. `DeliveryType` er `Grid` i samtlige — ingen
`OwnConsumption`. **Ingen kall traff noe tak**, fordi nedlastingsendepunktet ikke har ett.

**Allokeringsinvariansen er re-verifisert på årssummer:** `Production_MWh` er identisk under
125 %, 200 % og Total i alle fire år. Nøkkelvalget endrer ikke tallet, og det bekrefter dagens
tidligere funn uavhengig.

## Metodemerknad

Det paginerte `/dataset/`-endepunktet er strupet på **svarstørrelse**, ikke bare på takt:
`limit=2` går gjennom, `limit=2000` én gang, `limit=20000` aldri. **Nedlastingsendepunktet**
`/dataset/<navn>/download?...&format=csv` har ikke grensen — hele året i ett kall. Fire kall
erstattet de ~70 det paginerte API-et ville krevd.

CSV-en bruker **semikolon som skilletegn og komma som desimaltegn**. Leses den med punktum,
blir alle tall feil.

---

# Steg 5 — DK1 hentet, mekanismen bekreftet · 11.09.2026

A75 DK1 2021–2024: **48/48 månedskall, null feil**. Energinet DK1 2021–2025 og DK2 2025 hentet
fra nedlastingsendepunktet. Alle kontroller passerer: null duplikater, 60 min målt gjennomgående,
rader = timer × 3 allokeringsnøkler, allokeringsinvarians bekreftet i samtlige filer. Én
MultiIndex-fil fanget per sone for 2021 (oktober, DST-måneden).

## DK1 — kildene er enige

| År | A75 GWh | Energinet GWh | Forhold |
|---|---:|---:|---:|
| 2021 | 4592.3 | 3979.3 | 1.15× |
| 2022 | 4124.3 | 3922.1 | 1.05× |
| 2023 | 2250.9 | 2291.8 | 0.98× |
| 2024 | 2265.1 | 1595.7 | 1.42× |
| 2025 | 938,9 | 668,9 | 1,40× |

## DK2 — kildene er ikke i nærheten

| År | A75 GWh | Energinet GWh | Forhold |
|---|---:|---:|---:|
| 2021 | 1238.5 | 1.4 | 915× |
| 2022 | 963.9 | 127.1 | 8× |
| 2023 | 1079.3 | 0.3 | 3931× |
| 2024 | 1005.0 | 0.0 | 70548× |
| 2025 | 731,9 | 0,0 | ∞ |

**Dommen på sonespørsmålet: sonespesifikt.** DK1 ligger innenfor 0,98–1,42× hvert år, og 2023 er
praktisk talt eksakt. DK2 er ute med to til fem tierpotenser. **Det er ikke et generelt
A75-problem for dansk kull** — Jylland stemmer, Sjælland gjør det ikke.

## Mekanismen — bekreftet fra data

Hvis A75s kull er Energinets tre, skal **A75(kull + biomasse)** møte
**Energinet(kull + tre + halm)**. Den gjør det:

| Sone | År | A75 kull | A75 bio | A75 sum | Eng kull | Eng tre | Eng halm | Eng sum | Forhold |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DK1 | 2021 | 4592.3 | 1771.3 | 6363.6 | 3979.3 | 2009.3 | 349.4 | 6338.0 | **1.00×** |
| DK1 | 2022 | 4124.3 | 1753.0 | 5877.3 | 3922.1 | 1489.5 | 385.2 | 5796.8 | **1.01×** |
| DK1 | 2023 | 2250.9 | 1540.7 | 3791.6 | 2291.8 | 966.2 | 319.0 | 3577.0 | **1.06×** |
| DK1 | 2024 | 2265.1 | 1699.0 | 3964.1 | 1595.7 | 1873.6 | 249.3 | 3718.6 | **1.07×** |
| DK2 | 2021 | 1238.5 | 3107.3 | 4345.8 | 1.4 | 3776.0 | 293.8 | 4071.2 | **1.07×** |
| DK2 | 2022 | 963.9 | 2353.1 | 3317.1 | 127.1 | 2939.2 | 241.8 | 3308.1 | **1.00×** |
| DK2 | 2023 | 1079.3 | 2225.4 | 3304.7 | 0.3 | 2891.0 | 260.7 | 3152.0 | **1.05×** |
| DK2 | 2024 | 1005.0 | 2311.0 | 3316.0 | 0.0 | 2878.3 | 218.5 | 3096.8 | **1.07×** |

**Summen bevares til 1,00–1,07× i alle åtte sone-år.** DK2 2022 lander på 1,00×.

Der A75 fører ~1,0 TWh kull og Energinet fører null, fører A75 **tilsvarende mindre biomasse**:
2,2–3,1 TWh mot Energinets 2,9–3,8 TWh tre. Massen er den samme, etiketten er ulik.

**Reklassifisering ved kilden er bekreftet fra data, ikke bare sannsynliggjort.** A75s
`Fossil Hard coal` for DK2 bærer generering Energinet fører som `Wood`. Blokkene på Sjælland er
konvertert; A75s anleggsregistrering følger ikke etter.

Det forklarer også hvorfor 2022 pekte motsatt vei i steg 4: da kull faktisk ble fyrt i DK2
(Energinet 127 GWh), var totalmassen uendret. Konverteringen var allerede gjennomført, og
2022-toppen er en midlertidig tilbakevending innenfor samme anleggspark.

## Avfall spriker uavhengig

| | 2021 | 2022 | 2023 | 2024 |
|---|---:|---:|---:|---:|
| DK1 A75/Eng | 1.13× | 0.93× | 0.83× | 0.76× |
| DK2 A75/Eng | 0.77× | 0.72× | 0.47× | 0.44× |

A75 underrapporterer avfall mot Energinet, verst i DK2 der forholdet nær halveres. Det er en
**egen akse** og inngår ikke i kull-tre-balansen over. Ikke undersøkt videre her.

---

# Steg 6 — dateringen · 11.09.2026

To nye år hentet, 2019 og 2020. 48 A75-kall, **48 ok / 0 feil**. Energinet via
nedlastingsendepunktet: `mek-2019.csv` 50 449 124 B / 210 241 linjer, `mek-2020.csv`
50 714 902 B / 210 817 linjer — semikolon som skilletegn, komma som desimaltegn.

**Kryssjekk før bruk:** aggregeringen ble validert mot `energinet_mek.json` for 2021 — **8 av 8
treff**, og identiske tall på alle tre allokeringsmetoder (`125%`, `200%`, `Total`), som
bekrefter at `Production_MWh` er allokeringsinvariant.

**Kolonnesammensetningen endret seg.** 2019–2020 har **10 produksjonstyper i DK1** og **8 i
DK2**, mot 15–16 i 2021+. `Fossil Hard coal` og `Biomass` finnes i alle fire sone-år.
Kolonner valgt på navn, ikke indeks.

## A75 kull mot Energinet kull, 2019 til 2025

### DK1

| År | A75 GWh | Energinet GWh | Forhold |
|---|---:|---:|---:|
| 2019 | 2939,9 | 2437,441 | 1,21× |
| 2020 | 3050,2 | 2624,043 | 1,16× |
| 2021 | 4592,3 | 3979,292 | 1,15× |
| 2022 | 4124,3 | 3922,091 | 1,05× |
| 2023 | 2250,9 | 2291,826 | 0,98× |
| 2024 | 2265,1 | 1595,659 | 1,42× |

### DK2

| År | A75 GWh | Energinet GWh | Forhold |
|---|---:|---:|---:|
| 2019 | 875,1 | 567,904 | **1,54×** |
| 2020 | 810,2 | 148,840 | **5,44×** |
| 2021 | 1238,5 | 1,353 | **915×** |
| 2022 | 963,9 | 127,106 | **7,58×** |
| 2023 | 1079,3 | 0,275 | **3 931×** |
| 2024 | 1005,0 | 0,014 | **70 548×** |
| 2025 | 731,9 | 0,000 | **∞** |

## Dommen: kolonnen er aldri null

Av de tre utfallene var det det tredje.

**A75 fører 0,73–1,24 TWh kull for DK2 hvert eneste år fra 2019 til 2025.** Tallet varierer med
under en faktor to over sju år. Det er ikke en serie som slås av og på — det er en serie som
står stille.

**Det som beveger seg, er Energinet.** 568 → 149 → 1,4 GWh. Divergensen vokser ikke fordi
telleren stiger; **den vokser fordi nevneren forsvinner.**

**Divergensen har likevel en dato: 2020.** Asnæsværkets blokk 6 ble satt i drift på træflis i
2020, og Amagerværkets kullblokk 3 ble lukket samme år. Det er nøyaktig der Energinets DK2-kull
faller fra 568 til 149 til null — og A75 registrerer det ikke.

**Allerede 2019 er for høyt.** 1,54× da Asnæs og Amager fortsatt fyrte med kull. Avedøre var
biomasse fra 2018-rettelsen, så overskuddet i 2019 må komme fra de to andre.

**#1161-rettelsen ble aldri komplett.** Den holdt for Avedøre og bare for Avedøre. Se
`A73-ANLEGGSNIVAA.md`: Asnæsværket og Amagerværket står som `Fossil Hard coal` i
kapasitetsregisteret hvert år 2019–2025, og de er DK2s **eneste** kullregistrerte enheter.

## Massebevaring, 2019 og 2020

| Sone | År | A75 kull | A75 bio | A75 sum | Eng kull | Eng tre | Eng halm | Eng sum | Forhold |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DK1 | 2019 | 2939,9 | 1469,5 | 4409,4 | 2437,4 | 1455,7 | 225,2 | 4118,3 | **1,07×** |
| DK1 | 2020 | 3050,2 | 1274,4 | 4324,6 | 2624,0 | 1314,7 | 270,1 | 4208,9 | **1,03×** |
| DK2 | 2019 | 875,1 | 2236,4 | 3111,5 | 567,9 | 2007,5 | 211,7 | 2787,1 | **1,12×** |
| DK2 | 2020 | 810,2 | 1770,3 | 2580,5 | 148,8 | 2060,6 | 157,8 | 2367,2 | **1,09×** |

**Summen bevares også i de to nye årene.** Serien er nå **1,00–1,12× over tolv sone-år**.

## Kontrollkategorier

Kjernekraft finnes ikke i Danmark. Energinets uttrekk dekker fire brensler, så **avfall** er den
eneste kategorien som kan stilles mot en uavhengig kilde:

| Sone | År | A75 avfall | Energinet avfall | Forhold |
|---|---|---:|---:|---:|
| DK1 | 2019 | 760,6 | 750,3 | **1,01×** |
| DK1 | 2020 | 729,1 | 715,6 | **1,02×** |
| DK2 | 2019 | 553,2 | 741,2 | 0,75× |
| DK2 | 2020 | 529,6 | 728,8 | 0,73× |

**DK1 på 1,01–1,02× er kontrollen som validerer kjøringen** — varighetsvekting, kolonnevalg og
tidssoner er riktige. DK2s 0,73–0,75× er det samme avviket som i 2021–2024 og er et eget,
uavklart forhold på avfallssiden, ikke en feil i denne kjøringen.

A75s egne entydige kategorier, ført for fullstendighet (ingen uavhengig motpart i uttrekket):
DK1 2019 vind 8 338,0 + 4 272,5 GWh, sol 627,7 · DK2 2019 vind 1 974,3 + 1 343,9, sol 341,5.
