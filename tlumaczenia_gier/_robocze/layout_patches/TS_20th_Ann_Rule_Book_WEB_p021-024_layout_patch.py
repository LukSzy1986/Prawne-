#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Rule_Book_WEB, s. 21–24 (redaktor tr21_24, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
#
# Wspólne dla s. 21–23: nagłówki w kroju Veneer (Veneer-TwoRegular / Veneer-Regular) render.py składa
# zastępnikiem LSerif (Liberation Serif, krój szeryfowy i ok. 55% szerszy od wąskiego Veneer) – polskie
# nagłówki scenariuszy nie mieściły się nawet w skali 0,6. Akapity/wiersze tych nagłówków dostają krój
# MyriadPro-BoldCond (zastępnik HerosCnN Bold – wąski, pogrubiony bezszeryfowy, bliższy Veneer).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Rule_Book_WEB'
VENEER_SUB = 'MyriadPro-BoldCond'


def veneer(P, u, i=0):
    """nagłówek Veneer -> wąski bezszeryfowy zastępnik"""
    if u['kind'] == 'flow':
        P.para(u, i, font=VENEER_SUB)
    else:
        P.line(u, i, font=VENEER_SUB)


def table(P, u, order, x_cols, base0, pitch, size, rows_a, start=0):
    """Przebudowa tabeli państw (jednostka lines) na kolumny x_cols: wiersze w kolejności `order`
    (teksty EN z units), pierwsze rows_a w kolumnie A, reszta w B; linia bazowa 1. wiersza base0."""
    old = u['lines']
    keep = old[:start]
    pool = old[start:]
    by_en = {}
    for ln in pool:
        by_en.setdefault(ln['en'], []).append(ln)
    new = []
    for k, en in enumerate(order):
        src = dict(by_en[en].pop(0))
        col = 0 if k < rows_a else 1
        row = k if k < rows_a else k - rows_a
        x0, mr = x_cols[col]
        b = round(base0 + row * pitch, 2)
        src.update(x0=x0, x1=round(x0 + (src['x1'] - src['x0']) * size / src['size'], 2), base=b,
                   top=round(b - 0.75 * size, 2), bottom=round(b + 0.25 * size, 2), size=size,
                   maxLeft=x0, maxRight=mr, align='left')
        new.append(src)
    assert all(not v for v in by_en.values()), 'tabela: nie wszystkie wiersze użyte'
    u['lines'] = keep + new
    u['top'] = min(l['top'] for l in u['lines'])
    u['bottom'] = max(l['bottom'] for l in u['lines'])
    return u


# ---------------------------------------------------------------------------------------- s. 21
P = Patch(D, 21); P.restore()
# nagłówek „PRZYGOTOWANIE SCENARIUSZA APOGEUM”
veneer(P, P.find('A LATE WAR SCENARIO SETUP'))
# „Karty”: akapit 0 (pierwszy wiersz EN, osobny akapit z unitize) pusty – cały tekst w akapicie 1,
# który zaczyna się w miejscu akapitu 0
u = P.find('Remove all Early and Mid War Events')
# polski tekst o ok. 2 wiersze dłuższy (tytuły kart i nazwy elementów z EN), a pod jednostką są żetony
# (tło, y = 361): nagłówek „Karty” i tekst 3,5 pt wyżej, odstępy przed „Znaczniki” i „Żetony…”
# mniejsze o 3,3 i 1,5 pt (linie bazowe akapitów wyznaczają odstępy)
P.move_to(P.find('Cards', kind='lines'), base=107.62)
P.para(u, 1, base=120.82, top=113.78)
P.para(u, 2, base=199.62)
P.para(u, 4, base=351.12)
P.set(u, maxBottom=359.0)
# „Zwycięstwo”: lewa krawędź karty Wargames jest skośna (x 204 -> 181 przy y 476 -> 584), więc poniżej
# y = 545 wiersze kończą się przed x = 177 (obrazek opływany z prawej); wyrównanie do lewej (justowanie
# w wąskim łamie dawało rozstrzelone wiersze – QA 26.10)
v = P.find('The US may not win through')
P.para(v, 0, align='left', cuts=[{'side': 'r', 'top': 545.0, 'bottom': 600.0, 'w': 8.5}])
# ramka „Kontrola i Wpływy”: tytuły wyśrodkowane w ramce (jak w oryginale), krój zastępczy dla Veneer
for uid, en in (('u7', 'A LATE WAR SCENARIO'), ('u8', 'Control and Influence')):
    u = P.unit(uid)
    assert u['paras'][0]['en'] == en
    P.set(u, x0=327.0, x1=557.12)
    P.para(u, 0, left=0.0, align='center')
veneer(P, P.unit('u7'))
# „• USA dominują…”: dwa wiersze w szerokości ramki, punktor z wcięciem wiszącym (QA 26.10)
u = P.find('US Dominates South America')
P.set(u, x0=327.0, x1=557.12)
P.para(u, 0, align='left', hang=8.0, left=0.0)
# „Umieść minimalną liczbę…”: wyśrodkowany akapit bez wcięcia wiszącego (z unitize: hang 74,5 –
# przesuwał 2. i dalsze wiersze w prawo)
P.para(P.find('needed for Control, except where'), 0, hang=0.0)
# paski KONTROLA USA / KONTROLA ZSRR / NEUTRALNE (tło: prostokąty x 395–477): tekst wyśrodkowany
# w pasku, krój zastępczy; lekkie ścieśnienie (hs) dla „KONTROLA ZSRR”
# napisy 12 pt (zastępnik HerosCnN Bold jest szerszy od Veneer 14,5 pt), pole x 400–472 – zapas
# ok. 5 pt od krawędzi paska; linie bazowe na środku pasków (tło: y 226–247, 427–448, 572–593)
for t, b in (('US CONTROL', 240.8), ('USSR CONTROL', 441.8)):
    u = P.find(t)
    P.set(u, x0=400.0, x1=472.0, maxLeft=400.0, maxRight=472.0)
    P.move_to(u, base=b)
    P.para(u, 0, align='center', x0=400.0, x1=472.0, hs=0.95, size=12.0, pitch=14.4)
    veneer(P, u)
u16 = P.find('NEUTRAL')
P.line(u16, 0, x0=400.0, x1=472.0, maxLeft=400.0, maxRight=472.0, align='center', hs=0.95, size=12.0,
       base=586.8, top=577.8, bottom=589.8)
veneer(P, u16, 0)
# tabele państw: polskie nazwy z EN w nawiasie nie mieszczą się w 3 kolumnach (do 123 pt na kolumnę
# 80 pt) – 2 kolumny, stopień 9 pt, odstęp wierszy 10,5 pt, w granicach pasków tła
COLS = ((325.37, 441.0), (447.0, 567.0))
US = ['UK', 'Italy', 'Benelux', 'Denmark', 'Norway', 'W. Germany <b>(5/1)</b>', 'Israel', 'Iran',
      'Pakistan', 'Turkey', 'Zaire', 'Somalia', 'Kenya', 'Nigeria', 'Japan', 'South Korea', 'Taiwan',
      'Philippines <b>(3/1)</b>', 'Thailand', 'Indonesia', 'Australia', 'Malaysia <b>(3/1)</b>', 'Nicaragua',
      'Panama', 'Haiti', 'Honduras', 'Venezuela', 'Chile', 'Argentina', 'Colombia <b>(2/1)</b>',
      'Dominican Republic']
table(P, P.find('Dominican Republic'), US, COLS, 261.5, 10.5, 9.0, 16)
USSR = ['E. Germany', 'Poland', 'Hungary', 'Czechoslovakia', 'Bulgaria', 'Iraq', 'Syria <b>(0/3)</b>',
        'India', 'Afghanistan', 'Cuba', 'Libya', 'Algeria', 'Ethiopia', 'Zimbabwe', 'North Korea',
        'Angola <b>(1/3)</b>', '<f MyriadPro-Cond>Laos</f> (0/2)', 'Vietnam <b>(0/5)</b>']
table(P, P.find('Czechoslovakia'), USSR, COLS, 462.0, 10.5, 9.0, 9)
# „Państwa Afryki Południowo-Wschodniej (SE African States, 0/2)” – wiersz 10 tabeli ZSRR, cała szerokość
u = P.find('SE African States')
P.move_to(u, base=462.0 + 9 * 10.5)
P.set(u, x0=325.37, x1=567.0, maxLeft=312.5, maxRight=567.0)
P.para(u, 0, size=9.0, pitch=10.8, x0=325.37, x1=567.0)
NEU = ['Spain <b>(1/0)</b>', 'France <b>(3/1)</b>', 'Romania <b>(1/3)</b>', 'Jordan <b>(2/2)</b>',
       'Egypt <b>(1/0)</b>', 'South Africa <b>(2/1)</b>', 'Finland <b>(1/2)</b>', 'Burma <b>(0/1)</b>',
       '<f MyriadPro-Cond>Peru</f> (2/1)', 'Yugoslavia <b>(1/2)</b>', 'Saudi Arabia <b>(2/0)</b>']
table(P, u16, NEU, COLS, 607.0, 10.5, 9.0, 6, start=1)
P.save()


# ---------------------------------------------------------------------------------------- s. 22
# Polski tekst (tytuły kart i nazwy elementów z EN, dwuwierszowe nagłówki scenariusza) jest o ok. 1/4
# dłuższy, a oryginał wypełnia obie łamy do dołu. Każda łama staje się jedną jednostką flow
# (tekst główny strony – wspólna skala), listy kart i miejsc rozmieszczenia Wpływów – akapitami
# z punktorem ◊ i wcięciem wiszącym (pozycje mogą się łamać na 2 wiersze). Odstępy między akapitami
# jak w oryginale (gap = odległość linii bazowych), chyba że niżej podano inaczej.
import copy as _copy


def _para(src, **kw):
    p = {k: _copy.deepcopy(v) for k, v in src.items() if k not in ('cuts',)}
    p.update(kw)
    return p


def _line_para(ln, **kw):
    p = {'en': ln['en'], 'font': ln['font'], 'size': ln['size'], 'color': ln.get('color', '#231f20'),
         'align': 'left', 'pitch': round(ln['size'] * 1.2, 2), 'nlines': 1, 'left': 0.0, 'right': 0.0,
         'indent': 0.0, 'hang': 0.0, 'top': ln['top'], 'bottom': ln['bottom'], 'base': ln['base'],
         'lastbase': ln['base'], 'x0': ln['x0'], 'x1': ln['x1'], 'bg': '#ffffff', 'gap': None}
    p.update(kw)
    return p


def rebuild(P, keep_id, drop_ids, seq, x0, x1, max_bottom):
    """Jednostka keep_id = akapity z seq [(akapit, gap), …] (gap – odległość linii bazowych od
    poprzedniego akapitu; dla pierwszego: linia bazowa); jednostki drop_ids usunięte."""
    u = P.unit(keep_id)
    paras = []
    prev = None
    for p, gap in seq:
        p = dict(p)
        b = gap if prev is None else round(prev + gap, 2)
        p.update(base=b, lastbase=b, top=round(b - 0.75 * p['size'], 2),
                 bottom=round(b + 0.25 * p['size'], 2), x0=x0 + p.get('left', 0.0), x1=x1, gap=None)
        paras.append(p)
        prev = b
    u.update(kind='flow', x0=x0, x1=x1, top=paras[0]['top'], bottom=max_bottom, base=paras[0]['base'],
             maxBottom=max_bottom, maxRight=x1 + 0.5, maxLeft=x0 - 0.5, bg='#ffffff', body=True,
             nowrap=False, paras=paras)
    u.pop('lines', None)
    P.lay['units'] = [v for v in P.lay['units'] if v['id'] not in drop_ids]
    return u


P = Patch(D, 22); P.restore()
U = {u['id']: u for u in P.lay['units']}
assert U['u2']['paras'][0]['en'] == 'RED SUN RISING SCENARIO' and U['u4']['paras'][0]['en'].startswith('RED SUN')
EM = '\u2003'                                 # spacja firetowa po punktorze ◊
# --- lewa łama
h1 = _para(U['u2']['paras'][0], font=VENEER_SUB, pitch=26.4)
by, intro, h3, comp = (U['u3']['paras'][i] for i in range(4))
h2 = _para(U['u4']['paras'][0], font=VENEER_SUB, pitch=19.8)
setup = U['u5']['paras'][0]
cards = _line_para(U['u6']['lines'][0], pitch=16.8)
remove = _para(U['u7']['paras'][0], align='justify')
early = U['u7']['paras'][1]
lst = U['u8']['lines']
heads = {l['en']: l for l in lst if l['en'] in ('Mid War:', 'Late War:')}
titles = [l['en'] for l in lst if l['en'] not in ('◊', 'Mid War:', 'Late War:')]
k9 = U['u9']['paras'][0]
assert k9['en'] == 'Soviets Shoot Down KAL-007 Yuri and Samantha'
titles = titles[:-1] + ['Soviets Shoot Down KAL-007', 'Yuri and Samantha'] + titles[-1:]
assert len(titles) == 19, titles
it_src = lst[1]


def item_l(t):
    # punktor ◊ w x = 90 (left 45 od x0 = 45), tekst po spacji firetowej; wiersze łamane – wcięcie wiszące
    return _para({}, en=f'◊{EM}{t}', font=it_src['font'], size=9.5, color=it_src.get('color', '#231f20'),
                 align='left', pitch=11.4, nlines=1, left=45.0, right=0.0, indent=0.0, hang=12.92,
                 bg='#ffffff')


def head_l(src, en):
    return _para({}, en=en, font=src['font'], size=src['size'], color=src.get('color', '#231f20'),
                 align='left', pitch=13.2, nlines=1, left=36.0, right=0.0, indent=0.0, hang=0.0, bg='#ffffff')


ITEM_GAP_L = 13.5
seqL = [(h1, 89.76), (by, 18.0), (intro, 17.7), (h3, 23.0), (comp, 13.2), (h2, 26.0), (setup, 13.2),
        (cards, 23.0), (remove, 13.2), (head_l(early, 'Early War:'), 17.7)]
seqL += [(item_l(t), ITEM_GAP_L) for t in titles[:9]]
seqL += [(head_l(heads['Mid War:'], 'Mid War:'), 18.0)]
seqL += [(item_l(t), ITEM_GAP_L) for t in titles[9:14]]
# koniec listy kart (Che, Our Man in Tehran oraz „Apogeum (Late War):” z 3 kartami) przechodzi na początek
# prawej łamy: lewa łama nie mieści całej listy, a w prawej pod listami Wpływów było ok. 120 pt wolnego
late = ([(item_l(titles[14]), 80.0), (item_l(titles[15]), ITEM_GAP_L)]
        + [(head_l(heads['Late War:'], 'Late War:'), 18.0)] + [(item_l(t), ITEM_GAP_L) for t in titles[16:]])
# --- prawa łama
r0, rmark_h, rmark, rinf_h, rinf = (U['u10']['paras'][i] for i in range(5))
it_r = U['u11']['lines'][1]


def item_r(t):
    return _para({}, en=f'◊{EM}{t}', font=it_r['font'], size=10.0, color=it_r.get('color', '#231f20'),
                 align='left', pitch=12.0, nlines=1, left=45.0, right=0.0, indent=0.0, hang=13.6, bg='#ffffff')


ussr = ['1 in Syria', '1 in Iraq', '2 in PRC', '3 in Korea', '1 in Ainu DPR', '3 in East Germany', '1 in Finland',
        '6 anywhere in Eastern Europe']
us = ['2 in Canada', '1 in Iran', '1 in Israel', '1 in Japan', '2 in ROC', '1 in French Indochina', '4 in Australia',
      '1 in the Philippines', '1 in New Zealand', '1 in Panama', '1 in South Africa', '5 in the United Kingdom',
      '7 anywhere in Western Europe']
ITEM_GAP_R = 14.5   # oryginał 15,5 – nieco ciaśniej, by obie łamy miały tę samą skalę
seqR = late + [(r0, 17.7), (rmark_h, 23.0), (rmark, 13.2), (rinf_h, 23.0), (rinf, 13.2)]
seqR += [(item_r(t), ITEM_GAP_R) for t in ussr]
seqR += [(_para(U['u15']['paras'][0]), 18.0)]
seqR += [(item_r(t), ITEM_GAP_R) for t in us]

rebuild(P, 'u3', ('u2', 'u4', 'u5', 'u6', 'u7', 'u8', 'u9'), seqL, 45.0, 295.45, 751.0)
rebuild(P, 'u10', ('u11', 'u12', 'u13', 'u14', 'u15', 'u16', 'u17', 'u18'), seqR, 307.66, 558.1, 751.0)
# QA 27.10 (stretch.py): rozstrzelone wiersze we wstępie (y ≈ 150, 209) i w „Znacznikach” (y ≈ 255–338) –
# lekko węższe odstępy między wyrazami (word-spacing) zmieniają przełamanie bez zmiany skali
assert P.unit('u3')['paras'][2]['en'].startswith('This “what if”')
P.para('u3', 2, ws=-0.03)
assert P.unit('u10')['paras'][8]['en'].startswith('Place the <b>US</b>')
P.para('u10', 8, ws=-0.05)
P.save()


# ---------------------------------------------------------------------------------------- s. 23
P = Patch(D, 23); P.restore()
# lewa łama „Zasady specjalne”: sztuczne prawe wcięcia akapitów z unitize wyzerowane; trzeci punkt
# (u3 – punktor, u4 – tekst) dołączony do u2 jako akapit z punktorem i wcięciem wiszącym jak dwa
# pierwsze (QA 26.10: punkt nad kartą jak w oryginale); tekst do obrazka karty RS1 (tło: y = 302)
u2 = P.find('Special Rules')
for i in (2, 3, 4):
    P.para(u2, i, right=0.0)
u4 = P.find('Security Council Resolutions')
P.set(u4, x0=54.0)
P.para(u4, 0, x0=67.5)
P.merge(u2, u4)
P.para(u2, len(u2['paras']) - 1, left=13.5, hang=13.5, indent=0.0, align='left')
P.lay['units'] = [v for v in P.lay['units'] if v['id'] != 'u3']
# koniec trzeciego punktu może opłynąć kartę z prawej (puste pole x 196–304 do y ≈ 404, zdjęcie od y = 412);
# szerokość opływu 155,5 = 142 + wcięcie wiszące 13,5 – punktor w x = 196, tekst w x = 209,5 jak w punktach wyżej
P.para(u2, len(u2['paras']) - 1, cuts=[{'side': 'l', 'top': 301.0, 'bottom': 413.0, 'w': 155.5}])
P.set(u2, maxBottom=404.0)
# ramka TWÓRCY (tło: x 317–566, y 72–746): nagłówki Veneer – krój zastępczy; „TWÓRCY WYDANIA 20TH
# ANNIVERSARY HALL OF FAME EDITION” w dwóch wierszach, więc cała lista twórców (u6–u11) staje się jedną
# jednostką flow (własna skala), żeby dalsze pozycje przesunęły się w dół w granicach ramki
veneer(P, P.find('CREDITS', kind='lines'), 0)
cr = P.find('Game Design')
for uid in ('u7', 'u8', 'u9', 'u10', 'u11'):
    v = P.unit(uid)
    if v['kind'] == 'lines':
        P.lines_to_flow(v, align='left')
    P.merge(cr, v)
hof = [i for i, p in enumerate(cr['paras']) if p['en'].startswith('20TH ANNIVERSARY')][0]
P.para(cr, hof, font=VENEER_SUB, pitch=14.4)
for i, p in enumerate(cr['paras']):
    if p['en'] in ('Development', 'Graphics'):
        P.para(cr, i, pitch=14.4, indent=0.0)
P.set(cr, maxBottom=742.0, body=False)
# „Szczególne podziękowania…” – w oryginale wyrównane do lewej (unitize: justowanie; QA 27.10)
P.para(cr, [i for i, p in enumerate(cr['paras']) if p['en'].startswith('Special thanks')][0], align='left')
# „Korekta” (lista nazwisk, justowana jak w oryginale): wiersz „sanof, David Kurtz…” rozstrzelony (0,59 em) –
# lekkie zwężenie odstępów liter (hs 0,95) mieści „Kasanof,” bez dzielenia nazwiska
P.para(cr, [i for i, p in enumerate(cr['paras']) if p['en'].startswith('Fabian Amstad')][0], hs=0.95)
P.save()
