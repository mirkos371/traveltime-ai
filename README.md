# TravelTime – Public AI Mirror

Tento repozitár je verejný, sanitizovaný AI mirror projektu TravelTime.

## Dôležité

Tento repozitár **nie je autoritatívny zdroj projektu**.

Jediným autoritatívnym Git zdrojom je súkromný repozitár:

`mirkos371/traveltime`

Obsah tohto mirroru je jednosmerne odvodený z konkrétneho commitu súkromného repozitára a je určený najmä pre AI nástroje, ktoré k private repozitáru nemajú prístup.

Aktuálny source private commit je uvedený v:

`SOURCE_PRIVATE_COMMIT.md`

## Odporúčané poradie čítania

1. `SOURCE_PRIVATE_COMMIT.md`
2. `AI_START.md`
3. `PRAVIDLA_PROJEKTU_AI.md`
4. `STAV_PROJEKTU_AI.md`
5. `MODEL_SPOLUPRACE_AI.md`

## Bezpečnostný rozsah

Mirror zámerne neobsahuje:

- produkčné FIT, Parquet ani GPX dáta,
- prihlasovacie údaje, tokeny ani tajomstvá,
- osobné alebo lokálne prevádzkové detaily, ktoré AI na analýzu nepotrebuje,
- úplnú históriu súkromného repozitára.

Ak sa verejný mirror a súkromný repozitár rozchádzajú, rozhodujúci je vždy súkromný repozitár pri evidovanom source commit SHA.
