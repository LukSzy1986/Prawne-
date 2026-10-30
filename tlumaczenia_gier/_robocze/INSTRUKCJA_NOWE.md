# INSTRUKCJA DLA TŁUMACZA PARTII – NOWE DOKUMENTY (SPQR Deluxe; Twilight Struggle 20th Anniversary)

Utworzono 26.10.2026 na podstawie INSTRUKCJA_SE.md. Obowiązuje razem z: /home/claude/tr/GLOSARIUSZ.md (zasady ogólne A, G, H, K, L, M – obowiązują zawsze) oraz glosariuszem gry:
- SPQR → /home/claude/tr/GLOSARIUSZ_SPQR.md (terminologia serii Great Battles of History – spójna z przekładami GBJC, Aleksandra i modułów GBOA),
- Twilight Struggle (Zasady i Background Book) → /home/claude/tr/GLOSARIUSZ_TS.md.
W sprawach terminów glosariusz gry ma pierwszeństwo przed ogólnym. Hasła oznaczone w glosariuszu jako propozycje stosuj, a uwagi zgłoś w raporcie.

## Dokumenty i odbiorca
- DOK (nazwy robocze; pliki w /home/claude/tr/src/<DOK>.pdf):
  - SPQR_Deluxe_Rule_book_WEB (44 s.) – instrukcja gry SPQR Deluxe (GMT, Richard Berg; system Great Battles of History).
  - TS_20th_Ann_Rule_Book_WEB (24 s.) – instrukcja Twilight Struggle 20th Anniversary Hall of Fame Edition (Ananda Gupta, Jason Matthews).
  - TS_20th_Ann_Background_Book_WEB (48 s.) – Background Book do tej edycji (artykuły historyczne, uwagi projektantów, strategie, omówienia kart).
- Odbiorca: polski gracz, który gra z angielskimi elementami gry (mapa, karty, żetony, znaczniki, tabele na planszy). Kryterium nadrzędne: przekład nie może wprowadzać zamieszania ani niezrozumienia – czytelnik zawsze musi wiedzieć, o który termin, fazę, kartę, znacznik, tabelę chodzi, i móc je odnaleźć na elementach gry.
- Jakość jest ważniejsza niż tempo. Nie skracaj, nie upraszczaj, nie dopisuj objaśnień bez pokrycia w oryginale; nie pomijaj zdań, wyjątków, przykładów, punktów list, uwag i podpisów.
- Tekst historyczny i eseje (Background Book, „Historical Notes”, „Design Notes”): ma być naturalną, poprawną polszczyzną, bez kalek; nazwy własne – polskie formy utrwalone w piśmiennictwie (np. Chruszczow, Mao Zedong, Ho Chi Minh, Kuba, Zatoka Świń), zgodne z glosariuszem. Fakty, daty, liczby i cytaty oddaj dokładnie; cytaty znanych osób tłumacz wiernie (nie szukaj „oficjalnych” polskich wersji, chyba że glosariusz je podaje).

## Źródła językowe
- Znaczenie EN: Merriam-Webster, American Heritage Dictionary. Termin gry rozumiemy przez jego funkcję w zasadach (sprawdź definicję w instrukcji i miejsce użycia).
- Polszczyzna: słowniki PWN (poprawność, odmiana, pisownia), terminologia wojskowa/historyczna; dla Twilight Struggle – także utrwalone polskie nazewnictwo wydarzeń zimnej wojny (PWN Encyklopedia, Wikipedia PL jako pomoc). Polskie wydanie Twilight Struggle (Phalanx, „Zimna Wojna 1945–1989”) – tylko pomocniczo i tylko wtedy, gdy glosariusz tak mówi (nie mamy jego instrukcji).
- Brzmienie terminu bierzesz z glosariusza gry; jeśli go brak – zaproponuj wg tych samych zasad i zgłoś w raporcie (NOWE TERMINY: „EN – PL [uzasadnienie]”). Nie zgadujesz: sprawy dyskusyjne zgłaszaj z rekomendacją.

## Materiały i osobliwości plików
- Oryginały: /home/claude/tr/src/<DOK>.pdf. KAŻDĄ stronę obejrzyj narzędziem Read z parametrem pages (2–4 strony naraz; drobny druk, tabele, ramki, karty i diagramy – render pdftoppm 200 dpi do własnego katalogu roboczego i oglądanie wycinków). Tekst stron: /home/claude/tr/pages/<DOK>/pNNN.txt (pdftotext -layout).
- Kolejność tekstu w .txt bywa pomieszana (dwa/trzy łamy, ramki, przykłady przechodzące między łamami, tekst opływający obrazy) – o kolejności i podziale na akapity decyduje obraz strony. Rozbite inicjały, rozstrzelone nagłówki i spłaszczone indeksy – odczytuj z obrazu.
- Znaki: punktor „•”, półpauza „–” i pauza „—”, cudzysłowy “ ” i apostrof ’, „©”, tabulatory, znak strony \f, miękki dywiz U+00AD – w md stosuj polską typografię: „…”, półpauza z odstępami jako myślnik, apostrof tylko w nazwach EN.
- Dla SPQR: wzorce brzmień – GLOSARIUSZ_SPQR.md oraz zatwierdzone przekłady serii (PDF: /mnt/user-data/outputs/PL/GBJC_Rules_Final_Low-Res_PL.pdf, GBJC_NavalRules_Final_PL.pdf, Deluxe_Alexander_6th_Edition_Rules_PL.pdf, GBOA_*; oryginały EN: /home/claude/val/en_pages/<DOK>/; tekst PL: pdftotext -layout z outputs/PL). Dla fragmentów SPQR identycznych lub bliskich z tymi dokumentami (system Great Battles of History: sekwencja gry, ZOC, ostrzał, szturm/Shock, rozbicie, spójność, dowódcy) przejmij polskie brzmienie – sprawdź zdanie po zdaniu z EN; różnice w tekście EN oddaj według oryginału.

## Format wyjściowy (Pandoc Markdown) – jeden plik na stronę
- Zapisz tłumaczenie KAŻDEJ strony do osobnego pliku /home/claude/tr/out/<DOK>/pNNN.md (NNN – numer strony trzycyfrowo, jak w nazwie pliku .txt). Pierwsza linia: `<!-- s. N -->`.
- Nie tłumacz i nie przepisuj żywej paginy (nagłówka biegnącego: „SPQR: Great Battles of the Roman Republic – 5th Ed.”, „TWILIGHT STRUGGLE 20th Anniversary Hall of Fame Edition”, „BACKGROUND BOOK” itp.), numerów stron, stopek „© … GMT Games, LLC” ani znaczników drukarskich.
- Akapit przechodzący na następną stronę przetłumacz w całości w pliku strony, na której się zaczyna; plik następnej strony zaczyna się od pierwszego nowego akapitu (możesz dodać komentarz `<!-- dokończenie akapitu X – w pNNN.md -->`). Tak samo tabela lub przykład przechodzący na następną stronę.
- Nagłówki: tytuły rozdziałów i punktów jako `## …` z numerem jak w oryginale („## 5.7 …”; wersaliki, gdy oryginał ma wersaliki). Etykiety wpuszczone w akapit („6.31 Zasady ruchu:”) – pogrubione na początku akapitu, nie jako nagłówek. Nagłówki artykułów w Background Book – `## …` lub `### …` wg rangi w oryginale.
- Ramki: `> UWAGA DO ROZGRYWKI (Play Note): …`, `> UWAGA PROJEKTANTA (Design Note): …`, `> UWAGA HISTORYCZNA (Historical Note): …`, `> WAŻNE (Important): …` – nazwy ramek wg glosariusza; ramki zapisuj tak samo niezależnie od koloru tła. Przykłady: `*PRZYKŁAD:* …` (kursywa etykiety jak w oryginale; treść przykładu – zwykłym krojem, kursywą tylko tam, gdzie jest w oryginale).
- Tabele: tabela pipe (`| … | … |`); tytuł tabeli zwykłym akapitem nad tabelą; gwiazdka na początku komórki jako `\*`; liczby i kody bez zmian; puste komórki puste.
- Ilustracje, diagramy, żetony, karty, zdjęcia: `*[Ilustracja (s. N oryginału): opis – z przekładem napisów]*`. Napisy na żetonach, kartach i mapach – w oryginale, a ich tłumaczenie w opisie (karty: „Tytuł (Title):”, „Efekt (Event):”… wg glosariusza). Podpisy pod zdjęciami i ilustracjami – przetłumacz (jako osobne akapity `*Podpis (s. N): …*`). Nie opisuj zdjęć archiwalnych szczegółowo – jedno zdanie, napisy i podpisy w całości.
- Wyróżnienia: nowe/zmienione zasady lub tła podświetlone w oryginale – fragment w zdaniu `[…]{.nowe}`, cały akapit lub ciąg akapitów w bloku `::: nowe` … `:::` (zgodnie z obrazem; tła ramek i pasków w tabelach nie oznaczamy); kapitaliki `[…]{.smallcaps}` tylko tam, gdzie są w oryginale (tytuły kart w Background Book są wersalikami/kapitalikami – oddaj kapitalikami); podkreślenia `[…]{.underline}`; indeksy `^x^` / `~x~`. Pogrubienia w środku zdań oryginału oddaj kursywą (albo bez wyróżnienia), kursywę – kursywą.
- Listy: punktory „•” → `- `; listy literowe zachowują litery; słowne wyliczenia („1st–4th”) – słownie, żeby Pandoc nie tworzył list numerowanych.
- Po zapisaniu sprawdź każdy plik: `pandoc -f markdown -t html pNNN.md > /dev/null` bez ostrzeżeń; klamry `[…]{.…}` i bloki `:::` domknięte.

## Zasady spójności i nawiasy EN (md)
- Zasada A z GLOSARIUSZ.md: w md każdy termin gry przy każdym użyciu ma formę „polski termin (English)” (odmieniamy tylko człon polski). Bez nawiasu – słowa potoczne (gracz, przeciwnik, mapa, żeton, kość, tura, runda, zwykłe czasowniki) i lista z glosariusza gry. W tekście historycznym i fabularnym (Background Book) nawiasy EN tylko przy terminach gry i tytułach kart; przy nazwach własnych historycznych – bez nawiasów, chyba że glosariusz każe (nazwa EN myląca, np. operacje).
- Ten sam tekst EN = ten sam tekst PL w obrębie gry; Zasady i Background Book Twilight Struggle używają tych samych terminów i tych samych tytułów kart.
- Błędów oryginału nie poprawiamy – przekładamy wiernie i zgłaszamy w raporcie („błąd oryginału: strona, cytat, co jest nie tak”).

## Raport końcowy partii (krótko, po polsku, maks. ok. 30 linii)
- Lista zapisanych plików (ścieżki).
- Trudne miejsca (kolejność tekstu, strony odtworzone z obrazu, rozbieżności i błędy oryginału – oddane wiernie).
- NOWE TERMINY („EN – PL [uzasadnienie]”) i uwagi do haseł glosariusza (tylko rzeczywiste problemy).
- Karty/ilustracje/napisy w grafice, które będą wymagały etykiet w składzie (strona + napis).
- Nie wklejaj tłumaczenia do raportu.

## Kontrola przed oddaniem
- Dla każdej strony partii istnieje plik pNNN.md; nie pominięto żadnego akapitu, ramki, przykładu, punktu listy, wiersza tabeli, podpisu ani napisu na karcie/żetonie (porównaj z .txt i z obrazem strony).
- Każdy termin gry w formie „polski (EN)” wg zasady A; nazwy kart, znaczników, faz i tabel zgodne z glosariuszem; pary z „Pułapek znaczeniowych” glosariusza sprawdzone zdanie po zdaniu; skryptem sprawdź listę słów zakazanych z glosariusza.
- Liczby, daty, parametry, numery punktów i odesłania („zob. 5.7”, „s. 12”) przepisane dokładnie (porównaj skryptem zbiór liczb EN i PL strony; różnice uzasadnij).
- Klamry `[…]{.nowe}`, `[…]{.smallcaps}`, `[…]{.underline}` i bloki `:::` domknięte; pandoc bez błędów.
- Pliki robocze (obrazy stron, notatki) trzymaj wyłącznie we własnym, unikalnym podkatalogu (np. /home/claude/work/<TAG>/) i uruchom na końcu /home/claude/backup.sh.
