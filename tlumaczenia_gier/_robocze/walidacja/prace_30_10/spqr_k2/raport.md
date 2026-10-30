# spqr_k2 – nawiasy EN z listy ZAWSZE (K.2) w składzie SPQR Deluxe (30.10.2026)

**Zakres.** Skryptem (`bin/scan.py`, `md.py`, `ser.py`) przejrzano wszystkie akapity trans s. 2–41 pod kątem terminów z GLOSARIUSZ_SPQR 0.2 bez nawiasu EN/kodu i porównano je z md oraz z tymi samymi zdaniami w PDF serii (GBJC_Rules, ALEX). md nie był zmieniany. Łatek layoutu nie trzeba było dodawać.

**Zmiany.** Zmieniono 29 plików trans (s. 2, 6, 8–19, 21, 25–35, 37, 39, 41). Dodano 93 nawiasy lub rozszerzenia nawiasów, w tym 6 skrótów robiących miejsce. Wszystko jest w `zmiany.tsv` (108 wierszy, w tym korekty i cofnięcia). Najważniejsze miejsca:
- 4.32: „poza harcownikami (SK) i welitami (Velites), zob. 9.2” – w myślnikach, żeby nie zagnieżdżać nawiasów (K.4). 5.34: „(Elite rule, 5.5)”.
- 6.42–6.45, przykład i noty 6.4: falanga (PH)/(Phalanx), (Cohesion Hits). Przykłady 6.51: (PH, MA 5), (EL, MA 7), harcowników (SK); „Wycofanie (Withdrawal)”.
- Przykład OW (s. 17): (OW), (RC, MA 8), (PH). 6.63 przykład nr 2: welici (Velites), harcownicy (SK). 6.71 Wyjątki: „(Column movement)”.
- 7.33 Wyjątki: (SK), (LI), (LC), „w starciu (Shock)”. 8.11: „skorpiony (Scorpios)”.
- 8.4–8.47: punktory „starcia (Shock)”, falanga (PH), (BI), (Superiority), (Shock-capable), (column, 8.45), rozbite (rout), (Cohesion Hits), (3R).
- 8.5–8.6: (advance), (Pursuit), (Routed), harcownicy (SK). 9.1: oddział słoni (EL) w punktach zasad i przykładach. 9.2: harcownicy (SK) w punktach 9.23–9.24.
- 9.5: (IO)/(LC). 9.66: (flank hexes). Rydwan (CH) w 9.7. 10.2: (Routed). 11.1: (Rout Points). 3.0: „(Army Withdraws)” jak w GBJC. 2.21: (HI).
- Pozostałe miejsca: 4.33 pkt 2: (Line); 4.5: (Praefect), (Ala Cohorts), (Pursuit); 4.82/4.9: (EL); przykład 5.2: (LC); przykład 6.2: (HI); noty 6.6: (PH), (RC).

**Skróty (szczegóły w zmiany.tsv).**
- Przykład 7.32: „Jeśli chce, by oddział zaatakował” → „Jeśli chce ataku”; „ponieważ musi ona zaatakować” → „bo musi zaatakować”.
- 8.11: „Jeśli oddział strzelający wykonuje ruch” → „Jeśli wykonuje ruch” (podmiot jest w poprzednim zdaniu).
- 9.21: „podczas uporządkowanego odwrotu (OW)” → „podczas OW”; „Welici (Velites) otrzymują ubytki spójności z powodu OW” → „…otrzymują je”.
- 4.5 pkt 6: „jazdy prowadzącej pościg” → „jazdy w pościgu (Pursuit)”.
- 9.24, ostatni punktor: „jeśli przerwa” przeniesione z s. 33 na s. 34.

**Skale (przed → po).** Spadły: s. 9 0,855→0,851; s. 17 0,880→0,853; s. 29 0,859→0,856; s. 30 0,870→0,862; s. 32 0,873→0,859; s. 33 0,861→0,851; s. 37 0,875→0,866; s. 39 0,878→0,875; s. 27 0,859→0,858; s. 15 0,867→0,866; s. 35 0,868→0,867. Wzrosła: s. 21 0,851→0,854. Bez zmian: pozostałe strony, w tym s. 8 (0,854). Wszystkie strony ≥ 0,85.

**Kontrola.** check_trans 1–44 OK. build_doc → „do sprawdzenia: brak”. overlap.py: 0 trafień przed i po. Obejrzane PNG s. 9, 15–17, 19, 21, 26, 32–34, 37: bez kolizji z żetonami, diagramami i ramkami.

**Czego nie dodano.**
- Brak miejsca: s. 33, 9.23, punktor 4: „w starciu” bez (Shock) – dodanie zwiększało liczbę wierszy, skala spadała do 0,843. s. 21, 7.33 Wyjątki: „skorpiony” bez (Scorpios), bo jednostka u18 jest już na granicy skali.
- Zgodnie z PDF serii (te same zdania są tam bez nawiasu):
  - 6.5x: „wycofać się/wycofanie” w znaczeniu uporządkowanego odwrotu (w md też bez EN);
  - 4.33 „Słonie nie blokują…”, 4.92 „Słonie mogą prowadzić ostrzał”;
  - 9.14 „Każdy szał słoni (Rampage)…” – nawias jest przy „szał”;
  - definicje w 2.x „Terminy” (s. 4–6) i opis skali 2.x, np. „Procarze… harcowników”, „Kopijnicy… lekka jazda”, „Wyjątkiem są harcownicy”;
  - „kolumna” tabeli przy nazwie tabeli z EN, np. „kolumna tabeli wyników starcia (Shock CRT)”.
- Termin użyty nie w znaczeniu gry: uwagi historyczne i projektanta, gdzie „linia”, „przewaga”, „falanga”, „słonie”, „jazda rzymska”, „harcownicy” opisują historię (s. 2–5, 7, 8 UH, 10 UP, 13 UP, 17 6.6, 23, 30 UH, 31–33 UH/UP, 35, 38, 41).
- Nagłówki, podpisy diagramów i etykiety: s. 3 „(falanga)”, s. 25 „Przegląd procedury…”, s. 28 tytuł przykładu, s. 35 „Po manipularnym wydłużeniu linii” (K.4).

**Uwaga.** Dla 5.34 i przykładu nr 3 w 6.51 PDF GBJC ma to samo zdanie bez nawiasu. Nawias dodano, bo wskazała je walidacja (lista ZAWSZE).

**Pliki.**
- `/home/claude/lay/trans/SPQR_Deluxe_Rule_book_WEB/p{002,006,008–019,021,025–035,037,039,041}.json`
- `/home/claude/final/SPQR_Deluxe_Rule_book_WEB_PL.pdf`
- Kopie zapasowe: `/home/claude/work/spqr_k2/trans_bak/`, `/home/claude/work/pre_spqr_k2.pdf`
