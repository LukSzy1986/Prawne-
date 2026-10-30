# GLOSARIUSZ OGÓLNY – ZASADY PRZEKŁADU INSTRUKCJI GIER GMT (EN → PL)

Odtworzono 16.10.2026. Zasady obowiązują we wszystkich grach projektu. Terminologię konkretnej gry zawiera jej glosariusz (GLOSARIUSZ_<GRA>.md, np. GLOSARIUSZ_SE.md) – w sprawach terminów ma on pierwszeństwo przed tym plikiem; sekcje A, G, H, K, L, M obowiązują zawsze.

## Odbiorca i kryterium nadrzędne
- Odbiorca: polski gracz, który gra z angielskimi elementami gry (żetony, karty, arkusze, plansze, tabele na planszy). Zna gry strategiczne, nie musi znać angielskiego.
- Kryterium nadrzędne: przekład nie może wprowadzać zamieszania ani niezrozumienia. Gracz zawsze musi wiedzieć, o który termin, fazę, żeton, kartę, tabelę i rubrykę chodzi, i móc je odnaleźć na elementach gry.
- Jakość jest ważniejsza niż tempo. Wierność sensu reguły ma pierwszeństwo przed stylem; polszczyzna ma być naturalna, ale bez upiększeń zmieniających treść.

## Wierność, błędy oryginału, errata
- Nie dodajemy glos ani dopowiedzeń bez pokrycia w oryginale (np. „w heksie”, gdy oryginał mówi „present”); nie pomijamy zdań, wyjątków, punktów list, przykładów ani podpisów.
- Błędów oryginału nie poprawiamy – przekładamy wiernie i odnotowujemy je (raport partii, dziennik weryfikacji: „błąd oryginału”). Poprawka tylko na decyzję użytkownika – wtedy w tekście z dopiskiem „[przyp. red.: …]”.
- Errata to osobne dokumenty – przekładamy je osobno i nie wprowadzamy ich treści do przekładu zasad. Cytowane w erracie brzmienia reguł muszą używać tych samych terminów co przekład zasad.

## Źródła językowe
- Znaczenie słów i zwrotów angielskich: słowniki amerykańskie – Merriam-Webster i American Heritage Dictionary (AHD); oryginały GMT są amerykańskie. Znaczenie terminu gry ustalamy z jego funkcji w zasadach, nie ze słownika ogólnego.
- Polszczyzna: polska terminologia wojskowa i morska (typy okrętów, formacje, stopnie), astronomiczna (układ planetarny, mgławica, planetoida, czarna dziura), słowniki PWN (poprawność, odmiana, pisownia). Polskie wydania innych gier – pomocniczo i tylko wtedy, gdy nie kolidują z zasadą L.
- Nie zgadujemy: gdy źródła się różnią, wybór i uzasadnienie zapisujemy w glosariuszu gry; sprawy rzeczywiście dyskusyjne – do decyzji użytkownika (z rekomendacją).

## A – terminy gry w plikach md
1. W plikach md każdy termin gry przy każdym użyciu ma formę „polski termin (English)”. Odmieniamy tylko człon polski: „krążowników (Cruisers)”.
2. Bez nawiasu EN – słowa potoczne (gracz, przeciwnik, mapa, heks, żeton, kość, tura, runda, zwykłe czasowniki). Listę i zasadę gęstości podaje glosariusz gry.
3. W nawiasie EN dokładnie tak, jak w danym miejscu oryginału (wielkość liter, liczba, skrót); polski termin – zawsze według glosariusza.
4. Nazwy znaczników, kart, tabel i stron żetonów: polska nazwa wielką literą + EN („znacznik Niebezpieczeństwo! (Danger!)”).
5. Skróty z elementów gry zostają w brzmieniu oryginału; nie tworzymy polskich skrótów.

## G – liczby, jednostki, zapis
1. Nie przeliczamy jednostek miary („22 x 30 inch map” → „mapa 22 × 30 cali”).
2. Liczby, oznaczenia i parametry z elementów gry przepisujemy bez zmian; ułamki dziesiętne z przecinkiem, numery reguł i wersji z kropką.
3. Zakresy liczb – półpauza („1–6”); odesłania „(zob. 5.7)”, „(s. 45)”.

## H – format tekstu
1. Tytuł tabeli – zwykłym akapitem nad tabelą (nie nagłówkiem i nie wierszem tabeli).
2. Pogrubienie tylko dla etykiet na początku akapitu („**Procedura:**”); pogrubienia w środku zdań oryginału oddajemy kursywą albo bez wyróżnienia.
3. Gwiazdka na początku komórki tabeli zapisana jako „\*” (żeby Pandoc nie utworzył listy).
4. Kursywa, kapitaliki i podkreślenia – jak w oryginale (zapis według instrukcji tłumacza danej gry).

## K – angielskie nawiasy w składzie PDF
1. W składzie (PDF w układzie oryginału) nie powtarzamy EN przy każdym użyciu jak w md – nawiasy zostają według pkt 2–6. Na pierwszej stronie z tekstem ciągłym dokumentu skład dodaje notę „Od redakcji” o zasadzie nawiasów.
2. Zawsze (raz na akapit) – przy terminach łatwych do pomylenia i z listy „ZAWSZE” w glosariuszu gry; przy obu członach pary w jednym akapicie – przy każdym.
3. Pozostałe terminy gry – przy pierwszym użyciu w każdym numerowanym punkcie reguł, sekcji scenariusza lub ramce.
4. Nie obok innego nawiasu – scalamy: „(Fast 1, 9.9)”, „(Resource Cards, 39.0)”; nie stosujemy nawiasów kwadratowych zamiast zagnieżdżonych. W nagłówkach – tylko jeśli nagłówek nie zyska przez to wiersza.
5. W uwagach projektanta, tekście historycznym i fabularnym oraz w przykładach – bez nawiasów EN, poza terminami z listy ZAWSZE.
6. Nawiasy usuwamy tylko wtedy, gdy tekst się nie mieści, w kolejności: (a) powtórzenia w tym samym punkcie, (b) nawiasy przy terminach jednoznacznych z kontekstu lub z kodu żetonu, (c) nawiasy pierwszego użycia (pkt 3) w długich punktach; nawiasy z listy ZAWSZE i tytuły kart – na końcu, a każde takie pominięcie zgłaszamy w raporcie. Nigdy nie skracamy treści reguły, żeby zmieścić nawias.

## L – jeden rdzeń dla jednego terminu
1. Jeden termin EN ma jeden polski rdzeń w całej grze i we wszystkich jej dokumentach.
2. Różne terminy EN nigdy nie dostają tego samego polskiego rdzenia (np. Combat – walka, Battle – bitwa; screen – osłonić, protect – chronić).
3. Wyjątek jest dopuszczalny tylko wtedy, gdy jest opisany w glosariuszu gry (tabela rozdziału rdzeni) z uzasadnieniem.
4. Przed oddaniem glosariusza i każdej partii przekładu sprawdzamy skryptem duplikaty: ten sam polski odpowiednik dla różnych terminów EN.

## M – uwagi autorów
- Developer’s Notes / Developer Notes – Uwagi wydawcy.
- Designer’s Notes / Designer Notes – Uwagi projektanta; Design Note / Designer Note – Uwaga projektanta.

## Spójność między dokumentami
- Ten sam tekst angielski = ten sam tekst polski we wszystkich dokumentach gry (zasady, księgi scenariuszy, errata, karty pomocy). Wzorcem jest dokument wskazany w glosariuszu gry (dla Space Empires – zatwierdzony PDF Głównej księgi zasad); dokumenty tłumaczone później przejmują jego brzmienie, a różnice wprowadzają tylko tam, gdzie różni się tekst EN.
