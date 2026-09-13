# MANIFEST — psrtype-arbeidsdokumenter v1.0.0

Frosset 2026-09-13.

22 filer  175 114 B

| Fil | B | sha256 |
|---|---:|---|
| `.gitignore` | 42 | `a50431a748974350585736705c4cd4725a60341f58914c4dab2d0fda627fcae0` |
| `CITATION.cff` | 2650 | `27ab4c60314fb48b3161e5ce4fdc5b8c941a95b3ba28ed18cf14ce239e7923cf` |
| `LICENSE` | 11358 | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| `LICENSE-DATA` | 568 | `9df11493bc46950b03443ee26128c1763bb117c59f9ebc3669fec44e0e0f0307` |
| `README.md` | 6807 | `f195624a3fb5a65e8928ce13867dc9dffee26c554fab05fea75df24de0d6773e` |
| `SHA256SUMS` | 1882 | `4a7cfd7b364945b55443615653cf742e0b4a8fa3ba425100c4ba0df9613988ec` |
| `dok/A73-MOT-A75.md` | 10623 | `9ec7ae6c10fc906da03176d38d25fc73b8e7590b9da1c38c8bf0924faa10c520` |
| `dok/DK-ENHETSTILORDNING.md` | 7611 | `3c44013030bf916bbd5e265319a1178eb862704385e826039b01e77bfe9c2baa` |
| `dok/DK-KULL-TIDSSERIE.md` | 24611 | `8c365a41fb5e9cf19c4b9b3e6e2868dadd7cc8290a990d0d3bd4477f7324cf32` |
| `dok/EFFEKT-PER-SONE.md` | 10227 | `f6c5a1e38cfb926d0cd6d93e94df65e26d90e4790508a8a4b66aceb961564775` |
| `dok/FI-LUKKING.md` | 36608 | `040dc5298c2adb425810564b0c08959c8a16085e80bc883f0ecf9b23acdee3a7` |
| `dok/PSRTYPE-SKJEMA.md` | 16648 | `ff2a52d5a8561de612bbe436c56818b120402bb2046bc367180fd1a7fca55f7a` |
| `dok/RAPPORT-A75-2026-09-12.md` | 20706 | `4952719111fda74d60b041718adf02b7766d4110795d19220b61a15c6acbcd48` |
| `kode/a03_revisjon.py` | 2743 | `9d38101e2e3e61e07fcf5cad84bdfb01bbd31de842bb4e2c684fbd5c6151fc56` |
| `kode/a73_mot_a75.py` | 4011 | `1e3d82cfe7f4ef5b7218810a5da216502cde05ed07dcfbcd2f29f1aa4d08cfa2` |
| `kode/a73_mot_a75_FEIL-naiv.py` | 3401 | `4f4bf1948b65efc787022c22e09625b869bedc28380eb9e17d6d7bc69129f6dc` |
| `kode/a73_mot_a75_endelig.py` | 4750 | `eebdd66ce442d0de3b0e7008d398ff729cdddafa775f01eafc924bb5365ace9e` |
| `kode/effekt_per_sone.py` | 2409 | `ac815a286d3f531f8a2a37743b92db35194e7278840ad6b19395c8f8d75d4e85` |
| `kode/reprod_unnewehr.py` | 3970 | `a6aadd719ffb9d0dfbff225e1ae6675256d6023ae47b15c6050c2a05c76072a0` |
| `utskrift/a03-revisjon.txt` | 835 | `97d4b6b3c91613d52b77fe577c9d27f98e492278aa7bffeec48255c2c1b16ae2` |
| `utskrift/a73-mot-a75-dom-A03.txt` | 1183 | `7e8d8e16c40d79e09d787ca910c7324c51d9320c30644d56ac039119fdbb3045` |
| `utskrift/a73-mot-a75-dom.txt` | 1471 | `7488cb63c78f13c22ad2953e44bd6244ea54bd95dd67a60b52bd06e3c0f1d8bf` |

## Kontrollstreng

Kjørt med positive kontroller, så et nulltreff skiller seg fra et ødelagt søk.

| Mønster | Treff |
|---|---:|
| absolutt sti, Vault-sti, tilde-sti | **0** |
| arbeidsrotens navn | **0** utenom denne tabellen og én prosaomtale av en historikkomskriving |
| e-postadresse | **0** |
| GitHub-, Slack-, API-, AWS-token, privat nøkkel, ENTSO-E securityToken | **0** |
| personnavn utenom forfatteren selv | **0** |

Positive kontroller i samme kjøring: `psrtype-samfyring` 16 treff, `kapregister` 32,
`10.5281/zenodo` 9, ORCID 3, `sha256` 7, `curveType` 14. En plantet teststreng ble funnet.
Søket virker; nullene er egenskaper ved filene.

## Hva som ble endret mot arbeidskopiene

- lokale filstier erstattet med relative navn eller beskrivelser
- `pathlib.Path.home()` med fast underkatalog erstattet med `ARBEIDSROT`-miljøvariabel (3 skript)
- `/tmp`-sti erstattet med `UNNEWEHR_GEN`-miljøvariabel (1 skript)
- stale docstring i `kode/a73_mot_a75_endelig.py` rettet: 57,0 %/121 par → 54,7 %/124 par
- en datert note øverst i hvert dokument
- **`dok/A73-MOT-A75.md` har fått en supersedert-tabell** — dokumentet er kjørt før A03-rettelsen
- **`dok/EFFEKT-PER-SONE.md` §0 har fått en rettelse av GB-dekningen** — 4 125/6 521 dekket
  januar–februar, ikke hele 2021; full dekning gir 14 278/23 403
- `kode/a03_revisjon.py` og `utskrift/a03-revisjon.txt` er nye
