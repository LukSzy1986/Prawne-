# Raport walidacji – SPQR Deluxe, s. 32–38 (tag spqr_32_38)

Zakres: 9.11 (kroki 3–4) – 9.14 słonie i szał, 9.15–9.19, 9.2 harcownicy/welici/LI, 9.3 lekka jazda, 9.4 obrona falangi, 9.5 DD, 9.6 legion manipularny (MLE), 9.7 triarii, 9.8 artyleria, 9.9 barbarzyńcy i rydwany, 10.0–10.22. Sprawdzono każde zdanie EN↔md↔trans (+carry s. 37), zbiory liczb i numerów reguł (skrypt w_32_38/nums.py – wszystkie różnice wyjaśnione: numery stron w podpisach ilustracji, „wyd. 5.” z paginy, cyfry róży wiatrów z opisu ilustracji), spqr_zakazane.py (zakazane 0, podejrzane 8 – wszystkie opisowe lub z EN), brzmienia wzorców (GBJC 9.91–9.93, 9.2x, 10.0–10.2; Aleksander 11.7 DD, 10.0).

**Zgłoszenia: 14** – wagi: K 0, I 4, D 10; kategorie: składnia 8, kontekst 3, gramatyka 1, kolokacja 1, typografia 1. Plik: val_spqr_32_38.tsv (md 4, json 7, oba 3).

Najpoważniejsze:
1. s. 33 (9.23, md+json): „Wszystkie oddziały atakujące … nie muszą wykonywać testu” → „Żaden oddział atakujący w starciu (Shock attack) wyłącznie harcowników nie musi wykonywać testu…” – kalka; brzmienie GBJC 9.23 (ten sam tekst EN).
2. s. 33 (9.23, json): „dzieli się na pół (w dół)” → „(zaokrąglając w dół)” – skrót składu nieczytelny dla gracza.
3. s. 36 (9.96, json): „…z oddziałem CH stojącym samotnie w heksie, oddział ten zostaje natychmiast wyeliminowany” → „oddział CH zostaje…” – zaimek po skróceniu wskazuje na oddział wroga.
4. s. 33 (9.16, md): „Jeśli oddział jazdy jest rozbity (routed)” → „ulegnie rozbiciu” (GBJC DOCX); Aleksander czyta odwrotnie – do oceny.
5. s. 34 (9.53, oba): „Oddziały muszą się cofnąć (retreat) na oddzielne heksy” – oba oddziały są rozbite; Aleksander 11.73: „muszą uciekać”.
6. s. 37 (10.0, json): „ubytki … za nadmierny ruch i/lub walkę” → „wskutek nadmiernego ruchu i/lub walki” (Aleksander 10.0).
7. s. 37 (9.96 carry, json): „nie kosztuje punktów ruchu (MP) ani ubytków spójności” → „…ani nie powoduje ubytków spójności”.
8. s. 36 (9.94, oba): „miejscowi zdają się wkładać” → „zdawali się” (czas przeszły).

**Ocena: język 4,5/5, wierność 5/5.** Nie znaleziono żadnej zmiany sensu reguły, pominięcia ani błędnej liczby/odesłania; terminologia zgodna z glosariuszem i wzorcami (szał słoni, kornak, róża wiatrów, osłony słoni, DD, MLE, zaciekłość/porywczość, znaczniki ROUTED/ACTIVE FIRE). md powtarza niemal dosłownie zatwierdzone brzmienia GBJC/Aleksandra tam, gdzie EN jest identyczny. Usterki to przede wszystkim skróty redaktora składu w trans (nieczytelne nawiasy, zaimki bez odniesienia, niezręczne kolokacje) – drobne, ale widoczne dla czytelnika.

Problemy systemowe (mogą występować w innych partiach): (a) skróty składu typu „(w dół)”, „oddział ten”, „jego gracz”, „mieć odstępy” – przy skracaniu gubi się odniesienie lub czytelność; warto przejrzeć trans całego dokumentu pod kątem zaimków po skróceniu; (b) konstrukcja „Wszystkie X nie muszą/nie mogą” zamiast „Żaden X nie musi” (sprawdzić grepem w pozostałych stronach); (c) wyjątek w ramce WAŻNE s. 37 i wyjątki 10.13 zgodne – bez uwag.

Glosariusz a wzorzec serii – rozbieżności: (1) „retreat” w kontekście rozbicia (9.53 „must retreat to separate hexes”, 10.22 „after the conclusion of the retreat”): glosariusz 7 każe „cofnąć się”, Aleksander ma „uciekać”, GBJC „odwrót” – rekomendacja: w obu miejscach SPQR rdzeń „ucieczka/uciekać” z EN w nawiasie (ruch rozbitego oddziału), bo „cofnięcie” odsyła do 8.62; (2) 9.16 „is routed”: GBJC PDF „Rozbita jazda…”, GBJC DOCX „ulegnie rozbiciu”, Aleksander „jest już rozbity” – rekomendacja: „ulegnie rozbiciu” (wynik testu z poprzedniego zdania; md) i bez zmian w trans.

Do decyzji użytkownika: pkt (1)–(2) powyżej; dopuszczalne wydłużenia w trans (zgłoszenia 2, 7, 9 – 11–12 znaków) wymagają sprawdzenia w składzie; błędy oryginału w zakresie są już odnotowane w dzienniku spójności (9.22 „Skirmishers..”, 9.23 „Pre-Shock TQ”, brak 9.92, „impassible”), nowy drobiazg: s. 38 „routing/ retreating” (spacja) – zgłoszony jako D typografia w md.
