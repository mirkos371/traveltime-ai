# TravelTime – Model spolupráce Miro + ChatGPT + Gemini (verejný AI pohľad)

**Odvodené z private modelu v1.1, 16. 10. 2026**

## 1. Zdroj pravdy a mirror

* **Private repo `mirkos371/traveltime`:** jediný autoritatívny Git zdroj projektu.
* **Public repo `mirkos371/traveltime-ai`:** neautoritatívny, jednosmerne generovaný, sanitizovaný AI mirror.
* **Lokálne produkčné dáta:** autoritatívne veľké dátové vrstvy sú mimo Gitu; ich identita je ukotvená SHA-256 manifestmi v private projekte.
* **Google Drive:** môže slúžiť ako pracovný výmenník a pasívna záloha, nie ako projektová pravda.
* **Konečný arbiter:** Miro. Rozhodnutia sa opierajú o dôkazy a merateľné experimenty.

## 2. Rozdelenie rolí

* **EXEKÚCIA – Miro + ChatGPT:** implementácia, refaktoring, testovanie, práca v termináli, správa private Gitu a integrácia schválených riešení.
* **VÝSKUM, ARCHÍV A OPONENTÚRA – primárne Gemini:** hĺbkový web research, práca s veľkým kontextom, hľadanie alternatívnych algoritmov a nezávislá oponentúra návrhov.
* **Zásada priepustnosti:** primárna rola nie je výlučná kompetencia. Oba modely môžu vstúpiť aj do druhej oblasti, ale nevytvárajú paralelné autoritatívne implementácie.

## 3. BLIND_ANALYSIS

Pri novej architektonickej vrstve alebo zásadnom metodickom rázcestí:

1. vznikne neutrálne zadanie bez predpojatého riešenia,
2. v private repozitári sa určí konkrétny source commit SHA,
3. z neho sa vytvorí nemenný public AI snapshot so všetkými dohodnutými podkladmi,
4. ChatGPT aj Gemini dostanú obsahovo rovnaký spoločný vstup,
5. oba modely vypracujú riešenie nezávisle bez poznania návrhu druhého,
6. výsledky sa vymenia a každý model spraví krížovú oponentúru,
7. pri nezhode sa spíšu pevné body, riziká a merateľný overovací test,
8. experiment na reálnych dátach rozhodne o prijatom smere,
9. schválené riešenie sa integruje v private repozitári,
10. podľa potreby sa z nového private commitu publikuje nový AI mirror snapshot.

Pri `BLIND_ANALYSIS` nesmie mať jeden model analytickú výhodu z private-only podkladov, ktoré druhý model nedostal.
