# FI — anleggsheterogeniteten målt. Og hva som da står igjen

> **Deponert arbeidsdokument.** Skrevet under arbeidet med `psrtype-samfyring` og
> `kapregister`, og deponert her uendret bortsett fra at lokale filstier er erstattet
> med relative navn. Utsagn om publiseringsstatus, åpne løkker og «ingen DOI» gjelder
> skrivetidspunktet, ikke i dag. Tallene er dem manuskriptene viser til.


**12.09.2026.** Rådata i `anlegg/`, sjekksum i `anlegg/MANIFEST.md`.

---

## 1 · Registeret: hvilke anlegg brenner torv

`Energiaviraston voimalaitosrekisteri`, oppdatert 22.05.2026, ark «English», 534 anlegg.
202 416 B, `sha256 c7f281baa4f3548162c9730f86fb42aa217c61ba1703bd9dafd0f1f51301d08c`.
Kontrollstreng `Peat` som hovedbrensel: **21**; som reservebrensel: **17**.

**Alle 21 torv-hovedbrensel-anlegg er kraftvarme. Separate power production = 0,0 MW for hvert
eneste ett.**

| Kategori | MW el |
|---|---:|
| Kaukolämpö-CHP | **718,3** |
| Industri-CHP | **453,6** |
| Ren el (lauhde) | **0,0** |
| **Sum** | **1 171,9** |

De fem største: Alholma AK 2 (240, industri), Keljonlahti (190, kaukolämpö), Seinäjoki SEVO
(120), Haapaniemi (118,1), Toppila 2 (98). **Samtlige har et trebasert reservebrensel** —
*Industrial wood residues* eller *Forest fuelwood* — med to unntak som har olje.

Registeret oppgir **kun elektrisk** kapasitet. Varmekapasitet per anlegg finnes ikke der, så
el/varme-forholdet må måles fra produksjonen, ikke fra registeret.

### Et avvik registeret ikke forklarer

**13j5 fører torv-el under `Lauhdevoiman tuotanto` hvert år** — 366, 482, 106 og 90 GWh for
2021–2024 — mens registeret har **null MW** torvfyrt lauhdekapasitet. Enten kjøres
kraftvarmeanlegg i kondensmodus og føres som lauhde, eller registeret og statistikken bruker ulik
avgrensning. **Ikke avklart her.**

---

## 2 · A73 for Finland — påbegynt, ikke fullført

Uttrekket kjører. `documentType=A73&processType=A16`, `in_Domain=10YFI-1--------U`, døgn for døgn
fordi A73 har hard **P1D**-grense der A75 har P1M. Rådata til `anlegg/a73-raw/` som XML før
parsing, token sanert i alt som logges.

**Ved rapportskriving: ~60 av 1 461 døgn.** Takten er ~2,4 døgn/minutt, så fullt uttrekk
2021–2024 tar rundt **ti timer**. Det er ikke ferdig i denne økten, og **årssummer kan ikke
regnes av et delvis uttrekk** — de ville vært systematisk for lave. Prosessen er ikke stoppet.

**~70 %-tallet er derfor ikke reverifisert.** Det som står fra forrige måling gjelder **2025**:
A73 dekket **0,7886 av A75s 1,1302 TWh = 69,8 %**, båret av fem enheter — Alholmens Kraft
0,2005, Keljonlahti 0,3310, Toppila 2 0,2267, Seinäjoki 0,0303, og Haapavesi **0,0000**.
Haapaniemi manglet i A73 til tross for 145 MW i A71. **Det tallet gjelder ett år og er ikke
utvidet til 2021–2024.**

---

## 3 · Testen: torvanleggenes el-til-varme-forhold

Målt fra 13j5, tuotantomuoto `012`, torv mot alle brensler:

| År | Torv el/varme | Flåte el/varme | **Forhold** |
|---|---:|---:|---:|
| 2021 | 0,3821 | 0,3182 | **1,20** |
| 2022 | 0,4273 | 0,3024 | **1,41** |
| 2023 | 0,3786 | 0,2739 | **1,38** |
| 2024 | 0,3641 | 0,2565 | **1,42** |

**Torvfyrte anlegg ligger systematisk høyere, alle fire år. Heterogeniteten er bekreftet.**

### Hvorfor: varmen er en annen slags varme

| År | Torv: industrivarmens andel | Flåte: industrivarmens andel |
|---|---:|---:|
| 2021 | 33,70 % | 65,54 % |
| 2024 | 32,19 % | 71,06 % |

Flåten domineres av **industri-CHP** med lavt el-til-varme-forhold — mottrykk mot prosessdamp.
Torv ligger overveiende i **kaukolämpö-CHP**, som har høyere forhold. Registeret sier det samme
strukturelt: 718,3 MW kaukolämpö mot 453,6 MW industri.

### Restavviket dekomponerer eksakt

Avviket `(E/F)_torv / (E/F)_flåte − 1` er produktet av et el-andelsledd og et η-ledd:

| År | El-andelsledd | η-ledd | Produkt | Målt avvik |
|---|---:|---:|---:|---:|
| 2021 | 1,1454 | 1,0424 | 1,1940 | **+19,4 %** |
| 2022 | 1,2893 | 1,0070 | 1,2982 | **+29,8 %** |
| 2023 | 1,2774 | 1,0356 | 1,3229 | **+32,3 %** |
| 2024 | 1,3075 | 1,0314 | 1,3485 | **+34,9 %** |

**Produkt og målt avvik er identiske til siste desimal.** El-andelsleddet bærer 80–90 %;
virkningsgradsleddet er marginalt. **Restavviket er forklart, og forklaringen er fysisk.**

---

## 4 · Men det lukker feil gap

Restavviket som nå er forklart lå mellom **min egen prediksjon** og **StatFins eget torvtall**.
Det er en intern StatFin-sak: de regner per anlegg og summerer, ikke flatt etter brenselsandel.

**A75/StatFin-gapet på 1,8–2,7 er urørt av dette.**

Og registeret peker på hva det kan være. **Alle 21 torvanlegg samfyrer**, med tre som
reservebrensel. Fører A75 hele anleggets elproduksjon under anleggets hovedbrensel, mens StatFin
fører torvandelen, gir gapet denne implisitte torvandelen av brenselet:

| År | Implisert torvandel |
|---|---:|
| 2021 | **55,0 %** |
| 2022 | **55,7 %** |
| 2023 | **47,1 %** |
| 2024 | **37,3 %** |

**Monotont fallende, i takt med at tre fortrenger torv i de samme anleggene — mens
hovedbrenselsetiketten blir stående.** Det er en fysisk plausibel bane, og den forklarer både
nivået og driften som ingen av de foregående hypotesene klarte.

**Dette er ikke bevist.** Det krever anleggsnivå i A75, som ikke finnes — A73 er den nærmeste,
og den dekker ~70 % og er ikke ferdig hentet. Men det er den første hypotesen som er forenlig
med alle fire årene.

**Og det er DK-mekanismen på en annen akse.** DK2: anlegget er konvertert, etiketten står. FI:
anlegget samfyrer, hele produksjonen bokføres under etiketten. Begge er *etikett mot virkelighet
på anleggsnivå*.

---

## 5 · Hva utfallet gjør med codecarbon

**FI-tallet er ikke robust.** Erstattes A75s torvkolonne med StatFins:

| År | CI torv=816 | CI m/StatFin-torv | Endring |
|---|---:|---:|---:|
| 2021 | 168,91 | 148,39 | **−12,1 %** |
| 2022 | 148,25 | 127,64 | **−13,9 %** |
| 2023 | 92,86 | 79,55 | **−14,3 %** |
| 2024 | 68,31 | 56,15 | **−17,8 %** |

Antakelsen bak kolonnen til høyre: at StatFins torv-el er den riktige tilordningen og A75s er
inflatert av anleggsbokføring. **Den antakelsen er ikke belagt** — det er nettopp det §4 sier
står åpent.

**Utslaget vokser med utfasingen**, fordi den impliserte torvandelen faller. For 2025, der
47,88 er beregnet, er StatFin-tallet ikke hentet, og utslaget er derfor ikke regnet. Banen
tilsier at det ville vært større enn −17,8 %.

**Dom for codecarbon: FI-oppføringen er ikke klar.** Et tall som flytter seg 12–18 % på en
uavklart tilordningsantakelse skal ikke leveres oppstrøms, uansett hva #1415 gjør med
faktornøklene for avfall og biomasse. Gaten er ikke lenger bare #1415; den er dette.

---

## 6 · Dom

**FI er et funn, og det er ikke et codecarbon-bidrag ennå.**

Funnet er ikke torvfaktoren og ikke allokeringsmetoden. Det er at **A75s torvkolonne for Finland
er omtrent dobbelt så stor som den nasjonale statistikkens, at gapet vokser monotont med
utfasingen, og at alle anleggene bak kolonnen samfyrer med tre.** Metodesporet er lukket
underveis: allokeringsmetoden kansellerer algebraisk ut av StatFins tall (§ `ALLOKERINGSMETODE.md`),
og anleggsheterogeniteten er målt og forklarer det den skal forklare — men ingen av delene rører
gapet.

### FI hører i kapregister, som andre sone

**Ja, og det er den klareste anbefalingen her.**

- **Metoden er den samme.** kapregister måler etikett mot virkelighet per anlegg, på EIC-nøkkel,
  mellom to årganger. FI-spørsmålet er etikett mot virkelighet per anlegg, med samfyring som
  mekanisme framfor konvertering.
- **Artefaktet finnes.** Repo, prereg med sjekksum, ADR-kjede, testsuite, DOI
  `10.5281/zenodo.22722722`. Å bygge det samme på nytt for FI er dobbeltarbeid.
- **Klassene passer nesten.** `revidert` / `urevidert` / `forlatt` / `uavklart` er definert på
  typeendring. FI trenger en akse til — *andel av produksjonen som faktisk stammer fra den
  registrerte typen* — og den kan ikke smugles inn i v1.0.0s kriterier. **Den krever egen
  preregistrering**, som `PREREG-v1.md` §4 er låst nettopp for å tvinge fram.
- **Et eget FI-arbeid ville bære torv- og dekningsdiskusjonen som sitt tema.** Presset inn i
  Khepri v2.0 sammen med DK1/DK2 blir det en fotnote. Det står i `NOTAT.md` fra før og holder
  fortsatt.

**Anbefaling: FI føres som sone to i kapregister, under egen preregistrering, med samfyringsaksen
som det nye kriteriet. Ikke som eget arbeid, og ikke som en codecarbon-PR.**

### Det som må gjøres før det

1. **A73 2021–2024 ferdig** — kjører, ~ti timer. Uten den er anleggsnivået udekket.
2. **Lauhde-anomalien** — 90–482 GWh torv-lauhde i 13j5 mot 0 MW i registeret.
3. **Brenselsmiks per anlegg** — den impliserte torvandelen 55 → 37 % må belegges mot en
   uavhengig kilde, ikke utledes av gapet den skal forklare. YLVA eller EU ETS per installasjon
   er de nærmeste sporene; ingen av dem er forsøkt her.

---

# Sirkulariteten — forsøkt brutt, og den står

**12.09.2026, andre runde.** Den impliserte torvandelen 55,0 → 37,3 % er utledet av
A75/StatFin-gapet den skal forklare. Den måtte måles uavhengig eller falle.

## A · Kildene som ble prøvd, og hva de faktisk gir

| Kilde | Utfall |
|---|---|
| **EU ETS, verifiserte utslipp** (`verified_emissions_2024_en.xlsx`) | **77 kolonner, null med `BIO`/`SUSTAIN`/`BIOGENIC`.** Kolonnefamiliene er `ALLOCATION_*`, `VERIFIED_EMISSIONS_*`, `CH_*`. **Biogent utslipp rapporteres ikke i denne fila.** 695 FI-installasjoner, 216 med hovedaktivitetskode 20 (forbrenning) |
| **Energiaviraston voimalaitosrekisteri** | elektrisk kapasitet, hovedbrensel og to reservebrensler — **ingen brenselsmengder, ingen årstall** |
| **YLVA / ympäristöhallinto** | myndighetssystem for rapportering og tilsyn. Opplysningene er offentlige etter miljøvernloven §210, men **ikke publisert som nedlastbart datasett** |
| **avoindata.fi** | API-et svarte ikke på tre spørringer (`ylva`, `polttoaine`, `energiantuotanto turve`) |
| **Energiateollisuus, kaukolämpötilasto** | `DH_Regional_*.xlsx` er **NUTS2-nivå — fem regioner**, ikke anlegg. Kontrollstreng `laitoskohta` (anleggsvis) i de finske PDF-ene: **0** |

## B · Dekningsgrad: 0 av 21

**Ingen kilde funnet gir brenselsmiks per anlegg per år for de 21 torvanleggene.**
Dekningsgrad **0 av 21**, og **0 % av torvkolonnen**. Ingenting er ekstrapolert.

Det nærmeste som lot seg måle er en **annen størrelse**, og den kan verken bekrefte eller
avkrefte hypotesen:

| År | Torvs andel av alt kaukolämpö-CHP-brensel |
|---|---:|
| 2023 | **4,61 %** |
| 2024 | **2,90 %** |

Regnet som `Fuels, all` minus `Fuels, separate` i `DH_Regional`, over tre torvkolonner
(*Milled peat*, *Sod peat*, *Peat pellets and briquettes*). **Nevneren er alt CHP-brensel i
kaukolämpö, ikke brenselet i de 21 anleggene.** Den faller fordi torvanleggene krymper, mens
hypotesen handler om at tre fortrenger torv *inne i* de samme anleggene. **To ulike forhold med
ulik nevner. Å lese det ene som belegg for det andre ville vært samme sirkularitet i ny form.**

## C · Dommen på samfyringshypotesen

**IKKE BELAGT.** Hypotesen om at A75 fører hele anleggets produksjon under hovedbrenselet, med en
torvandel som faller 55 → 37 %, står fortsatt bare på gapet den skal forklare.

Den er ikke avkreftet heller. Det som taler for den er strukturelt og indirekte: alle 21
anleggene samfyrer, alle har trebasert reservebrensel, og banen er fysisk plausibel. Det er ikke
måling.

---

# Lauhde-anomalien — LUKKET, og den var ingen anomali

`stat.fi/til/salatuo/kas.html`, definisjonen av **Sähkön erillistuotanto**, ordrett:

> «Sähkön erillistuotannolla tarkoitetaan sähkön tuotantoa pelkästään sähköntuotantoon
> suunnitelluissa lämpövoimalaitoksissa, ydinvoimalaitoksissa, erillistuotantoa kaasuturbiineilla
> ja polttomoottoreilla sekä vesivoimaa ja tuulivoimaa. **Erillistuotantoon sisältyy myös
> yhteistuotantolaitoksissa pienen lämpökuorman aikana ajokohtaisesti erotettu lauhdekuormaa
> vastaava sähköntuotanto sekä lisätuotanto apulauhduttimilla.**»

Erillistuotanto omfatter altså **den kondensdelen av kraftvarmeanlegg som skilles ut driftsvis
ved lav varmelast, og tilleggsproduksjon med hjelpekondensatorer.**

**Registeret og statistikken er ikke i konflikt.** Registeret fører anleggets *type* — alle 21 er
kraftvarme, null dedikert lauhdekapasitet. 13j5 fører *driftsmodus* — de 366/482/106/90 GWh er de
samme anleggene kjørt i kondens ved lav varmelast. **Anomalien er lukket som en feillesning fra
min side.**

Kontrollstreng på siden: `lauhde` **1**, `yhteistuotanto` **4**. Fila er cp1252-kodet; første
lesning ga mojibake og ble gjort om.

---

# A73 — framdrift

**340 av 1 461 døgn** ved skriving, ~7,7 døgn/minutt, feillogg tom (`300 doegn, 300 ok`).
Gjenstående ~2,5 time. **Prosessen kjører og er ikke stoppet.** Ingenting er regnet på det
delvise settet. ~70 %-dekningen er fortsatt ikke reverifisert for 2021–2024.

---

# Dom, rått

**FI står som åpent funn.**

Gapet er målt og robust: A75s torvkolonne er 1,8–2,7 ganger StatFins, og forholdet drifter
monotont. Tre forklaringer er prøvd og felt hver for seg — allokeringsmetoden kansellerer
algebraisk ut av StatFins tall, sammensetningseffekten via lauhde peker feil vei, og
anleggsheterogeniteten forklarer et annet gap enn dette. Den fjerde, samfyring med etikett på
hovedbrenselet, er den eneste som passer alle fire årene — **og den er ikke belagt av noen
uavhengig kilde.**

**Ikke sone to i kapregister ennå.** Forrige runde anbefalte det. Den anbefalingen holder ikke
uten mekanismen: kapregister måler etikett mot virkelighet, og for FI vet vi at *tallene* avviker,
ikke at *etiketten* gjør det. En preregistrering skrevet nå ville låst kriterier rundt en
uverifisert mekanisme — nøyaktig det `PREREG-v1.md` §4 finnes for å hindre.

**Det som mangler er én måling:** brenselsmiks per anlegg per år for de 21. Den finnes ikke i
noen åpen kilde vi har lest. Den ville krevd enten YLVA-uttrekk, eller anleggenes egne
miljørapporter, eller et spørsmål til en kilde — og det siste er utenfor rammen her.

---

# STÅENDE LINJE — skal ikke forsvinne

> **FI-tallet går ikke oppstrøms til codecarbon før tilordningen mellom A75s torvkolonne og
> nasjonal statistikk er avklart.** Tallet flytter seg 12–18 % på den antakelsen alene, og
> utslaget vokser med utfasingen. Dette er en egen gate, uavhengig av #1415 og faktornøklene for
> avfall og biomasse.

---

# Anleggenes egne rapporter — målt, og hypotesen holder ikke

**12.09.2026, tredje runde.** Rådata i `anlegg/rapporter/`.

## A · Dekningsgrad, oppgitt før letingen

De 21 rangert etter el-kapasitet. **Topp 6 = 846,1 MW = 72,2 %** av installert torv-el-kapasitet:
Alholma AK 2 (240), Keljonlahti (190), Seinäjoki SEVO (120), Haapaniemi (118,1), Toppila 2 (98),
Rauhalahti (80). Over halvparten, så øvelsen ble kjørt.

**Kapasitet er ikke produksjon.** Vektene under er MW, ikke GWh, og det er en svakhet i testen som
ikke lar seg rette uten produksjon per anlegg.

## B · Det som faktisk ble funnet

**Alholmens Kraft publiserer per-enhet-tall i sine `Ympäristöraportti`-sider.** Det er den eneste
kilden som gir brenselsmengder per enhet per år. Serien **stopper ved 2021**; 2022–2024 er ikke
publisert.

AK 2, 2021, MWh, ordrett fra rapporten:

| Brensel | MWh | Andel |
|---|---:|---:|
| **Turve** | **597 784** | **32,07 %** |
| Puu | 871 819 | 46,78 % |
| Hiili | 205 838 | 11,04 % |
| REF | 165 610 | 8,89 % |
| Öljy | 12 143 | 0,65 % |
| Peltomassa | 148 | 0,01 % |
| **PA-energia** | **1 863 789** | delsum 99,4 % |

Sähkö 591 405 MWh, kaukolämpö 144 555, prosessihöyry 100 993.

**Kuopion Energia** (Haapaniemi) oppgir torvandel av brenselsforbruket i årsrapporten:
**31,1 % (2021)**, **33,3 % (2022)**, Turve 499,6 og 494,1 GWh, av 1 605 og 1 485 GWh totalt.
For 2023 «uusiutuvien osuus 74 %» og for høsten 2024 «turpeesta (16,4 %)» — **de to siste fra
selskapets nettsider, ikke fra årsrapport-PDF**, og er svakere belagt.

**Oulun Energia** oppgir **turpeen osuus energiantuotannosta 21 % (2022) og 15 % (2023)** — men
nevneren er all energiproduksjon inkludert vann og vind, ikke brensel, og **selskapet har flere
anlegg enn Toppila 2**. Ikke brukt i vektingen.

**Keljonlahti: 25 % torv / 75 % tre** (tidlig 2024), ned fra 70/30 ved oppstart.

**Rauhalahti: 100 % tre siden våren 2022.**

## C · Testen

| År | Anlegg | MW dekket | Dekning | **Målt vektet torvandel** | Implisert | Forhold |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 2 | 358,1 | **30,6 %** | **31,8 %** | 55,0 % | 1,73 |
| 2022 | 2 | 198,1 | 16,9 % | 19,9 % | 55,7 % | 2,81 |
| 2023 | 2 | 198,1 | 16,9 % | 14,3 % | 47,1 % | 3,29 |
| 2024 | 3 | 388,1 | **33,1 %** | **17,2 %** | 37,3 % | 2,16 |

**2022 og 2023 er under en firedel. Ingen dom for de to årene.** 2021 og 2024 klarer grensen.

### Dommen: hypotesen faller i sin enkle form

**Banen faller — 31,8 % → 17,2 %, som er −46 %** mot den impliserte banens −32 %. Retningen
stemmer.

**Nivået gjør det ikke. Den målte torvandelen er omtrent halvparten av den impliserte, begge år
med dekning.**

Det er en kvantitativ avkreftelse, ikke bare et savn. Var den sanne torvandelen 31,8 % i 2021, og
førte A75 hele anleggets produksjon under hovedbrenselet, ville A75s torvkolonne vært
`1 952 / 0,318 = 6 138 GWh`. **A75 sier 3 546.**

**A75 ligger mellom de to:** over StatFins 1 952, godt under helanleggs-bokføringens 6 138.
Verken «A75 = torvtilordnet el» eller «A75 = hele anleggets el» stemmer. Mekanismen er noe
tredje, og den er ikke identifisert.

## D · Ett anlegg som er et funn i seg selv

**Rauhalahti har kjørt 100 % tre siden våren 2022. Energiaviraston voimalaitosrekisteri,
oppdatert 22.05.2026, fører det fortsatt med `Peat` som hovedbrensel.**

Det er fire år gammel etikett mot kjent virkelighet, i et offentlig register — **nøyaktig
kapregister-mekanismen**, målt på ett anlegg i Finland. Det er én observasjon, ikke en
klassifisering av registeret, og det er ikke testet mot de øvrige tjue.

---

# A73 — framdrift

**445 av 1 461 døgn** ved skriving, feillogg ren (`400 doegn, 400 ok`). Gjenstående ~2,2 timer.
**Kjører, ikke stoppet.** Ingenting regnet på det delvise settet. Verken ~70 %-dekningen eller
den nye sjekken — om A73-enhetenes sum matcher A75s torvkolonne eller etterlater ~30 % utilordnet
— er gjort.

---

# Dom: FI er lukket som åpent funn

**Mekanismen er ikke belagt, og den enkle formen av den er avkreftet med tall.**

Gapet står: A75s torvkolonne er 1,8–2,7 ganger StatFins, monotont driftende. Fem forklaringer er
prøvd og felt:

1. **Allokeringsmetoden** — kansellerer algebraisk ut av StatFins tall
2. **Sammensetning via lauhde** — peker feil vei; torv falt raskere fra lauhde enn fra kraftvarme
3. **Anleggsheterogenitet** — forklarer et annet gap, eksakt, men ikke dette
4. **Lauhde-anomalien** — var min feillesning, lukket på StatFins egen definisjon
5. **Samfyring med hovedbrenselsetikett** — riktig retning, **feil nivå med faktor ~2**

### Uttømte kilder, så ingen kjører runden om igjen

| Kilde | Hva den ikke gir |
|---|---|
| EU ETS verifiserte utslipp | ingen biogen kolonne — 77 kolonner, null treff på `BIO`/`SUSTAIN`/`BIOGENIC` |
| Energiaviraston voimalaitosrekisteri | kapasitet og hovedbrensel, **ingen mengder, ingen årstall** |
| YLVA / ympäristöhallinto | myndighetssystem, ikke nedlastbart datasett |
| avoindata.fi | API svarte ikke |
| Energiateollisuus kaukolämpötilasto | NUTS2, fem regioner, ikke anlegg |
| StatFin `salatuo` — seks sider | metoden ikke oppgitt noe sted |
| Eurostat/IEA fellesskjema | pålegger ingen metode; energimetoden kun som fallback |
| Alholmens Kraft ympäristöraportti | per enhet per år — **men serien stopper 2021** |
| Kuopion/Oulun Energia årsrapporter | selskapsnivå; Kuopio ≈ ett anlegg, Oulu ikke |

**Det som gjenstår er ikke en åpen kilde.** Det er enten YLVA-uttrekk, anleggenes egne
miljøtillatelsesrapporter hos ELY, eller et spørsmål til Fingrid som allerede er sendt og
ubesvart siden 11.09. **Ingen av dem lar seg gjøre uten å be noen om noe.**

### Ikke sone to i kapregister

Anbefalingen fra runde én er trukket og blir stående trukket. kapregister måler etikett mot
virkelighet; for FI er det **tallene** som avviker, og mekanismen bak dem er nå eksplisitt
avkreftet i sin enkle form. En preregistrering ville låst kriterier rundt noe vi vet ikke stemmer.

**Rauhalahti-observasjonen hører derimot hjemme i kapregister-rammen** — som ett dokumentert
tilfelle av stale hovedbrenselsetikett i et nasjonalt register, ved siden av Studstrup. Den
krever ingen ny preregistrering for å nevnes; den krever at noen teller de øvrige tjue.

---

# STÅENDE LINJE — uendret

> **FI-tallet går ikke oppstrøms til codecarbon før tilordningen mellom A75s torvkolonne og
> nasjonal statistikk er avklart.** Tallet flytter seg 12–18 % på den antakelsen alene, og
> utslaget vokser med utfasingen. Egen gate, uavhengig av #1415.

Etter denne runden er linja **sterkere**, ikke svakere: vi vet nå at A75 verken fører torvtilordnet
el eller hele anleggets el, og at den sanne torvandelen i anleggene er omtrent halvparten av det
gapet forutsetter. **Tilordningen er ikke bare uavklart — den er uforklart.**

---

# Rettelse til runde tre: Rauhalahti

**Påstanden «Rauhalahti har kjørt 100 % tre siden våren 2022» er trukket.** Den kom fra et
søkesammendrag, ikke fra en lest kilde. Primærkilden — **Yle, 06.02.2026** — sier at torv er
**støttebrensel for tre** ved både Rauhalahti og Keljonlahti, tre måneder før registeret ble
oppdatert. Alvas egne tall gir Rauhalahti **36,5 % torv i 2021 og 21 % i 2022**, ikke null.

**Konsekvens for testen i runde tre:** Rauhalahti inngikk med 0 % i vektingen for 2022, 2023 og
2024. Med 21 % for 2022 blir den vektede torvandelen for det året **26,4 %** framfor 19,9 % —
men 2022 var uansett under dekningsgrensen og bar ingen dom. **For 2024, det ene året med
dekning der Rauhalahti inngikk, er torvandelen ukjent og nullen var en antakelse.** Tallet
17,2 % for 2024 er derfor et **gulv**, ikke et estimat, og forholdet 2,16 mot den impliserte
banen er et **tak**.

**Konklusjonen i runde tre står likevel:** for 2021, der begge anleggene i vektingen har lest,
datert kilde og Rauhalahti ikke inngår, er målt torvandel **31,8 %** mot implisert **55,0 %**.
Nivåavviket på ~1,7× hviler ikke på Rauhalahti.

---

# A73 — framdrift, fjerde runde

**591 av 1 461 døgn**, feillogg ren. Uttrekket **kjører fortsatt** og har ~2,5 time igjen ved
skriving. **Ingenting er regnet på det delvise settet**, etter instruks.

Følgende står dermed ugjort og venter på at uttrekket lander:

1. Reverifisering av dekningsgraden 2021–2024 — hvor stor andel av A75s torvkolonne som lar seg
   tilordne navngitte enheter, per år.
2. Per enhet: kraftvarme eller ren el, og el-andel der den lar seg lese.
3. **Summerer A73-enhetene til A75s torvkolonne, eller er resten de ~30 % som ikke lar seg
   tilordne?** Det er den sjekken som kan skille mellom «A75 fører flere anlegg enn A73 ser» og
   «A75 fører mer per anlegg enn StatFin tilordner» — og den er den eneste gjenstående veien til
   mekanismen fra åpne data.

`a73-raw/` sjekksummes per fil når uttrekket er ferdig, ikke før.

---

# Registersjekken — egen fil

Steg 2 er ført i **`FI-REGISTERSJEKK.md`**. Kort: **tre anlegg byttet brensel før registerets
oppdateringsdato uten at etiketten fulgte etter** — Joensuu (siste torv 29.12.2025), Iisalmi og
Pieksämäki (våren 2025). Alle tre er Savon Voimas, dokumentert av **én pressemelding fra
operatøren selv**, ikke av tre uavhengige kilder.

**Terskelen på tre er nådd, men grunnlaget er smalere enn det danske.** Anbefalingen er å ikke
skrive preregistreringen før minst én annen operatør er dokumentert på samme måte.

---

# Registersporet lukket — femte runde

**Bare Savon Voima.** Ingen fjerde urevidert hos en annen operatør lot seg belegge med lest,
datert kilde. Detaljene i `FI-REGISTERSJEKK.md`; kort:

- **Endelig dekning: 9 av 21 anlegg med datert kilde som er lest — 71,5 % av kapasiteten.**
  Tre byttet uten at registeret fulgte (Savon Voima), seks brenner fortsatt torv.
- **Tornio er det klareste «fortsatt torv»:** 44,9 % av levert energi i 2025, fra Tornion
  Energias egen side.
- **Aittaluoto (Pori Energia) er den eneste reelle kandidaten til en fjerde**, og den falt på at
  primærkilden ga 404 to ganger — ikke på at påstanden ble motbevist. **Den står åpen.**
- **Ingen preregistrering skrives.** Kriteriet «minst to uavhengige operatører» er ikke innfridd.

**Og et tredje søkesammendrag falt:** «SEVO, turve yli 90 % polttoaineesta» stammer fra en
YVA-arviointiohjelma **innkommet 27.6.2008**. Atten år gammelt, presentert som nåværende.

---

# Rauhalahti-rettelsen — gjentatt her fordi den endrer et tall

**Påstanden «Rauhalahti har kjørt 100 % tre siden våren 2022» er trukket.** Kilden var et
søkesammendrag. **Yle, 06.02.2026**, ordrett: «Tällä hetkellä Keljonlahden ja Rauhalahden
voimalaitoksissa **turve toimii tukipolttoaineena puulle**.» Alvas egne tall gir Rauhalahti
36,5 % torv i 2021 og 21 % i 2022.

**Konsekvens for runde tre, eksplisitt:** Rauhalahti inngikk med **0 %** i vektingen for 2022,
2023 og 2024. **Tallet 17,2 % for 2024 er derfor et GULV, ikke et estimat**, og forholdet 2,16
mot den impliserte banen er et **TAK**. Rauhalahtis faktiske torvandel for 2024 er ukjent.

**2021-resultatet står urørt:** der er begge anleggene i vektingen lest og datert, Rauhalahti
inngår ikke, og målt torvandel **31,8 %** mot implisert **55,0 %** hviler ikke på feilen.

---

# A73 — status ved femte runde

**752 av 1 461 døgn** (51 %), feillogg ren, **kjører**. ~2 timer igjen. **Ingenting regnet på
det delvise settet.**

Det som venter, uendret: dekningsgrad per år · CHP eller ren el per enhet · og hovedsaken —
**summerer A73-enhetene til A75s torvkolonne, eller står ~30 % utilordnet?** Er resten stor og
stabil, ligger mekanismen der. Er den liten, er kolonnen i hovedsak tilordnet navngitte enheter
og el-andelen per enhet kan regnes direkte.

`a73-raw/` sjekksummes per fil når uttrekket er ferdig.

---

# A73 LANDET — og mekanismen lar seg lese

**1 461 av 1 461 døgn, 0 feil, 36 unike enheter.** Parset med varighetsvekting, stegkurve A03,
manglende posisjoner viderefører forrige verdi. `a73-per-enhet.json` bærer resultatet.

## Dekningen er 55–62 %, ikke ~70 %

| År | A73-torvenheter | A73 sum GWh | A75 torvkolonne | **Dekning** | Utilordnet |
|---|---:|---:|---:|---:|---:|
| 2021 | 5 | 1 983,9 | 3 546,5 | **55,9 %** | 1 562,6 (44,1 %) |
| 2022 | 5 | 2 219,1 | 3 609,9 | **61,5 %** | 1 390,8 (38,5 %) |
| 2023 | 5 | 1 245,4 | 2 269,5 | **54,9 %** | 1 024,1 (45,1 %) |
| 2024 | 5 | 1 120,5 | 1 836,5 | **61,0 %** | 715,9 (39,0 %) |

**MASTERs ~70 % gjaldt 2025 alene. For 2021–2024 er den 55–62 %, og den er stabil.**

De fem enhetene er **Alholmens B2, Keljonlahti B1, Seinäjoki B1, Toppila B2** og **Haapavesi B1**,
som produserer **0,0 GWh i alle fire år** — samme nullresultat som for 2025. **Alle fem er
kraftvarme**; ingen ren kondensenhet fører torv i A73. Det stemmer med registeret, som har null
MW torvfyrt lauhdekapasitet.

**Resten — 39–45 % — er stor og stabil.** Den svarer omtrent til kapasitetsandelen til de
torvanleggene som ligger under A73s rapporteringsgrense: de fem A73-enhetene utgjør rundt 55 % av
de 1 171,9 MW i registeret. **Det er altså ikke en uforklart rest. Det er de små anleggene.**

## Enhetstesten: mekanismen, målt

**Alholmens AK 2, 2021.** Anleggets egen `Ympäristöraportti 2021` mot A73:

| | GWh |
|---|---:|
| **A73 fører under `Fossil Peat`** | **664,2** |
| Anleggets hele elproduksjon, egen rapport | 591,4 |
| Torvtilordnet el (591,4 × 32,07 %) | **189,7** |

- **A73 / torvtilordnet = 3,50**
- **A73 / hele produksjonen = 1,12**
- Implisert torvandel av A73-tallet: **28,6 %** — mot **32,07 %** målt i anleggets eget regnskap

**A73 fører i praksis hele enhetens elproduksjon under hovedbrenselet.** Den impliserte
torvandelen treffer den målte innenfor 11 %.

**Overskuddet på 12 % over anleggets egen tall er ikke forklart.** Mest sannsynlig brutto mot
netto — en 240 MW kraftvarmeenhet bruker lett 10 % selv — men det er en antakelse, ikke en måling.
Det svekker ikke hovedpunktet: 664 mot 190 er en faktor 3,5, og 12 % forklarer ikke den.

## Hva dette gjør med hele sporet

**Mekanismen er tilordning på anleggsnivå, ikke allokering mellom el og varme.** A75 og A73 bokfører
enhetens samlede produksjon under enhetens registrerte hovedbrensel. StatFin fordeler etter
brenselsandel. Forholdet mellom dem er derfor omtrent én delt på torvandelen — og torvandelen faller
når tre fortrenger torv i de samme kjelene.

**Og det retter min egen feil fra runde tre.** Den impliserte torvandelen på 55,0 → 37,3 % ble
regnet som `StatFin / A75`. Men A75s kolonne inneholder også de **39–45 %** som kommer fra anlegg
under A73-grensen. Nevneren var for stor, så den impliserte andelen ble for høy. **Regnet på de
navngitte enhetene alene, der begge tall gjelder samme anlegg, treffer den målte torvandelen.**

Det var derfor «målt ~30 % mot implisert ~55 %» så ut som en avkreftelse i runde tre. **Det var
ikke hypotesen som var gal. Det var basen jeg regnet den på.**

---

# LÆRDOM — søkesammendrag bærer ikke alder

**Tre ganger i dette sporet har et søkesammendrag båret noe som ikke tålte å leses:**

| Påstand fra sammendrag | Hva primærkilden sa |
|---|---|
| «Rauhalahti 100 % tre siden våren 2022» | Yle 06.02.2026: torv er **støttebrensel**. Alva: 21 % torv i 2022 |
| «SEVO turve yli 90 % polttoaineesta» | Tallet er fra en **YVA-arviointiohjelma innkommet 27.6.2008** — atten år gammelt |
| «Aittaluoto avviklet torv i 2022» | **Aldri lest.** Tre hentinger, tre 404 |

**Regel, ført som stående:**

> **Et søkesammendrag bærer ikke alder.** Det gjengir en setning uten å si når den ble skrevet,
> og et attenårig tall leses som et nåværende. **Alt som ikke er lest i primærkilden føres som
> udatert — uansett hvor presist sammendraget lyder.** En påstand er lest eller den finnes ikke.

Den første av de tre gikk inn i en levert rapport før den ble fanget.

---

# De fire andre enhetene — mønsteret testet

## Enhetene, med EIC og årssummer under `Fossil Peat`, GWh

| EIC | Navn | 2021 | 2022 | 2023 | 2024 | Andel av A73-torv |
|---|---|---:|---:|---:|---:|---:|
| `44W-T-YT-100021D` | Alholmens B2 | 664,2 | 891,7 | 317,6 | 285,1 | 32,9 % |
| `44W-T-YT-1000239` | Keljonlahti B1 | 529,5 | 657,1 | 502,6 | 429,5 | 32,3 % |
| `44W-T-YT-100011G` | Seinäjoki B1 | 534,8 | 452,9 | 166,1 | 177,3 | 20,3 % |
| `44W-T-YT-1000166` | Toppila B2 | 255,4 | 217,3 | 259,2 | 228,6 | 14,6 % |
| `44W-T-LV-1000086` | Haapavesi B1 | **0,0** | **0,0** | **0,0** | **0,0** | 0,0 % |

**Haapavesi B1 er ført som null, ikke som manglende.** Enheten rapporterer, og den rapporterer
null, hvert døgn i fire år.

**En rettelse til oppdraget:** Kuopios Haapaniemi **er ikke blant A73s torvenheter**. Tallene
31,1 % og 33,3 % kan derfor ikke brukes i denne testen — det finnes ingen A73-serie å holde dem
mot. Haapaniemi mangler i A73 til tross for 118,1 MW i registeret og 145 MW i A71.

## Det som ikke lot seg skaffe

**Anleggsvis elproduksjon per år finnes ikke i åpne kilder for Keljonlahti, Seinäjoki eller
Toppila 2.** Søkt; ingen treff med tall. Det som fantes var aldret og ubrukelig:
«Toppila 2: 70 % turvetta, 30 % biopolttoaineita» — **fra 2014**, tolv år gammelt. Samme felle
som SEVO-tallet fra 2008.

Den direkte testen mot anleggets eget regnskap står derfor fortsatt bare for **AK 2**.

## Men to andre tester avgjør mønsteret

### Test 1 — ingen enhet bærer to produksjonstyper

**Av 36 finske A73-enheter har 0 mer enn én `psrType`.** Hver enhet bærer nøyaktig én type
gjennom alle 1 461 døgn. **A73 fordeler ikke samfyrt produksjon mellom brensler.** Det er ikke en
tolkning — det er strukturen i dataene.

### Test 2 — brukstiden gjør torvandels-lesningen fysisk umulig

Leses A73-tallet som hele enhetens produksjon, gir det brukstider på **13–49 %** — normalt for
kraftvarme. Leses det som en torvandel på typiske 30 %, må enhetens virkelige produksjon ha vært
3,3 ganger så stor:

| Enhet | MW | År | A73 GWh | Brukstid som hel prod. | **Brukstid hvis A73 var 30 %-andel** |
|---|---:|---|---:|---:|---:|
| Seinäjoki B1 | 125 | 2021 | 534,8 | 48,8 % | **162,8 %** |
| Alholmens B2 | 240 | 2022 | 891,7 | 42,4 % | **141,4 %** |
| Seinäjoki B1 | 125 | 2022 | 452,9 | 41,4 % | **137,9 %** |
| Keljonlahti B1 | 190 | 2022 | 657,1 | 39,5 % | **131,6 %** |
| Alholmens B2 | 240 | 2021 | 664,2 | 31,6 % | **105,3 %** |
| Keljonlahti B1 | 190 | 2021 | 529,5 | 31,8 % | **106,0 %** |
| Toppila B2 | 98 | 2023 | 259,2 | 30,2 % | **100,6 %** |

**Brukstid over 100 % er fysisk umulig.** Torvandels-lesningen er utelukket for **tre enheter i to
år hver**, med god margin for Seinäjoki. Kapasitetene er hentet fra Energiaviraston register, og
for Seinäjoki er selskapets egen høyere verdi (125 MW mot registerets 120) brukt — altså i
lesningens favør.

## Dekningsgrad for testen

| Test | Enheter | Andel av A73-torvsummen |
|---|---:|---:|
| Direkte mot anleggets eget regnskap | **1** (AK 2) | 32,9 % |
| Brukstidstesten | **4** (alle med produksjon) | **100 %** |
| Én-psrType-strukturen | **36** (alle FI-enheter) | 100 % |

---

# Overskuddet på 12 % — hypotesen felt, avviket står

AK 2 ga 664,2 GWh i A73 mot 591,4 GWh i anleggets egen rapport. Jeg antok brutto mot netto.

**ENTSO-E rapporterer NETTO.** Fra arXiv:2311.01103, ordrett: «ENTSO-E provides data on the
Aggregated Generation per Type (AGPT), i.e. the **net electricity production** per individual
energy carrier/generation technology».

**Da går fortegnet feil vei.** Var anleggets tall brutto og A73 netto, skulle A73 ligget *lavere*.
**Brutto-mot-netto er utelukket som forklaring.**

Det som står igjen som kandidat — og det er en kandidat, ikke en måling — er at anleggets
`Sähkö 591 405 MWh` kan være **levert** elektrisitet, altså etter eget forbruk, mens A73 er
generert netto ved generatoren. **Ikke verifisert. Avviket på 12 % er uforklart**, og det skal
stå slik til noen har lest ENTSO-Es egen definisjonstekst for A73, som ga HTTP 400 ved henting.

**Det svekker ikke hovedfunnet:** 664 mot 190 er en faktor 3,5, og 12 % forklarer ikke den.

---

# DOM: mønsteret holder på fire enheter

**FI-mekanismen er bevist.**

- **Direkte målt på én enhet** — AK 2, mot anleggets eget brenselsregnskap: A73 fører 3,50 ganger
  den torvtilordnede elen, og 1,12 ganger hele produksjonen.
- **Strukturelt utelukket for alle 36** — ingen enhet bærer to produksjonstyper i noe døgn.
- **Fysisk utelukket for fire** — torvandels-lesningen krever brukstider over 100 %.

**A75 og A73 bokfører enhetens samlede produksjon under enhetens registrerte hovedbrensel.**
StatFin fordeler etter brenselsandel. Forholdet mellom dem er derfor omtrent én delt på
torvandelen, og det vokser når tre fortrenger torv i de samme kjelene.

## Hva det gjør med rammen

**DK og FI er to akser av samme funn, og det endrer rammen for kapregister.**

| | DK | FI |
|---|---|---|
| Registrert type | `Fossil Hard coal` | `Fossil Peat` |
| Virkelighet | anlegget er **konvertert** | anlegget **samfyrer** |
| Feilen | etiketten ble aldri endret | hele produksjonen føres under én etikett |
| Måles på | typeendring mellom årganger (14.1.B) | produksjon per enhet mot brenselsmiks (A73) |
| Effekt på A75 | feil kolonne | riktig kolonne, for stort tall |

**kapregister v1.0.0 måler bare den første.** Kriteriene i `PREREG-v1.md` §4 er definert på
typeendring, og de kan ikke fange den finske aksen — der skjer det ingen typeendring i det hele
tatt. **Det er derfor FI krever egen preregistrering, og hvorfor den ikke kunne smugles inn.**

**Men det gjør også noe med det danske funnet:** om A75 bokfører hele enheten under hovedbrenselet
også i Danmark, er DK2-tallene ikke bare feil etikett — de er feil etikett **på en mengde som selv
er for stor**. Det er ikke målt, og det er den neste tråden.

