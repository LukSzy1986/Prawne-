# ts_naglowki – nagłówki R jak Phalanx (decyzja 30.10) + s. 6 – raport

Zmieniono 18 nagłówków (md + skład), w tym 6 pozycji spisu treści s. 1 (kropki dobrane renderem: koniec kropek x = 420,3–420,6 pt, jak przed zmianą 420,0–420,7). Odesłań słownych do tytułów rozdziałów w tekście R ani w BB nie ma (BB – nic do zmiany). Dziennik: `zmiany.tsv` (55 wpisów).

| pkt | było (md / skład) | jest | Phalanx |
|---|---|---|---|
| 2.0 | Elementy gry | Komponenty | 2.0 KOMPONENTY |
| 2.1 | Mapa gry | Plansza | 2.1 PLANSZA |
| 2.1.7 | Kontrolowanie państw | Kontrolowanie państwa | 2.1.7 Kontrolowanie państwa: |
| 3.0 | Przygotowanie gry | Przygotowanie rozgrywki | spis: „Przygotowanie rozgrywki”, nagł.: „PRZYGOTOWANIE” – wybrano formę ze spisu |
| 4.0 | Przebieg gry | Przebieg rozgrywki | 4.0 PRZEBIEG ROZGRYWKI |
| 6.2 | Rzuty na Wywieranie Presji | Wywieranie Presji | 6.2 WYWIERANIE PRESJI |
| 6.3 | Próby Przewrotu | Przewroty | 6.3 PRZEWROTY |
| 8.0 | Status DEFCON i Operacje Wojskowe | Status DEFCON oraz Operacje Wojskowe | 8.0 STATUS DEFCON ORAZ OPERACJE WOJSKOWE |
| 9.0 | Chiny | Karta Chińska | 9.0 KARTA CHIŃSKA |
| 10.0 | Rozstrzygnięcie i zwycięstwo | Rozstrzygnięcie i warunki zwycięstwa | 10.0 ROZSTRZYGNIĘCIE I WARUNKI ZWYCIĘSTWA |
| 10.1 | Rozstrzygnięcie | Rozstrzygnięcia | 10.1 ROZSTRZYGNIĘCIA |
| 10.3 | Zwycięstwo | Warunki zwycięstwa | 10.3 WARUNKI ZWYCIĘSTWA |
| 11.1 | Pole Chińska wojna domowa | Pole „Chińska wojna domowa” | 12.1 Pole „Chińska Wojna Domowa” |
| 11.3 | Skutki Kontroli | Skutki Kontroli pola | 12.3 Skutki kontroli pola |
| 11.4 | Ograniczenia Wydarzeń | Ograniczenie Wydarzeń | 12.4 Ograniczenie Wydarzeń |
| 13.3 | Opcjonalne zasady projektantów | Opcjonalne zasady autorów | OPCJONALNE ZASADY AUTORÓW |
| 13.3 podtytuł | Rzuty na Wywieranie Presji | Wywieranie Presji | Wywieranie Presji |
| Scen. Apogeum | Zwycięstwo | Warunki zwycięstwa | Warunki Zwycięstwa |

Bez zmian (jak w Phalanx): 1.0, 2.1.4, 2.2, 2.3, 4.5 A–E, G–I, 5.0, 5.2, 6.0, 6.1, 6.4, podtytuł 13.3 „Wyścig Kosmiczny”, 7.0, 7.3, 7.6, 8.1, 8.1.7, 8.2, 10.2, 10.3.1, 10.3.2, 11.0, 11.2, 11.4.1, Scenariusz Apogeum, Karty, Kontrola i Wpływy, Twórcy. Bez odpowiednika (wierne): 4.5 F, 8.1.6 (w 20th bez tytułu), 12.–12.3, 13.0–13.2, 13.4, Przygotowanie scenariusza Apogeum, Znaczniki, Żetony Wydarzeń w grze, Red Sun Rising. Wielkie litery wg 0.2 („Chińska wojna domowa”, „Warunki zwycięstwa” małą). Do decyzji: „Elementy Etapu zero (Turn Zero Components)” i „Elementy scenariusza WCS (… Components)” zostały przy „Elementy” – niespójne z 2.0 „Komponenty”; etykiety w Twórcach (Phalanx np. „Testerzy edycji Deluxe”, „Dodatkowa edycja zasad”) – nie zmieniane.

Skład: s. 14 nagłówek 8.0 – łatka maxRight 310 + hs 0,92 (skala 0,92 → ok. 15,6 pt; było 0,95); s. 15 9.0 sięgał na ilustrację karty – x1/maxRight 488 (skala 0,919); s. 16 10.0 – dwa wiersze jak w Phalanx (<br>, fixscale 0,9 = 16,2 pt, drugi wiersz na linii bazowej oryginału). Pozostałe nagłówki – skala bez zmian. Skale stron (page_scale) bez zmian na wszystkich 24 s.

s. 6 – przywrócone: 3.2/3.3 „, rozmieszczając <b>15/25 znacz-</b>” + „<b>ników Wpływów</b>” na początku następnego wiersza (hs 0,94 fragmentów, 3.3 akapit hs 0,96 – bez dzielenia „Kana-dzie”); 3.4 – „Znaczniki Wyścigu Kosmicznego (Space Race) USA i ZSRR” nie mieści się przed ikoną ⑤ (wszystkie fragmenty do ⑥ pełne), więc przeredagowane: „3.4 Oba znaczniki Wyścigu Kosmicznego (Space Race) ⑤ umieść na polu Start…” (hs 0,93; „USA i ZSRR” → „Oba” – te same dwa znaczniki). W 3.2 łamanie „(East Ger-many)”. Obejrzane w 200 dpi obok oryginału – bez kolizji.

Kontrola: check_trans OK; łatki idempotentne (md5); build_doc → „do sprawdzenia: brak”; overlap.py – wynik identyczny jak przed zmianami. Po ponownym uruchomieniu łatki s. 9–16 uruchomiono qa_pagina_patch tylko dla R (stopka; plików BB nie dotykano).

Pliki: tr/out/TS_20th_Ann_Rule_Book_WEB/p001, 002, 004, 005, 006, 008, 011, 012, 014–017, 019, 021.md (md s. 6 – tylko nagłówek 3.0; 3.2–3.4 w md bez zmian); lay/trans/…/p001,002,004,005,006,008,011,012,014–017,019,021.json; lay/custom/TS_20th_Ann_Rule_Book_WEB_p001-008_layout_patch.py (s6), …_p009-016_layout_patch.py (blok ts_naglowki: s. 14, 15, 16); tr/GLOSARIUSZ_TS.md (0.1.3 c–d, 4, 4.1, 2.1, 2.4, 3.5, 10, 11.1, 12 pkt 1, 12.2 pkt 4); final/TS_20th_Ann_Rule_Book_WEB_PL.pdf.
