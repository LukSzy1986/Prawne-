#!/usr/bin/env python3
"""Generator specu etykiet: SPQR_Deluxe_Rule_book_WEB – podpisy heksów na diagramach poglądowych
(redaktor spqr_lab, 2026-10-26).

Brzmienie jak w przekładzie serii (GBJC_Rules_Final_Low-Res_PL s. 19–20, 24, 39; Deluxe_Alexander_6th_PL
s. 17–20; glosariusz GLOSARIUSZ_SPQR.md: Front / Flank / Rear hex – heks frontowy / skrzydłowy / tylny):
  „Flank” → „Skrzydło”, „Rear” → „Tył”; „Front” brzmi po polsku tak samo – oryginał zostaje bez nakładki
  (jak w GBJC; nakładka tego samego słowa niczego nie zmienia, a dokłada ryzyko śladów).

s. 16 (diagram nad przykładem nr 3, 6.52; raster JPX 144 ppi): czarne „Flank” ×6 (#231f20), czerwone „Rear” ×5
  (#ed1c24); krój oryginału = Times Bold → LSerif 700 (metrycznie zgodny), 9,2 pt (szerokość i wysokość
  liter jak „Front”/„Flank”/„Rear” oryginału: Flank 62×17 px, Rear 53×18 px). Zakrycie płaskie "auto"
  (tło heksów jednolite: #ffffff / #dcddde), okna = luźna ramka napisu (różnica od tła > 6) ± 3 px, wewnątrz
  heksu (obrzeże okna w całości w kolorze tła – sprawdzone skryptem winchk.py). Tekst wyśrodkowany na środku
  napisu oryginału, linia bazowa = dolna krawędź liter oryginału.
  Wyjątek: „Rear” nad żetonem LG (heks w dolnym rzędzie) – napis leży pod wierzchołkiem heksu, „R” styka się
  z lewą krawędzią heksu (antyaliasing litery zlewa się z linią), a pod napisem jest żeton (cień od y = 1679).
  Zakrycie = łaty rastrowe: piksele napisu (+3 px) zastąpione tym samym miejscem sąsiedniego heksu w rzędzie
  (przesunięcie (116,7; 0) px, dopasowane korelacją na czystej części linii; śr. błąd ≈ 1 poziom jasności) –
  linie heksu przy „R” i „r” odtworzone bez wcięcia; poza maską łaty przezroczyste (dwie łaty: „R”, „ear”).
  „Tył” ma wydłużenie dolne („y”), którego „Rear” nie ma,
  więc: 8,8 pt, linia bazowa 1672 (4 px wyżej), środek x = 329 (wierzchołek heksu x ≈ 330) – dobrane
  skryptem fit_tyl.py tak, by tekst był ≥ 2 px od linii heksu i od cienia żetonu.
s. 22 (diagram przy 8.13; grafika wektorowa): czarne „Flank” ×2 na heksach #c4c093 → „Skrzydło”, LSerif 700,
  7,0 pt (jak GBJC s. 24 – ten sam diagram), zakrycie "auto".
Współrzędne: px obrazu 200 dpi pełnego MediaBox (612×792 pt = 1700×2200 px).
Użycie: python3 spec_spqr.py [WYJŚCIE.json]   (domyślnie /home/claude/lay/custom/labels_SPQR_Deluxe_Rule_book_WEB.json)
Pliki robocze (pomiary): /home/claude/work/spqr_lab/scripts/ (measure.py, winchk.py, fit_tyl.py).
"""
import json, sys, io, base64
import numpy as np
import cv2
from PIL import Image
sys.path.insert(0, '/home/claude/lay')
import labels as LB  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/lay/custom/labels_SPQR_Deluxe_Rule_book_WEB.json'
ST = "font-family:LSerif;font-weight:700"
BLACK, RED = "#231f20", "#ed1c24"


def lab(win, x, y, t, en, color, fs, cover="auto"):
    return {"win": win, "x": x, "y": y, "t": t, "al": "c", "fs": fs, "st": ST, "color": color,
            "cover": cover, "en": en}


FS16 = 9.2
# (okno zakrycia, środek x napisu oryginału, linia bazowa)
FLANK16 = [([177, 1495, 250, 1522], 214.0, 1517),     # rząd 3, heks biały
           ([294, 1495, 367, 1522], 331.0, 1517),     # rząd 3, heks biały (obok żetonu Bal'ric)
           ([527, 1494, 600, 1521], 564.0, 1517),     # rząd 3, heks szary
           ([644, 1494, 717, 1521], 680.5, 1517),     # rząd 3, heks szary
           ([235, 1596, 308, 1623], 272.0, 1618),     # rząd 4
           ([586, 1595, 658, 1623], 622.5, 1618)]     # rząd 4
REAR16 = [([357, 1595, 421, 1623], 389.0, 1618),      # rząd 4
          ([473, 1595, 537, 1623], 506.0, 1618),      # rząd 4
          ([415, 1698, 479, 1724], 447.5, 1720),      # rząd 5
          ([533, 1698, 596, 1724], 564.5, 1720)]      # rząd 5
# „Rear” nad żetonem LG: łata rastrowa z sąsiedniego heksu (to samo położenie względem heksu)
BG = '/home/claude/lay/bg/SPQR_Deluxe_Rule_book_WEB.pdf'   # grafika diagramu identyczna jak w bazie (sprawdzone)
# Dwie łaty: „R” i „ear”. Prostokąty łat na siatce 25 px (= 12 px CSS = 9 pt) – poza nią Chromium dosuwa obraz do
# px CSS i rozciąga go o 1–2 % (kopia linii mija się wtedy z oryginałem o ok. 1 px). Styk napisu z linią heksu
# (lewa krawędź przy „R”, x ≈ 305; prawa przy „r”, x ≈ 360) leży blisko prawej krawędzi i środka wysokości łaty –
# tam pdftoppm (Splash, który poszerza obrazy o ok. 1 px w lewo/górę i w dół) przesuwa zawartość najmniej
# (≤ 0,3 px); pdftocairo – zgodnie co do piksela.
REGS = [(250, 1625, 325, 1700),     # „R” (x ≤ 324)
        (325, 1625, 375, 1700)]     # „ear”
TXT_Y1 = 1679                       # napis tylko w wierszach < 1679 (od 1679 cień i ramka żetonu LG – też czerwonawa)
SHIFT = (116.7, 0.0)                # wektor sieci heksów: sąsiad w tym samym rzędzie (na prawo)


def rear_top_patch(img, reg_box):
    x0, y0, x1, y1 = reg_box
    X0, Y0, X1, Y1 = x0 - 6, y0, x1 + 6, y1          # maska liczona z zapasem (dylatacja przez granicę łat)
    reg = img[Y0:Y1, X0:X1].astype(np.int32)
    red = ((reg[..., 0] - reg[..., 1]) > 25).astype(np.uint8)           # napis (czerwony + antyaliasing)
    red[TXT_Y1 - 2 - Y0:, :] = 0
    m = cv2.dilate(red, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))) > 0
    m[TXT_Y1 - Y0:, :] = False
    m = m[:, x0 - X0:x0 - X0 + (x1 - x0)]
    mx, my = np.meshgrid(np.arange(x0, x1) + SHIFT[0], np.arange(y0, y1) + SHIFT[1])
    src = cv2.remap(img.astype(np.float32), mx.astype(np.float32), my.astype(np.float32), cv2.INTER_LINEAR)
    rgba = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
    # w masce napisu kopia z sąsiedniego heksu, poza nią łata przezroczysta (widać oryginał – bez szwów na żetonie)
    rgba[..., :3] = np.where(m[..., None], np.clip(np.round(src), 0, 255), img[y0:y1, x0:x1]).astype(np.uint8)
    rgba[..., 3] = np.where(m, 255, 0)
    b = io.BytesIO()
    Image.fromarray(rgba, 'RGBA').save(b, 'PNG', optimize=True)
    return {"png": base64.b64encode(b.getvalue()).decode(), "x": x0, "y": y0,
            "note": f"„Rear” nad żetonem LG – w masce napisu kopia z przesunięcia {SHIFT} px, obszar {list(reg_box)}"}


IMG16 = LB.render_page(BG, 16)
PATCH16 = [rear_top_patch(IMG16, r) for r in REGS]

P16 = ([lab(w, x, y, "Skrzydło", "Flank", BLACK, FS16) for w, x, y in FLANK16]
       + [lab(w, x, y, "Tył", "Rear", RED, FS16) for w, x, y in REAR16]
       + [lab([303, 1657, 362, 1678], 329.0, 1672, "Tył", "Rear (nad żetonem LG)", RED, 8.8, cover="none")])

FS22 = 7.0
P22 = [lab([157, 923, 213, 943], 184.0, 940, "Skrzydło", "Flank", BLACK, FS22),
       lab([740, 923, 796, 943], 767.5, 940, "Skrzydło", "Flank", BLACK, FS22)]

spec = {"_uwagi": "SPQR_Deluxe_Rule_book_WEB s. 16 i 22: podpisy heksów Flank/Rear na diagramach "
                  "(generator patches_SPQR_Deluxe_Rule_book_WEB/spec_spqr.py); „Front” bez zmian",
        "pages": {"16": {"labels": P16, "patches": PATCH16}, "22": P22}}
json.dump(spec, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(OUT, len(P16) + len(P22), 'etykiet,', len(PATCH16), 'łaty')
