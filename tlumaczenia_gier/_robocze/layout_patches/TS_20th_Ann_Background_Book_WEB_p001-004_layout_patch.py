#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Background_Book_WEB, s. 1–4 (redaktor tb1_4, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import copy
import sys
sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Background_Book_WEB'

# Krój Veneer (tytuł okładki, nagłówki przykładu, żywa pagina, numery stron) nie ma odwzorowania w laylib
# (fallback LSerif – szeroki krój szeryfowy; polskie nagłówki nie mieściły się w miejscu oryginału).
# Zastępnik najbliższy wyglądem: wąski pogrubiony bezszeryfowy (HerosCnN bold – jak MyriadPro-BlackCond).
VENEER_SUB = 'MyriadPro-BlackCond'


def veneer(P):
    for u in P.lay['units']:
        for it in (u.get('paras') or u.get('lines') or []):
            if str(it.get('font', '')).startswith('Veneer'):
                it['font'] = VENEER_SUB


def nocuts(P, u):
    for p in P._u(u)['paras']:
        p.pop('cuts', None)


def icon_head(P, uid, x_text, x_icon, hs=None):
    """nagłówek z ikonami po obu stronach (ikony i podkreślenie w tle – bez <u> w trans): tekst od x_text,
    jeden wiersz, własna skala, nie dalej niż do prawej ikony (hs – lekkie zwężenie odstępów liter)"""
    u = P._u(uid)
    nocuts(P, u)
    P.para(u, 0, left=round(x_text - u['x0'], 2), indent=0.0, hang=0.0)
    if hs:
        P.para(u, 0, hs=hs)
    P.set(u, nowrap=True, body=False, x1=x_icon, maxRight=x_icon)


def bullets(P, uid, x_bullet, hang=13.5):
    """punktory: znak „•” w miejscu oryginału, ciąg dalszy akapitu z wcięciem wiszącym"""
    u = P._u(uid)
    nocuts(P, u)
    for i, p in enumerate(u['paras']):
        if p['en'].lstrip().startswith('•') or '>•' in p['en']:
            P.para(u, i, left=round(x_bullet - u['x0'], 2), hang=hang, indent=0.0)


def gaps(P, u, values):
    """odstępy między akapitami (linia bazowa akapitu i względem ostatniej linii bazowej akapitu i-1,
    przy skali 1) – values[k] dla akapitu k+1"""
    u = P._u(u)
    ps = u['paras']
    for k, g in enumerate(values, start=1):
        n = ps[k]['nlines']
        d = ps[k]['lastbase'] - ps[k]['base'] if n > 1 else 0.0
        ps[k]['base'] = round(ps[k - 1]['lastbase'] + g, 2)
        ps[k]['lastbase'] = round(ps[k]['base'] + d, 2)
        ps[k]['gap'] = g


# ---------------------------------------------------------------- s. 1 – okładka
P = Patch(D, 1); P.restore()
veneer(P)
# spis treści (QA r3): kropki wiodące z tła (okrągłe, Myriad, y 464,6 … 584,6) zakryte jednostką-zakrywką
# (pierwsza w kolejności składu – tekst spisu leży nad nią); wszystkie kropki składa trans (krój Schola – okrągła
# kropka 1,5 pt, podziałka 3,34 pt jak w tle, koniec przy x ≈ 419,5); pozycje co 23 pt, 2-wierszowa pozycja 3
# z interlinią 14 pt (y 464,6 / 487,6 / 510,6–524,6 / 547,6 / 570,6 / 593,6; ramka spisu do y ≈ 625)
TOC_Y = [464.61, 487.6, 524.6, 547.6, 570.6, 593.6]
P.line('u1', 0, maxRight=421.0)
for uid in ('u2', 'u4', 'u6'):
    P.set(uid, maxRight=421.0)
P.move_to('u2', base=TOC_Y[1])
P.set('u3', maxRight=421.8, maxBottom=528.0)
P.para('u3', 0, base=510.6, lastbase=524.6, pitch=14.0, nlines=2)
P.move_to('u3', base=510.6)
P.move_to('u4', base=TOC_Y[3])
P.line('u5', 0, maxRight=421.0, base=TOC_Y[4])
P.move_to('u6', base=TOC_Y[5])
for i, y in enumerate(TOC_Y):
    P.line('u9', i, base=y)
ids = [int(x['id'][1:]) for x in P.lay['units'] if x['id'][1:].isdigit()]
cov = {'id': f'u{max(ids) + 1}', 'kind': 'lines', 'x0': 221.0, 'top': 450.0, 'x1': 421.0, 'bottom': 588.0,
       'maxBottom': 588.0, 'maxRight': 424.0, 'maxLeft': 221.0,
       'lines': [{'en': '[zakrycie kropek wiodących z tła]', 'font': 'MyriadPro-Cond', 'size': 12.0,
                  'color': '#231f20', 'x0': 221.0, 'x1': 421.0, 'top': round(y - 12, 2), 'bottom': round(y + 3, 2),
                  'base': y, 'rot': 0, 'bg': '#f7e1c8', 'maxRight': 424.0, 'maxLeft': 221.0, 'align': 'left'}
                 for y in (464.61, 488.61, 512.61, 536.61, 560.61, 584.61)]}
P.lay['units'].insert(0, cov)
# tytuł: „KSIĘGA TŁA HISTORYCZNEGO” + drugi, mniejszy wiersz „(BACKGROUND BOOK)” (glosariusz TS 4.4)
u = P.unit('u7')
P.para(u, 0, size=46.0, pitch=50.0, base=367.0, lastbase=367.0, top=334.0, bottom=380.0)
# qa_pagina_patch.py (orkiestrator) rozpoznaje żywą paginę po tekście EN „BACKGROUND BOOK” i zmniejsza ją do 14,5 pt –
# tytuł okładki ma ten sam tekst EN, więc w layout spacja twarda (tekst EN bez zmian w treści), żeby go nie dotknęła
P.para(u, 0, en='BACKGROUND\u00a0BOOK')
p1 = copy.deepcopy(u['paras'][0])
p1.update({'en': '[(BACKGROUND BOOK) – drugi wiersz tytułu w przekładzie]', 'size': 17.0, 'pitch': 20.0,
           'base': 393.0, 'lastbase': 393.0, 'top': 380.0, 'bottom': 397.0, 'gap': 26.0})
u['paras'].append(p1)
P.set(u, maxBottom=401.0)
P.save()

# ---------------------------------------------------------------- s. 2
P = Patch(D, 2); P.restore()
veneer(P)
P.set('u3', maxBottom=385.6, body=False)          # (QA r3) ostatnia linia bazowa ≤ ok. 383 (jak w oryginale; ramka do y = 395,8)
P.set('u3', fixscale=0.955)                        # (QA r3) skala z najrówniejszym łamaniem (rozstrzelenie ≤ 0,45 em)
icon_head(P, 'u6', 58.0, 161.6, hs=0.96)           # Wpływy początkowe ZSRR (ikony 45–55,5 i od 163,5)
icon_head(P, 'u9', 58.0, 149.4, hs=0.94)           # Wpływy początkowe USA (podkreślenie do 149,5, ikona od 151,8)
icon_head(P, 'u16', 356.5, 406.8)                  # Ręka ZSRR (prawa ikona od 408,5)
icon_head(P, 'u18', 356.5, 394.4, hs=0.95)         # Ręka USA (podkreślenie do 394,5, ikona od 396,8)
for uid in ('u7', 'u8', 'u10'):
    bullets(P, uid, 58.5)
P.merge('u7', 'u8')                                # (QA 26.10) lista Wpływów ZSRR – równe odstępy
P.set('u7', x1=299.5, maxRight=299.5)
P.set('u11', x1=558.45)                            # punktory prawej łamy – pełna szerokość łamu
P.set('u13', maxRight=553.0)                       # cytaty: do prawego marginesu ramki (562,2 − 9)
P.set('u14', x1=553.0, maxRight=553.0)
# karty na rękach: kolumna ◊ i tytułów przesunięta w lewo o 15,7 pt (tytuły PL + EN dłuższe od EN)
for uid in ('u17', 'u19'):
    u = P.unit(uid)
    for i, ln in enumerate(u['lines']):
        if ln['en'] == '◊':
            P.line(u, i, x0=337.0, x1=342.32, maxLeft=330.0, maxRight=349.0)
        else:
            w = ln['x1'] - ln['x0']
            P.line(u, i, x0=354.0, x1=round(354.0 + w, 2), maxLeft=350.0, maxRight=562.0)
# nota „Od redakcji” (glosariusz TS 9.2, K.1) – wolne miejsce pod listą „Ręka USA” (prawa łama)
ids = [int(x['id'][1:]) for x in P.lay['units'] if x['id'][1:].isdigit()]
nid = f'u{max(ids) + 1}'
note = {'id': nid, 'kind': 'flow', 'x0': 307.66, 'top': 676.0, 'x1': 558.45, 'bottom': 748.0, 'base': 683.0,
        'maxBottom': 749.0, 'maxRight': 558.45, 'maxLeft': 307.16, 'bg': '#ffffff', 'body': False,
        'nowrap': False,
        'paras': [{'en': '[nota „Od redakcji” – brak w oryginale]', 'font': 'MinionPro-CnIt', 'size': 9.0,
                   'color': '#231f20', 'align': 'justify', 'pitch': 10.6, 'nlines': 7, 'left': 0.0,
                   'right': 0.0, 'indent': 0.0, 'hang': 0.0, 'top': 676.0, 'bottom': 748.0, 'base': 683.0,
                   'lastbase': 746.6, 'x0': 307.66, 'x1': 558.45, 'bg': '#ffffff', 'gap': None}]}
P.lay['units'].append(note)
P.save()

# ---------------------------------------------------------------- s. 3
P = Patch(D, 3); P.restore()
veneer(P)
# podpis mapy: krój MinionPro-CnItCapt laylib składa prosto (nie rozpoznaje kursywy) – kursywa jak w oryginale;
# pod mapą wolne miejsce w prawo
P.para('u9', 0, font='MinionPro-CnIt')
P.set('u9', maxRight=420.0)
u10 = P.unit('u10')                                # FAZA WYDARZEŃ KLUCZOWYCH / ZSRR: … / zdanie kursywą
a = P.split(u10, 1)                                # każdy wiersz z własną skalą (jednowierszowe)
b = P.split(a, 1)
nocuts(P, a)
P.para(a, 0, left=8.65)                            # trójkąt (tło) przed „ZSRR:”
P.set(a, maxRight=305.0)
P.set(b, maxRight=308.0)                           # do prawej krawędzi ramki cytatu poniżej
P.set('u11', maxRight=302.0)                       # cytaty: ramki x 49,5–308,5
P.set('u13', maxRight=302.0)
P.para('u11', 0, hs=0.945)                         # (QA r3) jednowierszowe dialogi w 9 pt (lekkie zwężenie liter)
P.para('u13', 0, hs=0.96)
u12 = P.unit('u12')                                # USA: Nadzwyczajne relacje … | zdanie + punktor
nocuts(P, u12)
P.para(u12, 0, left=8.65)                          # trójkąt przed „USA:”
c = P.split(u12, 1)                                # zdanie (3 wiersze po polsku) i punktor – własna skala
P.move_to(c, base=638.0)
gaps(P, c, [13.0])
P.set(c, maxBottom=672.1)                          # (QA 26.10) ok. 5,5 pt nad niebieską ramką (od y = 677,5)
P.save()

# ---------------------------------------------------------------- s. 4
P = Patch(D, 4); P.restore()
veneer(P)
# nagłówki AR z ikonami (ikony i podkreślenia w tle)
# (tekst kończy się najdalej z końcem podkreślenia z tła; prawe ikony 2,3 pt dalej)
icon_head(P, 'u3', 60.5, 112.6)
icon_head(P, 'u15', 60.5, 100.9, hs=0.95)
icon_head(P, 'u18', 323.2, 375.3)
icon_head(P, 'u21', 323.2, 363.6, hs=0.95)
icon_head(P, 'u24', 323.2, 375.3)
u27 = P.unit('u27')
rest = P.split(u27, 1)                             # AR3 (USA) | Karta: Doktryna Trumana …
icon_head(P, u27, 323.2, 363.6, hs=0.95)
# wiersze „Karta:” za trójkątem z tła
u4 = P.unit('u4')
P.set(u4, x1=295.43, nowrap=True, body=False)
P.para(u4, 0, left=8.65)
# AR1 (USA): Karta | opis NORAD (5 wierszy po polsku – własna skala, od y = 601,3)
u16 = P.unit('u16')
nocuts(P, u16)
P.para(u16, 0, left=8.65)
n16 = P.split(u16, 1)
P.set(u16, nowrap=True, body=False)
P.move_to(n16, base=600.2)
P.para(n16, 0, pitch=10.7)                         # interlinia −2,7%
P.set(n16, maxBottom=639.4)                        # (QA 26.10) ok. 5 pt nad niebieską ramką (od y = 644,2)
# AR2 (ZSRR): Karta | Poszerzanie Strefy Wpływów + punktory (podkreślenie nagłówka w tle – w miejscu oryginału)
u19 = P.unit('u19')
nocuts(P, u19)
P.para(u19, 0, left=8.65)
n19 = P.split(u19, 1)
for x in (u19, n19):
    P.set(x, x1=558.39, body=False)
P.set(u19, nowrap=True)
# podkreślenie z tła (y = bazowa + 0,84…1,32) leży wyżej niż podkreślenie <u> tekstu (bazowa + 1,33…2,0) –
# linia bazowa nagłówka o 0,5 pt wyżej, żeby obie kreski się pokrywały (polski nagłówek dłuższy od kreski z tła)
P.move_to(n19, base=120.25)
# AR2 (USA): Karta w dwóch wierszach (10 pt, interlinia 10,6) | Poszerzanie Strefy Wpływów + punktor
u22 = P.unit('u22')
n22 = P.split(u22, 1)
# (QA r3) oba wiersze 10 pt (bez zmniejszenia), 2. wiersz wcięty pod tekst po „Karta: ” (wariant całego Przykładu),
# ok. 3,5 pt odstępu nad nagłówkiem „Poszerzanie…” (nagłówek na kresce z tła – nie przesuwa się)
P.set(u22, nowrap=False, maxBottom=268.2)
P.para(u22, 0, pitch=10.2, nlines=2, hang=25.0, hs=0.97)
P.move_to(u22, base=255.4)
P.para(u22, 0, lastbase=265.6)
P.move_to(n22, base=278.55)                        # jak wyżej (podkreślenie z tła)
# AR3 (ZSRR): Karta (2 wiersze) + zdanie + 2 punktory – ciaśniejsze odstępy, własna skala
u25 = P.unit('u25')
nocuts(P, u25)
P.para(u25, 0, left=8.65, nlines=2, pitch=12.8, lastbase=397.04)
gaps(P, u25, [14.0, 15.5, 15.5])
P.set(u25, x1=558.39, body=False, maxBottom=437.6)  # (QA 26.10) ok. 5 pt nad różową ramką (od y = 442,8)
P.set(u25, fixscale=0.87)                          # (QA r3) skala stała – wcięcie 2. wiersza „Karta:” pod tekst po „Karta: ”
P.para(u25, 0, hang=round(27.5 * 0.87, 2))
# AR3 (USA): Karta | zdanie (2 wiersze) + punktor + zdanie – własna skala
nocuts(P, rest)
P.para(rest, 0, left=8.65)
n31 = P.split(rest, 1)
P.set(rest, nowrap=True)
P.set(n31, nowrap=False, x1=558.4, maxBottom=560.8)  # ok. 5 pt nad niebieską ramką (od y = 565,5)
P.move_to(n31, base=524.2)
gaps(P, n31, [15.5, 12.5])
# cytaty
P.set('u13', maxRight=294.0)
P.set('u14', x1=294.0, maxRight=294.0)
P.set('u17', maxRight=295.5)
P.para('u17', 0, hs=0.97)                          # (QA r3) dialog w 9 pt
for uid in ('u20', 'u23', 'u28', 'u29'):
    P.set(uid, x1=553.0, maxRight=553.0)
P.set('u26', maxRight=553.0)
# ramka „Przewrót w Iranie”: biała ramka x 55–184,5; wiersze wyśrodkowane jak w oryginale
for uid in ('u7', 'u10', 'u12'):
    u = P.unit(uid)
    P.set(u, x0=57.5, x1=182.5, maxLeft=57.5, maxRight=182.5)
    for i in range(len(u['paras'])):
        P.para(u, i, left=0.0, align='center')
u10 = P.unit('u10')                                # „Siła Przewrotu (Coup strength)” w 2 wierszach | „Iran: …”
n10 = P.split(u10, 1)
P.para(u10, 0, pitch=12.0, nlines=2)
P.move_to(u10, base=240.0)
P.para(u10, 0, lastbase=252.0)
P.set(u10, maxBottom=255.0)
P.move_to(n10, base=266.8)
u8 = P.unit('u8')                                  # „Rzut kością:” – kończy się przed kością (tło, x ≈ 130)
P.set(u8, x0=57.5, x1=127.5, maxLeft=57.5, maxRight=127.5)
P.para(u8, 0, left=0.0, align='right')
P.line('u11', 0, align='right', x1=130.6, maxLeft=60.0)   # „DEFCON: 5” przed strzałką (tło, x ≈ 132)
# „Poziom Stabilizacji (Stability Number)” – kończy się przy linii odnośnika (x ≈ 257)
P.line('u6', 0, align='right', x0=150.0, x1=255.5, maxLeft=60.0, maxRight=255.5)
P.save()

# ================================================================ 30.10 nawiasy kart (bb_karta)
# Decyzja użytkownika 30.10: brakujące nawiasy EN (lista ZAWSZE, tytuły kart) – łatki z dodatkowym wierszem.
# Blok NIE woła restore(): startuje od stanu po łatkach strony powyżej (cały plik jest idempotentny).

# ---- s. 4
P = Patch(D, 4)
# ramka „Przewrót w Iranie” (biała, y 189–312): „Iran: 0/2 (Kontrola ZSRR, USSR Control)” i „Operacje Wojskowe
# ZSRR (USSR Military Ops): 3” w dwóch wierszach; „Rzut kością” (kość z tła) i „DEFCON: 5 → 4” (strzałka z tła)
# zostają na swoich liniach bazowych – „Siła Przewrotu” i „Iran” ścieśnione między nimi (10–10,5 pt, interlinia 10–10,2)
u10 = P.unit('u10')
P.para(u10, 0, size=10.5, pitch=10.2)
P.move_to(u10, base=238.4)
P.para(u10, 0, lastbase=248.6)
P.set(u10, maxBottom=251.5)
u36 = P.unit('u36')
P.para(u36, 0, size=10.0, pitch=10.0, nlines=2)
P.move_to(u36, base=260.6)
P.para(u36, 0, lastbase=270.6)
P.set(u36, maxBottom=272.5)
u12 = P.unit('u12')
P.para(u12, 0, size=10.0, pitch=10.2, nlines=2)
P.move_to(u12, base=295.3)
P.para(u12, 0, lastbase=305.5)
P.set(u12, maxBottom=308.6)                        # ≥ 3 pt nad dolną krawędzią białej ramki (y = 312)
# AR3 (ZSRR): „Karta: … (Arab‑Israeli War, Wydarzenie ZSRR)” w jednym wierszu (nowrap, lekkie zwężenie liter),
# zdanie z „(US Controlled)” w dwóch wierszach + 2 punktory – osobna jednostka (własna skala), 5 pt nad ramką
u25 = P.unit('u25')
if len(u25['paras']) > 1:
    n25 = P.split(u25, 1)                          # nowa jednostka u37
else:
    n25 = P.unit('u37')
u25.pop('fixscale', None)
P.para(u25, 0, nlines=1, lastbase=u25['paras'][0]['base'], hang=0.0, hs=0.95)
P.set(u25, nowrap=True, maxRight=561.0, maxBottom=388.0)
n25.pop('fixscale', None)
P.set(n25, nowrap=False, body=False, maxBottom=437.6)
P.move_to(n25, base=397.6)
P.para(n25, 0, nlines=2, pitch=10.6, lastbase=408.2, align='justify')
P.para(n25, 1, base=421.6, lastbase=421.6, gap=13.4)
P.para(n25, 2, base=434.4, lastbase=434.4, gap=12.8)
P.save()

# ---- s. 3
P = Patch(D, 3)
# faza Wydarzeń Kluczowych: „W tym Etapie (this turn) wszystkie karty USA mają −1 do Operacji (Operations, min. 1).”
# w 2 wierszach (ramka dialogu CHRUSZCZOW z tła od y = 592,2 – nie przesuwa się). Nagłówek i wiersz „ZSRR: …”
# 11 pt wyżej (pod podpisem mapy było ok. 30 pt wolnego miejsca). Trójkąt ▶ z tła (x 54–60, y 563–573, #231f20)
# zakryty białą łatką u950 (twarde spacje podświetlone na biało, pod tekstem); nowy trójkąt 11 pt wyżej – u951:
# dwa trójkąty prostokątne ◣ + ◤ (DejaVu Sans, 7,2 pt: ok. 5,3 × 5,2 pt każdy; zmierzone w składzie (1200 dpi):
# szerokość i wysokość ok. 0,73·stopnia, góra 0,616·stopnia nad linią bazową) złożone w trójkąt ok. 5,3 × 10,4 pt
# (w tle 6,2 × 10,1 pt; pojedynczy znak ▶ jest kwadratowy – wyraźnie szerszy od trójkątów tła na tej stronie).
DY3 = 11.0
P.move_to('u10', base=round(559.18 - DY3, 2))
P.set('u10', maxBottom=round(564.34 - DY3, 2))
u20 = P.unit('u20')
P.move_to(u20, base=round(572.38 - DY3, 2))
P.set(u20, maxBottom=round(580.48 - DY3, 2))
u21 = P.unit('u21')
P.move_to(u21, base=575.4)
P.para(u21, 0, nlines=2, pitch=11.0, lastbase=586.4, align='justify')
P.set(u21, nowrap=False, maxBottom=589.2)


def wline(en, size, x0, x1, base, color, top, bottom, hl=None):
    ln = {'en': en, 'font': 'MinionPro-Cn', 'size': size, 'color': color, 'x0': x0, 'x1': x1, 'top': top,
          'bottom': bottom, 'base': base, 'rot': 0, 'bg': '#ffffff', 'maxRight': x1, 'maxLeft': x0, 'align': 'left'}
    if hl:
        ln['hl'] = hl
    return ln


cov = wline('\u00a0' * 4, 9.5, 52.8, 61.5, 571.6, '#ffffff', 561.5, 574.5, hl='#ffffff')
P.lay['units'].insert(0, {'id': 'u950', 'kind': 'lines', 'x0': 52.8, 'top': 561.5, 'x1': 61.5, 'bottom': 574.5,
                          'maxBottom': 574.5, 'maxRight': 61.5, 'maxLeft': 52.8, 'bg': '#ffffff', 'fixscale': 1.0,
                          'lines': [cov]})
T0, SZ = round(563.0 - DY3 - 0.1, 2), 7.2                   # góra trójkąta, stopień znaków
b1 = round(T0 + 0.616 * SZ, 2)                              # ◣: górna połowa (wierzchołek u góry z lewej)
b2 = round(b1 + 0.725 * SZ - 0.15, 2)                        # ◤: dolna połowa (0,15 pt zakładki – bez szczeliny)
tri = [wline('\u25e3', SZ, 54.0, 59.5, b1, '#231f20', round(b1 - 5, 2), round(b1 + 1, 2)),
       wline('\u25e4', SZ, 54.0, 59.5, b2, '#231f20', round(b2 - 5, 2), round(b2 + 1, 2))]
P.lay['units'].append({'id': 'u951', 'kind': 'lines', 'x0': 54.0, 'top': T0, 'x1': 59.5, 'bottom': round(T0 + 10.4, 2),
                       'maxBottom': round(T0 + 10.4, 2), 'maxRight': 59.5, 'maxLeft': 54.0, 'bg': '#ffffff',
                       'fixscale': 1.0, 'lines': tri})
P.save()
