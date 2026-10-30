# Raport walidacji – SPQR Deluxe, s. 9–16 (TAG spqr_9_16)

Zakres: 4.34–4.9 (dowodzenie rzymskie i kartagińskie, dowódcy a oddziały wroga, słonie dowódców, dowodzenie słoniami), 5.0–5.5 (aktywacja, rozkazy, impet, przebicie, inicjatywa elitarnego wodza), 6.0–6.55 (ruch, teren, falangi, uporządkowany odwrót). Sprawdzono każde zdanie md i trans JSON (z carry p010) z EN, glosariuszem SPQR i brzmieniami serii (spqr_seria.py, 30+ zapytań). Plik: val_spqr_9_16.tsv – 12 zgłoszeń.
**Liczba zgłoszeń:** waga I – 1 (gramatyka); waga D – 11 (termin 3, interpunkcja 2, skladnia 2, oryginal 2, kolokacja 1, dodatek 1); K – 0. Wg miejsca: md 5, json 5, oba 2.

**Najpoważniejsze:**
1. s. 9 (4.55, oba): „nie dorównuje swoim towarzyszom” → „nie dorównują swoim towarzyszom” (podmiot szeregowy).
2. s. 13 (5.42 pkt 1, json): „przebić tę pierwszą aktywację uzyskaną przebiciem własnym nieaktywnym (inactive) dowódcą” → „przebić – własnym nieaktywnym (inactive) dowódcą – tę pierwszą aktywację uzyskaną przebiciem” (dwuznaczny szyk po skrócie składu).
3. s. 12 (5.28, md): „podjąć próbę uzyskania fazy rozkazów uzyskanej dzięki impetowi” → „spróbować uzyskać fazę rozkazów dzięki impetowi” (powtórzenie).
4. s. 16 (uwaga historyczna 6.52, json): „wrogiem na długo, zanim ten zdoła” → „wrogiem, na długo zanim ten zdoła” (przecinek przejęty z PDF GBJC; DOCX GBJC, ALEX i md poprawnie).
5. s. 13 (wyjątek do 5.34, json): „zasady elitarnego wodza (5.5)” → „(Elite rule, 5.5)” – skład usunął jedyny EN w akapicie przy terminie z listy ZAWSZE (do oceny).
6. s. 9 (4.5, oba): „hierarchii dowodzenia przedstawiają trybuni” → „reprezentują” (do oceny).
7. s. 10 (4.6, md): „wspólnie odbytym kampaniom” – dopowiedzenie bez pokrycia w EN; s. 10 (4.71, md): zbędny przecinek przed „albo gdy”.

**Ocena:** polszczyzna 5/5 – tekst naturalny, bez kalek, terminologia zgodna z glosariuszem i wzorcem (zdania wspólne z GBJC/Aleksandrem – 4.34, 4.71–4.73, 5.11–5.12, 5.21, 5.33, 5.4, 5.42, 5.46, 6.11–6.14, 6.21–6.22, 6.31, 6.44, 6.5–6.55 – mają brzmienie serii; md = DOCX, trans = PDF serii); jedyny błąd gramatyczny to orzeczenie w lp. przy podmiocie szeregowym. Wierność 5/5 – żadnego pominięcia, odwrócenia sensu, zgubionego warunku ani liczby; skróty składu (s. 10–16) zachowują kwantyfikatory, numery reguł i wyjątki. Liczby EN↔PL (nums.py): wszystkie różnice wyjaśnione (akapity przenoszone między stronami 9/10, 13/14, 15/16; numery stron; podwojone „nr 3 (Example #3)”; „po 1 za … i za …” w przykładzie 6.21 w trans). Słowa zakazane: 0 (4 „podejrzane” to opisowa „przewaga” w uwagach – poprawnie bez EN).

**Problemy systemowe (mogą dotyczyć innych partii):**
- Interpretacja listy ZAWSZE w składzie: skład glosuje typy oddziałów (falanga, harcownicy) wg K.3 (raz w punkcie), choć 0.2 wymienia je wśród terminów ZAWSZE (raz na akapit) – w 6.42–6.44 i przykładach s. 15–16 „falanga” bez EN. Trzeba rozstrzygnąć jednolicie dla całego dokumentu.
- Usuwanie nawiasów EN przy skracaniu (K.6) zdarza się też tam, gdzie polski termin zawiera człon ZAWSZE („zasady elitarnego wodza (Elite rule)”).
- Przejmowanie brzmień z PDF GBJC przenosi też jego usterki interpunkcyjne („na długo, zanim”) – przy identycznych zdaniach warto porównywać z DOCX.
- Błędy oryginału w zakresie (oddane wiernie, już w dzienniku spójności): 4.91 „Order Phase”, przykład 5.26 (zdanie urwane kropką); nowe, drobne: 4.72 „that combat units enters”, cudzysłów „retreat’ (6.52).

**Glosariusz a wzorzec serii:** rozbieżności tylko między PDF a DOCX serii, SPQR konsekwentnie przejmuje DOCX w md i PDF w składzie (zgodnie z 0.4): „sytuacje, w których nalicza się kary” / „sytuacje karne” (6.52), „kara w postaci ubytku spójności” / „kara w spójności” (6.13), „raz na każdy oddział” / „raz do każdego … oddziału” (6.55), „przed dowolnym / przed każdym oddziałem przeciwnika” (6.14). Rekomendacja: zostawić; ewentualnie w składzie „Są trzy dodatkowe sytuacje karne” → „W trzech dodatkowych sytuacjach nalicza się kary” (stylistycznie lepsze, ale odbiega od PDF GBJC).

**Do decyzji użytkownika:** (1) czy w składzie PDF typy oddziałów z 0.2 (falanga, harcownicy, hastati itp.) mają EN/kod raz na akapit, czy raz w punkcie (K.3) – dotyczy całego dokumentu; (2) czy przywrócić „(Elite rule, 5.5)” kosztem wydłużenia akapitu na s. 13; (3) poprawka „nie dorównują” (4.55) – rekomendacja: wprowadzić w md i json.
