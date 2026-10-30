# GLOSARIUSZ I ZASADY TŁUMACZENIA – SPQR DELUXE (GMT; Richard Berg, Mark Herman; seria Great Battles of History, tom II)

Utworzono 26.10.2026. Dokument: SPQR_Deluxe_Rule_book_WEB (SPQR: Great Battles of the Roman Republic, 5th Ed., 44 s.). Obowiązuje razem z /home/claude/tr/GLOSARIUSZ.md (zasady A, G, H, K, L, M) i /home/claude/tr/INSTRUKCJA_NOWE.md (format, ramki, kontrola partii) – tych zasad tu nie powtarzamy, podajemy tylko ich zastosowanie w SPQR.

Wzorce brzmień (dostarczone przekłady serii, stan z 26.10.2026): Zasady GBJC (GBJC_Rules_Final_Low-Res_PL.pdf/.docx – wzorzec główny), GBJC Naval, Księga scenariuszy GBJC, errata GBOJC; Great Battles of Alexander 6. wyd. (Deluxe_Alexander_6th_Edition_Rules_PL), moduły GBOA (Diadochoi, Raphia, Tyrant, Scenario Book) i errata GBOA. SPQR to ten sam system, a wiele punktów SPQR 5. wydania ma brzmienie identyczne z GBJC lub Aleksandrem – wtedy obowiązuje brzmienie polskie wzorca (ten sam tekst EN = ten sam tekst PL), także w zdaniach, nie tylko w terminach.

Oznaczenia źródeł w hasłach:
- [z GBJC] – brzmienie z przekładów GBJC (zasady, Naval, księga scenariuszy, errata GBOJC);
- [z GBOA] – brzmienie z Aleksandra 6. wyd. lub modułów GBOA (Diadochoi, Raphia, Tyrant, Scenario Book, errata);
- [z GBJC+GBOA] – to samo brzmienie w obu rodzinach;
- [nowe 26.10 – propozycja] – termin bez odpowiednika w przekładach serii; brzmienie ustalone tu (źródło lub analogia w uwagach); stosować, uwagi zgłaszać w raporcie partii.

Pomoc dla tłumaczy i kontroli: teksty polskie serii – /home/claude/tr/ref/GBoH_PL/docx (z DOCX, „polski (EN)” przy każdym użyciu) i /home/claude/tr/ref/GBoH_PL/pdf (z PDF); wyszukiwarka brzmień: `python3 -I /home/claude/tr/verify/spqr_seria.py 'Orderly Withdrawal'` (dokładny termin EN w nawiasie) lub `python3 -I /home/claude/tr/verify/spqr_seria.py -t 'fragment'` (fragment tekstu). Teksty EN serii: /home/claude/val/en_pages/<DOK>/pNNN.txt (strona EN = strona PDF PL).

## 0. Zastosowanie zasad ogólnych w SPQR

### 0.1 Zasada A – nawiasy EN w md

- W md każdy termin gry przy każdym użyciu: „polski termin (English)”, EN dokładnie jak w danym miejscu oryginału (wielkość liter, liczba, skrót, wersaliki znaczników). Polski termin zawsze według glosariusza, także gdy oryginał używa skrótu nazwy tabeli albo innego zapisu („Clash of Swords chart” – zob. 7).
- Pełna nazwa + skrót w oryginale: „rozkaz indywidualny (Individual Order, IO)”; sam skrót: „rozkaz indywidualny (IO)”; sam kod typu: „lekka jazda (LC)”. Skróty z żetonów i tabel zostają (A.5): TQ, MA, MP, DR, DRM, ZOC, LOS, OC, SC, IO, LC, EIO, OW, PW, MLE, H&D, SRD, MRRC, CRT, AS, DS, DD, RP, PAC, GBoH oraz kody typów i klas (sekcja 2). W nawiasie skrót bez angielskiego „s” i apostrofu („IOs”, „LCs”, „ZOCs” → „(IO)”, „(LC)”, „(ZOC)”), chyba że przepisujemy całą etykietę („Facing and ZOCs”).
- Liczba mnoga typów: „harcownicy (Skirmishers)”, „oddział harcowników (Skirmisher)” – EN jak w danym miejscu.
- Gdy polska forma jest identyczna z EN (hastati, principes, triarii, legion, Sentinum, Telamon itp.), nawias EN pomijamy (jak GBJC „Legion:”); kod z żetonu dopisujemy, gdy stoi w oryginale: „hastati (HA)”.
- Bez nawiasu EN (słowa potoczne i ogólne): gracz, przeciwnik, armia, strona, mapa, heks, bok heksu, wierzchołek heksu, żeton, znacznik (ogólnie), kość, rzut kością (gdy w oryginale nie ma „DR”), tura (ogólnie), oddział, oddział bojowy, dowódca (ogólnie – poza definicją 2.4), wróg / oddział wroga, własny, sąsiedni / sąsiadujący, przyległy, wyeliminować, usunąć, odwrócić (żeton), położyć (znacznik), strzelać, atakować, ruch / poruszać się (zwykły czasownik), zasięg (odległość), teren (ogólnie), piechota i jazda w znaczeniu ogólnym („oddziały piechoty”, „jazda”), liczebniki i numery heksów, nazwy własne historyczne (osoby, ludy, bitwy – sekcja 6), nazwy kolorów legionów.
- Z EN: wszystkie rzeczowniki z sekcji 1–4 (w tym typy oddziałów, fazy, etapy, tabele, znaczniki, współczynniki) oraz czasowniki nazywające mechanizm: zebrać (Rally), przebić (Trump), wycofać się (withdraw – OW, PW), cofnąć się (retreat), zostać rozbitym / ulec rozbiciu (rout), wykonać ucieczkę rozbitych (rout move), wpaść w szał (Rampage), podjąć pościg (Pursue), oderwać się (Break-Off), wykonać posunięcie (Advance), aktywować (activate) przy pierwszym użyciu w punkcie.
- Gęstość: jak w DOCX GBJC (ok. 12–16 nawiasów na 1000 znaków). Strony wyraźnie gęstsze lub rzadsze – sprawdzić.

### 0.2 Lista ZAWSZE (zasada K.2 – w składzie PDF nawias EN raz na akapit; przy obu członach pary w jednym akapicie – przy każdym)

- starcie (Shock, Shock Combat) wobec walka (Combat), walka na dystans (Missile Combat) i bitwa (battle);
- ubytek spójności (Cohesion Hit) / ubytki (Hits);
- test jakości wojsk (TQ Check), test jakości wojsk przed starciem (Pre-Shock TQ Check);
- przewaga (Superiority): przewaga atakującego (AS), przewaga obrońcy (DS), przewaga pozycyjna (Position Superiority), przewaga systemu uzbrojenia (Weapon System Superiority) – AS koliduje z kodem ali na żetonach („AS/XIX”);
- rozkaz indywidualny (IO), rozkaz liniowy (LC) – LC koliduje z lekką jazdą (LC); linia (Line);
- impet (Momentum), przebicie (Trump), przebity (Trumped), pominięty (Bypassed), zakończony (Finished), nieaktywny (Inactive);
- uporządkowany odwrót (Orderly Withdrawal, OW) wobec wycofanie (withdrawal: PW, Army Withdrawal, Line Withdrawal), cofnąć się (retreat) i rozbicie (Rout) / ucieczka rozbitych (Rout Movement);
- wcześniej zaplanowane wycofanie (Pre-Arranged Withdrawal, PW); manipularne wydłużenie linii (Manipular Line Extension, MLE); nękanie i rozproszenie (H&D);
- zebranie (Rally) wobec odzyskiwanie spójności (Recovery); uszczuplony (Depleted); związany walką (Engaged); załamanie (Collapse);
- posunięcie po walce (Advance After Combat) wobec pościg (Pursuit, Pursue) i oderwanie się (Break-Off);
- heks frontowy / skrzydłowy / tylny (Front / Flank / Rear hex);
- kolumna (Column, In Column – szyk) wobec kolumna tabeli wyników starcia (column);
- słoń dowódcy (Leader Elephant) wobec dowódca słoni (Elephant Leader); szał (Rampage); przepuszczenie (Pass-Thru);
- wódz naczelny (OC), dowódca podległy (SC), elitarny wódz (Elite Commander), trybun (Tribune), prefekt sprzymierzeńców (Praefect Sociorum), prefekt jazdy (Praefect Equitum), prokonsul (Proconsul), dowódca zastępczy (Replacement leader);
- typy i klasy oddziałów z kodem żetonu („lekka piechota (LI)”, „hastati (HA)”), legion / ala (Legion/Ala), piechota legionowa (LG);
- nazwy znaczników, tabel i stron żetonów (sekcje 3–4).

W uwagach projektanta, uwagach historycznych, dygresji i przykładach – nawiasy EN tylko przy terminach z tej listy (K.5). Nota redakcji w składzie (pierwsza strona z tekstem ciągłym, s. 2; brzmienie GBJC): „Od redakcji: Angielskie nazwy terminów gry podano w nawiasach przy ich pierwszym użyciu w danym punkcie zasad oraz zawsze przy terminach, które łatwo pomylić.”

### 0.3 G, H, M i konwencje zapisu przyjęte w serii

- Wymiary jak w przekładach serii: „22″ × 34″”, „11″ × 17″”, „8½″ × 11″”, „½″” (znak sekundy, bez przeliczania – G.1); odległości: „70+ paces (yards)” – „70 i więcej kroków (jardów)”, „150+ yards” – „ponad 150 jardów” / „150 i więcej jardów” [z GBJC+GBOA]; „9-foot spear” – „włócznia długości 9 stóp”.
- Daty: BCE / B.C. – p.n.e.; „c. 210 BCE” – „ok. 210 p.n.e.”; rok samodzielnie po „w” – „w 217 r. p.n.e.” (DECYZJE_WALIDACJA, pkt 5).
- Wyniki rzutów i zakresy z półpauzą: „0–6”, „7–9”, „1-9” → „1–9”; stosunki liczebności jak w oryginale z półpauzą („2–1”, „1–2”, „#–1 (lub 1–#)”); „3:1”, „4:1” bez zmian; „2(3)”, „1(4)”, „0(4)” bez zmian; mnożniki „2x”, „3x”, „½x” → „2×”, „3×”, „½×”.
- Przesunięcia kolumn: „1L”, „2L”, „1R” – zostają; przy pierwszym użyciu w punkcie opis: „przesunięcie o 2 kolumny w lewo (2L)” [z GBJC+GBOA].
- Numery reguł z kropką („8.46[1.B]”, „5.42 #1” → „5.42 pkt 1”, „6.68 bullet #6” → „6.68, szósty punktor”, „8.47[2]” bez zmian); „(D/1)” bez zmian.
- Liczba porządkowa wydania: „5th Edition” – „5. wydanie” / „wydanie 5.”, „4th Edition rules” – „zasady 4. wydania”; edition = wydanie (DECYZJE_WALIDACJA, rodzina GBOA).
- Zasady opcjonalne w nagłówkach: „(OPTIONAL)” – „(zasada opcjonalna)” (DECYZJE_WALIDACJA, pkt 1).
- Nazwy znaczników w tekście: polska nazwa wielką literą (A.4), EN w nawiasie dokładnie jak w oryginale (w SPQR zwykle wersalikami): „znacznik Starcie: obowiązkowy test TQ (SHOCK MUST CHECK TQ)”. Kapitaliki `[…]{.smallcaps}` tylko tam, gdzie oryginał ma kapitaliki (np. 8.4, przegląd procedury, pkt 1; 9.96 „Missile Low/No”).
- M: Design Note – UWAGA PROJEKTANTA (Design Note); Play Note – UWAGA DO ROZGRYWKI (Play Note) – zob. sekcja 8.
- Płeć: oryginał mówi „he/his” o graczu i dowódcy – po polsku rodzaj męski („gracz”, „dowódca”), bez „jego/jej”.

### 0.4 Konwencje serii różniące PDF i DOCX (wybór dla SPQR)

| Zjawisko | PDF serii | DOCX serii | SPQR (md) |
|---|---|---|---|
| enemy | „wróg” (GBJC 181×, Aleksander 97×; „oddział wroga”, „ZOC wroga”) | „nieprzyjaciel” (GBJC 205×, Aleksander 157×) | wróg – jedna forma w całym dokumencie (tak jak PDF serii i GLOSARIUSZ_SE); „nieprzyjaciel” w md SPQR nie występuje |
| TQ check | „test TQ” (skrót dla miejsca) | „test jakości wojsk (TQ Check)” | md: „test jakości wojsk (TQ check)”; skład PDF może skrócić do „test TQ” jak PDF GBJC; w nazwach znaczników zawsze „test TQ” |
| Cohesion Hit and TQ Check Chart | „tabela ubytków spójności i testów TQ” | „tabela ubytków spójności i testów jakości wojsk” | md: pełna forma DOCX; PDF – jak PDF GBJC |
| Leaders & Enemy Combat Units | „Dowódcy a oddziały wroga” | „Dowódcy a oddziały bojowe nieprzyjaciela” | md: „Dowódcy a oddziały bojowe wroga” |

### 0.5 Niespójności w dostarczonych przekładach serii (stan 26.10) i wybór dla SPQR

| Termin EN | Warianty w serii | Wybór dla SPQR i powód |
|---|---|---|
| Hastati / Principes / Triarii | GBJC 2.23, 2.4 (Kohorta) i GBJCSB: łacińskie „hastati, principes i triarii” (4×); GBJC (uwaga o legionie, 1×): „hastatów, pryncypów i triariuszy” | wariant dominujący: hastati, principes, triarii – nieodmienne (zob. 2.2; sprawa w 11) |
| Velites | GBJC 2.23 „Welitów”, GBJCSB „welitów” | welici (Velites) – odmieniane |
| Shock Requirements | GBJC 7.3 (nagłówek PDF i DOCX) „Warunki starcia”; indeks PDF GBJC „wymogi starcia”; Aleksander 7.3 „Wymogi starcia” | Wymogi starcia (3:2) |
| Movement Procedures | GBJC 6.3 „Procedury ruchu”; Aleksander 6.3 „Procedura ruchu” | Procedury ruchu (liczba mnoga jak EN) |
| Recovery | GBJC 10.16 nagłówek „Odzyskanie spójności”, tekst i indeks GBJC „odzyskiwanie spójności”; Aleksander 10.16 „Odzyskiwanie spójności” | odzyskiwanie spójności (rozkaz: „rozkaz odzyskania spójności” – jak GBJC) |
| Elephant Rampage | GBJC 9.93 „Szał słoni”; Aleksander 11.14 „Szał słonia” | Szał słoni (wzorzec główny; żeton = kilka słoni) |
| Example #1 | GBJC: „PRZYKŁAD NR 1” 3×, „PRZYKŁAD 1” 1×; Aleksander: po 6× | PRZYKŁAD NR 1 (Example #1) (9:7) |
| Edition Note | GBJC „UWAGA DO EDYCJI DELUXE”; rodzina GBOA – „wydanie” (decyzja walidacji); okładka GBJC „Wydanie Deluxe” | „wydanie”: „Uwaga do 5. wydania (5th Edition Note):” (w SPQR etykieta pogrubiona, nie ramka) |
| Active Leader | GBJC „dowódca aktywny (Active Leader)”; Aleksander „dowódca aktywowany (Activated Leader)” – różny tekst EN | SPQR ma „Active Leader” – dowódca aktywny |

## 1. Mechanika i terminy ogólne (alfabetycznie wg EN)

| EN | PL | Uwagi / źródło |
|---|---|---|
| activate / activation | aktywować / aktywacja | [z GBJC+GBOA]; „order of activation” – kolejność aktywacji |
| Activated (strona żetonu dowódcy) | „aktywowany” (strona „aktywowany”) | [z GBJC+GBOA] 4.0; zob. 4 |
| Activation Phase | faza aktywacji | [z GBJC] 5.12; = Leader Activation Phase |
| Active Fire | ostrzał aktywny | [z GBJC+GBOA] 9.85 (skorpiony) |
| Active Leader | dowódca aktywny | [z GBJC] 2.4; nie „aktywowany” (to Activated Leader u Aleksandra) |
| active player / Active Player | gracz aktywny | [z GBJC+GBOA] |
| active unit | oddział aktywny | [z GBJC] 8.23 |
| Adjust Columns and Resolve (Step 3) | przesuń kolumny i rozstrzygnij walkę | [z GBJC] 8.46 |
| Advance / advance (after combat) | posunięcie / wykonać posunięcie | [z GBJC+GBOA]; „advancing unit” – oddział wykonujący posunięcie; „must advance” – musi wykonać posunięcie |
| Advance After Combat / Advance after Combat | posunięcie po walce | [z GBJC+GBOA] 8.5 |
| Advance (podpis diagramu 8.53) / No Advance / Pivot Advance / Advance with Wheel | posunięcie (Advance) / brak posunięcia / posunięcie z obrotem / posunięcie połączone z manewrem zwrotu | [z GBOA] podpisy ilustracji Aleksandra (to samo zestawienie) |
| advantage / advantages (ogólnie); superiority (opisowo, np. „superiority in command”) | przewaga / korzyść, atut; przewaga | [z GBJC+GBOA]: 8.46 „the effect of any advantages” – „skutki wszelkich przewag” (GBJC), 5.4 „superiority in command” – „przewaga w dziedzinie dowodzenia” (GBJC); w tekście opisowym bez EN; termin gry Superiority – zawsze z EN (0.2, 7) |
| Apply Results (Step 4) | zastosuj wyniki | [z GBJC] 8.46 |
| approach / approached from a Rear (Flank) hex | zbliżać się / gdy przeciwnik zbliża się od strony heksu tylnego (skrzydłowego) | [z GBJC] 6.52 |
| Army Withdrawal | wycofanie armii | [z GBJC+GBOA] 11.0, 11.2 |
| Army Withdrawal Level / Withdrawal Level | próg wycofania armii / próg wycofania | [z GBJC+GBOA] |
| attack / attacker / attacking player | atak / atakujący / gracz atakujący | ogólne; bez EN |
| Attack Superiority (AS) / Attack Superior | przewaga atakującego (AS) / mieć przewagę atakującego | [z GBJC+GBOA]; AS ≠ ala sociorum na żetonach (7) |
| automatic (Cohesion Hit) | automatyczny ubytek spójności | [z GBJC] |
| Away („Away” means…) | „oddalanie się” (Away) | [z GBJC] 6.51 – to samo zdanie EN |
| Basic (stacking) | podstawowy | [z GBJC] 6.63; oddział podstawowy, wiersz „Podstawowy” tabeli |
| battle / battlefield | bitwa / pole bitwy | nigdy „walka” ani „starcie” |
| block / blocked / unobstructed path | blokować / zablokowany / niezablokowana ścieżka | [z GBJC] 4.21, 8.14, 10.22 |
| Break-Off | oderwanie się; oderwać się | [z GBJC] 8.62 |
| Bypassed Leader / Bypassed / passed over | dowódca pominięty / pominięty | [z GBJC+GBOA] 5.44 |
| casualty (dowódcy) | strata | [z GBJC+GBOA]; zwroty jak w GBJC (te same zdania EN): 4.73 „has suffered a casualty” – „dowódca został trafiony”; 8.19 „has suffered a “casualty”” – „dowódca znalazł się wśród „strat””; 8.44 i przykład starcia „suffer a casualty / has become a casualty” – „padł ofiarą walki”; „casualties rose” (tekst historyczny) – straty |
| Cavalry Line Withdrawal | wycofanie linii jazdy | [z GBJC+GBOA] 6.57 |
| Cavalry Pursuit | pościg jazdy | [z GBJC+GBOA] 8.6 |
| Cavalry Pursuit Option | opcja pościgu jazdy | [nowe 26.10 – propozycja] 8.66; „opcja” jak Trump Option |
| change facing / facing change | zmienić front / zmiana frontu | [z GBJC+GBOA] |
| change formation | zmienić szyk | [z GBJC] 6.71 |
| Charge, The / charge (szarża) | szarża | [z GBJC+GBOA] 8.43; „charged by” – zaatakowany szarżą |
| Charisma / Charisma Rating | charyzma / współczynnik charyzmy | [z GBJC+GBOA] |
| Class | klasa | [z GBJC+GBOA]; „class status in Roman society” – klasa społeczna (bez EN) |
| Clash of Spears and Swords / Clash of Spears & Swords | szczęk włóczni i mieczy | [nowe 26.10 – propozycja] 8.45; złożenie „szczęku włóczni” (Aleksander) i „szczęku mieczy” (GBJC) |
| Clear (terrain, hex) | teren otwarty / heks terenu otwartego | [z GBJC+GBOA] |
| Cohesion | spójność | [z GBJC+GBOA] |
| Cohesion Hit(s) / Hit(s) | ubytek (ubytki) spójności / ubytek (ubytki) | [z GBJC+GBOA]; nigdy „trafienie” |
| Cohesion Markers / numeric marker | znaczniki spójności / znacznik liczbowy | [z GBJC+GBOA] 10.12 |
| Collapse / Collapse step | załamanie / krok załamania | [z GBJC+GBOA] 8.47 |
| Collapse Check / Collapse TQ check | test załamania / test jakości wojsk w kroku załamania | [nowe 26.10 – propozycja] 8.5 (uwaga projektanta), 8.61 |
| Column / In Column / Column Movement | kolumna / w kolumnie / ruch w kolumnie | [z GBJC+GBOA] 6.7; szyk, nie kolumna tabeli (7) |
| column (tabeli) / base column / Shock Column / column adjustment, Column Shifts | kolumna / kolumna wyjściowa / kolumna starcia / przesunięcie kolumny, przesunięcia kolumn | [z GBJC+GBOA] |
| Combat / combat unit / combat results | walka / oddział bojowy / wyniki walki | [z GBJC+GBOA]; 8.0 „Combat” – Walka |
| Command Range | zasięg dowodzenia | [z GBJC+GBOA] |
| Command Restriction | ograniczenie dowodzenia; „Command Restriction word” – słowo ograniczenia dowodzenia | [z GBJC] 4.1, 4.35 |
| command hierarchy | hierarchia dowodzenia | [nowe 26.10 – propozycja] 4.33 |
| Commander | wódz | [z GBJC+GBOA]; „Leader: Interchangeable with the word Commander” – „określenie używane zamiennie ze słowem „wódz”” (zob. 7) |
| counter / marker | żeton / znacznik | [z GBJC+GBOA] |
| crossbow / Welsh longbow (uwaga historyczna 8.1) | kusza / walijski łuk długi | [nowe 26.10 – propozycja] |
| cumulative | sumują się | [z GBJC] |
| Defense Superiority (DS) | przewaga obrońcy (DS) | [z GBJC+GBOA] |
| defender / defending player | obrońca / gracz broniący się | ogólne |
| Depleted / Depletion | uszczuplony / uszczuplenie | [z GBJC+GBOA] 10.3 |
| Determine Size Ratio Difference (Step 2) | ustal różnicę stosunku liczebności | [z GBJC] 8.46 |
| Determine Superiority (Step 1) | ustal przewagę | [z GBJC] 8.46 |
| die / DR / DRM / die roll | kość / rzut kością (DR) / modyfikator rzutu kością (DRM) / rzut kością | [z GBJC+GBOA] 2.4 „DR: Die roll.” – „DR: rzut kością (die roll)” |
| Die Roll of Doom | fatalny rzut | [z GBJC+GBOA] 5.33 |
| directional die roll | rzut kością na kierunek | [z GBJC] 9.14 |
| Double Depth / Double-Depth (DD) formation | szyk podwójnej głębokości (DD) | [z GBOA] 9.5 |
| Double Depth Phalanx / Double-Depth Phalanxes | falanga o podwójnej głębokości / falangi o podwójnej głębokości | [z GBOA] |
| elevation / level / Level 1, Level 2 | wysokość terenu / poziom / poziom 1, poziom 2 | [z GBJC+GBOA]; „moving uphill” – ruch pod górę |
| eliminate / eliminated | wyeliminować / wyeliminowany | [z GBJC+GBOA] |
| Elite Commander / Elite OC / Elite Overall Commander | elitarny wódz / elitarny wódz naczelny (OC) | [z GBJC+GBOA] |
| Elite Commander Initiative | inicjatywa elitarnego wodza | [z GBOA] 5.5 |
| Elite Initiative | inicjatywa elitarna | [z GBJC+GBOA] |
| Elite Initiative Orders (EIO) Phase / EIO Phase | faza rozkazów inicjatywy elitarnej (EIO) | [z GBJC+GBOA] 5.51 |
| enable Shock | umożliwić starcie | [nowe 26.10 – propozycja] 4.1, 4.52 |
| enemy | wróg (oddział wroga, ZOC wroga) | [z GBJC+GBOA – PDF] zob. 0.4 |
| Engaged / Engaged rule | związany walką / zasada „związanie walką” | [z GBJC+GBOA] 10.4 |
| Entry Reaction / Entry Reaction Fire | ostrzał reakcyjny przy wejściu | [z GBJC+GBOA] 8.21 |
| Entry Fire | ostrzał przy wejściu | [z GBJC+GBOA] 8.21 |
| exit hex | heks wyjścia | [nowe 26.10 – propozycja] 8.62 |
| Extended Movement Allowance | rozszerzona zdolność ruchu | [z GBOA] 2.25 |
| Extended Range | zasięg rozszerzony | [z GBJC+GBOA] 8.16 |
| Facing / face (a vertex, a hexside) | ustawienie frontu / być zwróconym frontem do (wierzchołka, boku heksu) | [z GBJC+GBOA] |
| Ferocity / Ferocity check | zaciekłość / test zaciekłości | [z GBJC] 9.94 |
| Finished / Finished Leader / Finish (him) | zakończony / dowódca zakończony / staje się zakończony | [z GBJC+GBOA]; „temporarily finished” (5.53) – „chwilowo zakończony” |
| fire / Fire order / Fire mode | strzelać, prowadzić ostrzał / rozkaz ostrzału / tryb ostrzału | [z GBJC+GBOA] |
| Flank / Flank hex / Flank-to-Flank / front-flank hex | skrzydło / heks skrzydłowy / skrzydłem do skrzydła / przedni heks skrzydłowy | [z GBJC+GBOA] |
| Flip and Remove | odwrócenie i usunięcie | [z GBJC] 3.0 D.3 |
| formation | szyk | [z GBJC+GBOA] |
| friendly | własny | ogólne |
| Front / Front hex / frontal(ly) / Front-to-Rear | front / heks frontowy / od frontu / frontem do tyłu | [z GBJC+GBOA] |
| Front-to-Flank Maneuver | manewr front–skrzydło | [z GBOA] 6.43 |
| Game Turn | tura gry | [z GBJC+GBOA] |
| Hand-to-Hand Struggle, The | zmagania wręcz | [z GBJC+GBOA] 8.46 |
| Harassment & Dispersal (H&D) / H&D fire | nękanie i rozproszenie (H&D) / ostrzał w ramach nękania i rozproszenia (H&D) | [z GBJC+GBOA] 8.3 |
| “heavy” units / “light” units | „ciężkie” oddziały / „lekkie” oddziały | [z GBJC] 7.31 |
| hex / hexside / vertex (vertices) | heks / bok heksu / wierzchołek heksu | [z GBJC+GBOA] |
| Hit allocation / allocated, distributed | przydział ubytków / przydzielone, rozdzielone | [z GBJC] 10.13 |
| impassable | nieprzekraczalny | [z GBJC+GBOA] |
| Impetuosity | porywczość | [z GBJC] 9.95 |
| Inactive / Inactive Leader / inactive player | nieaktywny / dowódca nieaktywny / gracz nieaktywny | [z GBJC+GBOA] |
| Individual Order(s) (IO) | rozkaz indywidualny (rozkazy indywidualne) (IO) | [z GBJC+GBOA]; „IO Move order” – rozkaz indywidualny ruchu |
| Initial Orders Phase | początkowa faza rozkazów | [z GBJC+GBOA] |
| Initiative / Initiative Rating | inicjatywa / współczynnik inicjatywy | [z GBJC+GBOA] |
| Leader / leader | dowódca | [z GBJC+GBOA] |
| Leader Casualty / Leader Casualties / leader casualty check | strata wśród dowódców / straty wśród dowódców / sprawdzenie strat wśród dowódców | [z GBJC+GBOA] 4.73, 8.19, 8.44 |
| Line | linia | [z GBJC+GBOA] 2.4, 4.32 |
| Line Command (LC) | rozkaz liniowy (LC) | [z GBJC+GBOA]; „2 LC capability” – zdolność wydania 2 rozkazów liniowych |
| Line Command Eligibility | uprawnienia do rozkazów liniowych | [z GBJC+GBOA] 4.33 |
| Line Command Rating | współczynnik rozkazów liniowych | [z GBJC] 4.1 |
| Line Composition | skład linii | [z GBJC+GBOA] 4.32 |
| Line of Sight (LOS) | linia widzenia (LOS) | [z GBJC+GBOA] 8.14 |
| Line Withdrawal | wycofanie linii | [z GBJC] 6.57 |
| two-space (three-space) Line | linia z odstępami do 2 (3) heksów | [nowe 26.10 – propozycja] 4.32; nie „linia dwuheksowa” (oddziały dwuheksowe to falangi) |
| MA (Movement Allowance) | zdolność ruchu (MA) | [z GBJC+GBOA] |
| Manipular Line Extension (MLE) / MLE rights | manipularne wydłużenie linii (MLE) / prawo do MLE | [nowe 26.10 – propozycja] 9.66; z GBJC „wydłużenie linii (Line Extension)” + „legion manipularny” |
| melee | walka wręcz | [z GBJC+GBOA] (opis starcia 2.4) |
| Missile Combat | walka na dystans | [z GBJC+GBOA] |
| Missile Fire / Missile Fire Resolution / Missile Fire DR | ostrzał / rozstrzyganie ostrzału / rzut kością na ostrzał | [z GBJC+GBOA] |
| Missile Capability / Missile Indicator / Type of Missile | zdolność do ostrzału / oznaczenie pocisku / rodzaj pocisku | [z GBJC+GBOA] |
| Missile Range / range | zasięg ostrzału / zasięg | [z GBJC+GBOA] |
| Missile Strength / missile strength | siła ostrzału | [z GBJC+GBOA] 8.15 |
| Missile Supply / missile supply markers | zapas pocisków / znaczniki zapasu pocisków | [z GBJC+GBOA] 8.17, 9.12 |
| missile unit / Missile-armed | oddział strzelający / uzbrojony w pociski | [z GBJC+GBOA] |
| Momentum | impet | [z GBJC+GBOA] |
| Momentum attempt / Momentum DR, Momentum die roll / first-try Momentum die rolls | próba uzyskania impetu / rzut kością na impet / rzuty na impet przy pierwszej próbie | [z GBJC+GBOA]; ostatnie – [nowe 26.10 – propozycja] 9.95 |
| Momentum Orders Phase / Momentum-generated Orders Phase | faza rozkazów uzyskana dzięki impetowi | [z GBJC+GBOA] |
| Momentum Phase | faza impetu | [z GBJC+GBOA] |
| Momentum Trump | przebicie impetu | [z GBJC+GBOA] 5.42 |
| momentum (fizyczny rozpęd, małą literą) | rozpęd | [nowe 26.10 – propozycja] 8.15 i 8.46 (uwagi projektanta); nie „impet” (7) |
| Move / Move order / Move mode / moving player | ruch / rozkaz ruchu / tryb ruchu / gracz wykonujący ruch | [z GBJC+GBOA] |
| Movement / Movement Allowance / Movement Point (MP) | ruch / zdolność ruchu / punkt ruchu (MP) | [z GBJC+GBOA] |
| Movement and Missile Fire Segment / Movement/Missile Segment / Movement and Missile Segment | etap ruchu i ostrzału | [z GBJC+GBOA] |
| Movement Cost Chart | tabela kosztów ruchu | [z GBJC+GBOA] 6.27 |
| Non-Momentum Trump | przebicie niezwiązane z impetem | [z GBJC+GBOA] 3.0 A |
| Off-Map Regroup | przegrupowanie poza mapą | [z GBJC] 8.64 |
| Order(s) / orders / order path | rozkaz(y) / rozkazy / ścieżka rozkazu | [z GBJC+GBOA]; „for the sake of brevity, the word orders…” – zdanie jak GBJC |
| Order/Line Command | rozkaz/rozkaz liniowy | [nowe 26.10 – propozycja] 2.4; GBJC: „Rozkaz lub rozkaz legionowy/liniowy” (inny tekst EN) |
| Order Phase (4.91 – literówka oryginału zamiast Orders Phase) | faza rozkazów (Order Phase) | przekładać jak Orders Phase, EN jak w oryginale; zgłosić jako błąd oryginału |
| Orderly Withdrawal (OW) / Orderly Withdraw | uporządkowany odwrót (OW) / wykonać uporządkowany odwrót | [z GBJC+GBOA] 6.5 |
| Orders Phase | faza rozkazów | [z GBJC+GBOA] |
| owning player | gracz, do którego należy oddział | [z GBJC] |
| pass (5.15) | spasować | [z GBJC] |
| Pass-Thru / Elephant Pass-Thru | przepuszczenie / przepuszczenie słoni | [z GBJC] 9.11 |
| Pass-Thru TQ Check / Elephant Pass-Thru Check | test jakości wojsk po przepuszczeniu / test po przepuszczeniu słoni | [z GBJC] 9.11; drugi – [nowe 26.10 – propozycja] 9.24 |
| pivot | obrót, obracać się | [z GBOA] 6.43, 7.13 |
| Position Superiority | przewaga pozycyjna | [z GBJC+GBOA] |
| Pre-Arranged Withdrawal / Pre-arranged Withdrawal (PW) | wcześniej zaplanowane wycofanie (PW) | [z GBJC+GBOA] 6.8 |
| Pre-Shock Procedure / The Basic Pre-Shock Procedure | procedura przed starciem / podstawowa procedura przed starciem | [z GBJC+GBOA] 8.42 |
| Pre-Shock TQ Check | test jakości wojsk przed starciem | [z GBJC+GBOA]; skład PDF: „test TQ przed starciem” (0.4) |
| Pursue / Pursuit / pursuing cavalry | pościg; podjąć pościg / pościg / jazda prowadząca pościg | [z GBJC+GBOA] 8.6 |
| Pursuit Rating | współczynnik pościgu | [z GBJC] (errata GBOJC) 8.66 |
| Rally / rally / Rallied / Rally attempt | zebranie; zebrać / zebrany / próba zebrania | [z GBJC+GBOA] 10.28 |
| Rally order / Recovery order | rozkaz zebrania / rozkaz odzyskania spójności | [z GBJC] |
| Rampage / Rampages / rampaging (Elephant) / Rampage DR | szał / wpada w szał / (słoń) w szale, rozszalały / rzut kością na szał | [z GBJC+GBOA] 9.14 |
| range (odległość) / at a range of 2 hexes | zasięg / z odległości 2 heksów | [z GBJC+GBOA] |
| Reaction Facing Change | reakcyjna zmiana frontu | [z GBJC+GBOA] 7.15 |
| Reaction Fire | ostrzał reakcyjny | [z GBJC+GBOA] 8.2 |
| Rear / Rear hex | tył / heks tylny | [z GBJC+GBOA] |
| Re-activation / Reactivation / Re-Activated | ponowna aktywacja / ponownie aktywowany | [z GBJC+GBOA] 5.33 |
| Recovery / recover Hits | odzyskiwanie spójności / odzyskiwać spójność (usuwać ubytki) | [z GBJC+GBOA] 10.16; zob. 0.5 |
| Regroup and Return / Regroup and Return Order | przegrupowanie i powrót / rozkaz przegrupowania i powrotu | [z GBJC] 8.64 |
| Reload / Reload Segment | uzupełnianie pocisków / etap uzupełniania pocisków | [z GBJC+GBOA] |
| Replacement leader / Replacement | dowódca zastępczy / zastąpienie | [z GBJC+GBOA] 4.74 |
| Republican era / tribal-style warfare | epoka republikańska / walka w stylu plemiennym | [nowe 26.10 – propozycja] |
| Resolve the Shock | rozstrzygnięcie starcia | [z GBJC] 3.0 B.2.e |
| Resolution of Possible Leader Casualties | rozstrzygnięcie ewentualnych strat wśród dowódców | [z GBJC] 3.0 B.2.c |
| retreat (v., n.) / retreating units | cofnąć się, cofanie się / cofające się oddziały | [z GBJC] 10.42 („cofnąć się o 1 heks”); OW „is a form of retreat” – „forma cofania się” [z GBJC PDF] |
| Retreat Edge | krawędź odwrotu | [z GBJC+GBOA] |
| Retire Reaction / Retire Reaction Fire | ostrzał reakcyjny przy wyjściu | [z GBJC+GBOA] 8.22 |
| Return Fire | ostrzał odwetowy | [z GBJC+GBOA] 8.23 |
| Reverse Face / Reverse Face Maneuver | odwrócić front / manewr odwrócenia frontu | [z GBOA] 6.45, 7.16 |
| Rough Terrain / Rough | teren trudny | [z GBJC+GBOA] |
| Rout / rout (v.) / Routed / routing unit | rozbicie / zostać rozbitym, ulec rozbiciu / rozbity / uciekający oddział | [z GBJC+GBOA] |
| Rout move / Rout Movement / Rout Movement Segment | ucieczka rozbitych / ucieczka rozbitych / etap ucieczki rozbitych | [z GBJC+GBOA] |
| rout check / rout threshold | test rozbicia / próg rozbicia | [z GBJC] |
| Rout and Reload Phase | faza rozbicia i uzupełniania pocisków | [z GBJC+GBOA] |
| Rout Points (RP) | punkty rozbicia (RP) | [z GBJC+GBOA] |
| Shock / Shock Combat | starcie | [z GBJC+GBOA] |
| Shock attack / Shock attack (v.) | atak w starciu / atakować w starciu, przeprowadzić atak w starciu | [z GBJC+GBOA] |
| Shock-capable / non-Shock-capable | zdolny do starcia / niezdolny do starcia | [z GBJC+GBOA] |
| Shock Designation | wyznaczenie do starcia | [z GBJC+GBOA] |
| Shock Determination (4.83) | ustalanie parametrów starcia | [nowe 26.10 – propozycja]; jednorazowe, z EN; chodzi o wybór typu oddziału do 8.45–8.46 |
| Shock Resolution | rozstrzyganie starcia; rozstrzygnięcie starcia | [z GBJC+GBOA] |
| Simultaneous Rout (indeks) | jednoczesne rozbicie | [nowe 26.10 – propozycja] |
| Size / Size Rating / Size points | liczebność / współczynnik liczebności / punkty liczebności | [z GBJC+GBOA] |
| Size advantage | przewaga liczebności (Size) | [z GBOA] przykłady Aleksandra; wyjątek od zasady L opisany w 10 |
| Size Ratio Difference (SRD) / size ratio | różnica stosunku liczebności (SRD) / stosunek liczebności | [z GBJC+GBOA] |
| stack / stacking / Stacking | stos / łączenie w stosy | [z GBJC+GBOA] |
| stacking order / top unit / bottom unit | kolejność w stosie / oddział wierzchni / oddział spodni | [z GBJC] |
| Stacking Chart(s) / Voluntary / Rout (rodzaje ruchu w tabeli) | tabela (tabele) łączenia w stosy / ruch dobrowolny / ucieczka rozbitych | [z GBJC] 6.63, 6.69 |
| Moving through… / Stopping in… (kolumny tabeli) | przejście przez… / zatrzymanie w… | [z GBJC] |
| Different Color / Same Color / Different Class / Roman (założenia 6.63) | inny kolor / ten sam kolor / inna klasa / rzymski | [nowe 26.10 – propozycja] |
| voluntary / involuntary, mandatory movement | ruch dobrowolny / niedobrowolny | [z GBJC] 6.6 |
| Voluntary Stacking | dobrowolne łączenie w stosy | [nowe 26.10 – propozycja] 6.6 (uwaga projektanta) |
| Strategy / Strategy Rating | współczynnik strategiczny | [z GBJC+GBOA] |
| Subordinate Commander (SC) | dowódca podległy (SC) | [z GBJC+GBOA] |
| Superiority | przewaga | [z GBJC+GBOA] |
| Terrain / terrain cost | teren / koszt terenu | [z GBJC+GBOA] |
| Terrain Effects Chart | tabela skutków terenu | [z GBJC+GBOA] (GBJCSB, Tyrant) 6.24 |
| threshold (TQ threshold) | próg (próg jakości wojsk (TQ)) | [z GBJC] |
| TQ / Troop Quality / TQ Rating | jakość wojsk (TQ) / współczynnik jakości wojsk | [z GBJC+GBOA] |
| TQ Check | test jakości wojsk | [z GBJC+GBOA]; PDF: „test TQ” (0.4) |
| Trump / Trump Option / trumped / trumping leader | przebicie / opcja przebicia / przebity / dowódca przebijający | [z GBJC+GBOA] |
| Trumping the Trump / trump-the-trump | przebicie przebicia | [z GBJC+GBOA] 5.42 |
| Type | typ | [z GBJC+GBOA] |
| unit | oddział | [z GBJC+GBOA]; nigdy „jednostka” |
| Weapon System / weapon class / weapons/armor system | system uzbrojenia / klasa uzbrojenia / system uzbrojenia zaczepnego i ochronnego | [z GBJC+GBOA] |
| Weapon System Superiority | przewaga systemu uzbrojenia | [z GBJC+GBOA] |
| Wheeling Maneuver / Wheel | manewr zwrotu / wykonać manewr zwrotu | [z GBOA] 6.44 |
| withdraw (OW, PW, dowódcy 4.72) / withdrawing unit | wycofać się / wycofujący się oddział | [z GBJC+GBOA] |
| Withdrawal Fire (indeks 6.55) | ostrzał podczas wycofania | [nowe 26.10 – propozycja] |
| Withdrawal Phase | faza wycofania | [z GBJC+GBOA] |
| within one Hit of Rout (indeks, 8.47) | o jeden ubytek od rozbicia | [nowe 26.10 – propozycja] |
| Zone of Control (ZOC) / ZOCs | strefa kontroli (ZOC) / strefy kontroli (ZOC) | [z GBJC+GBOA] |

### 1.1 Teren i mapa

| EN | PL | Uwagi / źródło |
|---|---|---|
| map / map sheet / hex grid / battlefield | mapa / arkusz mapy / siatka heksagonalna / pole bitwy | [z GBJC+GBOA] |
| Clear / Clear hex / Clear and level | teren otwarty / heks terenu otwartego / otwarty i płaski | [z GBJC+GBOA] |
| Rough Terrain (Woods, Broken, Marsh) | teren trudny (las, teren nierówny, bagno) | [z GBJC+GBOA] 6.24 |
| Woods / Woods hex / Level 2 Woods hex | las / heks lasu / heks lasu na poziomie 2 | [z GBJC+GBOA] |
| Broken | teren nierówny | [z GBJC] |
| Marsh | bagno | [z GBJC] |
| Stream / River / Aufidus River | strumień / rzeka / rzeka Aufidus | [z GBJC] (GBJCSB: legenda mapy) |
| town / the town of Cannae | miasto / miasto Kanny | [nowe 26.10 – propozycja] 6.24, 8.14 |
| Roman Road / dirt road | droga rzymska / droga gruntowa | [z GBJC] („Road” – droga) |
| Roman Camp (mapa Beneventum) | obóz rzymski | [z GBJC] („obóz (Camp)”) |
| elevation / Level / higher elevation / uphill | wysokość terenu / poziom / wyżej położony heks / pod górę | [z GBJC+GBOA] |
| impassable hexes or hexsides | nieprzekraczalne heksy lub boki heksów | [z GBJC] 6.24 |
| vacant hex / friendly-occupied hex / enemy-occupied hex | pusty heks / heks zajęty przez własny oddział / heks zajęty przez wroga | [z GBJC] 10.22 |
| majority terrain | teren przeważający w heksie | [nowe 26.10 – propozycja] 6.23 |
| Compass (róża kierunków na mapie) | róża wiatrów | [z GBJC] 9.14 |
| retreat edge (mapa) | krawędź odwrotu | zob. 1 |

## 2. Oddziały, formacje i typy (z kodami żetonów), dowódcy i współczynniki

### 2.1 Typy oddziałów (Type) – kody z żetonów

| EN (kod) | PL | Uwagi / źródło |
|---|---|---|
| Phalanx (PH); a Phalanx unit; Phalanxes; the Phalanx (szyk) | falanga (PH); oddział falangi; falangi; falanga | [z GBJC+GBOA]; „phalangite(s)” – falangita (falangici) [z GBOA] |
| Heavy Infantry (HI) | ciężka piechota (HI) | [z GBJC+GBOA] |
| Medium Infantry (MI) | średnia piechota (MI) | [z GBJC+GBOA] |
| Legion Infantry (LG); LG units, Legion units | piechota legionowa (LG); oddziały legionowe (LG) | [nowe 26.10 – propozycja] dla nazwy typu; „oddziały legionowe (LG) z SPQR” – [z GBJC] 2.23 |
| Light Infantry (LI) | lekka piechota (LI) | [z GBJC+GBOA] |
| Skirmisher(s) (SK) | harcownicy (SK); oddział harcowników | [z GBJC+GBOA] |
| Barbarian Infantry (BI) | piechota barbarzyńska (BI) | [z GBJC] |
| Heavy Cavalry (HC) | ciężka jazda (HC) | [z GBJC+GBOA] |
| Roman Cavalry (RC) | jazda rzymska (RC) | [z GBJC] |
| Light Cavalry (LC) | lekka jazda (LC) | [z GBJC+GBOA]; kod LC = także rozkaz liniowy (7) |
| Lancers (LN) | kopijnicy (LN) | [z GBJC+GBOA] |
| Barbarian Cavalry (BC) | jazda barbarzyńska (BC) | [z GBJC] 8.66 |
| Elephant(s) (EL) | słonie (EL); oddział słoni | [z GBJC+GBOA] |
| Chariot(s) (CH); Gallic Chariot (CH) | rydwany (CH); rydwan galijski (CH) | [z GBJC+GBOA]; „galijski” – [nowe 26.10 – propozycja] |
| Artillery; Scorpio (typ na żetonie: LI) | artyleria; skorpion | [z GBJC+GBOA]; skorpiony traktuje się jak LI (9.81) |
| Infantry / Cavalry (ogólnie) | piechota / jazda | [z GBJC+GBOA]; nigdy „kawaleria” |

### 2.2 Klasy (Class) i rodzaje pocisków

| EN (kod) | PL | Uwagi / źródło |
|---|---|---|
| Hastati (HA); HA Class, LG Type | hastati (HA); klasa HA, typ LG | wariant dominujący w serii (0.5): łacińskie, nieodmienne, małą literą w tekście, bez nawiasu EN (0.1): „oddział hastati”, „linia hastati”, „hastati legionu XIV”; „a Hastati / the Hastati” (jeden żeton) – „oddział hastati”; etykieta 2.4 „Hastati:” – „Hastati:” |
| Principes (PR) | principes (PR) | jak wyżej [z GBJC]; „oddział principes” |
| Triarii (TR) | triarii (TR) | jak wyżej [z GBJC]; „Triarii units” – oddziały triarii; „HA/PR/CO/TR units” – oddziały HA/PR/CO/TR |
| Velites | welici (Velites); oddział welitów | [z GBJC] („Welitów”, GBJCSB „welitów”); odmieniane: welici, welitów, welitom, welitami; klasa (4.52 „as its one Class”) – kodu w tekście brak, nie tworzyć |
| Cohort (CO); Ala Cohorts | kohorta (CO); kohorty ali | [z GBJC]; „ali” – zob. 2.3 |
| Hoplite (HO); HO Class, HI Type; Hoplite-style Heavy infantry; Mercenary Hoplite | hoplici (HO); klasa HO, typ HI; ciężka piechota typu hoplickiego; najemni hoplici | [z GBOA] |
| Cataphract (CAT) | katafrakci (CAT); jazda katafraktów | [z GBJC+GBOA] |
| A = arrow / J = javelin / S = stone / B = Bolt | A = strzała / J = oszczep / S = kamień / B = bełt | [z GBOA] (Aleksander 2.21: „S = kamień (stone)”; GBJC: „pocisk z procy (stone pellet)” – inny tekst EN) |
| Archers (A); Archer | łucznicy (A); łucznik | [z GBJC+GBOA] |
| Slingers (S) | procarze (S) | [z GBJC+GBOA] |
| Javelinists (J); foot javelinists; Mounted Javelinists | oszczepnicy (J); piesi oszczepnicy; konni oszczepnicy | [z GBJC+GBOA] |
| Mounted Archers | łucznicy konni | [z GBJC] 6.55 |
| Light Infantry Archers (LI Class A) / Light Cavalry Archers / Skirmisher and Light Infantry Archers (Class A) | łucznicy lekkiej piechoty (LI klasy A) / łucznicy lekkiej jazdy / harcownicy i łucznicy lekkiej piechoty (klasy A) | [z GBJC+GBOA] |
| Archer Screen („a” na żetonie słoni) | osłona łuczników | [z GBJC] 2.25 |
| Mounted Javelin (wiersz MRRC) / Elephant Screen (wiersz MRRC) | wiersz „konni oszczepnicy” (Mounted Javelin) / wiersz „osłona słoni” (Elephant Screen) | [nowe 26.10 – propozycja]; nazwa wiersza z EN, bo tabela jest po angielsku |

### 2.3 Organizacja rzymska i kartagińska

| EN | PL | Uwagi / źródło |
|---|---|---|
| Legion; I Legion, III Legion, XIV Legion; Legions | legion; legion I, legion III, legion XIV; legiony | [z GBJC] („legion X”); numer po nazwie, cyfry rzymskie bez zmian |
| Legion/Ala; Legions/Alae; Roman Legion/Ala infantry | legion/ala; legiony/alae; rzymska piechota legionów i ali | [nowe 26.10 – propozycja]; z EN |
| Ala; Alae | ala (odm.: ali, alę, alą, ali); lm. alae (nieodmienne) | [nowe 26.10 – propozycja]; łac. termin konstrukcyjny gry (2.7); lm. łacińska, by uniknąć polskiego „ale” |
| Alae Sociorum / Ala infantry units / AS/XIX, AS/XIV | alae sociorum („skrzydła sprzymierzeńców”) / oddziały piechoty ali / AS/XIX, AS/XIV bez zmian | [nowe 26.10 – propozycja]; AS na żetonie ≠ AS = przewaga atakującego (7) |
| extraordinarii (kursywa) | *extraordinarii* | łacina bez tłumaczenia, kursywą jak w oryginale; „elite cohorts of infantry” – doborowe kohorty piechoty |
| Consular Army / double legion | armia konsularna / „podwójny legion” | [z GBJC] („armii konsularnej”) / [nowe 26.10 – propozycja] |
| Maniple / manipular legion / manipular tactics / manipular flexibility | manipuł / legion manipularny / taktyka manipularna / manipularna elastyczność | [z GBJC] |
| quincunx (checkerboard) | szachownica (quincunx) | [nowe 26.10 – propozycja] 2.4, 6.6 |
| legionary / legionary infantry | legionista / piechota legionowa | [z GBJC]; „legionary infantry” w tekście historycznym – piechota legionowa (bez EN) |
| Roman stack / Stacked Romans | stos rzymski / Rzymianie w stosie | [nowe 26.10 – propozycja] |
| skill levels: Crack/Elite; Veteran; Standard; Recruits | poziomy wyszkolenia: doborowy/elitarny (Crack/Elite); weterani (Veteran); standardowy (Standard); rekruci (Recruits) | [nowe 26.10 – propozycja] 2.23; „weterani”, „rekruci” jak klasy GBJC (VET, REC) |
| colored border / color bands / border color | kolorowe obramowanie / kolorowe paski / kolor obramowania | [z GBJC] („różnokolorowe obramowania”) |
| XIV (Yellow) Legion; Same Color (I Legion and I Ala) | legion XIV (żółty); ten sam kolor (legion I i ala I) | kolory legionów bez EN (0.1) |
| Carthaginian Command | dowodzenie kartagińskie | [nowe 26.10 – propozycja] 4.6 |
| Roman Command | dowodzenie rzymskie | [nowe 26.10 – propozycja] 4.5; GBJC „Rzymski system dowodzenia” to inny tekst EN |
| Left Wing (Carthaginian Left Wing cavalry) | lewe skrzydło (jazda kartagińskiego lewego skrzydła) | [z GBJC] (GBJCSB „Jazda lewego skrzydła (Left Wing Cavalry)”); zob. 7 (Flank/Wing) |

### 2.4 Słonie, artyleria, rydwany

| EN | PL | Uwagi / źródło |
|---|---|---|
| War Elephants / war elephants | słonie bojowe | [z GBOA] (11.1) |
| African Elephant / Indian Elephant; “Forest” elephants; big Indian tuskers | słoń afrykański / słoń indyjski; słonie „leśne”; wielkie słonie indyjskie | [z GBJC+GBOA] / [nowe 26.10 – propozycja] (tekst historyczny) |
| Elephant Screen(s) | osłona (osłony) słoni | [z GBJC+GBOA] 9.12 |
| Tower Riders / towers | wojownicy w wieżach / wieże | [z GBOA] 9.13 |
| mahout / “the wedge” | kornak / „klin” | [z GBJC+GBOA] 9.14 |
| Leader Elephant(s) | słoń dowódcy (słonie dowódców) | [z GBOA] (GBOASB „słoni dowódców (Leader Elephants)”); żeton słonia z dowódcą (Hannibal) |
| Elephant Leader(s) | dowódca słoni (dowódcy słoni) | [nowe 26.10 – propozycja] 4.9; specjalny żeton dowódcy („Elephant -1”); nie mylić ze słoniem dowódcy (7) |
| Elephant Pass-Thru / Pass-Thru TQ Check | przepuszczenie słoni / test jakości wojsk po przepuszczeniu | [z GBJC] 9.11 |
| Elephant Rampage / Rampage | szał słoni / szał | [z GBJC] 9.14 (0.5) |
| Scorpio(s) / Scorpion (podpis ilustracji 2.25) | skorpion(y) | [z GBJC+GBOA] |
| Bolt-firing (B) engines with built-in crews | machiny miotające bełty (B) z własną obsługą | [z GBOA] („miotające bełty oksybelesy”) |
| Fire mode / Move mode | tryb ostrzału / tryb ruchu | [z GBJC+GBOA] 9.82 |
| Active Fire / Reaction Fire (skorpiony) | ostrzał aktywny / ostrzał reakcyjny | [z GBJC+GBOA] 9.85–9.86 |
| Gallic Chariot (CH); CH+LI; mount / dismount; mounted (LI) | rydwan galijski (CH); CH+LI; wsiąść na rydwan / zsiąść z rydwanu; (LI) na rydwanie | [z GBJC] (zasady rydwanów brytyjskich: „wsiadanie… na rydwan (CH) i zsiadanie z niego”) |
| Camel (podpis 2.25) | jeźdźcy na wielbłądach | [nowe 26.10 – propozycja] |
| Chariot (podpis 2.25, „Seleucid CH”) | rydwan | [z GBJC+GBOA] |
| jousting chariots / flaming pigs (tekst historyczny) | rydwany taranujące / płonące świnie | [nowe 26.10 – propozycja] |

### 2.5 Dowódcy

| EN | PL | Uwagi / źródło |
|---|---|---|
| Leader | dowódca | [z GBJC+GBOA] |
| Overall Commander (OC) | wódz naczelny (OC) | [z GBJC+GBOA] |
| Subordinate Commander (SC) | dowódca podległy (SC) | [z GBJC+GBOA]; SC ≠ dowódca odcinka (Section Commander, GBJC) |
| Elite Commander | elitarny wódz | [z GBJC+GBOA] |
| Proconsul(s) | prokonsul (prokonsulowie) | [z GBJC] (GBJCSB „prokonsul” w tekście historycznym) |
| Tribune(s) | trybun (trybuni) | [z GBJC] |
| Praefect(s); Prefects (11.1) | prefekt (prefekci) | [z GBJC] |
| Praefect Sociorum / Praefects Sociorum | prefekt sprzymierzeńców / prefekci sprzymierzeńców | [nowe 26.10 – propozycja]; dowodzi piechotą ali |
| Praefect Equitum / Praefects Equitum / Praefectus Equitum | prefekt jazdy / prefekci jazdy / prefekt jazdy (praefectus equitum) | [z GBJC] (żetony „Cav Prf” – „prefekt jazdy”) |
| Tribunes/Praefects; Tribune/Praefect counter | trybuni/prefekci; żeton trybuna/prefekta | [z GBJC] |
| Replacement leader | dowódca zastępczy | [z GBJC+GBOA] 4.74 |
| Elephant Leader | dowódca słoni | 2.4 |
| named leaders | imiennie wymienieni dowódcy | [z GBJC] 11.1 |
| consul / king / general (2.4 „generals, consuls, tribunes and kings”) | konsul / król / wódz | [z GBJC] (2.4: „wodzowie, konsulowie, legaci, trybuni i królowie”) |
| seconds-in-command / subordinates and aides | zastępcy / podwładni i adiutanci | [z GBJC] („podwładnych i adiutantów”) |

### 2.6 Współczynniki i opisy żetonów (ilustracje 2.25 i 4.1)

| EN | PL | Uwagi / źródło |
|---|---|---|
| Examples of Combat Units | Przykładowe oddziały bojowe | [z GBJC+GBOA] |
| Double-sized Infantry (Phalanx) | piechota na podwójnych żetonach (falanga) | [nowe 26.10 – propozycja]; por. „dwuheksowy żeton” [z GBOA] |
| Unit Name/ID | nazwa/oznaczenie oddziału | [z GBJC] („nazwa oddziału”, „ID – oznaczenie identyfikacyjne”) |
| Unit Type / Unit Class | typ oddziału / klasa oddziału | [z GBJC+GBOA] |
| Size / Troop Quality (TQ) / Movement Allowance / Extended Movement Allowance | liczebność / jakość wojsk (TQ) / zdolność ruchu / rozszerzona zdolność ruchu | [z GBJC+GBOA] |
| Type of Missile / Range / Archer Screen | rodzaj pocisku / zasięg / osłona łuczników | [z GBJC+GBOA] |
| Infantry / Cavalry / Scorpion / Elephant / Camel / Archer / Chariot / Leader / Elephant Leader | piechota / jazda / skorpion / słonie / jeźdźcy na wielbłądach / łucznicy / rydwan / dowódca / dowódca słoni | podpisy 2.25 |
| Sample Leader Counter | przykładowy żeton dowódcy | [nowe 26.10 – propozycja]; por. Aleksander „przykładowy dowódca macedoński” (inny tekst EN) |
| Name / Elite Initiative Indicator / Command Range / Strategy Rating / Charisma / Initiative / Line Command Rating | imię / oznaczenie inicjatywy elitarnej / zasięg dowodzenia / współczynnik strategiczny / charyzma / inicjatywa / współczynnik rozkazów liniowych | [z GBJC+GBOA] |
| triangle symbol (▲) | symbol trójkąta (▲) | [z GBJC] |
| boxed number | liczba w ramce | [z GBJC] |

### 2.7 Oddziały wymieniane w przykładach i na żetonach (napisy żetonów bez zmian)

| EN | PL | Uwagi / źródło |
|---|---|---|
| Numidian Light Cavalry unit #1; Numidian LC | oddział lekkiej jazdy numidyjskiej nr 1; lekka jazda numidyjska (LC) | [z GBJC] („lekkiej jazdy numidyjskiej”) |
| Balearic Slinger(s) | procarze balearscy | [z GBJC] |
| Crete Archer A | łucznicy kreteńscy A | [z GBJC] („łucznicy kreteńscy”) |
| Celtic Infantry; Celtic Medium Infantry; Celts MI C; Celt C | piechota celtycka; średnia piechota celtycka; Celtowie (MI) C; Celtowie C | [nowe 26.10 – propozycja]; litery oznaczeń bez zmian |
| Carthaginian PH / HC / Heavy Infantry | kartagińska falanga (PH) / ciężka jazda (HC) / ciężka piechota | [nowe 26.10 – propozycja] |
| African Phalanx | falanga afrykańska | [nowe 26.10 – propozycja] |
| Macedonian Phalanx / Macedon LC D | falanga macedońska / lekka jazda macedońska (LC) D | [z GBOA] |
| Mercenary Hoplite | najemni hoplici | [z GBOA] |
| Thrace Peltast B, C / Thrace LI A, D, E | peltaści traccy B, C / lekka piechota tracka (LI) A, D, E | [z GBOA] („peltastów trackich”) |
| Aetolian LC T | lekka jazda etolska (LC) T | [nowe 26.10 – propozycja] |
| Allied Heavy Cavalry | ciężka jazda sprzymierzeńców | [nowe 26.10 – propozycja] 8.45; „Allied” = jazda ali |
| Roman Cavalry U; Roman CO – U, V; Cohort V | jazda rzymska U; rzymskie kohorty (CO) U, V; kohorta V | [z GBJC] |
| Seleucid (żeton CAT HC, CH) | Seleukidzi (seleukidzki) | [z GBOA] |
| Africa 2, Thrace, Nmdia, Seleucid, Scorpio, Africa, Camel, Crete, Hannibal, Elephant -1 | napisy żetonów – bez zmian w opisie ilustracji, z polskim objaśnieniem | INSTRUKCJA_NOWE (ilustracje) |

## 3. Fazy, etapy, sekwencja gry, tabele i elementy gry

### 3.1 Sekwencja gry (3.0) – litery faz według SPQR (A–E), nie GBJC (A–G)

| SPQR (EN) | PL | Odpowiednik w GBJC (Aleksander) |
|---|---|---|
| A. Leader Activation Phase | A. Faza aktywacji dowódców | GBJC B. (Aleksander A.) – to samo brzmienie |
| B. Orders Phase | B. Faza rozkazów | GBJC C. |
| 1. Movement and Missile Fire Segment | 1. Etap ruchu i ostrzału | GBJC C.1 |
| a. For each Individual Order issued… / b. For each Line Command issued… | a. Za każdy wydany rozkaz indywidualny… / b. Za każdy wydany rozkaz liniowy… | GBJC C.1 a–b (brzmienie zdań przejąć, różnice EN oddać) |
| 2. Shock Combat Segment | 2. Etap starcia | GBJC C.2 |
| a. Shock Designation | a. Wyznaczenie do starcia | GBJC |
| b. The Charge (Pre-Shock TQ Check) | b. Szarża (test jakości wojsk przed starciem) | GBJC |
| c. Resolution of Possible Leader Casualties | c. Rozstrzygnięcie ewentualnych strat wśród dowódców | GBJC |
| d. The Clash of Spears and Swords (determine Superiority and Shock column) | d. Szczęk włóczni i mieczy (ustalenie przewagi i kolumny tabeli starcia) | GBJC „d. Szczęk mieczy (The Clash of Swords) (ustalenie przewagi (Superiority) i kolumny tabeli starcia (Shock))”; nazwa – 1 |
| e. Resolve the Shock | e. Rozstrzygnięcie starcia | GBJC |
| f. Check for possible Collapse, Rout, and Cavalry Pursuit | f. Sprawdzenie, czy nastąpiło załamanie, rozbicie i pościg jazdy | GBJC |
| C. Momentum Phase or Return to A | C. Faza impetu albo powrót do A | GBJC „D. Faza impetu albo powrót do B” |
| D. Rout and Reload Phase | D. Faza rozbicia i uzupełniania pocisków | GBJC F. |
| 1. Rout Movement | 1. Ucieczka rozbitych | GBJC F.2 |
| 2. Reload Segment | 2. Etap uzupełniania pocisków | GBJC F.3 |
| 3. Flip and Remove | 3. Odwrócenie i usunięcie | GBJC F.4 („Flip & Remove”) |
| E. Withdrawal Phase | E. Faza wycofania | GBJC G. |
| (D/1), Phase A, Phase B | (D/1), faza A, faza B | odesłania bez zmian |

### 3.2 Procedura starcia (8.4)

| EN | PL | Uwagi / źródło |
|---|---|---|
| PROCEDURE | PROCEDURA | [z GBJC] |
| SHOCK RESOLUTION | ROZSTRZYGNIĘCIE STARCIA | [z GBJC] |
| An Overview of the Shock Combat Resolution Procedure. | Przegląd procedury rozstrzygania starcia. | [z GBJC] |
| 1.–6. (lista kroków) | brzmienie GBJC 8.4: „1. Oddziały atakujące ze znacznikiem Starcie: obowiązkowy test TQ (Shock Must Check TQ) i broniące się przed nimi oddziały wykonują test jakości wojsk przed starciem (Pre-Shock TQ Check, 8.43). 2. Sprawdź, czy wśród dowódców są straty (Leader Casualties, 8.44). 3. Za pomocą tabeli szczęku włóczni i mieczy (Clash of Spears and Swords Chart) ustal, która kolumna tabeli wyników starcia (Shock CRT) zostanie użyta (8.45). 4. Ustal, czy teren, dowódcy i/lub względna siła i możliwości oddziałów mają jakikolwiek wpływ na walkę (8.46). 5. Rozstrzygnij starcie (Shock) za pomocą tabeli wyników starcia (Shock CRT, 8.46). 6. Sprawdź, czy dochodzi do rozbicia (Rout, 8.47).” | [z GBJC]; jedyna różnica EN – nazwa tabeli w pkt 3 |
| Step 1: Determine Superiority: / A. Position Superiority: / B. Weapon System Superiority: | Krok 1: Ustal przewagę (Determine Superiority): / A. Przewaga pozycyjna (Position Superiority): / B. Przewaga systemu uzbrojenia (Weapon System Superiority): | [z GBJC] (w GBJC „Krok 1.” – interpunkcja jak w SPQR) |
| Step 2: Determine Size Ratio Difference: | Krok 2: Ustal różnicę stosunku liczebności (Determine Size Ratio Difference): | [z GBJC] |
| Step 3: Adjust Columns and Resolve: | Krok 3: Przesuń kolumny i rozstrzygnij walkę (Adjust Columns and Resolve): | [z GBJC] |
| Step 4: Apply Results: | Krok 4: Zastosuj wyniki (Apply Results): | [z GBJC] |
| 8.47[1]–[3] (kroki załamania) | 8.47[1]–[3] | numeracja bez zmian |

### 3.3 Tabele, zestawienia, karty (nazwy tabel z PAC i scenariuszy – EN zawsze w nawiasie)

| EN | PL | Punkt SPQR / odpowiednik w serii |
|---|---|---|
| Charts, Tables (and the Die) | tabele, zestawienia (i kość) | 2.3 [z GBJC+GBOA] |
| The Combat Tables | tabele walki | 8.7 [z GBJC] |
| Missile Range and Results Chart (MRRC); Missile Table (2.21) | tabela zasięgu i wyników ostrzału (MRRC) | 8.71 [z GBJC+GBOA]; „Missile Table” to ta sama tabela – polska nazwa pełna, EN jak w oryginale |
| Shock Superiority Chart | tabela przewagi w starciu | 8.72 [z GBJC+GBOA] |
| Clash of Spears and Swords Chart; Clash of Swords chart (8.46) | tabela szczęku włóczni i mieczy | 8.73 [nowe 26.10 – propozycja]; GBJC „tabela szczęku mieczy”, Aleksander „tabela szczęku włóczni” |
| Shock Combat Results Table; Shock CRT; Shock Results Table; Shock Table; Shock Combat CRT | tabela wyników starcia | 8.74 [z GBJC+GBOA]; „Shock Results Table Column adjustment” – przesunięcie kolumny tabeli wyników starcia |
| Cohesion Hit and TQ Check Chart | tabela ubytków spójności i testów jakości wojsk | 8.75 [z GBJC+GBOA]; PDF – 0.4 |
| Movement Cost Chart | tabela kosztów ruchu | 6.27 [z GBJC+GBOA] |
| Stacking Chart / Stacking Charts | tabela łączenia w stosy / tabele łączenia w stosy | 6.69 [z GBJC+GBOA] |
| Line Command Eligibility Chart | tabela uprawnień do rozkazów liniowych | 4.31 [z GBOA] |
| Leader Casualty Table | tabela strat wśród dowódców | 4.73 [z GBJC+GBOA] |
| Rally Table | tabela zebrania | 10.29 [z GBJC] |
| Terrain Effects Chart (Roman Camp, Beneventum) | tabela skutków terenu | 6.24 [z GBJC+GBOA] |
| Elephant Rampage (tabela 9.14): Die Roll / Result | Rzut kością / Wynik | [z GBJC] (GBJC „DR / Wynik”) |
| Compass (na mapie) | róża wiatrów | 9.14 [z GBJC] |
| Game Turn Track | tor tur gry | 2.6 [z GBOA] |
| Rout Point Tracking/Game Turn Card | karta śledzenia punktów rozbicia i tur gry | 2.0 [z GBOA] („karta śledzenia punktów rozbicia (Rout Point Tracking Card)”) |
| player aid cards, PAC I and PAC II | karty pomocy gracza (PAC I i PAC II) | 2.0 [z GBJC] |
| Pursuit boxes (mapa Beneventum) | pola pościgu | 8.6 [nowe 26.10 – propozycja] |

### 3.4 Elementy gry (2.0) i tytuły

| EN | PL | Uwagi / źródło |
|---|---|---|
| The Great Battles of History Series — Volume II | Seria The Great Battles of History — tom II | [z GBJC] („tom IV/VI”) |
| SPQR: Great Battles of the Roman Republic | SPQR: Great Battles of the Roman Republic (tytuł bez zmian); objaśnienie: Wielkie bitwy Republiki rzymskiej | tytuł gry nie jest tłumaczony (jak GBJC); żywej paginy w md nie przepisujemy |
| a Richard Berg / Mark Herman game | gra Richarda Berga i Marka Hermana | [z GBOA] („gra autorstwa Marka Hermana i Richarda H. Berga”) |
| RULE BOOK / Rulebook | ZASADY GRY / zasady gry | [z GBJC+GBOA] |
| 5th Edition | wydanie 5. (5. wydanie) | 0.3 |
| Table of Contents | Spis treści | [z GBJC+GBOA] |
| Six 22” x 34” map sheets, backprinted | 6 × arkusz mapy 22″ × 34″, zadrukowany dwustronnie | [z GBJC] |
| Six counters sheets (1/2”, 280 counters per full sheet) | 6 × arkusz żetonów (½″, 280 żetonów na pełnym arkuszu) | [z GBJC] (wzór listy) |
| Scenario Book I - The Rise of Rome | Księga scenariuszy I – Narodziny potęgi Rzymu | [nowe 26.10 – propozycja] |
| Scenario Book II - The 2nd Punic War | Księga scenariuszy II – II wojna punicka | [nowe 26.10 – propozycja] |
| Scenario Book III - Macedonia, Syria, and Africa | Księga scenariuszy III – Macedonia, Syria i Afryka | [nowe 26.10 – propozycja] |
| Four 11” x 17” player aid cards, PAC I and PAC II, two-sided, two identical copies of each | 4 × karta pomocy gracza 11″ × 17″ (PAC I i PAC II), dwustronna, po dwa identyczne egzemplarze każdej | [z GBJC] |
| One ten-sided die | 1 × kość dziesięciościenna | [z GBJC+GBOA] |
| Plastic counter storage bags | plastikowe woreczki do przechowywania elementów | [z GBJC+GBOA] |
| Learning Scenario | scenariusz szkoleniowy | [nowe 26.10 – propozycja] 1.0 |
| GBoH publications | publikacje GBoH | 1.0 |

## 4. Znaczniki i strony żetonów

| EN (jak w oryginale) | PL | Uwagi / źródło |
|---|---|---|
| SHOCK MUST CHECK TQ / Shock Must Check TQ | Starcie: obowiązkowy test TQ | [z GBJC+GBOA] |
| SHOCK NO TQ CHECK / SHOCK-NO TQ CHECK | Starcie: bez testu TQ | [z GBJC+GBOA] |
| “#’s” (Cohesion Hits); numeric marker; „3” | znaczniki liczbowe („#’s”, oznaczające ubytki spójności) | [z GBJC] 2.23 |
| ROUTED TQ=1 / ROUTED | Rozbity, TQ=1 / Rozbity | [z GBJC+GBOA] |
| RALLIED (druga strona ROUTED) | Zebrany | [z GBJC+GBOA] 10.28 |
| MISSILE LOW / MISSILE NO / Missile Low/No | Mało pocisków / Brak pocisków / Mało pocisków/Brak pocisków | [z GBJC+GBOA] |
| MOVED | Wykonał ruch | [z GBJC] |
| FIRED | Wykonał ostrzał | [nowe 26.10 – propozycja] 3.0 D.3; analogia do „Wykonał ruch” |
| PURSUIT/FINISHED | Pościg/Zakończony | [z GBJC] |
| TRUMPED / NO MOMENTUM; TRUMPED/NO MOMENTUM markers | Przebity / Bez impetu | [z GBJC+GBOA] |
| PRE-ARRANGED WITHDRAWAL / NO PW | Wcześniej zaplanowane wycofanie / Bez PW | [z GBJC+GBOA] |
| IN COLUMN | W kolumnie | [z GBJC+GBOA] |
| ENGAGED | Związany walką | [z GBJC+GBOA] |
| ACTIVE FIRE ONCE / ACTIVE FIRE FINISHED | Ostrzał aktywny – raz / Ostrzał aktywny – zakończony | [z GBJC+GBOA] |
| REACTION FIRE ONCE / REACTION FIRE FINISHED | Ostrzał reakcyjny – raz / Ostrzał reakcyjny – zakończony | [z GBJC+GBOA] |
| Activated / Finished (strony żetonu dowódcy); front sides | „aktywowany” / „zakończony”; awersy | [z GBJC+GBOA] |
| Fire mode / Move mode (strony żetonu skorpiona) | tryb ostrzału / tryb ruchu | [z GBJC+GBOA] |
| reverse side (Depleted) | strona odwrotna (oddział uszczuplony) | [z GBJC] |
| Informational Markers / informational markers | znaczniki informacyjne | [z GBJC+GBOA] |
| Shock Check / Shock No Check (8.43 – skróty nazw znaczników) | Starcie: obowiązkowy test / Starcie: bez testu | [z GBJC] 8.43 |
| SHOCK marker / Shock markers (6.66, 8.41) | znacznik starcia / znaczniki starcia | [nowe 26.10 – propozycja]; oba znaczniki Starcie: … łącznie |
| Elephant Leader counter (Elephant -1) | żeton dowódcy słoni | 2.4 |

## 5. Nagłówki rozdziałów i punktów

Nagłówki numerowane – `## …` jak w INSTRUKCJA_NOWE (wersaliki jak w oryginale), polski tytuł + EN w jednym nawiasie (w składzie PDF – K.4). Etykiety wpuszczone w akapit (run-in) – pogrubione, z dwukropkiem lub kropką jak w oryginale. Tytuły identyczne z GBJC/Aleksandrem mają brzmienie wzorca.

### 5.1 Spis treści i nagłówki

| Nr | EN | PL | Źródło |
|---|---|---|---|
| 1.0 | INTRODUCTION | WPROWADZENIE | [z GBJC+GBOA] |
| – | 5th Edition Note: | Uwaga do 5. wydania (5th Edition Note): | [nowe 26.10 – propozycja]; 0.5 |
| – | Note to Players: | Uwaga dla graczy: | [z GBJC] |
| – | For Those Who Have Not Played the System Before: | Dla tych, którzy jeszcze nie grali w tym systemie: | [nowe 26.10 – propozycja] |
| 2.0 | GAME COMPONENTS AND TERMINOLOGY | ELEMENTY GRY I TERMINOLOGIA | [z GBJC+GBOA] + 2.4 |
| 2.1 | THE MAPS | MAPY | [z GBJC+GBOA] |
| 2.2 | THE PLAYING PIECES | ŻETONY | [z GBJC+GBOA] |
| 2.23 | The Legions. | Legiony. | [z GBJC] |
| 2.24 | Legion Units. | Oddziały legionowe. | [nowe 26.10 – propozycja] |
| 2.25 | Examples of Combat Units | Przykładowe oddziały bojowe | [z GBJC+GBOA] |
| 2.3 | CHARTS, TABLES AND THE DIE | TABELE, ZESTAWIENIA I KOŚĆ | [z GBJC+GBOA] |
| 2.4 | TERMINOLOGY | TERMINOLOGIA | [z GBJC+GBOA]; hasła 2.4: „Dowódca aktywny (Active Leader):” itd. – sekcja 1 i 2 |
| 2.5 | GAME SCALE | SKALA GRY | [z GBJC+GBOA] |
| 2.6 | GAME LENGTH | DŁUGOŚĆ GRY | [z GBJC+GBOA] |
| 2.7 | LATIN | ŁACINA | [nowe 26.10 – propozycja] |
| 3.0 | SEQUENCE OF PLAY (spis: The Sequence of Play) | SEKWENCJA GRY | [z GBJC+GBOA] |
| 4.0 | LEADERS | DOWÓDCY | [z GBOA] |
| 4.1 | LEADER COUNTERS | ŻETONY DOWÓDCÓW | [z GBJC+GBOA] |
| 4.2 | LEADER CAPABILITIES: INDIVIDUAL ORDERS | MOŻLIWOŚCI DOWÓDCÓW: ROZKAZY INDYWIDUALNE | [z GBJC+GBOA] |
| 4.3 | LEADER CAPABILITIES: LINE COMMANDS | MOŻLIWOŚCI DOWÓDCÓW: ROZKAZY LINIOWE | [z GBJC+GBOA] |
| 4.32 | Line Composition: | Skład linii (Line Composition): | [z GBJC+GBOA] |
| 4.33 | Line Command Eligibility: | Uprawnienia do rozkazów liniowych (Line Command Eligibility): | [z GBJC+GBOA] |
| 4.33 | Overall Commanders / Subordinate Commanders (podtytuły) | Wodzowie naczelni / Dowódcy podlegli | [z GBOA] |
| 4.33 | Exception #1: / Exception #2: | Wyjątek nr 1: / Wyjątek nr 2: | [nowe 26.10 – propozycja]; jak „PRZYKŁAD NR 1” |
| 4.4 | OVERALL COMMANDERS | WODZOWIE NACZELNI | [z GBOA] |
| 4.5 | ROMAN COMMAND: PROCONSULS, TRIBUNES AND PRAEFECTS | DOWODZENIE RZYMSKIE: PROKONSULOWIE, TRYBUNI I PREFEKCI | [nowe 26.10 – propozycja] |
| 4.6 | CARTHAGINIAN COMMAND | DOWODZENIE KARTAGIŃSKIE | [nowe 26.10 – propozycja] |
| 4.7 | LEADERS & ENEMY COMBAT UNITS | DOWÓDCY A ODDZIAŁY BOJOWE WROGA | [z GBJC+GBOA]; 0.4 |
| 4.8 | LEADER ELEPHANTS | SŁONIE DOWÓDCÓW | [z GBOA] |
| 4.9 | ELEPHANT COMMAND (OPTIONAL) | DOWODZENIE SŁONIAMI (ZASADA OPCJONALNA) | [nowe 26.10 – propozycja] |
| 5.0 | LEADER ACTIVATION AND ORDERS | AKTYWACJA DOWÓDCÓW I ROZKAZY | [z GBJC+GBOA] |
| 5.1 | HOW TO ACTIVATE LEADERS | JAK AKTYWOWAĆ DOWÓDCÓW | [z GBJC+GBOA] |
| 5.2 | THE ORDERS PHASE | FAZA ROZKAZÓW | [z GBJC+GBOA] |
| 5.22 | Individual Orders: | Rozkazy indywidualne (Individual Orders): | [z GBJC] |
| 5.23 | Line Commands: | Rozkazy liniowe (Line Commands): | [z GBJC] |
| 5.3 | MOMENTUM | IMPET | [z GBJC+GBOA] |
| 5.33 | The Die Roll of Doom: | Fatalny rzut (Die Roll of Doom): | [z GBJC+GBOA] |
| 5.4 | THE TRUMP OPTION | OPCJA PRZEBICIA | [z GBJC+GBOA] |
| 5.41 | Active Player Trump Option: | Opcja przebicia gracza aktywnego (Active Player Trump Option): | [z GBJC+GBOA] |
| 5.42 | Inactive Player Trump Options: | Opcje przebicia gracza nieaktywnego (Inactive Player Trump Options): | [z GBJC+GBOA] |
| 5.42 | 1. Trumping the Trump: / 2. Momentum Trump: | 1. Przebicie przebicia (Trumping the Trump): / 2. Przebicie impetu (Momentum Trump): | [z GBJC+GBOA] |
| 5.5 | ELITE COMMANDER INITIATIVE | INICJATYWA ELITARNEGO WODZA | [z GBOA] |
| 6.0 | MOVEMENT | RUCH | [z GBJC+GBOA] |
| 6.1 | MOVEMENT ALLOWANCES | ZDOLNOŚĆ RUCHU | [z GBJC+GBOA] |
| 6.2 | TERRAIN | TEREN | [z GBOA] |
| 6.27 | The Movement Cost Chart: | Tabela kosztów ruchu (Movement Cost Chart): | [z GBJC+GBOA] |
| 6.3 | MOVEMENT PROCEDURES | PROCEDURY RUCHU | [z GBJC]; 0.5 |
| 6.4 | PHALANX UNITS | ODDZIAŁY FALANGI | [nowe 26.10 – propozycja] |
| 6.43 | The Front-to-Flank Maneuver: | Manewr front–skrzydło (Front-to-Flank Maneuver): | [z GBOA] |
| 6.44 | The Wheeling Maneuver: | Manewr zwrotu (Wheeling Maneuver): | [z GBOA] |
| 6.45 | The Reverse Face Maneuver: | Manewr odwrócenia frontu (Reverse Face Maneuver): | [z GBOA] |
| 6.5 | ORDERLY WITHDRAWAL | UPORZĄDKOWANY ODWRÓT | [z GBJC+GBOA] |
| 6.57 | Cavalry Line Withdrawal: | Wycofanie linii jazdy (Cavalry Line Withdrawal): | [z GBJC+GBOA] |
| 6.6 | STACKING | ŁĄCZENIE W STOSY | [z GBJC+GBOA] |
| 6.61 | The Basic, non-Roman Stacking Rule: | Podstawowa, nierzymska zasada łączenia w stosy (The Basic, non-Roman Stacking Rule): | [nowe 26.10 – propozycja] |
| 6.63 | Basic: / Different Color: / Different Class: / Roman: | Podstawowy (Basic): / Inny kolor (Different Color): / Inna klasa (Different Class): / Rzymski (Roman): | [z GBJC] / [nowe 26.10 – propozycja] |
| 6.69 | The Stacking Chart: | Tabela łączenia w stosy (Stacking Chart): | [z GBJC+GBOA] |
| 6.7 | COLUMN MOVEMENT | RUCH W KOLUMNIE | [z GBJC+GBOA] |
| 6.8 | PRE-ARRANGED WITHDRAWAL | WCZEŚNIEJ ZAPLANOWANE WYCOFANIE | [z GBJC+GBOA] |
| 7.0 | FACING AND ZOCs | USTAWIENIE FRONTU I STREFY KONTROLI | [z GBJC+GBOA] |
| 7.1 | FACING | USTAWIENIE FRONTU | [z GBJC+GBOA] |
| 7.15 | Reaction Facing Change: | Reakcyjna zmiana frontu (Reaction Facing Change): | [z GBJC+GBOA] |
| 7.2 | ZONES OF CONTROL (ZOC) | STREFY KONTROLI (ZOC) | [z GBJC+GBOA] |
| 7.3 | SHOCK REQUIREMENTS | WYMOGI STARCIA | [z GBOA]; 0.5 |
| 8.0 | COMBAT | WALKA | [z GBJC] |
| 8.1 | MISSILE FIRE | OSTRZAŁ | [z GBJC+GBOA] |
| 8.15 | Missile Fire Resolution: | Rozstrzyganie ostrzału (Missile Fire Resolution): | [z GBJC+GBOA] |
| 8.16 | Extended Range: | Zasięg rozszerzony (Extended Range): | [z GBOA] |
| 8.17 | Missile Supply: | Zapas pocisków (Missile Supply): | [z GBJC+GBOA] |
| 8.19 | Leader Casualties: | Straty wśród dowódców (Leader Casualties): | [z GBJC+GBOA] |
| 8.2 | REACTION FIRE | OSTRZAŁ REAKCYJNY | [z GBJC+GBOA] |
| 8.21 | Entry Reaction: | Ostrzał reakcyjny przy wejściu (Entry Reaction): | [z GBJC] |
| 8.22 | Retire Reaction: | Ostrzał reakcyjny przy wyjściu (Retire Reaction): | [z GBJC] |
| 8.23 | Return Fire: | Ostrzał odwetowy (Return Fire): | [z GBJC+GBOA] |
| 8.3 | HARASSMENT & DISPERSAL | NĘKANIE I ROZPROSZENIE | [z GBJC+GBOA] |
| 8.4 | SHOCK COMBAT | STARCIE | [z GBJC+GBOA]; PROCEDURE, SHOCK RESOLUTION – 3.2 |
| 8.41 | Shock Designation: | Wyznaczenie do starcia (Shock Designation): | [z GBJC+GBOA] |
| 8.42 | The Basic Pre-Shock Procedure: | Podstawowa procedura przed starciem (Basic Pre-Shock Procedure): | [z GBJC+GBOA] |
| 8.43 | The Charge: | Szarża (The Charge): | [z GBJC] |
| 8.44 | Shock and Leaders: | Starcie a dowódcy (Shock and Leaders): | [z GBJC] |
| 8.45 | The Clash of Spears and Swords: | Szczęk włóczni i mieczy (The Clash of Spears and Swords): | [nowe 26.10 – propozycja] |
| 8.46 | The Hand-to-Hand Struggle: | Zmagania wręcz (The Hand-to-Hand Struggle): | [z GBJC+GBOA]; kroki – 3.2 |
| 8.47 | The Collapse: | Załamanie (The Collapse): | [z GBJC+GBOA] |
| – | Extended Shock Example—Bagradas Plains | ROZSZERZONY PRZYKŁAD STARCIA (Extended Shock Example) – [nad Bagradasem] | [z GBJC] („ROZSZERZONY PRZYKŁAD STARCIA (Extended Shock Example) – [BIBRAKTE]”); etykiety akapitów: Shock Designation:, Pre-Shock Procedure:, The Charge:, Leader Casualties:, The Hand-to-Hand Struggle:, The Collapse: – jak w 8.41–8.47 |
| 8.5 | ADVANCE AFTER COMBAT | POSUNIĘCIE PO WALCE | [z GBJC+GBOA] |
| 8.6 | CAVALRY PURSUIT | POŚCIG JAZDY | [z GBJC+GBOA] |
| 8.62 | Pursue: / Break-Off: | Pościg (Pursue): / Oderwanie się (Break-Off): | [z GBJC] |
| 8.64 | Off-Map Regroup. | Przegrupowanie poza mapą (Off-Map Regroup). | [z GBJC] |
| 8.66 | Cavalry Pursuit Option: | Opcja pościgu jazdy (Cavalry Pursuit Option): | [nowe 26.10 – propozycja] |
| 8.7 | THE COMBAT TABLES | TABELE WALKI | [z GBJC] |
| 8.71–8.75 | (nazwy tabel z dwukropkiem) | jak 3.3 | |
| 9.0 | SPECIAL COMBAT UNITS | SPECJALNE ODDZIAŁY BOJOWE | [nowe 26.10 – propozycja]; GBJC „Oddziały i szyki specjalne”, Aleksander „Oddziały specjalne” – inny tekst EN |
| 9.1 | WAR ELEPHANTS | SŁONIE BOJOWE | [z GBOA] |
| 9.11 | Elephant Pass-Thru: | Przepuszczenie słoni (Elephant Pass-Thru): | [z GBJC] |
| 9.12 | Elephant Screens: | Osłony słoni (Elephant Screens): | [z GBJC+GBOA] |
| 9.13 | Tower Riders: | Wojownicy w wieżach (Tower Riders): | [z GBOA] |
| 9.14 | Elephant Rampage: | Szał słoni (Elephant Rampage): | [z GBJC]; 0.5 |
| 9.15 | Cavalry vs. Elephants: | Jazda przeciwko słoniom (Cavalry vs. Elephants): | [z GBJC+GBOA] |
| 9.16 | Elephants vs. Cavalry: | Słonie przeciwko jeździe (Elephants vs. Cavalry): | [z GBOA] |
| 9.19 | Indians vs. Africans: | Słonie indyjskie przeciwko afrykańskim (Indians vs. Africans): | [nowe 26.10 – propozycja] |
| 9.2 | SKIRMISHERS, VELITES, AND LIGHT INFANTRY | HARCOWNICY, WELICI I LEKKA PIECHOTA | [z GBJC] („Harcownicy i lekka piechota”) + welici |
| 9.21 / 9.22 / 9.23 | Orderly Withdrawal: / Missile Fire: / Shock Combat: | Uporządkowany odwrót (Orderly Withdrawal): / Ostrzał (Missile Fire): / Starcie (Shock Combat): | [z GBJC+GBOA] |
| 9.3 | LIGHT CAVALRY | LEKKA JAZDA | [z GBJC+GBOA] |
| 9.4 | PHALANX DEFENSE | OBRONA FALANGI | [z GBJC+GBOA] |
| 9.5 | DOUBLE DEPTH PHALANXES | FALANGI O PODWÓJNEJ GŁĘBOKOŚCI | [z GBOA] |
| 9.52 / 9.53 | Movement Restrictions: / Combat Effects: | Ograniczenia ruchu: / Skutki w walce: | [z GBOA] (11.72–11.73 – to samo EN) |
| 9.6 | THE ROMAN MANIPULAR LEGION | RZYMSKI LEGION MANIPULARNY | [z GBJC] („legion manipularny”) |
| 9.66 | Manipular Line Extension: | Manipularne wydłużenie linii (Manipular Line Extension): | [nowe 26.10 – propozycja] |
| 9.66 | Original Deployment / After Manipular Line Extension (podpisy) | Rozstawienie wyjściowe / Po manipularnym wydłużeniu linii | [nowe 26.10 – propozycja] |
| 9.7 | ROMAN TRIARII TACTICAL DOCTRINE | DOKTRYNA TAKTYCZNA RZYMSKICH TRIARII | [nowe 26.10 – propozycja]; triarii – 2.2 |
| 9.8 | ARTILLERY | ARTYLERIA | [z GBJC+GBOA] |
| 9.85 / 9.86 | Active Fire: / Reaction Fire: | Ostrzał aktywny (Active Fire): / Ostrzał reakcyjny (Reaction Fire): | [z GBJC+GBOA] |
| 9.9 | THE BARBARIANS | BARBARZYŃCY | [nowe 26.10 – propozycja] |
| 9.91 | Movement Effects | Skutki dla ruchu | [z GBOA] („Skutki dla ruchu i ostrzału”); w oryginale brak 9.92 – nie dodawać numeru, zgłosić jako osobliwość oryginału |
| 9.93 | Rout and Recovery | Rozbicie i odzyskiwanie spójności | [z GBJC+GBOA] |
| 9.94 | Barbarian Ferocity | Barbarzyńska zaciekłość | [z GBJC] |
| 9.95 | Barbarian Impetuosity | Barbarzyńska porywczość | [nowe 26.10 – propozycja]; GBJC „Galijska porywczość” |
| 9.96 | Gallic Chariots | Rydwany galijskie | [nowe 26.10 – propozycja] |
| 10.0 | THE EFFECTS OF COMBAT | SKUTKI WALKI | [z GBJC+GBOA] |
| 10.1 | COHESION | SPÓJNOŚĆ | [z GBJC+GBOA] |
| 10.11 | TQ Checks: | Testy jakości wojsk (TQ Checks): | [z GBJC+GBOA] |
| 10.12 | Cohesion Markers: | Znaczniki spójności (Cohesion Markers): | [z GBJC+GBOA] |
| 10.16 | Recovery: | Odzyskiwanie spójności (Recovery): | [z GBOA]; 0.5 |
| 10.2 | UNIT ROUT AND RALLY | ROZBICIE I ZEBRANIE ODDZIAŁÓW | [z GBOA] |
| 10.28 | Rally: | Zebranie (Rally): | [z GBOA] |
| 10.29 | The Rally Table: | Tabela zebrania (Rally Table): | [z GBJC] |
| 10.3 | DEPLETION | USZCZUPLENIE | [z GBJC] |
| 10.4 | ENGAGED (OPTIONAL) | ZWIĄZANIE WALKĄ (ZASADA OPCJONALNA) | [z GBJC+GBOA] |
| 11.0 | ARMY WITHDRAWAL AND VICTORY | WYCOFANIE ARMII I ZWYCIĘSTWO | [z GBJC+GBOA] |
| 11.1 | ROUT POINTS | PUNKTY ROZBICIA | [z GBJC] |
| 11.2 | ARMY WITHDRAWAL | WYCOFANIE ARMII | [z GBJC] |
| – | Livy–The Disaster at Cannae | LIWIUSZ – KLĘSKA POD KANNAMI | [nowe 26.10 – propozycja] |
| – | Rules Index | INDEKS ZASAD | [nowe 26.10 – propozycja]; GBJC/Aleksander „Indeks” (EN „Index”) |

### 5.2 Indeks zasad (s. 42–43)

- Kolejność haseł jak w oryginale (praktyka indeksu PDF GBJC – bez przestawiania alfabetycznego po polsku); numery bez zmian; hasła i podhasła według glosariusza, w md z EN.
- Hasła główne: Cohesion Hits – Ubytki spójności; Depletion – Uszczuplenie; Facing – Ustawienie frontu; Leaders – Dowódcy; Missile Combat – Walka na dystans; Momentum – Impet; Movement – Ruch; Orderly Withdrawal – Uporządkowany odwrót; Orders – Rozkazy; Rout and Rally – Rozbicie i zebranie; Shock Combat – Starcie; Stacking – Łączenie w stosy; Trump – Przebicie; Zones of Control (ZOCs) – Strefy kontroli (ZOC).
- Podhasła z odesłaniem „[See …]” – „[zob. …]”; „5th bullet” – „piąty punktor”; „Wounded” – ranny, „Killed” – zabity, „Casualty” – straty; „Cause Elimination of routed unit” – eliminacja rozbitego oddziału; „Cause Rout” – powodujące rozbicie; „Condition of Collapse Die roll” – warunek rzutu w kroku załamania; „Who Must/May Shock” – kto musi/może prowadzić starcie; „Initial two-hex Rout” – początkowa ucieczka o 2 heksy. Pozostałe podhasła z „Restrictions” – ograniczenia (Column Restrictions – ograniczenia oddziałów w kolumnie; MLE Restrictions; Rout Restrictions; Withdrawal Restrictions; Triarii Restrictions – ograniczenia triarii); „Movement Into / Out of” – wejście do / wyjście ze (strefy kontroli); „Changing Top/Bottom unit” – zmiana oddziału wierzchniego/spodniego; „Firing During Movement” – ostrzał podczas ruchu; „When Missile Units Fire” – kiedy oddziały strzelające prowadzą ostrzał; „Automatic Depletion from Rally” – automatyczne uszczuplenie po zebraniu; „Size Adjustments” – modyfikacje za liczebność; „Stacking & Combat” – łączenie w stosy a walka; „Elephant vs. Elephant” – słonie przeciwko słoniom; „Elephants take two Hits from” – słonie otrzymują 2 ubytki od; „Phalanxes (Two-Hex units)” – falangi (oddziały dwuheksowe); „In-Column Units” – oddziały w kolumnie.

## 6. Nazwy własne

Formy polskie utrwalone w piśmiennictwie (PWN) i zgodne z przekładami serii; w tekście bez nawiasu EN (0.1), z wyjątkiem nazw bitew użytych jako nazwy scenariuszy przy pierwszym użyciu w punkcie: „pod Kannami (Cannae)”, oraz etykiet przykładów w nawiasie kwadratowym: „[Cannae]” → „[Kanny]”.

### 6.1 Bitwy, scenariusze, miejsca

| EN | PL | Uwagi / źródło |
|---|---|---|
| Cannae; at Cannae; the town of Cannae | Kanny; pod Kannami; miasto Kanny | [nowe 26.10 – propozycja] (PWN „bitwa pod Kannami”) |
| Zama | Zama; pod Zamą | [nowe 26.10 – propozycja] |
| Beneventum; Beneventum map | Beneventum (nieodm.); pod Beneventum; mapa Beneventum | [nowe 26.10 – propozycja]; miasto współcz. Benewent – nie używać w nazwie bitwy |
| Cynoscephalae | Kynoskefalaj (nieodm.); pod Kynoskefalaj | [nowe 26.10 – propozycja] (PWN) |
| Bagradas Plains; The Bagradas Plains (scenariusz) | nad Bagradasem; „Równina nad Bagradasem” | [nowe 26.10 – propozycja]; odmiana jak „nad Hydaspesem” [z GBOA] |
| Heraclea | Heraklea; pod Herakleą | [z GBOA] (GBOASB „słoni Pyrrusa pod Herakleą”) |
| Sentinum | Sentinum; pod Sentinum | [nowe 26.10 – propozycja] |
| Telamon | Telamon; pod Telamonem | [nowe 26.10 – propozycja] |
| Raphia | Rafia; pod Rafią | [z GBOA] |
| Hydaspes | Hydaspes; nad Hydaspesem | [z GBOA] |
| Allia | Allia; nad Allią | [nowe 26.10 – propozycja] (Liwiusz) |
| Canusium | Kanuzjum | [nowe 26.10 – propozycja] |
| the City (Liwiusz) | Miasto | = Rzym; wielką literą jak w oryginale, bez dopisku |
| Aufidus River | rzeka Aufidus | [nowe 26.10 – propozycja] |
| Roman Camp (mapa Beneventum) / Roman Road / dirt road (mapa Zamy) | obóz rzymski / droga rzymska / droga gruntowa | [nowe 26.10 – propozycja] |
| Rome / Republic of Rome, Roman Republic / Roman Empire | Rzym / Republika rzymska / Cesarstwo (rzymskie) | [z GBJC] („Republiki rzymskiej”, „wczesnego Cesarstwa”); „republic” (ustrój) – republika |
| Carthage | Kartagina | [z GBOA] |
| Macedonia / Syria / Africa / North African / southern Africa | Macedonia / Syria / Afryka / północnoafrykański / Afryka Południowa (południe Afryki) | ogólne |
| Etruria / northern Italy / Italy | Etruria / północna Italia / Italia | [nowe 26.10 – propozycja] |
| the Mediterranean / Balearic Islands / Crete | Morze Śródziemne / Baleary / Kreta | [z GBJC] („na Balearach”, „z Krety”) |

### 6.2 Osoby

| EN | PL | Uwagi / źródło |
|---|---|---|
| Hannibal | Hannibal | [z GBOA] |
| Scipio Africanus; Scipio (Africanus); Publius Cornelius Scipio | Scypion Afrykański; Scypion; Publiusz Korneliusz Scypion | [z GBJC] |
| Marius / Caesar | Mariusz / Cezar | [z GBJC] |
| Polybius | Polibiusz | [z GBJC+GBOA] |
| Maharbal | Maharbal | [nowe 26.10 – propozycja] |
| Masanissa (pisownia oryginału) | Masynissa | [nowe 26.10 – propozycja]; polska forma Masynissa (łac. Masinissa) – wariant pisowni, nie błąd do zgłaszania |
| Hasdrubal / Hasdrubals | Hazdrubal / Hazdrubalowie | [z GBOA] (Tyrant) |
| Hanno / Hannos | Hannon / Hannonowie | [z GBOA] |
| Hamilcar / Bomilcar | Hamilkar / Bomilkar | [z GBOA] |
| “Car Boys” (żart o Hamilkarze i Bomilkarze) | „chłopcy od -kara” | [nowe 26.10 – propozycja]; gra słów na końcówce imion – zachować żart |
| Bostar | Bostar | [nowe 26.10 – propozycja] |
| Regulus | Regulus | [z GBOA] („Regulusa”) |
| Servilius | Serwiliusz | [nowe 26.10 – propozycja] |
| Paullus; L. Aemilius | Paulus; L. Emiliusz | [nowe 26.10 – propozycja]; Lucjusz Emiliusz Paulus (PWN) |
| Laelius | Leliusz | [nowe 26.10 – propozycja] (Gajusz Leliusz) |
| P. Sempronius Tuditanus | P. Semproniusz Tuditanus | [nowe 26.10 – propozycja] |
| Pyrrhus / Pyrrhic era | Pyrrus / epoka Pyrrusa | [z GBOA] |
| Alexander / Alexander’s Companions | Aleksander / hetajrowie Aleksandra | [z GBOA] |
| Ptolemy / Seleucus / Antiochus / Porus | Ptolemeusz / Seleukos / Antioch / Poros | [z GBOA] |
| the Diadochi (Alexander’s successors) | diadochowie (następcy Aleksandra) | [z GBOA] |
| Livy | Liwiusz | [nowe 26.10 – propozycja] |
| Peter Connolly (PC) / Connolly’s argument | Peter Connolly (PC) / argument Connolly’ego | [z GBJC] („Petera Connolly’ego”) |
| Delbruckian experimentation (pisownia oryginału) | eksperyment w duchu Delbrücka | [z GBJC] („Delbrück”) |
| Occam’s Razor | brzytwa Ockhama | ogólne |
| Richard Berg / Mark Herman | Richard Berg / Mark Herman (Richarda Berga, Marka Hermana) | [z GBOA] |
| Rev. Canon Roberts (tłumacz Liwiusza na angielski) | ks. kanonik Roberts | [nowe 26.10 – propozycja] |

### 6.3 Ludy i przymiotniki

| EN | PL | Uwagi / źródło |
|---|---|---|
| Romans / Roman | Rzymianie / rzymski | ogólne |
| Carthaginians / Carthaginian | Kartagińczycy / kartagiński | [z GBOA] |
| Numidians / Numidian | Numidowie / numidyjski | [z GBJC] |
| Celts / Celtic / Celtic tribes | Celtowie / celtycki / plemiona celtyckie | [z GBJC+GBOA] |
| Gauls / Gallic | Galowie / galijski | [z GBJC] |
| Macedonians / Macedonian (system, era) | Macedończycy / macedoński (system, epoka) | [z GBOA] |
| Greeks / Greek / Hoplite Era | Grecy / grecki / epoka hoplitów | [z GBOA] |
| Samnites / Campanians / Umbrians | Samnici / Kampanowie / Umbrowie | [z GBOA] / [z GBOA] / [nowe 26.10 – propozycja] |
| Latin ally / non-citizen allies of Rome | sprzymierzeniec latyński / sprzymierzeńcy Rzymu nieposiadający obywatelstwa | [nowe 26.10 – propozycja] |
| Thracian (Thrace) / Aetolian / Seleucid / Balearic / Cretan | tracki / etolski / seleukidzki / balearski / kreteński | [z GBOA] / [nowe] / [z GBOA] / [z GBJC] / [z GBJC] |
| Indians / Africans (słonie, 9.19) | słonie indyjskie / słonie afrykańskie | 2.4 |
| Alexandrian era / post-Alexandrian | epoka Aleksandra / poaleksandryjski | [nowe 26.10 – propozycja] |
| Punic-era / 2nd Punic War | epoki wojen punickich / II wojna punicka | [z GBJC] („z epoki wojen punickich”) |

### 6.4 Łacina, dzieła, cytaty

| EN / łac. | PL | Uwagi / źródło |
|---|---|---|
| SPQR — Senatus Populusque Romanus, the Senate and the Roman People | SPQR – Senatus Populusque Romanus, Senat i Lud Rzymski | łacina bez zmian |
| scutum / pilum (lm. pila) / gladius / hasta / sarissa | scutum / pilum (lm. pila) / gladius / hasta / sarissa | [z GBJC+GBOA]; kursywa tylko gdzie w oryginale; „the Roman javelin was a pilum” – jak GBJC: „Rzymskim oszczepem było pilum” |
| “Spanish Sword” | „miecz hiszpański” | [nowe 26.10 – propozycja] |
| Caesar’s Commentaries | „Commentarii” Cezara | [nowe 26.10 – propozycja] |
| fifth declension / “bluu” it (żart oryginału) | piąta deklinacja / żartobliwie, z celowym błędem (np. „pokićkaliśmy”) | [nowe 26.10 – propozycja]; oddać żart, nie poprawiać |
| Great Battles of the Great Commanders (książka) | „Great Battles of the Great Commanders” | tytuł bez przekładu, w cudzysłowie |
| Spartacus (film) | film „Spartakus” | ogólne |
| The History of Rome, Book 22 (Liwiusz) | „Dzieje Rzymu” (The History of Rome), księga 22 | cytat przekładać z angielskiego wiernie (INSTRUKCJA_NOWE), bez szukania polskiego wydania |
| Trans. Rev. Canon Roberts; URL | przeł. na ang. ks. kanonik Roberts; adres URL bez zmian | |

## 7. Pułapki znaczeniowe

| Para EN | Rdzenie PL | Dlaczego / użycie w serii |
|---|---|---|
| Combat / Shock (Combat) / Missile Combat / battle / melee | walka / starcie / walka na dystans / bitwa / walka wręcz | GBJC 8.0 „Walka”, 8.4 „Starcie”; Aleksander 8.0 „Walka na dystans”. „Starcie” wyłącznie dla Shock; „bitwa” wyłącznie dla battle; „walka wręcz” tylko opisowo (2.4) |
| Shock (mechanizm) / shock (siła uderzenia w tekście historycznym, 1.0 „shock ability of heavy cavalry”) | starcie / siła uderzeniowa | Aleksander: „ich siła uderzeniowa”; gdy oryginał wyraźnie mówi o mechanice gry – starcie (Shock) |
| Cohesion Hit / Hit / casualty / losses | ubytek spójności / ubytek / strata / straty | nigdy „trafienie”; „losses in cohesion” – ubytki spójności; „casualty” dowódcy – strata [z GBJC+GBOA] |
| Orderly Withdrawal / withdraw / withdrawal (PW, Army, Line) / retreat / Retreat Edge / Rout | uporządkowany odwrót / wycofać się / wycofanie / cofnąć się / krawędź odwrotu / rozbicie | utrwalone w serii: rdzeń „odwrót” w OW i Retreat Edge (wyjątek – 10); poza tymi nazwami: withdraw = wycofać się, retreat = cofnąć się (GBJC 10.52, PDF 6.5 „forma cofania się”), rout = rozbicie; „EXAMPLE OF WITHDRAWAL” – PRZYKŁAD UPORZĄDKOWANEGO ODWROTU [z GBJC] |
| Rout / Rout move, Rout Movement / routing / Routed | rozbicie / ucieczka rozbitych / uciekający / rozbity | GBJC; nie mieszać „rozbicia” (stan, wynik testu) z „ucieczką rozbitych” (ruch); „routs in ancient warfare” (uwaga do rozgrywki 10.22) – ucieczki w bezładzie |
| Rally / Recovery | zebranie / odzyskiwanie spójności | Rally dotyczy oddziału rozbitego (Routed), Recovery – usuwania ubytków [z GBJC+GBOA] |
| Advance (After Combat) / Pursuit, Pursue / advance (zwykłe „iść naprzód”) | posunięcie (po walce) / pościg / posuwać się naprzód | GBJC; „posunięcie” tylko dla Advance |
| Line (grupa oddziałów) / Line Command / line (szereg legionu: Hastati line, rear lines) / Line (szyk liniowy, 6.7) / Line of Sight | linia / rozkaz liniowy / linia / szyk liniowy / linia widzenia | jeden rdzeń w serii; EN w nawiasie rozstrzyga; „Line” jako termin gry zawsze z EN |
| LC (Line Command) / LC (Light Cavalry) | rozkaz liniowy (LC) / lekka jazda (LC) | ten sam skrót w oryginale (np. 4.33 „2 LC capability” – rozkazy; 8.31 „Light Cavalry (LC)”) – zawsze polski termin + kod |
| AS (Attack Superiority) / AS (Alae Sociorum na żetonach: „AS/XIX”) | przewaga atakującego (AS) / oznaczenie ali na żetonie „AS/XIX” | nie rozwijać „AS/XIX” jako przewagi |
| Column (szyk) / column (tabeli) / Shock column | kolumna (szyk) / kolumna tabeli / kolumna starcia | „In Column” zawsze z EN; kolumny tabeli – „kolumna 7 tabeli wyników starcia” |
| Phase / Segment / Step | faza / etap / krok | GBJC: Movement and Missile Fire Segment – etap; Shock Designation step – krok; 10.41 „Shock Designation Segment” – etap wyznaczenia do starcia (EN jak w oryginale) |
| Leader / Commander | dowódca / wódz | Overall Commander – wódz naczelny, Elite Commander – elitarny wódz, ale Subordinate Commander – dowódca podległy (utrwalone w serii, wyjątek – 10) |
| Leader Elephant / Elephant Leader | słoń dowódcy / dowódca słoni | 4.8 wobec 4.9 – całkiem różne żetony; zawsze z EN |
| Flank (heks, atak) / Wing (Left Wing) / ala („wings of the allies”) | skrzydło, heks skrzydłowy / skrzydło (armii) / ala („skrzydła sprzymierzeńców”) | seria używa „skrzydła” dla Flank i Wing (Aleksander „Dowódcy skrzydeł (Wing Commanders)”) – EN w nawiasie rozstrzyga; „flanking Phalanx” – falanga obchodząca skrzydło |
| Front / frontage / front (formacji) | front / szerokość frontu / front | „frontage” – szerokość frontu [z GBOA] |
| Facing / orientation (4.32) / direction | ustawienie frontu / ustawienie / kierunek | 4.32 „same orientation – Flank-to-Flank or Front-to-Rear” – „to samo ustawienie” [z GBJC 4.72] |
| Superiority (termin gry) / advantage, superiority (opisowo) / Size advantage | przewaga (Superiority) / przewaga, korzyść / przewaga liczebności (Size) | seria używa „przewagi” także opisowo (GBJC 8.46 „skutki wszelkich przewag”, 5.4 „przewaga w dziedzinie dowodzenia”); dlatego termin gry Superiority (i AS/DS) zawsze z EN – to on rozstrzyga; „superior organization” – lepsza organizacja |
| Momentum (mechanizm) / momentum (rozpęd) | impet / rozpęd | 8.15, 8.46 (uwagi projektanta) – rozpęd |
| Trump (mechanizm) / trump (czasownik) | przebicie / przebić | nie „atut” |
| Finished / finished (zwykłe „zakończył wydawanie”) | zakończony / skończył | „After a leader has finished issuing orders” – gdy dowódca skończy wydawać rozkazy; „Finished” (stan) – zakończony, z EN |
| Size / size (wielkość, np. osłony) | liczebność / wielkość | |
| Class (typu) / class (społeczna) / weapon class | klasa / klasa społeczna / klasa uzbrojenia | |
| Type / type (rodzaj ogólnie: „type of movement”, „types of terrain”) | typ / rodzaj | „Unit Type” – typ oddziału; „type of movement” – rodzaj ruchu |
| counter / marker / piece | żeton / znacznik / element (żeton) | „playing pieces (counters)” – elementy, czyli żetony [z GBJC] |
| missile / missiles (pociski) / Missile Fire | pocisk / pociski / ostrzał | nie „ogień”; „fire” jako czasownik – strzelać / prowadzić ostrzał |
| Charge (8.43) / Shock attack | szarża / atak w starciu | „The Charge” to krok procedury, nie każdy atak |
| Engaged / engaged (zwykłe „zaangażowany”: „unit not engaged to its front”, 7.24) | związany walką / niezwiązany walką od frontu | w 7.24 (uwaga projektanta) bez EN, ale tym samym rdzeniem |
| elite (Elite Commander, Elite Initiative) / Crack/Elite (poziom legionu) / elite cohorts (extraordinarii) | elitarny / doborowy/elitarny / doborowe kohorty | |
| Active (Active Leader, Active Fire, active player) / Activated (strona żetonu) | aktywny / „aktywowany” | |

## 8. Ramki, uwagi, etykiety (format – INSTRUKCJA_NOWE)

| EN | PL | Źródło / uwagi |
|---|---|---|
| HISTORICAL NOTE: | UWAGA HISTORYCZNA (Historical Note): | [z GBJC+GBOA]; beżowa ramka |
| DESIGN NOTE: | UWAGA PROJEKTANTA (Design Note): | [z GBJC+GBOA]; niebieska ramka |
| PLAY NOTE: / PLAY NOTE #1: | UWAGA DO ROZGRYWKI (Play Note): / UWAGA DO ROZGRYWKI NR 1 (Play Note #1): | [z GBJC+GBOA] |
| Design/Play Note (1.0) | uwaga projektanta/do rozgrywki (Design/Play Note) | [nowe 26.10 – propozycja] |
| HISTORICAL DIGRESSION: | DYGRESJA HISTORYCZNA (Historical Digression): | [nowe 26.10 – propozycja] 4.6 |
| 5th Edition Note: | Uwaga do 5. wydania (5th Edition Note): | 0.5 |
| Note to Players: / For Those Who Have Not Played the System Before: | Uwaga dla graczy: / Dla tych, którzy jeszcze nie grali w tym systemie: | 5.1 |
| IMPORTANT: | WAŻNE (Important): | [z GBJC+GBOA]; czerwona ramka |
| EXAMPLE: / EXAMPLES: | PRZYKŁAD (Example): / PRZYKŁADY (Examples): | [z GBJC+GBOA]; kursywa etykiety jak w oryginale |
| EXAMPLE #1: (#2, #3) / EXAMPLE #1 (Voluntary) / EXAMPLE #2 (Rout/Retreat) | PRZYKŁAD NR 1 (Example #1): / PRZYKŁAD NR 1 (Example #1) (ruch dobrowolny – Voluntary) / PRZYKŁAD NR 2 (Example #2) (ucieczka rozbitych/cofanie się – Rout/Retreat) | 0.5 |
| EXAMPLE OF ORDER OF ACTIVATION: | PRZYKŁAD KOLEJNOŚCI AKTYWACJI (Example of Order of Activation): | [z GBJC] |
| EXAMPLE OF WITHDRAWAL: | PRZYKŁAD UPORZĄDKOWANEGO ODWROTU (Example of Withdrawal): | [z GBJC] – to samo EN, ten sam przykład w GBJC |
| EXAMPLE: [Cannae] / [Zama] / [Beneventum] / [Cynoscephalae] | PRZYKŁAD (Example): [Kanny] / [Zama] / [Beneventum] / [Kynoskefalaj] | [z GBJC] („[Farsalos]”) |
| Exception: / Exceptions: / Exception #1: | Wyjątek: / Wyjątki: / Wyjątek nr 1: | [z GBJC+GBOA] |
| Note / Remember | Uwaga / Pamiętaj | ogólne |
| Livy–The Disaster at Cannae (ramka) / Excerpted from… | Liwiusz – klęska pod Kannami / Fragment: … | 6.4 |
| Running head „SPQR: Great Battles of the Roman Republic – 5th Ed.”, „© 2026 GMT Games, LLC”, adres | w md pomijamy; w składzie: „SPQR: Great Battles of the Roman Republic – wyd. 5.”; stopka i adres bez zmian | INSTRUKCJA_NOWE |

## 9. Słowa zakazane i podejrzane (sprawdzane skryptem przed oddaniem partii)

Skrypt: `python3 -I /home/claude/tr/verify/spqr_zakazane.py [pliki.md]` (domyślnie /home/claude/tr/out/SPQR_Deluxe_Rule_book_WEB/p*.md). Wynik: plik:wiersz, słowo, poprawna forma. Trafienie „podejrzane” wymaga sprawdzenia, „zakazane” – poprawy.

Zakazane (forma właściwa w nawiasie): kawaleri* (jazda); szok* (starcie); rozgrom* (rozbicie); flank* (skrzydło, heks skrzydłowy); lansjer* (kopijnicy); falangist* (falangita); linia wzroku (linia widzenia); strefa wpływu (strefa kontroli); nękanie i rozpraszanie (nękanie i rozproszenie); punkty ucieczki (punkty rozbicia); słoń przywódcy, dowódca słonia, przywódca słoni (słoń dowódcy / dowódca słoni); edycj* (wydanie); nieprzyjaciel* (wróg – 0.4); wódz podległy, dowódca podwładny, głównodowodząc*, naczelny dowódca (dowódca podległy / wódz naczelny); stackow*, stertow*; test morale (test jakości wojsk); „inicjatywa elitarnego dowódcy” (inicjatywa elitarnego wodza); angielskie słowa małą literą w tekście polskim poza nawiasami EN: shock, momentum, hit(s), trump, rally, rout.

Podejrzane (sprawdzić kontekst): jednostk* (oddział; „jednostka organizacyjna/taktyczna” w tekście historycznym dopuszczalna); ogień / ognia (ostrzał; „pod ogniem” w tekście historycznym dopuszczalne); trafien*, trafień (Hit = ubytek; „dowódca został trafiony” w 8.19 – dopuszczalne); morale; zaangażowan* (Engaged = związany walką); wyczerpan*, osłabion* (Depleted = uszczuplony); atut* (Trump = przebicie; opisowo dopuszczalne); rozpęd* (Momentum = impet; fizyczny „momentum” – rozpęd); odwrót / odwrotu poza „uporządkowany odwrót”, „krawędź odwrotu”, „kierunek odwrotu”; wycofa* w znaczeniu retreat lub rout; przewag* bez nawiasu EN w tekście zasad (czy to nie Superiority?); test TQ poza nazwami znaczników (w md – test jakości wojsk); hastaci, hastatów, pryncyp*, triariusz* (2.2 – formy łacińskie); velites, welitowie (welici); kolumn* (szyk czy tabela – EN w nawiasie); walka wręcz (tylko opisowo); skrzydł* (Flank czy Wing – EN w nawiasie).

## 10. Rozdział rdzeni (zasada L) – kontrola skryptem

Skrypt: `python3 -I /home/claude/tr/verify/spqr_glos_L.py` – czyta tabele sekcji 1–4 tego glosariusza, rozdziela warianty „A / B” (EN i PL parami), normalizuje (małe litery, bez nawiasów) i wypisuje: (a) ten sam odpowiednik PL przypisany różnym terminom EN, (b) jednowyrazowe odpowiedniki o wspólnym rdzeniu (6 liter) dla różnych terminów EN, (c) mapę kluczowych rdzeni (odwrót, wycofanie, cofanie, rozbicie, ucieczka, starcie, walka, bitwa, ubytek, zebranie, odzyskiwanie, pościg, posunięcie, impet, przebicie, zakończony, skrzydło, przewaga, kolumna, szyk, linia, ostrzał, osłona) z terminami EN, które je zawierają. Przypadki z tabeli wyjątków oznacza jako WYJĄTEK. Wynik z 26.10.2026 – 10.1 (aktualizować po każdej zmianie glosariusza).

Wyjątki dopuszczone (L.3), utrwalone w dostarczonych przekładach serii lub wynikające z tego samego desygnatu:

| PL | Terminy EN | Uzasadnienie |
|---|---|---|
| odwrót | Orderly Withdrawal; Retreat Edge (retreat – cofnąć się) | utrwalone w serii (GBJC, Aleksander, GBJCSB, Tyrant); zmiana wymagałaby poprawy dostarczonych dokumentów; w SPQR „odwrót” tylko w tych dwóch nazwach (i „kierunek odwrotu”), poza nimi withdraw – wycofać się, retreat – cofnąć się |
| skrzydło / skrzydłowy | Flank; Wing (Left Wing); ala („wings of the allies” – objaśnienie) | utrwalone w serii (Flank – heks skrzydłowy; Wing Commanders – dowódcy skrzydeł); EN w nawiasie rozstrzyga |
| przewaga | Superiority (AS, DS, Position, Weapon System); Size advantage; advantage/superiority opisowo | utrwalone w serii (GBJC 8.46, 5.4; przykłady Aleksandra „przewaga liczebności (Size)”); termin gry zawsze z EN |
| dowódca / wódz | Leader, Subordinate Commander / Commander, Overall Commander, Elite Commander, general (2.4) | utrwalone w serii (GBJC 2.4: „Określenie używane zamiennie ze słowem „wódz” (Commander)”; „wodzowie, konsulowie…” dla „generals, consuls…”) |
| walka | Combat, Missile Combat (walka na dystans), melee (walka wręcz), Engaged (związany walką), warfare (opisowo) | utrwalone w serii; Shock nigdy „walka” |
| linia | Line, line (szereg), Line Command, Line of Sight | jeden desygnat ogólny; terminy gry zawsze z EN |
| kolumna | Column (szyk), column (tabeli) | utrwalone w serii; EN w nawiasie przy szyku |
| tabela | Chart, Table | w serii oba – „tabela” (MRRC raz „Chart”, raz „Table”); Track – tor |
| zakończony | Finished (dowódca, strona żetonu, PURSUIT/FINISHED), ACTIVE/REACTION FIRE FINISHED | ten sam wyraz EN „Finished” |
| ostrzał reakcyjny | Reaction Fire (8.2) i Reaction Fire skorpionów (9.86) | ten sam termin EN |
| ruch | Movement, Move, move | jeden termin |
| zebrany / zebranie | Rally, Rallied | jeden termin |

Wynik skryptu (26.10.2026): zob. 10.1.

### 10.1 Wynik kontroli (26.10.2026)

- (a) Ten sam odpowiednik PL dla różnych terminów EN: 2 przypadki, oba dopuszczone w tabeli wyjątków: „przewaga” (Superiority; advantage / superiority opisowo – brzmienie wzorca GBJC 8.46 i 5.4) oraz „wódz” (Commander; general w 2.4 – brzmienie GBJC 2.4). Do wyjaśnienia: 0. Warianty zapisu tego samego terminu (skrót i pełna nazwa, łacina i angielski, liczba mnoga: TQ / Troop Quality, Move / Movement, Rout Movement / Rout move, Praefect Equitum / Praefectus Equitum, Scorpio / Scorpion, Strategy / Strategy Rating, Legion Infantry / legionary infantry) skrypt traktuje jako jeden termin (lista EQUIV w skrypcie).
- (b) Jednowyrazowe odpowiedniki o wspólnym rdzeniu dla różnych EN: te same 2 (wyjątki jak wyżej).
- (c) Mapa rdzeni przejrzana: odwrót – tylko Orderly Withdrawal i Retreat Edge; wycofanie / wycofać się – tylko withdrawal / withdraw (PW, Army Withdrawal, Line Withdrawal, Withdrawal Phase/Level, OW-czasownik); cofnąć się – tylko retreat; rozbicie / rozbity – tylko Rout / Routed; ucieczka – tylko Rout Movement / Rout move; starcie – tylko Shock; walka – Combat, Missile Combat, melee, Engaged, warfare (wyjątek); bitwa – battle; ubytek – Hit; zebranie – Rally; odzyskiwanie spójności – Recovery; pościg – Pursuit; posunięcie – Advance; impet – Momentum; przebicie – Trump; zakończony – Finished; skrzydło – Flank i Left Wing (wyjątek); przewaga – Superiority i advantage (wyjątek); kolumna – Column i column tabeli (wyjątek); linia – Line i pochodne; osłona – Screen (Archer Screen, Elephant Screen). Kolizji poza tabelą wyjątków brak.

## 11. DO DECYZJI UŻYTKOWNIKA

1. Hastati, principes, triarii – w glosariuszu przyjęto formy łacińskie, nieodmienne („oddział hastati”, „linia triarii”), bo dominują w dostarczonych przekładach (Zasady GBJC 3×, Księga scenariuszy GBJC 1×, wobec 1× „hastatów, pryncypów i triariuszy” w uwadze historycznej Zasad GBJC); velites – „welici”, jak w serii. Alternatywa: polskie formy odmienne „hastaci, pryncypowie, triariusze” – wygodniejsze w ok. 60 miejscach SPQR, ale wtedy dla spójności trzeba by poprawić 4 miejsca w dostarczonych przekładach GBJC. Rekomendacja: zostawić formy łacińskie (dostarczonych dokumentów nie zmieniamy).
2. Dostarczone przekłady serii – jedyna niespójność wewnątrz jednego dokumentu: w Zasadach GBJC nagłówek 7.3 brzmi „Warunki starcia”, a indeks tego samego PDF i Aleksander 7.3 – „wymogi starcia”. Rekomendacja: przy najbliższej poprawce GBJC zmienić nagłówek 7.3 (PDF i DOCX) na „Wymogi starcia”. Pozostałe różnice z 0.5 (Recovery, Procedura/Procedury ruchu, Szał słonia/słoni, „PRZYKŁAD 1”/„PRZYKŁAD NR 1”, „UWAGA DO EDYCJI DELUXE”) nie wprowadzają w błąd – rekomendacja: nie poprawiać.

### 11.1 Decyzje i ustalenia z walidacji końcowej (30.10.2026)

Walidacja językowo-merytoryczna wszystkich 44 stron (md + skład) wobec EN i przekładów serii: 71 zgłoszeń (I 13, D 58; K 0), naniesiono 82 poprawki (md 33, skład 49) – dziennik: `_robocze/walidacja/FIXLOG.tsv`. Ustalenia:

1. Nagłówki zasad opcjonalnych w składzie – jednolicie „(ZASADA OPCJONALNA)” (s. 11 i s. 40; 10.4 mieści się w jednym wierszu 12 pt). Spis treści bez zmian.
2. `retreat` w opisie ruchu oddziału rozbitego (9.53 „must retreat to separate hexes”, 10.22 „after the conclusion of the retreat”) – rdzeń „ucieczka/uciekać (retreat)” (jak Aleksander 11.73 dla tego samego zdania EN), nie „cofnąć się”, które w SPQR odsyła do 8.62. Wyjątek od sekcji 7 ograniczony do tych dwóch miejsc.
3. `weapons system` (2.4 Klasa, Przewaga; 1.0) – „system uzbrojenia” (jak GBJC 2.4), nie „rodzaj uzbrojenia”; „rodzaj” pozostaje dla „type of movement”, „weapon type” (2.4 Harcownicy).
4. „approximately X+” – „X i więcej” bez „ok./około” (2.4 Łucznicy, 2.5).
5. Typy oddziałów z kodem w składzie: redaktorzy składu stosowali K.3 (EN raz w punkcie reguł) zamiast K.2 (raz na akapit, także w przykładach). Zostawiono stan składu – zmiana wymagałaby wielu wydłużeń na stronach o skali 0,85–0,87; pominięcia zgłoszone w raporcie (4.32, 6.63 przykład nr 2, 6.71 wyjątki, 7.33 wyjątki, 8.11, 6.42–6.44, 5.34 „Elite rule”). DO DECYZJI UŻYTKOWNIKA.
6. Nota © na okładce: skład odtwarza stopkę „GMT Games, LLC • P.O. Box 1308 • Hanford, CA 93232–1308” według obrazu okładki; warstwa tekstowa oryginału zawiera też „© 2026” – do sprawdzenia na okładce oryginału. DO DECYZJI.
7. Błędy oryginału odnotowane dodatkowo (oddane wiernie): 4.72 „that combat units enters”; 6.52 cudzysłów „retreat’; 8.34 nie mówi, kto otrzymuje 2 ubytki (z 9.15 – jazda); 10.32 ostatni punktor bez kropki (w PL kropkę dodano); indeks: „Skirmishers … 6.52” powtórzone, kolejność „8.12, 6.55”, zakresy 6.41–6.44/6.45; 9.22 „Skirmishers..”; brak 9.92; „impassible”.
8. Hastati/principes/triarii – zostają formy łacińskie nieodmienne (pkt 1 wyżej – potwierdzone brakiem uwag walidatorów).

### 11.2 Decyzje użytkownika z 30.10.2026 (po walidacji)

1. Nawiasy EN przy typach oddziałów w składzie PDF – jak w PDF GBJC i Aleksandra: raz na akapit także w przykładach i wyjątkach (K.2, lista 0.2) – DO WYKONANIA (PRZEKAZANIE pkt 1).
2. Nota „© 2026” na okładce – dodać, jeśli jest na okładce oryginału (DO WYKONANIA – brak oryginału SPQR EN w środowisku).
3. 7.0: md „…i strefy kontroli”, PDF „…i ZOC” – zostaje. 8.34 bez przypisu. Osobliwości indeksu bez przypisu. „ostrzał podczas wycofania”, „modyfikacje za liczebność” – zostają. Hastati/principes/triarii – łacina nieodmienna (spolszczenie odrzucone).
4. W dostarczonym przekładzie GBJC: nagłówek 7.3 „Warunki starcia” → „Wymogi starcia” (DO WYKONANIA przy poprawce GBJC).
