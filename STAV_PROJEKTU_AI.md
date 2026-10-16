# TravelTime – Aktuálny stav pre AI

Tento dokument je sanitizovaný verejný pohľad na projekt pri source private commite:

`03ce2905f7b2c2bfbf6b07a035508b2eba6e8f59`

## 1. Cieľ projektu

TravelTime má predikovať čas prejazdu dlhých viacdenných MTB/bikepacking trás približne v rozsahu 1000–2000 km na základe reálnych historických jázd a referenčnej trasy.

## 2. Aktuálna primárna dátová sada

Identifikátor:

`BIKEPACKING_2026_PRIMARNE_V1`

Základ:

- 8 Garmin FIT aktivít,
- približne 944,6 km reálnej jazdy,
- 447 017 FIT recordov,
- rovnaký záznamový profil a rovnaká generácia zariadenia.

Produkčné FIT a Parquet súbory nie sú vo verejnom mirrore.

## 3. Uzavretá Garmin RAW vrstva

Stav:

**UZAVRETÉ / STABILNÉ**

Aktuálny tok:

```text
Garmin FIT
    |
    +--> voliteľná diagnostika
    |
    v
FIT -> PARQUET_RAW
```

`PARQUET_RAW`:

- 8 Parquet súborov,
- spolu 447 017 riadkov,
- jednotná schéma 41 stĺpcov,
- zachovaná proveniencia k zdrojovým FIT súborom,
- plná regresia aktuálneho prevodu voči autoritatívnej vrstve skončila PASS.

Historické vrstvy `par_neutral` a `par_behavior` sa do novej Garmin pipeline neprebrali.

Dôvod: staré rýchlostné, behaviorálne a GPS heuristiky obsahovali prahy závislé od starého kontextu a neboli neutrálne ani potrebné pre aktuálny downstream kontrakt.

## 4. Referenčná geometria

Stav:

**AKTÍVNA OTVORENÁ VRSTVA**

Starší artefakt `BIKEPACKING_2026_REF_01` má overenú identitu a zostáva kontrolným/validačným podkladom. Už sa nepovažuje za finálnu produkčnú referenciu.

Aktuálny metodický smer:

- mapovo vedená geometria podľa OSM tam, kde je OSM vhodné,
- manuálna kontrola podľa reálnej jazdy,
- manuálna alebo Garmin geometria tam, kde potrebná fyzická cesta v OSM chýba,
- routing profil je iba nástroj tvorby geometrie, nie zdroj sémantických atribútov cesty,
- opakovaný prejazd po tej istej fyzickej ceste zostáva samostatnou sekvenčnou časťou referencie,
- žiadne globálne RDP alebo iné plošné zjednodušenie zdrojovej referencie.

Pri doterajších auditoch sa ukázalo, že automatický routing môže lokálne vytvoriť nesprávne skratky. Také úseky sa musia opraviť podľa reálnej jazdy a dostupnej mapovej geometrie.

## 5. Neskoršie vrstvy

Až po uzavretí referenčnej geometrie sa plánuje:

```text
REFERENČNÁ GEOMETRIA
    |
    v
OSM atribúty / referenčné segmenty
    |
    v
MAPMATCH reálnych jázd na referenciu
    |
    v
ďalšie modelovanie
```

Historický mapmatch kód nie je aktuálnym riešením.

Staré mapmatch konštanty a radiusy sa nesmú preniesť bez nového overenia.

## 6. Jeden aktuálny pracovný krok

**Dokončiť, technicky vyčistiť a auditovať referenčnú geometriu BIKEPACKING 2026 tak, aby mohla byť zaregistrovaná ako nová autoritatívna referenčná vrstva.**

Pred uzavretím vrstvy treba:

1. dokončiť chýbajúce úseky,
2. opraviť zostávajúce routingové skratky alebo odchýlky,
3. konzervatívne odstrániť technické duplicity a mikro-backtracky,
4. vykonať finálny audit voči reálnej Garmin jazde a kontrolnému artefaktu,
5. potvrdiť správne sekvenčné usporiadanie trasy,
6. až potom prideliť finálny identifikátor a vytvoriť SHA-256 manifest.

## 7. Čo sa teraz nerobí

Aktuálne sa:

- neobnovujú historické neutralizačné ani behaviorálne vrstvy,
- nemigruje mapmatch ako ďalší krok,
- nezačína modelovanie,
- nepreberajú staré prahy a heuristiky bez experimentu,
- nezverejňuje celý private repozitár.

Ďalšie zásadné architektonické vrstvy majú byť otvorené protokolom `BLIND_ANALYSIS`.
