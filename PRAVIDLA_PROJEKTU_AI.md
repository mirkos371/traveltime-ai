# TravelTime – Záväzné pravidlá relevantné pre AI

Tento súbor je sanitizovaný verejný výťah z autoritatívnych projektových pravidiel pri source private commite uvedenom v `SOURCE_PRIVATE_COMMIT.md`.

## 1. Jeden aktuálny stav

Projekt musí mať vždy jednoznačné rozlíšenie medzi:

- aktuálnym riešením,
- overovaným kandidátom,
- experimentom,
- nahradeným riešením,
- historickým archívom.

Existencia starého skriptu alebo dokumentu neznamená, že je stále platný.

## 2. Kontrolovaná iterácia

Je dovolené meniť architektúru, opustiť slepú vetvu a skúšať alternatívy.

Po zmene však musí byť znovu jasné:

- čo platí,
- aké dáta sú autoritatívne,
- ktoré riešenie je aktuálne,
- čo je jeden nasledujúci krok.

## 3. Dáta a proveniencia

Produkčné FIT, Parquet a produkčné referenčné GPX nepatria do verejného mirroru.

Každá používaná dátová vrstva musí mať jednoznačnú identitu a úlohu. Pre autoritatívne súbory sa používa SHA-256.

Výsledok bez spoľahlivej proveniencie sa nesmie automaticky považovať za autoritatívny.

## 4. Historické riešenia

Historický archív je zdroj know-how, nie zdroj automaticky platných pravidiel.

Staré:

- prahy,
- radiusy,
- heuristiky,
- schémy,
- algoritmy,
- pipeline kroky

sa musia pred novým použitím pochopiť a znovu experimentálne overiť na aktuálnych dátach.

## 5. Tools a pipelines

* `pipelines/` sú reprodukovateľné transformačné kroky s jasným vstupom a výstupom.
* `tools/` sú pomocné diagnostické, kontrolné a auditné nástroje.
* Pomocný nástroj sa nemá tváriť ako povinný pipeline krok.
* Adresárová štruktúra sa nevytvára špekulatívne dopredu.

## 6. Zásada minimálnej zmeny

Existujúca funkčná časť projektu sa nemení iba kvôli estetike alebo novej predstave o štruktúre.

Každá významná zmena musí priniesť konkrétny úžitok a mať spôsob overenia.

## 7. Geometria referenčnej trasy

Finálna referenčná geometria musí:

- zachovať správne poradie prejazdu,
- zachovať legitímne out-and-back a opakované prejazdy po tej istej fyzickej ceste,
- nemať technické po sebe idúce duplicity ani nulové segmenty,
- nemať technické mikro-backtracky,
- neobsahovať routingové skratky, ktoré vynechávajú reálny priebeh,
- nevzniknúť globálnym zjednodušením, ktoré mení geometriu,
- pri nejednoznačnosti vyžadovať kontrolu namiesto automatického hádania.

Routing profil je nástroj na tvorbu geometrie, nie sémantická klasifikácia cesty.

## 8. Rozhodovanie

Zhoda ChatGPT a Gemini zvyšuje dôveru v hypotézu, ale nie je dôkazom.

Pri zásadnom rozhodnutí má prednosť merateľný experiment na reálnych dátach.

## 9. Jeden aktuálny krok

Nová významná vrstva sa nemá otvárať skôr, než je predchádzajúca vrstva dostatočne uzavretá alebo vedome odložená.

Aktuálny krok je vždy uvedený v `STAV_PROJEKTU_AI.md`.
