# psrtype-arbeidsdokumenter

**Arbeidsdokumentene bak to preregistrerte målinger av produksjonstypemerking i ENTSO-Es
Transparency Platform.** Dette er ikke en ny måling. Det er filene som *bærer tall* som de to
frosne datasettene og de to manuskriptene viser til, men som ikke selv er del av noen av dem.

De to datasettene:

| Datasett | Konsept-DOI | Hva det inneholder |
|---|---|---|
| [`psrtype-samfyring`](https://github.com/avalyset/psrtype-samfyring) | [10.5281/zenodo.22726238](https://doi.org/10.5281/zenodo.22726238) | samtidig flerbrenselrapportering; konsistenstest A73 mot A75 |
| [`kapregister`](https://github.com/avalyset/kapregister) | [10.5281/zenodo.22722721](https://doi.org/10.5281/zenodo.22722721) | typeendring mellom registerårganger; vedvarende feilklassifisering |

**Ingen preregistrering hører til dette depotet.** Det er dokumentasjon, ikke måling. Kriteriene
som styrer målingene ligger låst og sjekksummet i de to datasettene, og de er ikke rørt her.

---

## Hva som ligger her

### `dok/` — arbeidsdokumentene

| Fil | Bærer blant annet |
|---|---|
| `RAPPORT-A75-2026-09-12.md` | negative kontroller (§2.4): kjernekraft **0,99–1,00×**, vind **0,94–0,98×**; fransk kjernekraft **1,99× → 0,996–0,997×** etter at éCO2mix-feltets oppløsning ble fastslått; massebevaring (§2.2) |
| `DK-KULL-TIDSSERIE.md` | A75 kull mot Energinet 2019–2025, **1,003–1,116** over seks år |
| `DK-ENHETSTILORDNING.md` | massebevaringen under begge lesninger (§4); **DK1 1,01–1,02×** som kontrollen som validerer kjøringen |
| `FI-LUKKING.md` | dekningen i den finske torvkolonnen: **39–45 %** kommer fra anlegg under 100 MW-terskelen |
| `PSRTYPE-SKJEMA.md` | XSD-kardinalitetene ordrett; **1 190 parallelle serier, alle retningsdelte, null med ulik `psrType`** |
| `EFFEKT-PER-SONE.md` | A03-feilen i egen parsing (§0); effekten per sone; hva årsoppløsning retter og ikke retter |
| `A73-MOT-A75.md` | konsistenstesten, de tre kriteriene, Amer 9 som referansetilfelle |

Hvert dokument har en note øverst: deponert uendret bortsett fra at lokale filstier er erstattet
med relative navn. **Utsagn om publiseringsstatus gjelder skrivetidspunktet, ikke i dag.**

### `kode/`

| Fil | Hva den gjør |
|---|---|
| `a73_mot_a75.py` | leser A73 og A75, **med korrekt A03-ekspansjon** |
| `a73_mot_a75_FEIL-naiv.py` | den samme, men summerer bare oppførte punkter — **beholdt så rettelsen kan etterprøves mot begge** |
| `a73_mot_a75_endelig.py` | de tre kriteriene og dommen per (sone, psrType) |
| `a03_revisjon.py` | teller `curveType` og perioder med hull, over full dekning |
| `effekt_per_sone.py` | karbonintensitet per sone, år og time, før og etter brenselskorreksjon |
| `reprod_unnewehr.py` | reproduserer Unnewehr m.fl. (2022) ligning (1) på deres egne publiserte mellomfiler |

### `utskrift/`

| Fil | Innhold |
|---|---|
| `a73-mot-a75-dom-A03.txt` | dommen etter A03-rettelsen: **124 rene par, median 0,0 %, 90-persentil 3,8 %, maks 54,7 %**; seks par med A73 > A75; Amer 9 lukker 98,9 % og lander −0,251 % |
| `a73-mot-a75-dom.txt` | den samme kjøringen **før** rettelsen: 121 par, 90-persentil 6,1 %, maks 57,0 %. Beholdt for sammenligning |
| `a03-revisjon.txt` | A03-tellingen over full dekning, og hva den første tellingen faktisk dekket |

---

## Trappekurven, og en rettelse av dekningen

**Alle ENTSO-E-seriene her er `curveType A03`.** En manglende posisjon i en `Period` betyr ikke
manglende data — den betyr at **forrige verdi holder** til neste oppgitte posisjon. En parser som
summerer bare de oppførte punktene underrapporterer energi, og ikke ensartet: målt på FI 2021 ga
den Alholmens B2 **+4,9 %** for lavt, Seinäjoki B1 **+7,2 %** og Keljonlahti B1 **+22,6 %**.

`a03_revisjon.py` over **full dekning** gir:

| | filer | `curveType` | perioder | hull i posisjonene |
|---|---:|---|---:|---:|
| A73 FI 2021 | 365 | **A03 i 12 412 av 12 412** | 12 417 | 3 265 |
| A73 GB 2021 | 113 | A03 i 23 403 av 23 403 | 23 403 | **14 278** |
| A75 NL 2023 | 12 | A03 i 240 av 240 | 240 | **171** |

**Den første tellingen 13.09.2026 oppga «4 125 av 6 521» for GB 2021.** Tallet reproduserer, men
globet var `GB-2021-0[12]-*.xml` avkortet til de førti første filstiene — **30 innholdsfiler fra
januar og februar**, ikke hele året. Dekningen var oppgitt for vid. Tabellen over står i stedet.

---

## Rådata

**Rådata følger ikke med.** XML-en fra ENTSO-Es API er re-hentbar og for stor til å arkiveres her.
Skriptene leser fra en rot som settes med miljøvariabelen `ARBEIDSROT`, og forventer
`a75-avvik/` og `finland/` under den.

Tredjepartskilder — CBS, Enea, ČEZ, DUKES, Elexon, Energinet, ACER, EUR-Lex, Ember, Hirth m.fl.,
Unnewehr m.fl. — er **ikke** inkludert. De er deres, og de siteres.

---

## Sitering

Se `CITATION.cff`. Depotet siteres når en figur herfra brukes; selve funnene siteres fra
`psrtype-samfyring` eller `kapregister`.

## Lisens

Kode under Apache-2.0 (`LICENSE`). Dokumenter og utskrifter under CC BY 4.0 (`LICENSE-DATA`).
