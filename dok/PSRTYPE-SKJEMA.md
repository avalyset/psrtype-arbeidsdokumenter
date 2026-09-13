# Én psrType per enhet — er det skjemaet?

> **Deponert arbeidsdokument.** Skrevet under arbeidet med `psrtype-samfyring` og
> `kapregister`, og deponert her uendret bortsett fra at lokale filstier er erstattet
> med relative navn. Utsagn om publiseringsstatus, åpne løkker og «ingen DOI» gjelder
> skrivetidspunktet, ikke i dag. Tallene er dem manuskriptene viser til.


**12.09.2026.** Hypotesen: A73 tilordner hver produksjonsenhet nøyaktig én `psrType`, uansett
faktisk brenselsmiks. Da kan plattformen ikke representere samfyring.

---

## 1 · Tellingen

**Utvalgsdesign, fastsatt før henting:** den **15. i hver måned 2023**, tolv døgn per sone.
Det er en **stikkprøve**, ikke et sensus. Unntaket er Finland, som er talt over **alle 1 461 døgn
2021–2024**. Rådata som XML til disk før parsing.

### Soner som publiserer A73

| Sone | Døgn | Enheter | **>1 psrType noensinne** |
|---|---:|---:|---:|
| AT | 12 | 35 | 0 |
| BE | 12 | 46 | 0 |
| CZ | 12 | 39 | 0 |
| **ES** | 12 | 173 | **11** |
| **FI** | **1 461** | 36 | 0 |
| FR | 12 | 151 | 0 |
| IT | 12 | 163 | 0 |
| NL | 12 | 43 | 0 |
| PL | 12 | 120 | 0 |
| PT | 12 | 73 | 0 |
| **Sum** | | **879** | **11** |

### Soner som ikke publiserer A73

**DE-LU, DE-AT-LU, DK1, GB, IE_SEM, SE3** — alle **12 av 12 døgn** med
`Acknowledgement_MarketDocument`, kode **999**:

> «No matching data found for Data item **ACTUAL_GENERATION_OUTPUT_PER_UNIT_R3 [16.1.A]**»

Sammen med DK2 og landsdomenet DK fra `kapregister/adr/0001` er det **åtte soner uten A73**.

---

## 2 · De elleve spanske — og hva de faktisk viser

**MUELA 1G–7G og SALLENT 1G–4G**, alle `Hydro Pumped Storage` **og** `Hydro Water Reservoir`.

**Men ikke samtidig.** MUELA 1G, døgn for døgn:

| Måned 2023 | psrType |
|---|---|
| januar, februar | `Hydro Water Reservoir` |
| mars–desember | `Hydro Pumped Storage` |

**Det er en omklassifisering over tid, ikke en fordeling av samtidig produksjon.**

Og det er **den samme omklassifiseringen kapregister allerede har målt i 14.1.B**: ES har
syv typeendringer 2019→2025, alle `Hydro Water Reservoir → Hydro Pumped Storage`, deriblant
MUELA G og SALLENT G. **Registerendringen forplanter seg til A73.**

### Den avgjørende testen

**Kan én EIC bære to `psrType` i samme dokument — altså samme døgn?**

| Materiale | Dokumenter | Enheter | **To psrTypes i samme dokument** |
|---|---:|---:|---:|
| 10 soner, 12 døgn hver | 108 | 843 | **0** |
| FI, sensus 2021–2024 | 1 461 | 36 | **0** |
| **Sum** | **1 569** | **879** | **0** |

**Ingen enhet bærer to produksjonstyper samtidig, i noen sone, i noe døgn.**

---

## 3 · ENTSO-Es egen dokumentasjon

**Manual of Procedures V2R1**, 42 444 tegn. Talt med Python:

| Term | Treff |
|---|---:|
| `co-firing`, `cofiring`, `co-fired` | **0, 0, 0** |
| `mixed fuel`, `multi-fuel`, `multiple production` | **0, 0, 0** |
| `secondary fuel`, `main fuel`, `primary fuel` | **0, 0, 0** |
| `fuel mix`, `psrtype`, `psr type` | **0, 0, 0** |
| *kontrollstreng* `transparency` | **133** |
| *kontrollstreng* `production type` | **7** |

**Alle tolv flerbrenselstermer er null, mot kontrollstrenger som treffer.** Samme form som
`CHP` 0 og `heat` 0 i forrige runde. **Fraværet er dokumentert, ikke antatt.**

**ENTSO-Es egne datavisningssider lot seg ikke hente.** `Data-view Production and Generation
Units` og `Data-view Actual Generation per Production Unit` ga **HTTP 400** mot både `curl` og
renderende henting. **XSD-en er dermed ikke lest**, og det har en konsekvens som står under.

---

## 4 · Fortegnet

Fra `kapregister/data/kapregister-2019-2025.csv`, 1 593 rader, **22 typeendringer, 19 unike**:

| Retning | Antall |
|---|---:|
| fossil → bio | **4** (Naantali, Amer, Värtaverket, BÖRZE) |
| fossil → fossil | 4 (Mellach, Scholven, KW Hastedt, Hemweg — alle kull → gass) |
| ingen brenselsakse | 11 (ES-hydro ×7, GB vind, HU ×2, BE) |
| **BIO → FOSSIL** | **0** |

**Ingen registrert typeendring går mot fossilt.** Ett dokumentert tilfelle ville felt
fortegnspåstanden; det finnes ikke i dette materialet.

**Presisering:** dette måler retningen på **registerendringer som faktisk skjedde**, ikke på
feilen. Fortegnsargumentet er: anlegg konverterer fossil → bio, etiketten henger etter, og en
etterslepende etikett teller derfor **for mye fossilt**. Siden ingen konvertering går motsatt vei
i de 55 domenene, kan etterslepet bare feile i én retning. **Det er et utsagn om 19 endringer i
55 domener, ikke et universelt.**

---

## 5 · Dom

**Det første utfallet, men med en skarpere formulering enn hypotesen ba om.**

**Ingen av 879 enheter i ti soner bærer to produksjonstyper samtidig.** Ikke én gang i 1 569
dokumenter. **Plattformen representerer ikke samfyring per enhet.**

**Men det er ikke bevist at skjemaet forbyr det.** De elleve spanske enhetene viser at verdien
**kan endres over tid**, så modellen er ikke frosset. Om XML-skjemaet tillater to `TimeSeries`
for samme EIC med ulik `psrType` i samme dokument, vet jeg ikke — **XSD-en ga HTTP 400 og er ikke
lest.**

**Skillet er reelt og skal stå:**

- **Målt:** det skjer aldri, i 1 569 dokumenter, 879 enheter, ti soner.
- **Ikke målt:** om det er umulig eller bare aldri gjort.

Det er forskjellen mellom **strukturell begrensning** og **rapporteringspraksis**, og den avgjøres
av et dokument jeg ikke fikk hentet. **Uten det er funnet «det skjer ikke», ikke «det kan ikke
skje».**

### Hva som følger uansett

Samfyrte anlegg **kan ikke representeres riktig i A73 slik plattformen faktisk brukes**. Det
gjelder minst de ti sonene her, og det gjelder alle brensler — ikke bare torv og kull.

**Det er et større funn enn DK og FI hver for seg.** De to er tilfeller av det; dette er
mønsteret. Men det er ikke det største funnet det kunne vært, fordi skjemaspørsmålet står åpent.

### Drax lar seg ikke sjekke

**GB publiserer ikke A73.** Europas største biomassekonvertering kan ikke undersøkes på
enhetsaksen i det hele tatt — verken for å bekrefte eller avkrefte mønsteret.

---

## Omfang, oppgitt uten generalisering

**Testet: 879 enheter i ti soner** — AT, BE, CZ, ES, FI, FR, IT, NL, PL, PT.
**Ikke testet: åtte soner uten A73** — DE-LU, DE-AT-LU, DK1, DK2, DK, GB, IE_SEM, SE3.
**Utvalget er tolv døgn per sone**, unntatt Finland med 1 461.

**Ingenting her gjelder soner eller døgn utenfor det.**

---

# XSD-en — avgjort. Det er PRAKSIS, ikke skjema

**Ett forsøk. Kilden er ENTSO-Es eget skjemadokument**, `Generation Load document and schema v1`,
hentet fra `eepublicdownloads.entsoe.eu/clean-documents/EDI/Library/cim_based/schema/`.
588 944 B, 22 sider, **hele XSD-en gjengitt i dokumentet**.

Kontroll på at skjemaet faktisk er der: `xs:element` **38**, `xs:complexType` **24**,
`minOccurs` **37**, `maxOccurs` **37**, `</xs:schema>` **1**.

## Kardinalitetene, ordrett fra XSD-en

```xml
<xs:element name="TimeSeries"            type="TimeSeries"       minOccurs="1" maxOccurs="unbounded"/>
<xs:element name="MktPSRType"            type="MktPSRType"       minOccurs="0" maxOccurs="1"/>
<xs:element name="psrType"               type="PsrType_String"   minOccurs="1" maxOccurs="1"/>
<xs:element name="PowerSystemResources"  type="MktGeneratingUnit" minOccurs="0" maxOccurs="unbounded"/>
<xs:element name="registeredResource.mRID" type="ResourceID_String" minOccurs="0" maxOccurs="1"/>
```

**Nøyaktig den strukturen spørsmålet forutsatte:** `MktPSRType` er **1..1 per TimeSeries**
(0..1, med `psrType` obligatorisk inni), og `TimeSeries` er **1..unbounded per dokument**.

## Og det finnes ingen unikhetsbetingelse

| Betingelse | Forekomster i XSD-en |
|---|---:|
| `xs:unique` | **0** |
| `xs:key` | **0** |
| `xs:keyref` | **0** |
| `xs:selector`, `xs:field`, `xs:assert` | **0, 0, 0** |
| `xs:ID` | **0** |

Ordet «unique» forekommer åtte ganger i dokumentet — **alle åtte i prosabeskrivelser av
attributter** («The unique identification of a resource», «The unique identification of the
document»), **ingen som skjemabetingelse**.

## Og dataene bekrefter det

**1 190 tilfeller** i de 1 569 dokumentene der **samme EIC har mer enn én `TimeSeries` i samme
dokument.** Gjentakelse av `PowerSystemResources/mRID` forekommer altså rutinemessig og avvises
ikke.

I alle observerte tilfeller bærer de gjentatte seriene **samme** `psrType`. Men siden `psrType`
ligger inne i hver `TimeSeries` uavhengig, og ingen `xs:unique` binder dem sammen, **er to
TimeSeries med samme EIC og ulik psrType skjemagyldige.**

---

# Dommen, revidert

**Forrige rundes forbehold er opphevet, og konklusjonen er den andre av de to.**

| | Utfall |
|---|---|
| Tillater skjemaet flere psrTypes per enhet i samme dokument? | **JA** |
| Skjer det i noen av de 879 enhetene i ti soner? | **NEI — null ganger i 1 569 dokumenter** |

**Det er ikke en strukturell begrensning i ENTSO-Es datamodell. Det er rapporteringspraksis.**

## Hva det gjør med påstanden

**Svakere om plattformen. Sterkere om etterlevelsen.**

Funnet er ikke lenger «ENTSO-E kan ikke representere samfyring». Det er:

> **Plattformen tillater å representere samfyring per enhet. Ingen av de ti sonene gjør det —
> ikke i ett eneste av 1 569 dokumenter, for 879 enheter.**

Det peker på **ENTSO-E som ikke krever det**, og på TSO-ene som ikke gjør det uoppfordret — ikke
på et skjema som stenger for det. Og det flytter spørsmålet fra datamodell til
**rapporteringskrav**: `Manual of Procedures` nevner ingen av tolv flerbrenselstermer, så det
finnes ingen regel som sier hvordan et samfyrt anlegg skal føres. **Fraværet av en regel er det
som produserer praksisen.**

## Hva som følger for DK og FI

**Uendret i substans, endret i innramming.** De to er fortsatt tilfeller av at hele enhetens
produksjon føres under én etikett. Men det kan ikke lenger beskrives som en tvang plattformen
pålegger. **Det er et valg hver rapporterende part tar, og som ingen regel hindrer dem i å ta
annerledes.**

Det gjør funnet mer anvendelig, ikke mindre: **en TSO som ville rapportere samfyring riktig,
kunne gjøre det i morgen uten noen skjemaendring.**

---

# SANITY — de fire premissene testet. To falt.

**12.09.2026.** Ingenting fryses. Dette er en revisjon av rundene over, ikke en utvidelse.

## §2 · De 1 190 beviser ikke det de ble brukt til — FALT

Alle 1 190 tilfellene er klassifisert. **1 190 av 1 190 er retningssplitt:** én `TimeSeries` med
`inBiddingZone_Domain` (generering) og én med `outBiddingZone_Domain` (forbruk/pumping), med
**samme `psrType`** i begge.

```
GRAND MAISON 1   TS  25   bt=A01  psr=B10  inBZ=10YFR-RTE------C   10:00Z → 12:00Z
                 TS 133   bt=A01  psr=B10  outBZ=10YFR-RTE------C  00:00Z → 10:00Z
FR_LANDIVISIAUGU TS   1   bt=A01  psr=B04  inBZ=...                hele døgnet
                 TS 128   bt=A01  psr=B04  outBZ=...               hele døgnet
```

Fordelingen: **ulik retning 1 190 · ulik psrType 0 · ulik businessType 0 · oppdelt tidsakse 0.**

**Null parallelle genereringsserier for samme enhet.** Gjentakelsen av `PowerSystemResources/mRID`
er en retningsdistinksjon, ikke et bevis på at mekanismen brukes for to samtidige
produksjonsserier.

**Setningen «Og dataene bekrefter det» i avsnittet over er trukket.** XSD-halvdelen står —
`xs:unique` 0, `xs:key` 0, kardinalitetene sitert ordrett — men den empiriske halvdelen bar ikke
vekten den fikk.

## §1 · Premisset er belagt for ÉN av ti soner — FALT for de ni

**Finland: ja, primærkilde, datert.** Alholmens Kraft `Ympäristöraportti 2021`, AK 2:

| Brensel | MWh |
|---|---:|
| Turve | 597 784 |
| Puu | 871 819 |
| Hiili | 205 838 |
| REF | 165 610 |

**Fire brensler i samme enhet samme år.** Det er samfyring, lest og datert.

**De ni andre: ikke belagt.** Kilden jeg fant er Embers *«Something nasty in the woodshed»* —
**datert 6. oktober 2017**, med 2015-tall. Den oppgir at Polen, Finland, Danmark, Tsjekkia og
Ungarn stod for over 88 % av europeisk samfyring, og at Finland alene har over 70
samfyringsenheter. **Det er en nioårig sekundærkilde**, og etter regelen som er brukt tre ganger
i dette sporet teller den ikke som belegg.

`IEA Bioenergy Finland 2024`, 49 128 tegn, hentet og lest: `co-fir` **0**, `cofir` **0**,
`co-combustion` **0**, `multi-fuel` **0** — mot kontrollstreng `bioenergy` 44, `biomass` 35.
**Landrapporten bruker ikke begrepet i det hele tatt.**

**Konsekvens:** «879 enheter i ti soner, null representasjon» forutsetter at det fantes noe å
representere. **Det er belagt for FI (36 enheter). For AT, BE, CZ, ES, FR, IT, NL, PL og PT er
det ikke belagt, og de skal ut av tellingen — ikke telles som null.**

## §3 · Stikkprøven holder for det den tester — STÅR, med et presist forbehold

**Sensus for ES, 2023: 365 av 365 døgn hentet, 0 feil.**

| | Døgn | Enheter | >1 psrType | **To psrTypes samme døgn** |
|---|---:|---:|---:|---:|
| Stikkprøve | 12 | 173 | 11 | **0** |
| **Sensus** | **365** | **174** | **11** | **0** |

**Stikkprøven mistet null enheter. Deteksjonsrate 100 %.** Og sensus bekrefter hovednegativet:
**null tilfeller av to produksjonstyper samme døgn i 365 døgn.**

### Men styrken er ikke universell, og det skal stå

De elleve ES-enhetene bærer `B10` i 312 døgn og `B12` i 53. Den sjeldneste tilstanden varer
**14,5 % av året**, og tolv tilfeldige døgn ville bommet på den med **15,2 %** sannsynlighet.
Den ble fanget fordi den var sammenhengende i januar–februar, og utvalget inneholder 15. januar
og 15. februar.

**Mot kortvarige hendelser er stikkprøven svak:**

| Varighet | Sannsynlighet for at 12 døgn bommer |
|---|---:|
| 1 døgn | 96,8 % |
| 7 døgn | 79,3 % |
| 30 døgn | 35,7 % |

**Men mot fenomenet som faktisk testes, er den sterk.** Et samfyrt anlegg som rapporterte begge
brensler ville gjort det hver dag det samfyrer — ikke én gang i året:

| Andel døgn med dobbeltføring | Sannsynlighet for at 12 døgn bommer |
|---|---:|
| 25 % | 3,17 % |
| 50 % | 0,024 % |
| 80 % | ~0 |

**Tellingen er gyldig for et vedvarende fenomen og usikker for et sjeldent.** Samfyring er
vedvarende. **Stikkprøven er forsvart for spørsmålet den ble stilt.**

## §4 · Regelen finnes ikke i noe ENTSO-E-dokument jeg har lest — STÅR

To uavhengige ENTSO-E-dokumenter, begge lest i sin helhet:

| Dokument | Tegn | Tolv flerbrenselstermer | Kontrollstreng |
|---|---:|---:|---|
| `Manual of Procedures V2R1` | 42 444 | **alle 0** | `transparency` 133, `production type` 7 |
| `Generation Load document and schema v1` | 43 532 | **alle 0** | `psrType` 31, `TimeSeries` 36 |

I skjemadokumentet er også `predominant` og `dominant` **0**.

**Ingen regel om hovedbrensel, samfyring eller flerbrenselanlegg er funnet.** «Fraværet av en
regel produserer praksisen» står.

---

# DOM

## Hva som står

1. **XSD-en tillater det.** `TimeSeries` er 1..unbounded, `MktPSRType` 0..1 per TimeSeries med
   `psrType` 1..1 inni, `PowerSystemResources` 0..unbounded, og **ingen `xs:unique`, `xs:key`
   eller `xs:keyref` finnes.** Sitert ordrett fra ENTSO-Es eget skjemadokument. **Det er praksis,
   ikke struktur.**
2. **Ingen regel finnes** i verken MoP eller skjemadokumentet.
3. **Stikkprøven er metodisk forsvart** for et vedvarende fenomen, verifisert mot sensus i ES med
   100 % deteksjon.
4. **For Finland er hele kjeden hel:** samfyring belagt i primærkilde, 36 enheter, sensus over
   1 461 døgn, **null dobbeltføring**.

## Hva som falt

1. **«De 1 190 bekrefter at mekanismen brukes.»** Nei — alle er retningssplitt. Trukket.
2. **«Ti soner, 879 enheter.»** Omfanget krymper til de sonene der samfyring er belagt.
   **Det er én: Finland, 36 enheter.** De øvrige 843 er talt, men uten belagt premiss.

## Hva funnet er nå

> **ENTSO-Es skjema tillater å rapportere flere produksjonstyper for samme enhet. I Finland, der
> samfyring er dokumentert i primærkilde for minst ett stort anlegg, skjer det ikke i noen av 36
> enheter over 1 461 døgn. Ingen regel i ENTSO-Es dokumentasjon krever det.**

Det er et smalere funn enn forrige runde påsto, og det er det som bæres av materialet.

**De 843 enhetene i ni andre soner er ikke et null-resultat — de er et ubelagt resultat.** For å
gjøre dem til evidens må samfyring dokumenteres per sone med dateret primærkilde. **Ember 2017
holder ikke.**

## Hva DK og FI står som

Uendret. Hel-enhets-tilordning er bevist for Alholmens AK 2 og avkoblingsmålt for DK2. **Det
funnet hviler ikke på psrType-tellingen** og berøres ikke av at omfanget krymper.

**Ingenting fryses. Ingen prereg, ingen repo, ingen DOI.**

