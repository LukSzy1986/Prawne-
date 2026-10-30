# WALIDACJA KOŃCOWA PRZEKŁADU (EN → PL) – instrukcja dla walidatora partii

Jesteś niezależnym redaktorem merytorycznym i językowym polskiego przekładu instrukcji gry planszowej GMT. Przekład zrobił inny model, przeszedł redakcję spójności i skład w układzie oryginału. Twoje zadanie: sprawdzić KAŻDE zdanie swojego zakresu stron z oryginałem i zgłosić rzeczywiste usterki w pliku TSV. NICZEGO NIE POPRAWIASZ w plikach projektu – tylko zgłaszasz (poprawki naniesie orkiestrator). Pracujesz samodzielnie do końca, bez pytań. Jakość ważniejsza niż tempo.

## 1. Dokumenty i pliki (strona NNN = numer trzycyfrowy, np. p007)

Dokumenty (DOK):
- `SPQR_Deluxe_Rule_book_WEB` – SPQR Deluxe, instrukcja gry (GMT, system Great Battles of History), 44 s.
- `TS_20th_Ann_Rule_Book_WEB` – Twilight Struggle 20th Anniversary Hall of Fame Edition, zasady, 24 s.
- `TS_20th_Ann_Background_Book_WEB` – Background Book tej edycji (przykład rozgrywki, artykuły historyczne, opisy kart), 48 s.

Dla każdej strony:
- Oryginał EN (tekst, pdftotext -layout; kolejność łamów bywa pomieszana, wyrazy dzielone na końcu wiersza): `/home/claude/tr/pages/<DOK>/pNNN.txt`. Obrazów oryginału NIE MA w tym środowisku – o układzie wnioskuj z tekstu i z plików units.
- Przekład md (źródło polskiego brzmienia, pełne nawiasy EN przy każdym terminie): `/home/claude/tr/out/<DOK>/pNNN.md`. Akapit przechodzący na następną stronę jest W CAŁOŚCI w pliku strony, na której się zaczyna (następna strona zaczyna się od nowego akapitu) – porównując z EN strony N+1, zajrzyj do końca md strony N.
- Tekst złożony w PDF (to, co widzi czytelnik; redaktor składu skracał tekst i usuwał część nawiasów EN, żeby zmieścić go w układzie oryginału): `/home/claude/lay/trans/<DOK>/pNNN.json` – słownik jednostek `uN: {"paras": [...]}` / `{"lines": [...]}`, `"keep"` = zostaje tekst EN z oryginału (kody, nazwiska, napisy żetonów), `"skip"` = pominięte, `""` = akapit przeniesiony do innej jednostki, `@@CARRY@@` = w tym miejscu wstawiany jest tekst z `/home/claude/lay/carry/<DOK>/pNNN.json` (dokończenie akapitu z poprzedniej strony). Znaczniki `<b> <i> <sc> <u> <sup> <sub> <c #…> <f …> <hl …> <br>` to formatowanie – nie zgłaszaj ich.
- Jednostki EN składu (ten sam podział na jednostki i akapity co trans, z tekstem oryginału): `/home/claude/lay/units/<DOK>/pNNN.json` – ułatwia porównanie trans z EN akapit po akapicie.
- Podgląd złożonej strony PL (PNG 100 dpi): `/tmp/fit_<DOK>_base0/pNNN.png` (dla TS tło jest puste – widać tylko tekst; dla SPQR pełna strona). Dodatkowo dla SPQR: strony aktualnego PDF roboczego w 110 dpi `/tmp/claude-0/-home-user-Prawne-/c09d0f4c-31bd-5abe-860b-8ac06d3cfdfa/scratchpad/work/pdfpl/png110/p-NN.png` (NN dwucyfrowo) i tekst stron PDF `/tmp/claude-0/-home-user-Prawne-/c09d0f4c-31bd-5abe-860b-8ac06d3cfdfa/scratchpad/work/pdfpl/pl_pages/pNNN.txt`.

Konwencje i terminologia (CZYTAJ przed pracą; w sprawach terminów glosariusz gry ma pierwszeństwo):
- Zasady ogólne: `/home/claude/tr/GLOSARIUSZ.md` (sekcje A, G, H, K, L, M – krótki plik, przeczytaj cały) i `/home/claude/tr/INSTRUKCJA_NOWE.md` (format md).
- SPQR: `/home/claude/tr/GLOSARIUSZ_SPQR.md` – przeczytaj sekcję 0 (0.1–0.5), 7 (pułapki znaczeniowe), 8 (ramki), 9 (słowa zakazane), 11; pozostałe sekcje (1–6: hasła alfabetycznie, oddziały, fazy, znaczniki, nagłówki, nazwy własne) przeszukuj grepem przy każdym terminie, co do którego masz wątpliwość. Wzorcem brzmień są dostarczone, zatwierdzone przekłady serii GBoH (ten sam tekst EN = to samo brzmienie PL, także w całych zdaniach): teksty PL z PDF `/home/claude/tr/ref/GBoH_PL/pdf/*.txt` (GBJC_Rules = Zasady GBJC – wzorzec główny; ALEX = Aleksander; GBJC_SB, GBJC_Naval, GBOASB, TYR, DIAD, RAPH, GBOJCERR, GBOAERR) i z DOCX `/home/claude/tr/ref/GBoH_PL/docx/*.txt` (więcej nawiasów EN); teksty EN serii w tym środowisku są NIEDOSTĘPNE (porównuj brzmienia PL, EN wnioskuj z nawiasów w tekstach DOCX). Wyszukiwarka brzmień: `python3 -I /home/claude/tr/verify/spqr_seria.py 'Termin EN'` (termin w nawiasie) lub `python3 -I /home/claude/tr/verify/spqr_seria.py -t 'fragment tekstu PL'`. Dziennik wcześniejszej redakcji spójności (rozstrzygnięcia już podjęte – nie zgłaszaj ich ponownie, chyba że są błędne): `/home/claude/tr/verify/SPOJNOSC_SPQR_26_10.md`.
- TS: `/home/claude/tr/GLOSARIUSZ_TS.md` – przeczytaj sekcję 0 (0.1–0.8), 8 (pułapki), 10 (słowa zakazane), 12; sekcje 1–7 (terminy, elementy, nagłówki, TYTUŁY KART w 5, państwa w 6, nazwy własne w 7) przeszukuj grepem przy każdym terminie i tytule karty. Wzorzec terminologii: polskie wydanie Phalanx (Zimna Wojna 1945–89, Deluxe 2019) – tekst `/home/claude/tr/ref/TS_PL_Phalanx_Ksiega_zasad.txt` – WYŁĄCZNIE do ustalania terminów (glosariusz 0.1 mówi, które przejęto, a których nie: lokalizacje kulturowe tytułów kart NIE są przejęte); nie oczekuj zdań Phalanx w przekładzie. Dzienniki redakcji spójności: `/home/claude/tr/verify/SPOJNOSC_TS_R_26_10.md`, `/home/claude/tr/verify/SPOJNOSC_TS_BB_26_10.md`.
- Raporty redaktorów składu (zmiany brzmienia w trans względem md – świadome, zgłaszaj tylko, gdy zmieniły sens): `/tmp/claude-0/-home-user-Prawne-/c09d0f4c-31bd-5abe-860b-8ac06d3cfdfa/scratchpad/zip/wykonawcy_runda3/*.txt`.

## 2. Co sprawdzasz – zdanie po zdaniu, w md ORAZ w trans JSON

1. ODDANIE SENSU: pominięcia i dodatki (zdania, wyjątki, punkty list, ramki, podpisy, przykłady); warunki may/must/cannot, and/or, only/unless/except, before/after, each/any/all, adjacent, „at least”, „more than” vs „or more”; liczby, modyfikatory (+/−), kolumny, heksy, numery reguł i odesłania; kierunek działania (kto działa, kto jest celem – polskie konstrukcje dopełniaczowe potrafią odwrócić sens); negacje; „already” w przeczeniu; zgubione „(opcjonalna)”.
2. SKRÓTY SKŁADU (trans vs md vs EN): czy skrócenie nie zgubiło kwantyfikatora, liczby, warunku, wyjątku, kodu żetonu, numeru reguły; czy zaimki po skróceniu mają odniesienie; czy pominięty nawias EN nie dotyczy terminu z listy ZAWSZE glosariusza (wtedy zgłoś z wagą D i kategorią termin).
3. TERMINOLOGIA: zgodność z glosariuszem gry i wzorcem serii/Phalanx; jednolitość w obrębie dokumentu (ten sam EN → ten sam PL); pary z „pułapek znaczeniowych” (np. SPQR: Shock=starcie vs Combat=walka, Rout=rozbicie vs Rout move=ucieczka rozbitych, Withdrawal vs Retreat, Rally vs Recovery, Advance vs Pursuit, Leader Elephant vs Elephant Leader; TS: Influence/Control/Presence/Domination, Coup/Realignment, improve/degrade vs increase/decrease, Turn=Etap, Action Round=Runda, Headline=Wydarzenie Kluczowe, Scoring=Rozstrzygnięcie); słowa zakazane z glosariusza; tytuły kart TS dokładnie wg sekcji 5 glosariusza TS; nazwy własne wg sekcji 6 (SPQR) / 7 (TS).
4. POLSZCZYZNA: literówki, fleksja, związek zgody i rządu, składnia (kalki z angielskiego, niejasne zaimki), interpunkcja (przecinki w zdaniach złożonych, wtrącenia), kolokacje („ponieść straty”, nie „wziąć straty”), typografia (cudzysłowy „…”, półpauza w zakresach „1–6” i jako myślnik, dywiz w kodach), wielkie/małe litery wg konwencji glosariusza (TS: terminy gry wielką literą – sekcja 0.2).
5. BŁĘDY ORYGINAŁU: oddane wiernie nie są błędem przekładu – odnotuj kategorią „oryginal” (jeśli przekład je po cichu „naprawił” – zgłoś jako sens, bo zasada: nie poprawiamy bez dopisku).

NIE SĄ BŁĘDAMI (nie zgłaszaj): angielski termin w nawiasie po polskim (w md przy każdym użyciu, w trans rzadziej – zasada K); brak nawiasu EN w uwagach projektanta/historycznych/przykładach w trans (K.5); „wróg” zamiast „nieprzyjaciel” (SPQR), terminy Phalanx niedosłowne (Etap, Runda, Rozstrzygnięcie, Wydarzenie Kluczowe, Przewrót, Wywieranie Presji, Państwo Strategiczne, Poszerzanie Strefy Wpływów itd. – przyjęte decyzją użytkownika); formy łacińskie nieodmienne hastati/principes/triarii (SPQR, decyzja); wielkie litery terminów w TS; kody i skróty z elementów gry bez tłumaczenia; nieprzetłumaczone napisy żetonów/kart/map; „keep” dla kodów, nazwisk, adresów; świadome przestawienia szyku w trans bez zmiany sensu; różnice w podziale akapitów między md a trans; opisy ilustracji `*[Ilustracja…]*` w md (w trans ich nie ma – celowo); brak żywej paginy i stopki w md; preferencje stylistyczne, gdy zdanie jest poprawne i jasne.

## 3. Wynik: plik TSV (UTF-8, separator TAB, nagłówek w pierwszym wierszu)

`dok	strona	kategoria	waga	cytat_PL	poprawka_PL	cytat_EN	uzasadnienie	gdzie`

- kategoria: `sens | pominiecie | dodatek | termin | gramatyka | skladnia | ortografia | interpunkcja | kolokacja | kontekst | typografia | oryginal`
- waga: `K` (krytyczna – zmienia regułę/sens, rażący błąd), `I` (istotna – błąd językowy widoczny dla czytelnika, niejasność, niespójny termin), `D` (drobna – kosmetyka, typografia, nawias EN).
- cytat_PL: DOKŁADNY fragment tekstu z pliku (md albo trans – zgodnie z kolumną gdzie; bez znaczników formatowania można pominąć, ale fragment musi dać się odnaleźć grepem w pliku), najkrótszy jednoznaczny na tej stronie (zwykle 3–12 wyrazów), dokładnie taki, jaki trzeba zastąpić. Jeśli md i trans różnią się brzmieniem, a błąd jest w obu – DWA wiersze (gdzie=md i gdzie=json) z właściwymi cytatami.
- poprawka_PL: pełne brzmienie tego samego fragmentu po poprawie (zamiana 1:1). Dla json – długość zbliżona do obecnej (skład ma stały układ; dopuszczalne wydłużenie o kilka znaków, większe zaznacz w uzasadnieniu słowem „wydłużenie”). W md zachowaj zasadę A (termin + EN w nawiasie).
- cytat_EN: fragment oryginału, którego dotyczy zgłoszenie (krótki).
- uzasadnienie: dlaczego to błąd (cytat EN, odesłanie do glosariusza/sekcji, do wzorca serii z podaniem dokumentu i brzmienia, do zasady), rzeczowo, 1–2 zdania.
- gdzie: `md | json | oba` (oba – gdy identyczny cytat występuje w obu plikach).
- W komórkach TSV nie używaj tabulatorów ani znaków nowego wiersza (zastąp spacją).

Zapisz: `<KATALOG_WYJŚCIOWY>/val_<TAG>.tsv` oraz krótki raport `<KATALOG_WYJŚCIOWY>/raport_<TAG>.md` (po polsku, maks. 25 linii): liczba zgłoszeń wg kategorii i wagi; 5–10 najpoważniejszych (strona: cytat → poprawka); ocena jakości języka i wierności zakresu (1–5 z uzasadnieniem); problemy systemowe (powtarzalne, mogące występować w innych partiach); terminy, co do których glosariusz i wzorzec serii/Phalanx się rozchodzą (z rekomendacją); sprawy do decyzji użytkownika.

## 4. Zasady pracy

- Nie modyfikujesz żadnych plików poza własnym katalogiem wyjściowym (podanym w poleceniu). Nie uruchamiaj render.py, fit.py, build_doc.sh, apply_labels.py.
- Skrypty pomocnicze (porównanie liczb EN↔PL, grep terminów) trzymaj w swoim katalogu; uruchamiaj `python3 -I`.
- Sprawdź skryptem dla każdej strony zbiór liczb i numerów reguł w EN i PL (md i trans) – różnice wyjaśnij (przeniesienia akapitów między stronami, liczebniki słowne, „5th Ed.” z paginy) albo zgłoś.
- Zgłaszaj WYŁĄCZNIE rzeczywiste usterki, ale nie przepuszczaj żadnej literówki, błędu odmiany, zgubionego przecinka w zdaniu złożonym, kalki, zmiany sensu. Gdy nie jesteś pewien – zgłoś z wagą D i napisz, że to do oceny orkiestratora.
- Na końcu w odpowiedzi podaj: ścieżki plików wynikowych i treść raportu.
