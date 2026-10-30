# RAPORT WALIDACJI – TS_20th_Ann_Background_Book_WEB, s. 1–8 (tsbb_1_8)

Zakres: okładka ze spisem treści (s. 1), Przykład rozgrywki – wstęp, przygotowanie, ręce, Etap 1 (Wydarzenia Kluczowe, AR1–AR6, koniec Etapu), Etap 2 (ręce, Wydarzenia Kluczowe, AR1–AR5), dialogi Kennedy/Chruszczow (s. 2–8). Sprawdzono każde zdanie md i trans JSON z EN; liczby Wpływów, rzuty, wzory siły Przewrotu, Ops, VP, stany Kontroli i listy kart na rękach – co do jednej, także pod kątem logiki gry (zgadzają się). Skrypt liczb EN↔PL: różnice tylko z numerów znaczników na ilustracjach map, zapisu „Etapu 1 (Turn 1)” i „Podpis (s. 6)”. Słowa zakazane (sekcja 10): 0 trafień w md i trans.

Plik: val_tsbb_1_8.tsv – 20 zgłoszeń: K 0, I 1, D 19. Kategorie: termin 9 (w tym 8 × brak nawiasu EN z listy ZAWSZE w trans), typografia 4, sens 2, kontekst 2, kolokacja 2, oryginal 1.

Najpoważniejsze (strona: cytat → poprawka):
1. s. 4 (json, I): „(Wojna nieudana, Wpływy (Influence) bez zmian)” → „(Wojna kończy się porażką, …)” – jedyne odstępstwo od formuły glosariusza 4.3 używanej w md s. 4 oraz md/json s. 8–9+.
2. s. 8 (json): „Karta: Pakt o wzajemnej obronie USA/Japonia (Wydarzenie USA)” – jedyny wiersz „Karta:” bez tytułu EN (US/Japan Mutual Defense Pact); tytuły kart – lista ZAWSZE, K.6.
3. s. 7 (json): „by zatrzymać naszych ludzi” → „by nie wypuścić naszych ludzi” („to keep our people in” – skrót składu zgubił „in”).
4. s. 8 (json): „Wasze przyjęcia emerytalne mają więcej pistoletów…” → „Wasze pożegnania emerytów mają…” (kalka; md poprawne).
5. s. 2 (json): „Jack bada Europę Zachodnią” → „Jack studiuje Europę Zachodnią” (studies; md: „przygląda się”).
6. s. 7 (json): nagłówek „FAZA WYDARZEŃ KLUCZOWYCH” bez „(HEADLINE PHASE)”, choć na s. 3 ten sam nagłówek ma EN.
7. s. 8 (md+json): „Modyfikator rzutu: -1”, „(modyfikator -1 = 2)” – dywiz zamiast minusa „−” (we wzorach obok „−”).
8. s. 2 (md+json): „Wpływy ZSRR (USA/ZSRR)” – zapis wg 0.6.5, ale „(USA/ZSRR)” czyta się jak glosa EN, a przy „Wpływy USA” nawias EN jest; propozycje osobno dla md (dopisać USSR Influence) i json (symetrycznie bez EN).
9. s. 4 (md+json, oryginal): kropka po „(…, Wydarzenie ZSRR).” – usterka oryginału oddana wiernie.

Ocena: wierność 5/5 – żadnej zmiany sensu reguły ani liczby; wszystkie etykiety (4.2–4.3), tytuły kart (5), państwa (6), zapis „(USA#/ZSRR#)” (0.6.5) zgodne z glosariuszem; md w całości poprawne językowo. Język: md 5/5, trans 4/5 – dialogi naturalne, ale trzy skróty składu dały słabsze kolokacje (s. 2, 7, 8).

Problemy systemowe (mogą wystąpić w innych partiach): (a) skład usuwa nawiasy EN także przy terminach z listy ZAWSZE w ramkach i jednowierszowych jednostkach (s. 3 Operacje, s. 4 Kontrola ×2, Operacje Wojskowe, s. 8 Kontrola, tytuł karty) – zgodnie z raportami składu, ale K.6 wymaga odnotowania; (b) skróty jednowierszowych dialogów zmieniają kolokacje – warto, by orkiestrator przejrzał wszystkie „Zmiany brzmienia” z raportów składu; (c) powtarzalne formuły Przykładu skracane niejednolicie (s. 4 vs 8–9); (d) znaki modyfikatorów ujemnych przepisywane za oryginałem (–/-/−) – zalecam w PL jednolicie „−”.

Glosariusz a Phalanx: na tych stronach brak rozbieżności poza już rozstrzygniętymi (tytuły kart Phalanx nie przejęte: Paraliż, Przysposobienie obronne, Wietkong, Trzecia droga, Traktat USA-Japonia/-Tajwan itd. – przekład wierny EN zgodnie z decyzją 26.10). Zapis „(USA/ZSRR)” (0.6.5) – rekomendacja: w md dodać „(USSR Influence)” przy „Wpływy ZSRR”, w trans zostawić symetrycznie bez EN.

Do decyzji użytkownika: (1) usunięcie kropki z oryginału po „(…, Wydarzenie ZSRR).” (s. 4); (2) ujednolicenie znaku minus w modyfikatorach (s. 3 „–1”, s. 8 „-1”) na „−”; (3) czy w ramce PRZEWRÓT W IRANIE (s. 4) wymuszać EN przy „Kontrola ZSRR” i „Operacje Wojskowe ZSRR” kosztem skali, czy zostawić (raport składu uzasadnia szerokością).
