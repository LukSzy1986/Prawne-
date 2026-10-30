# Raport aktualny – przekłady SPQR Deluxe, Twilight Struggle 20th Anniversary i poprawka GBJC (30.10.2026, stan końcowy sesji)

Uzupełnia `RAPORT_30_10_2026.md` (walidacja: 233 zgłoszenia, 305 poprawek) i `PRZEKAZANIE_DLA_KOLEJNEJ_SESJI.md` (środowisko, decyzje). Ten plik opisuje stan końcowy. Prace przerwano na polecenie użytkownika (limit kredytów); wszystko poniżej jest złożone i zapisane.

## 1. Gotowe pliki

| Dokument | PDF (układ oryginału) | DOCX | Najniższa skala strony |
|---|---|---|---|
| SPQR Deluxe – Zasady gry, wyd. 5. (44 s.) | `SPQR_Deluxe/SPQR_Deluxe_Rule_book_WEB_PL.pdf` | `SPQR_Deluxe/SPQR_Deluxe_Rule_book_WEB_PL.docx` | 0,851 |
| Twilight Struggle – Księga zasad (24 s.) | `Twilight_Struggle/TS_20th_Ann_Rule_Book_WEB_PL.pdf` | `Twilight_Struggle/TS_20th_Ann_Rule_Book_WEB_PL.docx` | 0,856 |
| Twilight Struggle – Księga tła historycznego (48 s.) | `Twilight_Struggle/TS_20th_Ann_Background_Book_WEB_PL.pdf` | `Twilight_Struggle/TS_20th_Ann_Background_Book_WEB_PL.docx` | 0,858 |
| GBJC – Zasady (dostarczony przekład, 48 s.) | `GBJC_poprawka/GBJC_Rules_Final_Low-Res_PL.pdf` | – (DOCX nie był przesłany) | – |

Wszystkie PDF: `build_doc.sh` → „do sprawdzenia: brak”; kontrola nachodzących wierszy (`overlap.py`) bez kolizji (pozostałe trafienia to warstwowe etykiety plansz i znaczniki ▶ – fałszywe); strony z ikonami, dymkami i kartami obejrzane obok oryginału.

## 2. Prace wykonane w ostatniej części sesji

1. **Narzędzie składu** (`lay/render.py`, kopia `_robocze/narzedzia/render.py`): polskie wtrącenia w nawiasach (z polskimi literami lub wyrazami funkcyjnymi, np. „(inicjatywa 6)”, „(Rzymianie i Kartagińczycy)”, „(zob. ilustracje poniżej)”) dzielone teraz wzorcami polskimi; angielskie nawiasy – nadal angielskimi. Po zmianie wszystkie trzy dokumenty przebudowane, skale stron bez zmian.
2. **SPQR – nawiasy EN jak w GBJC i Aleksandrze** (K.2, lista ZAWSZE): 93 nawiasy dodane lub rozszerzone w 29 plikach składu (s. 2, 6, 8–19, 21, 25–35, 37, 39, 41), m.in. 4.32, 5.34 „(Elite rule, 5.5)”, 6.42–6.45, przykłady s. 15–16, 6.63 przykład nr 2, 6.71 „(Column movement)”, 7.33 (SK), (LI), (LC), 8.11 „(Scorpios)”, 8.4–8.6, 9.1, 9.23–9.24, 9.5, 9.66, 10.2, 11.1. Sześć drobnych skrótów, by zrobić miejsce (np. przykład 7.32 „Jeśli chce ataku”, 9.21 „podczas OW”). Nie dodano z braku miejsca: s. 33, 9.23, 4. punktor – „w starciu” bez (Shock); s. 21, 7.33 – „skorpiony” bez (Scorpios). Dziennik: `_robocze/walidacja/prace_30_10/spqr_k2/zmiany.tsv`, raport: `…/raport.md`.
3. **TS Zasady – nagłówki jak w wydaniu Phalanx** (18 nagłówków, w tym 6 pozycji spisu treści): 2.0 Komponenty, 2.1 Plansza, 2.1.7 Kontrolowanie państwa, 3.0 Przygotowanie rozgrywki, 4.0 Przebieg rozgrywki, 6.2 Wywieranie Presji, 6.3 Przewroty, 8.0 „… oraz …”, 9.0 Karta Chińska, 10.0 Rozstrzygnięcie i warunki zwycięstwa (dwa wiersze, jak w Phalanx), 10.1 Rozstrzygnięcia, 10.3 Warunki zwycięstwa, 11.1 Pole „Chińska wojna domowa”, 11.3 Skutki Kontroli pola, 11.4 Ograniczenie Wydarzeń, 13.3 Opcjonalne zasady autorów, podtytuł w 13.3 Wywieranie Presji, scenariusz Apogeum – Warunki zwycięstwa. Wielkie litery zgodnie z glosariuszem 0.2 (nie Phalanx). Punkty nowe w 20th Anniversary bez odpowiednika w Phalanx – bez zmian. Glosariusz TS (0.1.3, 4.1, 12, 12.2) zaktualizowany. Tabela było/jest: `_robocze/walidacja/prace_30_10/ts_naglowki/raport.md`.
4. **TS Zasady s. 6** – przywrócone „rozmieszczając 15/25 znaczników” (łatka layoutu, bez kolizji z ikonami); w 3.4 „Oba znaczniki Wyścigu Kosmicznego (Space Race) ⑤ umieść…” (zamiast „Znaczniki … USA i ZSRR” – nie mieściło się przed ikoną ⑤). Efekt uboczny: „(East Germany)” dzielone „Ger-many”.
5. **Background Book – nawiasy EN w Przykładzie rozgrywki** (łatki layoutu z dodatkowym wierszem): s. 3 „(Operations, min. 1)”; s. 4 ramka PRZEWRÓT W IRANIE „(Kontrola ZSRR, USSR Control)”, „Operacje Wojskowe ZSRR (USSR Military Ops)”, AR3 „(US Controlled)”; s. 5 „(Western Europe)”; s. 8 „US control of Iran”, „US/Japan Mutual Defense Pact”; s. 10 „Indo-Pakistani War”, „Captured Nazi Scientist”; s. 12 „Arab-Israeli War”, „De Gaulle Leads France”. Wszystkie weszły i nie kolidują z dymkami (s. 4, 8, 10, 12 obejrzane). Prace przerwano przed przeglądem pozostałych wierszy „Karta:” na s. 2–15 (dalsze uzupełnienia) – stan zapisany, PDF złożony.
6. **GBJC 7.3**: „Warunki starcia” → „Wymogi starcia” w PDF (etykieta w tym samym kroju kapitalikami, s. 23; spec: `GBJC_poprawka/etykieta_7.3_spec.json`). DOCX GBJC do poprawienia, gdy będzie dostępny.
7. **SPQR – nota „© 2026” na okładce: nie dodano.** Oryginału SPQR EN nie ma w środowisku (serwer GMT niedostępny). Redaktor składu, który 26.10 widział obraz oryginału, zapisał stopkę okładki „GMT Games, LLC • P.O. Box 1308 • Hanford, CA 93232–1308” (bez ©); znak © i rok występują tylko w uszkodzonej warstwie tekstowej. Zgodnie z warunkiem decyzji („dodać, jeśli widać”) – bez zmian; do potwierdzenia na wydruku oryginału.

## 3. Wszystkie decyzje użytkownika z 30.10 – stan

| # | Decyzja | Stan |
|---|---|---|
| 1 | SPQR: nawiasy EN typów oddziałów jak GBoA/GBoJC | wykonane (2 miejsca bez miejsca – pkt 2.2) |
| 2 | SPQR: © na okładce, jeśli widoczne | niewykonane – wg opisu obrazu oryginału niewidoczne (pkt 2.7) |
| 3–7 | SPQR: 7.0, 8.34, indeks, „wycofania/modyfikacje”, łacina hastati… | bez zmian (zgodnie z rekomendacją) |
| 8 | GBJC 7.3 „Wymogi starcia” | wykonane w PDF; DOCX – brak pliku |
| 9 | TS 8.1.6 przypis | zostaje |
| 10 | TS 2.0 „księga zasad”, „księga tła historycznego” | wykonane |
| 11 | „scenariusz Apogeum” małą w tekście | wykonane |
| 12 | 11.1 „ZSRR (Soviet Union)” | wykonane |
| 13 | Nagłówki jak Phalanx | wykonane (18) |
| 14 | Rozróżnienia occur/increase/counter | bez zmian |
| 15 | TURN 4+ – pole 7 | wykonane (glosariusz) |
| 16 | BB: nawiasy EN w „Karta:” łatką | wykonane dla wskazanych miejsc (s. 3, 4, 5, 8, 10, 12) |
| 17 | BB s. 4 kropka | usunięta |
| 18 | BB s. 2 zapis Wpływów | wykonane |
| 19–20 | dialogi „ty/pan”; błędy oryginału bez przypisów | bez zmian |
| 21 | „Socialist Democratic party” z dopiskiem | wykonane (s. 30) |
| 22 | PDF TS z oryginałów | wykonane |
| 23 | Poprawka render.py | wykonane |

## 4. Do potwierdzenia przez użytkownika (część B i nowe)

- Poprawki z walidacji naniesione przeze mnie (lista w `PRZEKAZANIE_DLA_KOLEJNEJ_SESJI.md`, pkt 4) – m.in. „(ZASADA OPCJONALNA)”, „uciekać (retreat)”, „system uzbrojenia”, „legitymizacja”, „współprojektant”, wygładzenia niezręczności oryginału w BB („butem w stół”, Łazarz).
- TS 3.4: „Oba znaczniki Wyścigu Kosmicznego” zamiast „Znaczniki … USA i ZSRR”.
- TS: „Elementy Etapu zero (Turn Zero Components)” i „Elementy scenariusza Wschodzące czerwone słońce” – zostały „Elementy”, choć 2.0 to teraz „Komponenty” (Phalanx nie ma tych punktów). Ujednolicić?
- TS: nazwy ról w Twórcach (np. „Testerzy edycji Deluxe”) różnią się od Phalanx – nie są nagłówkami zasad, zostawione.
- SPQR: nota © (pkt 2.7).

## 5. Pozostało (dla kolejnej sesji)

- BB: przegląd pozostałych wierszy „Karta:” na s. 2–15 pod kątem brakujących nawiasów EN (wskazane miejsca są zrobione).
- SPQR: 2 nawiasy bez miejsca (pkt 2.2).
- GBJC: ta sama zmiana 7.3 w DOCX.
- Ewentualne decyzje z pkt 4.
