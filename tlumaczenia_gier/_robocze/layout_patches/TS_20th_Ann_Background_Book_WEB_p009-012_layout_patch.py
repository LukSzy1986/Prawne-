#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Background_Book_WEB, s. 9–12 (redaktor tb9_12, 2026-10-26)
# Przykład rozgrywki, Etap 2 (AR6) – Etap 3 (AR6). Idempotentny: każda strona startuje od stanu z unitize.
# Zasady stałe tej partii:
#  – podkreślenia (AR…, Influence placement, Realignment, Coup in Iraq, USSR/US Hand), ikony stron (sierp
#    i młot / gwiazda) i trójkąty ▶ są w TLE w miejscu oryginału: elementy przy nich muszą zaczynać jednostkę
#    (split) i stać na swojej linii bazowej; nagłówki AR / „Ręka …” – hdr (między ikonami, jak s. 5–8);
#  – jednostki zawężone w EN przez krótki tekst – szerokość łamu (x1 = prawa krawędź kolumny);
#  – dymki dialogów: szerokość tekstu do ramki tła (ramka − 6 pt);
#  – listy kart na ręce: lista przesunięta w lewo, wspólna skala wierszy, prawa granica = kolumna;
#  – odstępy między akapitami/punktami list zmniejszone (tekst PL dłuższy), gdy brak miejsca do ramki
#    dialogu (render liczy odstęp z linii bazowych: base akapitu − lastbase poprzedniego → setgap przesuwa
#    linie bazowe akapitu i wszystkich następnych).
import sys
sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Background_Book_WEB'
COL = {9: ((54.0, 304.43), (316.66, 567.0)), 11: ((54.0, 304.43), (316.66, 567.0)),
       10: ((45.0, 295.4), (307.66, 558.0)), 12: ((45.0, 295.4), (307.66, 558.0))}
BOX = {9: (308, 570), 11: (308, 570), 10: (299, 561), 12: (299, 561)}   # prawe krawędzie ramek dialogów


def col_right(p, u):
    l, r = COL[p]
    return l[1] if u['x0'] < 300 else r[1]


def cut(P, uid, i=0):
    """trójkąt ▶ z tła przed wierszem „Karta:”/„ZSRR:” – opływanie jak w pozostałych wierszach kart"""
    u = P.unit(uid)
    p = u['paras'][i]
    P.para(u, i, cuts=[{'side': 'l', 'top': round(p['base'] - 9.35, 2), 'bottom': round(p['base'] + 2.75, 2),
                        'w': 8.65}])


def widen(P, uid, r=None):
    u = P.unit(uid)
    r = r or col_right(P.page, u)
    P.set(u, x1=r, maxRight=max(u.get('maxRight', r), r))


def dialog(P, uid):
    """dymek łamany: szerokość tekstu do ramki z tła"""
    u = P.unit(uid)
    l, r = BOX[P.page]
    P.set(u, x1=(l if u['x0'] < 300 else r) - 6.0)


def setgap(P, uid, i, g):
    """odstęp linii bazowych między akapitem i-1 (ostatni wiersz) a akapitem i = g; akapity i… przesunięte"""
    u = P.unit(uid)
    ps = u['paras']
    d = round(ps[i - 1]['lastbase'] + g - ps[i]['base'], 2)
    if abs(d) < 0.005:
        return
    for p in ps[i:]:
        for k in ('base', 'lastbase', 'top', 'bottom'):
            p[k] = round(p[k] + d, 2)
    ps[i]['gap'] = g
    u['bottom'] = round(max(p['bottom'] for p in ps), 2)


def gaps(P, uid, g, minold=16.5, idx=None):
    """odstępy przed akapitami (punktami listy) ≥ minold (17,7 pt w EN) -> g"""
    u = P.unit(uid)
    for i in range(1, len(u['paras'])):
        old = u['paras'][i]['base'] - u['paras'][i - 1]['lastbase']
        if (idx is None and old >= minold) or (idx is not None and i in idx):
            setgap(P, uid, i, g)


def handlist(P, uid, dx, right):
    """lista ◊ tytułów kart: przesunięcie w lewo o dx, prawa granica = kolumna, wspólna skala"""
    u = P.unit(uid)
    for i, ln in enumerate(u['lines']):
        P.line(u, i, x0=round(ln['x0'] - dx, 2), x1=round(ln['x1'] - dx, 2),
               maxLeft=round(ln.get('maxLeft', ln['x0']) - dx, 2),
               maxRight=round(ln['x0'] - dx + 12.5, 2) if ln['en'] == '◊' else right)
    P.set(u, x0=round(u['x0'] - dx, 2), same_scale=True, maxRight=right)



# QA 26.10 (kontrola wizualna qb1_24): nagłówki AR/„Ręka …” jak na s. 5–8 (hdr), podkreślenia z tła zakryte
# białymi łatkami (whiteouts, twarde spacje na białym tle) i składane <u> pod polskim tekstem; tekst nad ramkami
# dialogów co najmniej 4 pt nad ramką (clear_boxes).

# linie podkreśleń w tle (x0, x1, y osi linii; grubość 0,55 pt) – z bg/…pdf (pdfplumber)
ULINES = {
    9: [(69.58, 121.84, 86.44), (69.58, 110.12, 315.04), (54.00, 139.14, 350.44), (329.56, 379.45, 612.50)],
    10: [(57.91, 96.08, 83.77), (60.58, 112.84, 529.57), (60.58, 101.12, 675.27), (45.00, 130.14, 710.67),
         (323.23, 375.49, 161.54), (323.23, 363.78, 376.24), (307.66, 361.74, 411.64)],
    11: [(69.58, 121.84, 120.14), (69.58, 110.12, 343.74), (332.23, 384.49, 216.90), (316.66, 401.79, 252.30),
         (332.23, 372.78, 514.40), (316.66, 369.69, 549.80)],
    12: [(60.58, 112.84, 209.30), (60.58, 101.12, 358.90), (45.00, 130.14, 394.30), (323.23, 375.49, 86.44),
         (307.66, 392.79, 121.84), (323.23, 363.78, 341.54)],
}
# ikony stron przy nagłówkach (prawa krawędź lewej ikony, lewa krawędź prawej) – z bg/…pdf
ICONS = {
    9: {'u2': (67.3, 124.0), 'u5': (67.3, 112.3), 'u27': (327.3, 381.6)},
    10: {'u2': (55.7, 98.3), 'u14': (58.3, 115.0), 'u17': (58.3, 103.3), 'u21': (321.0, 377.6), 'u27': (321.0, 365.9)},
    11: {'u3': (67.3, 124.0), 'u7': (67.3, 112.3), 'u16': (330.0, 386.6), 'u19': (330.0, 374.9)},
    12: {'u5': (58.3, 115.0), 'u9': (58.3, 103.3), 'u16': (321.0, 377.6), 'u20': (321.0, 365.9)},
}
# ramki dialogów w tle (x0, x1, y0, y1) – z bgimg
BOXES = {
    9: [(50, 308, 244, 282), (50, 308, 392, 409), (50, 308, 412, 429), (312, 570, 500, 517), (312, 570, 520, 537)],
    10: [(41, 299, 212, 229), (41, 299, 249, 266), (41, 299, 376, 393), (41, 299, 458, 486), (41, 299, 612, 639),
         (303, 561, 109, 126), (303, 561, 293, 310), (303, 561, 313, 340), (303, 561, 719, 747)],
    11: [(50, 308, 68, 84), (50, 308, 261, 288), (50, 308, 291, 308), (312, 570, 123, 151), (312, 570, 154, 181),
         (312, 570, 462, 479)],
    12: [(41, 299, 137, 154), (41, 299, 157, 174), (41, 299, 287, 303), (41, 299, 306, 323), (41, 299, 578, 595),
         (41, 299, 598, 615), (303, 561, 248, 275), (303, 561, 278, 306), (303, 561, 434, 462), (303, 561, 465, 492)],
}
BOX_COLORS = ('#f2d4cd', '#cbdcec')


def hdr(P, uid, us=False, gap_l=1.8, gap_r=None, hs=None):
    """nagłówek „ARn (…)”/„Ręka …” między ikonami z tła (jak hdr w łatce s. 5–8): od ikony lewej + gap_l do
    ikony prawej − gap_r, jeden wiersz, 11 pt, osobna skala; „(USA)” dłuższe od „(US)” – hs 0,92"""
    il, ir = ICONS[P.page][uid]
    if gap_r is None:
        gap_r = 2.4 if us else 1.8
    if hs is None:
        hs = 0.92 if us else 0.96
    u = P.unit(uid)
    p = u['paras'][0]
    x0, r = round(il + gap_l, 2), round(ir - gap_r, 2)
    u.update(x0=x0, maxLeft=x0, x1=r, maxRight=r, nowrap=True, body=False)
    p.update(left=0.0, right=0.0, hang=0.0, indent=0.0, x0=x0, hs=hs)
    p.pop('cuts', None)
    p.pop('ls', None)


def whiteouts(P):
    """białe prostokąty na liniach podkreśleń z tła (jak łatka s. 5–8): jednostka lines z twardymi spacjami
    podświetlonymi na biało, na początku listy (pod tekstem); szerokość linii + 0,5 pt z każdej strony.
    Wywoływać PO wszystkich split (id u901…)."""
    for k, (x0, x1, y) in enumerate(ULINES[P.page]):
        a, b = x0 - 0.5, x1 + 0.5
        w = b - a
        NB = 0.2275                       # szerokość twardej spacji w LSerifCn (em)
        n = max(1, round(w / (NB * 3.0)))
        size = round(w / (n * NB), 3)
        base = round(y + 0.45 * size / 3.0 + 0.05, 2)
        ln = {'en': '\u00a0' * n, 'font': 'MinionPro-Cn', 'size': size, 'color': '#ffffff', 'x0': a, 'x1': b,
              'top': round(y - 2, 2), 'bottom': round(y + 1.5, 2), 'base': base, 'rot': 0, 'bg': '#ffffff',
              'maxRight': b, 'maxLeft': a, 'align': 'left', 'hl': '#ffffff'}
        P.lay['units'].insert(k, {'id': f'u{901 + k}', 'kind': 'lines', 'x0': a, 'top': ln['top'], 'x1': b,
                                  'bottom': ln['bottom'], 'maxBottom': ln['bottom'], 'maxRight': b, 'maxLeft': a,
                                  'bg': '#ffffff', 'fixscale': 1.0, 'lines': [ln]})


def clear_boxes(P, gap=4.0):
    """jednostki tekstu nad ramką dialogu: dół najwyżej gap pt nad górną krawędzią ramki (w oryginale ok. 5,5 pt)"""
    for u in P.lay['units']:
        if u['kind'] != 'flow' or u.get('bg') in BOX_COLORS or u.get('role'):
            continue
        mb = u.get('maxBottom', u['bottom'])
        for (bx0, bx1, by0, by1) in BOXES[P.page]:
            if bx0 - 10 <= u['x0'] <= bx1 and mb - 3 <= by0 <= mb + 3:
                u['maxBottom'] = round(min(mb, by0 - gap), 2)


# ------------------------------------------------------------------ s. 9
P = Patch(D, 9); P.restore()
widen(P, 'u5'); widen(P, 'u6'); widen(P, 'u9')
# AR6 (ZSRR): wiersz karty 2 wiersze, akapity kursywą o wiersz dłuższe – mniejsze odstępy
setgap(P, 'u3', 1, 13.5); setgap(P, 'u3', 2, 14.0)
for i in (3, 4, 5):
    setgap(P, 'u3', i, 13.5)
setgap(P, 'u3', 6, 12.5)
dialog(P, 'u4')
P.split('u6', 1)                                     # -> u26: „Poszerzanie Strefy Wpływów…” na podkreśleniu z tła
setgap(P, 'u20', 1, 12.5)                            # „Jack długo…” – akapit DEFCON ma 4 wiersze
P.split('u23', 2)                                    # -> u27: „Ręka ZSRR” między ikonami
handlist(P, 'u24', 26.0, 567.0)
P.split('u9', 1)                                     # -> u28: „KONIEC ETAPU DRUGIEGO (END OF TURN TWO)” – osobna jednostka
P.set('u9', nowrap=True, body=False)                 #    jednowierszowa (z EN jak s. 5; skala własna ok. 0,96)
for uid in ICONS[9]:
    hdr(P, uid, us=(uid == 'u5'))
for uid in ('u7', 'u8', 'u22'):
    P.para(uid, 0, hs=0.94)                          # QA r3: dialogi jednowierszowe w 9 pt (tracking zamiast skali)
clear_boxes(P)
whiteouts(P)
P.save()

# ------------------------------------------------------------------ s. 10
P = Patch(D, 10); P.restore()
handlist(P, 'u3', 26.0, 295.4)
P.split('u8', 1)                                     # -> u35: „▶ USA: Rezolucja formozańska…” przy trójkącie
P.set('u8', nowrap=True)                             # „FAZA WYDARZEŃ KLUCZOWYCH (HEADLINE PHASE)” w 1 wierszu (jak s. 3, 6)
setgap(P, 'u35', 1, 12.0); setgap(P, 'u35', 2, 11.5)  # akapit o Tajwanie
cut(P, 'u10'); cut(P, 'u28')
P.para('u28', 0, ls=-0.01)                           # wiersz karty Interwencji ONZ w 1 wierszu (nad „Wywieranie Presji” z tła)
for uid in ('u12', 'u16', 'u19', 'u26', 'u33'):
    dialog(P, uid)
widen(P, 'u17'); widen(P, 'u18'); widen(P, 'u27'); widen(P, 'u28')
P.split('u18', 1)                                    # -> u36: „Poszerzanie Strefy Wpływów…” na podkreśleniu z tła
P.para('u36', 1, ls=-0.02)                           # „Tajlandia (Thailand): (3/1) Kontrola USA (US Control)” w 1 wierszu
P.para('u22', 0, pitch=12.0); setgap(P, 'u22', 1, 12.5)    # wiersz karty Igrzysk – 2 wiersze
P.line('u23', 0, base=226.6); P.set('u22', maxBottom=217.8)   # „Rzuty:” 3,5 pt niżej (akapit nad nim dłuższy),
P.move_to('u24', base=241.1)                         # wyniki rzutów za nim; punkty listy 17,7 -> 16 pt
setgap(P, 'u24', 2, 16.0); setgap(P, 'u24', 3, 16.0)
setgap(P, 'u11', 1, 13.0)                            # Pojmany naukowiec: odstęp nad ramką CHRUSZCZOW
setgap(P, 'u15', 1, 14.0); setgap(P, 'u15', 2, 15.0); setgap(P, 'u15', 3, 13.0)
# modyfikatory Wywierania Presji (akapit 0 i punkt „Żadna ze stron…” – po 2 wiersze): odstępy ok. 15,7 pt, żeby
# „ZSRR: +1” stał jak w oryginale (y ≈ 597) nad „Rzuty:” (QA r3: było 33 pt luki); punkty p2 i p5 lekko ścieśnione
for i in range(1, 7):
    setgap(P, 'u30', i, 15.7)
setgap(P, 'u30', 7, 15.5); setgap(P, 'u30', 8, 15.5)
P.para('u30', 2, hs=0.97); P.para('u30', 5, hs=0.97)
for uid in ICONS[10]:
    hdr(P, uid, us=uid in ('u17', 'u27'))
hdr(P, 'u2', gap_l=2.5, gap_r=2.5, hs=0.92)           # „Ręka USA”: odstępy od gwiazd jak na s. 6 (QA: gwiazda dotykała „R”)
for uid, hs in (('u5', 0.97), ('u7', 0.94), ('u20', 0.96)):
    P.para(uid, 0, hs=hs)                            # QA r3: dialogi jednowierszowe w 9 pt
clear_boxes(P)
whiteouts(P)
P.save()

# ------------------------------------------------------------------ s. 11
P = Patch(D, 11); P.restore()
gaps(P, 'u4', 14.0)
for uid in ('u5', 'u14', 'u15'):
    dialog(P, uid)
gaps(P, 'u8', 15.5)
P.para('u8', 3, ls=-0.02)                            # „Korea Południowa (South Korea) – Państwo Strategiczne” w 1 wierszu
widen(P, 'u12')
P.para('u10', 3, ls=-0.02); P.para('u10', 8, ls=-0.02)   # „Państwa sąsiadujące z supermocarstwem przeciwnika = 0” w 1 wierszu
P.split('u17', 1)                                    # -> u21: „Poszerzanie Strefy Wpływów…” na podkreśleniu z tła
gaps(P, 'u21', 13.5, minold=15.0)
# AR4 (USA): nagłówek, wiersz karty i „Przewrót w Iraku” – każdy przy swojej grafice tła
P.split('u19', 1)                                    # -> u22: wiersz karty
P.split('u22', 1)                                    # -> u23: „Przewrót w Iraku (Coup in Iraq)” i dalej
gaps(P, 'u23', 16.0, minold=16.5)
for uid in ICONS[11]:
    hdr(P, uid, us=uid in ('u7', 'u19'))
P.para('u18', 0, hs=0.94)                            # QA r3: dialog jednowierszowy w 9 pt
clear_boxes(P)
whiteouts(P)
P.save()

# ------------------------------------------------------------------ s. 12
P = Patch(D, 12); P.restore()
P.set('u2', nowrap=False)                            # akapit „Kryzys sueski … usunięte z gry.” łamany
gaps(P, 'u2', 13.5, minold=14.0)
widen(P, 'u5'); widen(P, 'u6'); widen(P, 'u20'); widen(P, 'u21', 558.5); widen(P, 'u23')
gaps(P, 'u6', 13.0)
P.set('u6', body=False)                              # AR5 (ZSRR): akapity między grafiką tła – własna skala
P.split('u10', 1)                                    # -> u27: „Poszerzanie Strefy Wpływów…” na podkreśleniu z tła
P.move_to('u13', base=487.9)
gaps(P, 'u13', 13.0)
P.split('u17', 1)                                    # -> u28: „Poszerzanie Strefy Wpływów…” na podkreśleniu z tła
# AR6 (USA): wiersz karty z EN – 2 wiersze; punkty listy (u21 p2, u22, u23) równo co 14,2 pt
setgap(P, 'u21', 1, 13.0); setgap(P, 'u21', 2, 13.0)
P.para('u21', 2, ls=-0.02)                           # „Niemcy Wschodnie (E. Germany): (0/4) Kontrola ZSRR” w 1 wierszu
P.line('u22', 0, base=411.5); P.line('u22', 1, base=411.5, maxRight=558.0)
P.move_to('u23', base=425.7)
for uid in ('u18', 'u19', 'u24', 'u25'):
    dialog(P, uid)
for uid in ICONS[12]:
    hdr(P, uid, us=uid in ('u9', 'u20'))
P.para('u3', 0, hs=0.94); P.para('u4', 0, hs=0.96)   # QA r3: dialogi jednowierszowe w 9 pt
clear_boxes(P)
whiteouts(P)
P.save()
