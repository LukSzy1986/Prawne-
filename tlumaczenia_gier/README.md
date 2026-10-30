# Tłumaczenia instrukcji gier GMT na język polski – stan po walidacji końcowej (30.10.2026)

Katalog zawiera wyniki dokończenia przekładów trzech dokumentów (kopia robocza z 27.10.2026 11:00 + walidacja językowo-merytoryczna i poprawki z 30.10.2026):

- `SPQR_Deluxe/` – SPQR Deluxe (GMT, seria Great Battles of History): instrukcja gry, 44 s.
  - `SPQR_Deluxe_Rule_book_WEB_PL.pdf` – skład w układzie oryginału (tekst polski na tle oryginału, etykiety diagramów),
  - `SPQR_Deluxe_Rule_book_WEB_PL.docx` – wersja tekstowa z pełnymi nawiasami EN,
  - `md/` – przekład źródłowy, jeden plik na stronę (Pandoc Markdown),
  - `GLOSARIUSZ_SPQR.md` – glosariusz gry (terminologia spójna z przekładami GBJC, Aleksandra i modułów GBOA).
- `Twilight_Struggle/` – Twilight Struggle 20th Anniversary Hall of Fame Edition: Zasady (24 s.) i Background Book (48 s.)
  - `*_PL.docx` – wersje tekstowe, `Zasady_md/`, `Background_Book_md/` – przekład źródłowy,
  - `GLOSARIUSZ_TS.md` – glosariusz (terminologia mechaniki wg polskiego wydania Phalanx 2019).
  - Składu PDF tych dwóch dokumentów nie dało się odtworzyć w tej sesji (w kopii roboczej brak tła stron `lay/bg` i oryginałów `tr/src`); pliki `trans` są gotowe do `build_doc.sh` na komputerze z pełnym środowiskiem.
- `_robocze/` – pliki składu (`trans`), łatki layoutu, zgłoszenia walidacji (TSV) i dziennik naniesionych poprawek.
- `RAPORT_30_10_2026.md` – raport z wykonanych prac, decyzje i sprawy otwarte.
