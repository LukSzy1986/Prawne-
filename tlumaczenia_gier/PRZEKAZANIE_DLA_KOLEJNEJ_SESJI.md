# Przekazanie prac – przekłady SPQR Deluxe i Twilight Struggle 20th Anniversary (stan 30.10.2026, ok. 08:00 UTC)

Dokument dla kolejnej sesji Claude, która dokończy prace po odnowieniu limitu. Uzupełnia `RAPORT_30_10_2026.md` (opis walidacji i poprawek). Czytaj oba.

## 1. Stan plików (wszystko w `tlumaczenia_gier/`)

| Dokument | PDF (skład w układzie oryginału) | DOCX | md |
|---|---|---|---|
| SPQR Deluxe – Zasady, 44 s. | `SPQR_Deluxe/SPQR_Deluxe_Rule_book_WEB_PL.pdf` – gotowy | gotowy | `SPQR_Deluxe/md/` |
| Twilight Struggle – Zasady, 24 s. | `Twilight_Struggle/TS_20th_Ann_Rule_Book_WEB_PL.pdf` – gotowy (pierwszy pełny skład z oryginałem) | gotowy | `Twilight_Struggle/Zasady_md/` |
| Twilight Struggle – Background Book, 48 s. | `Twilight_Struggle/TS_20th_Ann_Background_Book_WEB_PL.pdf` – gotowy (jw.) | gotowy | `Twilight_Struggle/Background_Book_md/` |

Wszystkie PDF: `build_doc.sh` → „do sprawdzenia: brak” (skala każdej strony ≥ 0,85; najniższe: SPQR 0,851, TS Zasady 0,856, BB 0,858). Etykiety na grafice: SPQR 13 (s. 16, 22), TS Zasady 57 (s. 1, 4, 5, 11, 15), BB 3 (s. 1, 22).

Pliki do odtworzenia składu: `_robocze/trans/<DOK>/pNNN.json` (tekst składu), `_robocze/carry/`, `_robocze/layout_patches/`, `_robocze/labels_*.json`, `_robocze/bg/SPQR_Deluxe_Rule_book_WEB.pdf` (tło SPQR odtworzone z PDF roboczego skryptem `_robocze/mkbg.py`). Tła TS powstają z oryginałów poleceniem `unitize.py <DOK> --force-bg` (oryginały EN przesłane przez użytkownika 30.10; kopiować do `/home/claude/tr/src/<DOK>.pdf`).

## 2. Środowisko (jak odtworzyć w nowej sesji)

1. Rozpakować kopię roboczą (`kopia_robocza_20261027_1100.tar.gz.001–003`) i podlinkować `/home/claude/{lay,tr,prompts,val}` do katalogów `lay`, `tr`, `prompts`, `val` z archiwum; utworzyć `/home/claude/{final,work}`.
2. Nadpisać z repozytorium: `lay/trans/<DOK>/` ← `_robocze/trans/<DOK>/`, `lay/carry/` ← `_robocze/carry/`, `tr/out/<DOK>/` ← md z katalogów dokumentów, `tr/GLOSARIUSZ_SPQR.md`, `tr/GLOSARIUSZ_TS.md` ← wersje z repozytorium (zawierają decyzje z 30.10).
3. `pip install --user pikepdf playwright==1.63.0 opencv-python-headless` (Chromium jest w `/opt/pw-browsers`; `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`).
4. Tło: SPQR – `cp _robocze/bg/SPQR…pdf /home/claude/lay/bg/`; TS – oryginały do `tr/src/`, potem `unitize.py <DOK> --force-bg` (layout nie jest nadpisywany; pliki `units` po tym poleceniu przywrócić z archiwum – unitize przelicza w nich opisy stylów).
5. Skład: `bash /home/claude/lay/build_doc.sh <DOK>`; DOCX: `python3 /home/claude/tr/build/build.py <DOK…>`.
6. WAŻNE: `fit.py` nie wykrywa kolizji tekstu z elementami o stałym położeniu (ikony, dymki, fragmenty między ikonami). Po każdej zmianie tekstu w trans obejrzeć stronę obok oryginału i uruchomić `python3 _robocze/walidacja/overlap.py <PDF>` (wykrywa nachodzące wiersze; trafienia na s. 4–5 Zasad TS to warstwowe etykiety planszy – fałszywe). Tak wykryto i cofnięto 3 kolizje 30.10 (Zasady TS s. 6, BB s. 4, SPQR s. 3).

## 3. Decyzje użytkownika z 30.10.2026 – DO WYKONANIA (stan: nie wykonane, chyba że zaznaczono)

SPQR Deluxe:
1. **Nawiasy EN przy typach oddziałów w składzie PDF – dodać „jak w przykładach GBoA i GBoJC”**, czyli wg zasady K.2 (lista ZAWSZE, glosariusz SPQR 0.2): nawias EN/kod raz na akapit także w przykładach i wyjątkach. Miejsca wskazane przez walidację: 4.32 (harcownicy, welici), 5.34 „(Elite rule, 5.5)”, 6.42–6.44 i przykłady s. 15–16 (falanga, harcownicy), 6.63 przykład nr 2 (welici, harcownicy), 6.71 wyjątki (Column movement), 7.33 wyjątki (Skirmishers, Light Infantry/Cavalry Archers – próba 30.10 obniżyła skalę s. 21 do 0,848), 8.11. Trzeba przejrzeć wszystkie strony (skrypt: `val_spqr/w_17_24/zawsze.py` z partii walidacji nie został skopiowany – napisać od nowa: dla każdego akapitu trans sprawdzić, czy termin z listy 0.2 ma EN lub kod). Gdzie skala spadnie < 0,85 – skracać inne słowa (zasady skracania INSTRUKCJA_UKLAD 6) albo łatka layoutu (`maxBottom`, wolne miejsce w tle). Wzór gęstości: PDF GBJC (`tr/ref/GBoH_PL/pdf/GBJC_Rules.txt`) i Aleksander (`ALEX.txt`).
2. **Nota „© 2026” na okładce** – dodać, jeśli jest na okładce oryginału SPQR (oryginału SPQR EN nie ma w środowisku; warstwa tekstu oryginału w `tr/pages/SPQR…/p001.txt` zawiera „GMT Games, LLC© • 2026”). Jeśli brak oryginału – zapytać użytkownika o PDF SPQR EN.
3. 7.0 – zostaje: md „Ustawienie frontu i strefy kontroli”, PDF „…i ZOC”. (wykonane – bez zmian)
4. 8.34 – bez przypisu. (bez zmian)
5. Indeks – osobliwości oryginału bez przypisu. (bez zmian)
6. „ostrzał podczas wycofania”, „modyfikacje za liczebność” – zostają. (bez zmian)
7. Hastati/principes/triarii – łacina nieodmienna (użytkownik: spolszczenie „wyglądałoby jak kaleczenie języka”). (bez zmian)
8. **GBJC (dostarczony przekład, osobny dokument): nagłówek 7.3 „Warunki starcia” → „Wymogi starcia”** (PDF i DOCX GBJC) – przy najbliższej poprawce tamtego dokumentu (narzędzie `lay/pdffix.py`, `lay/docxfix.py`).

Twilight Struggle – Zasady:
9. Przypis w 8.1.6 – zostaje. (bez zmian)
10. ✅ WYKONANE 30.10 (md + skład + PDF). **2.0: „zeszyt zasad” → „księga zasad”, „zeszyt tła historycznego” → „księga tła historycznego (Background Booklet)”** – md i skład.
11. ✅ WYKONANE 30.10 (R s. 18–20; BB nie zawiera). **„Scenariusz Apogeum” w tekście ciągłym małą literą: „scenariusz Apogeum”**; nagłówki bez zmian – md i skład (R s. 18–21; BB – sprawdzić).
12. ✅ WYKONANE 30.10 („ze ZSRR (Soviet Union)”; glosariusz 12.2). **11.1 „Związek Radziecki (Soviet Union)” → „ZSRR (Soviet Union)”** – md i skład; uzupełnić glosariusz TS 6.3.
13. **Nagłówki rozdziałów – JAK PHALANX** (decyzja użytkownika odmienna od rekomendacji): 2.0 „Komponenty”, 2.1 „Plansza”, 6.2 „Wywieranie Presji”, 6.3 „Przewroty”, 9.0 „Karta Chińska”, 10.0 „Rozstrzygnięcie i warunki zwycięstwa”, 10.3 „Warunki zwycięstwa”, 13.3 – brzmienie Phalanx („Opcjonalne zasady autorów” koliduje z zasadą M – zapytać albo dać „Opcjonalne zasady projektantów”); pełna lista w glosariuszu TS 0.1.3 d i 12 (sprawa 1). Zmienić: md, skład (nagłówki, spis treści s. 1 – sprawdzić długość wiersza i kropki), odesłania w BB, glosariusz 4.1 i 0.1.3. Sprawdzić tekst Phalanx: `tr/ref/TS_PL_Phalanx_Ksiega_zasad.txt`.
14. Rozróżnienia occur/resolve, increase/improve, counter/marker – zostają. (bez zmian)
15. ✅ WYKONANE 30.10 (glosariusz 2.1 poprawiony; opisy ilustracji w md już mówiły o polu 7). **„TURN 4+” na torze Rund – pole 7** (użytkownik sprawdził na mapach): poprawić glosariusz TS 2.1 („oznaczenie pola 8 toru” → pola 7); opis ilustracji w p007.md już mówi o polu 7 – sprawdzić p012.md i BB.

Twilight Struggle – Background Book:
16. **Nawiasy EN tytułów kart w wierszach „Karta:” – ZROBIĆ łatkę layoutu z dodatkowym wierszem**: s. 8 (US/Japan Mutual Defense Pact), s. 10 (Indo-Pakistani War; Wydarzenie Kluczowe ZSRR Captured Nazi Scientist), s. 12 (Arab-Israeli War, De Gaulle Leads France), s. 4 ramka PRZEWRÓT W IRANIE (Kontrola ZSRR – USSR Control, Operacje Wojskowe ZSRR – USSR Military Ops) i s. 4 „kontrolowane przez USA (US Controlled)”, s. 3 „−1 do Operacji (Operations, min. 1)”, s. 5 „z Europy Zachodniej (Western Europe)”, s. 8 „(Kontrola Iranu przez USA, US control of Iran)”. Wszystkie próbowano 30.10 – obniżały skalę stron (s. 5 do 0,83, s. 8 do 0,77, s. 10 do 0,82) albo kolidowały z dymkami (s. 4) – cofnięte. Wymagają łatek: `custom/TS_20th_Ann_Background_Book_WEB_p001-004/p005-008/p009-012_layout_patch.py` (dopisać sekcję; przesunięcie dymków dialogów nie jest możliwe – są w tle; zwiększyć `maxBottom` jednostek nad wolnym miejscem, zmniejszyć odstępy EXTRA, rozdzielić jednostkę). Po zmianie – kontrola wizualna!
17. ✅ WYKONANE 30.10. **Kropka po „(…, Wydarzenie ZSRR).” na s. 4 – usunąć** (md + skład).
18. ✅ WYKONANE 30.10. **s. 2: md – „Wpływy ZSRR (USSR Influence)” + objaśnienie zapisu (USA/ZSRR); skład – usunąć EN przy obu członach** („Wpływy USA, a liczba po ukośniku – Wpływy ZSRR (USA/ZSRR)”). Cytaty: `walidacja/val_tsbb_1_8.tsv` wiersze 2–3.
19. Dialogi „ty”/„pan” – zostają. (bez zmian)
20. Przypisy do błędów faktograficznych oryginału – bez przypisów. (bez zmian)
21. ✅ WYKONANE 30.10 (pełny dopisek w md i w składzie – zmieścił się, s. 30 skala 0,896). **„Socialist Democratic party” (BB s. 30, hasło Willy Brandt) – ZOSTAWIĆ poprawną nazwę Z DOPISKIEM**: np. „… partię socjaldemokratyczną [przyp. red.: w oryginale „Socialist Democratic party”; chodzi o SPD]” – md (pełny), skład (krótszy, jeśli się nie mieści: „[przyp. red.: SPD]”), DOCX z md.

Ogólne:
22. Tła i oryginały TS – dostarczone, PDF TS złożone 30.10. (wykonane)
23. **Poprawić `lay/render.py`: polskie słowa w nawiasach dzielone wzorcem angielskim** (np. „inic-jatywy”, „Rzymi-anie”; obejście: ręczne U+00AD). Funkcja `_hyph_sub` / wybór `hyph_en` dla tekstu w nawiasach – stosować `plhyph` dla słów z polskimi znakami lub rozpoznanych przez słownik PL; sprawdzić, że EN w nawiasach nadal dzieli się po angielsku. Po zmianie przebudować wszystkie trzy dokumenty i obejrzeć.

## 4. Poprawki naniesione 30.10 na podstawie walidacji (część B listy – do potwierdzenia przez użytkownika; użytkownik polecił ująć je w tym raporcie)

- SPQR: „(ZASADA OPCJONALNA)” jednolicie (s. 11, 40); „retreat” przy rozbitym → „uciekać/ucieczka” (9.53, 10.22); „weapons system” → „system uzbrojenia” (1.0, 2.4); „70 i więcej kroków”, „30 i więcej strzał” bez „ok.”; pauza w tytule serii; kropka na końcu 10.32; „ich EKG”; „Zdolność … »w grze«” zamiast „growa”.
- TS: „legitymizacja” zamiast „prawomocność” (BB s. 39, 42–44, 46); „Zagraj po Wydarzeniu Plan Marshalla” (R s. 9, BB s. 26); „współprojektant”; znak minus „−” w modyfikatorach; półpauza w epigrafach (R s. 2, 4, 10, 12–15; BB s. 19); „Czerwona Gwiazda” w cudzysłowie; „Karta OPA”; nota „Od redakcji” w R bez zdania o AR; 12.2 „odłóżcie”.
- BB, wygładzenia niezręczności oryginału: „Walnijmy raz jeszcze butem w stół”; szyk zdania o Łazarzu; „kosztowało … oraz przyniosło konflikty”; „Dla jednych terrorysta, dla innych bojownik o wolność”; „W rzeczywistej historii” (RS10).
- Pełna lista 305 zmian i 13 cofnięć: `_robocze/walidacja/FIXLOG.tsv` (kolumny: id, dok, strona, gdzie, status, było, jest; id „REV-…” = cofnięcie).

## 5. Cofnięte 30.10 z powodu składu (treść w md jest poprawna; w PDF zostało poprzednie brzmienie)

SPQR s. 3 „Nazwa/ozn.” (etykieta diagramu), s. 21 nawiasy (SK), (LI), (LC) w 7.33; TS Zasady s. 6: „kładąc” (zamiast „rozmieszczając”) i brak „(Space Race)” w 3.4 – fragmenty między ikonami ③–⑥ nie mieszczą dłuższego tekstu; BB s. 3, 4 („Wojna nieudana”, „(US Controlled)”), s. 5, 8, 10, 12 – zob. pkt 16.

## 5a. Stan po drugiej części sesji 30.10 (ok. 08:15 UTC)

- Wykonane decyzje: 10, 11, 12, 15, 17, 18, 21 (zaznaczone ✅ wyżej); glosariusze uzupełnione: SPQR 11.2, TS 12.2.
- PDF obu dokumentów TS przebudowane po zmianach; strony z elementami o stałym położeniu (Zasady s. 5, 6, 8, 9, 18; BB s. 2–12, 16–17) obejrzane – bez kolizji; `overlap.py` zgłasza tylko warstwowe etykiety planszy (Zasady s. 4, 5, 11, 15 – fałszywe trafienia).
- POZOSTAJĄ do wykonania: 1 (nawiasy EN typów oddziałów w składzie SPQR), 2 (© na okładce SPQR – potrzebny oryginał SPQR EN), 8 (GBJC 7.3), 13 (nagłówki rozdziałów Zasad TS jak w Phalanx – z odesłaniami i spisem treści), 16 (nawiasy EN w wierszach „Karta:” BB – łatki layoutu), 23 (poprawka `render.py`).

## 6. Kolejność prac dla następnej sesji

1. Odtworzyć środowisko (pkt 2), zbudować trzy PDF i porównać z PDF w repozytorium (powinny być identyczne).
2. Poprawić `render.py` (pkt 23) – wpływa na wszystkie dokumenty, więc najpierw.
3. Wykonać decyzje 1, 10–13, 15–18, 21 (md + skład + glosariusze), potem 2 (po uzyskaniu oryginału SPQR) i 8 (GBJC).
4. Po każdej stronie: `check_trans.py`, `fit.py`, `overlap.py`, porównanie wizualne z oryginałem (`pdftoppm -r 110`).
5. Przebudować PDF i DOCX, zaktualizować glosariusze (SPQR 11.1, TS 12.1) i raport, commit i push na gałąź roboczą.
