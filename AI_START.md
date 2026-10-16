# TravelTime – Vstupný bod pre AI vo verejnom mirrore

Tento repozitár je **neautoritatívny verejný AI mirror** projektu TravelTime.

Jeho účelom je poskytnúť rovnaký bezpečný analytický kontext AI nástrojom, ktoré nemajú prístup k súkromnému autoritatívnemu repozitáru.

## 1. Najprv over pôvod snapshotu

Prečítaj:

1. `SOURCE_PRIVATE_COMMIT.md`

Source private commit SHA určuje presný autoritatívny stav, z ktorého bol tento mirror odvodený.

**Dôležité:** Git commit SHA verejného mirroru a source private commit SHA sú dve rôzne identity. Pri otázke na pôvod snapshotu používaj výhradne hodnotu označenú `PRIVATE_SOURCE_COMMIT` v `SOURCE_PRIVATE_COMMIT.md`. Nikdy ju neodvodzuj z Git metadát verejného repozitára.

## 2. Povinné čítanie

Potom prečítaj v tomto poradí:

1. `PRAVIDLA_PROJEKTU_AI.md`
2. `STAV_PROJEKTU_AI.md`
3. `MODEL_SPOLUPRACE_AI.md`

Pri konkrétnom `BLIND_ANALYSIS` sa neskôr pridá aj neutrálne RFC zadanie a podľa potreby rovnaká diagnostická vzorka identifikovaná SHA-256.

## 3. Železné pravidlá

* **Private repo je zdroj pravdy:** tento mirror je iba odvodený čitateľný snapshot.
* **Nevymýšľaj chýbajúci kontext:** ak potrebná informácia v mirrore nie je, označ ju ako chýbajúcu.
* **Historický materiál nie je automaticky platný:** starý kód, prahy, schémy a algoritmy sú iba hypotézy, kým neprejdú novým overením.
* **Zhoda AI nie je dôkaz:** rozhodujú merateľné experimenty na reálnych dátach.
* **Pri BLIND_ANALYSIS používaj iba spoločný vstup:** nepokúšaj sa rekonštruovať private-only kontext z iných zdrojov.
* **Mirror sa neupravuje ako produkčný projekt:** návrhy patria do analýzy; schválené zmeny sa integrujú v private repozitári a až potom sa publikuje nový mirror snapshot.
* **Aktuálny pracovný krok sa vždy berie zo `STAV_PROJEKTU_AI.md`:** všeobecné pravidlá v `MODEL_SPOLUPRACE_AI.md` (napríklad kedy použiť `BLIND_ANALYSIS`) nesmú byť zamieňané za aktuálny pracovný krok.
* **Ak sa otázka pýta na „jeden aktuálny ďalší krok“, odpovedaj podľa sekcie „Jeden aktuálny pracovný krok“ v `STAV_PROJEKTU_AI.md`.**
