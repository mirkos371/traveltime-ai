# TravelTime – pôvod verejného AI snapshotu

**Typ:** DERIVED / NON-AUTHORITATIVE  
**Dátum snapshotu:** 2026-10-16

## Dve rôzne Git identity – NEZAMIEŇAŤ

### PRIVATE_SOURCE_COMMIT

Toto je commit v súkromnom autoritatívnom repozitári, z ktorého bol obsah tohto AI snapshotu odvodený:

`03ce2905f7b2c2bfbf6b07a035508b2eba6e8f59`

Toto je hodnota, ktorú treba uviesť pri otázke:

> „Z akého private commit SHA tento snapshot pochádza?“

### PUBLIC_MIRROR_COMMIT

Verejný mirror má vlastný Git commit SHA v repozitári:

`mirkos371/traveltime-ai`

Jeho aktuálny commit SHA sa číta z Git metadát verejného repozitára.

**PUBLIC_MIRROR_COMMIT NIE JE PRIVATE_SOURCE_COMMIT.**

Public commit sa po každej aktualizácii mirroru mení. Preto sa jeho vlastná hodnota zámerne nehardcoduje do tohto súboru – zápis nového SHA do súboru by sám vytvoril ďalší commit a SHA by sa znova zmenilo.

## Autoritatívny zdroj

Jediným autoritatívnym Git zdrojom projektu je súkromný repozitár:

`mirkos371/traveltime`

Tento verejný mirror obsahuje iba vybraný sanitizovaný kontext odvodený z uvedeného `PRIVATE_SOURCE_COMMIT`.

Mirror nepredstavuje úplnú kópiu súkromného repozitára.

Pri rozpore alebo nejasnosti je autoritatívny súkromný projektový stav pri uvedenom `PRIVATE_SOURCE_COMMIT`.
