#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Background_Book_WEB, s. 5–8 (Przykład rozgrywki; redaktor tb5_8, 2026-10-26)
# Idempotentny: każda strona startuje od stanu z unitize (P.restore()).
#
# Co robią (szczegóły przy funkcjach):
#  - nagłówki „ARn (…)”, „Ręka …”: tekst między ikonami z tła, jeden wiersz, osobna skala;
#  - podkreślenia nagłówków i śródtytułów są w tle (wektor, nie tekst) – polski tekst ma inną długość
#    i przy skali < 1 inne położenie, więc linie tła są zakrywane białym prostokątem (jednostki „u901…”
#    na początku listy = pod tekstem), a podkreślenie składa się znacznikiem <u> jak w EN;
#  - dialogi w ramkach: szerokość do prawej krawędzi ramki;
#  - x0 jednostek prawego łamu zawyżone przez żywą paginę – poprawione (wraz z obrazkami opływanymi);
#  - akapity scalone przez unitize z wierszy o różnych stylach – rozdzielone;
#  - listy kart (◊) i wypunktowania: przesunięcia/rozbicia, żeby polskie tytuły z EN mieściły się;
#  - odstępy między akapitami bloków przykładu nieco zmniejszone (tekst polski dłuższy, ramki stałe);
#  - jednostki tekstu bloków przykładu w jednej grupie skali strony (body); dół jednostek nad ramkami
#    dialogów 1,8 pt nad ramką; wiersze „Karta: …” do lewej; wcięcia wiszące punktorów w skali strony.
import copy
import sys
sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch  # noqa: E402

D = 'TS_20th_Ann_Background_Book_WEB'

# ramki dialogów w tle (x0, x1, y0, y1 w pt; wykryte z bgimg)
BOXES = {
    5: [(50, 309, 162, 190), (312, 571, 201, 230), (50, 309, 463, 492), (50, 309, 276, 304),
        (312, 571, 421, 450), (50, 309, 675, 692)],
    6: [(41, 300, 579, 596), (303, 562, 631, 660), (41, 300, 559, 576), (303, 562, 679, 708)],
    7: [(312, 571, 277, 294), (312, 571, 391, 408), (50, 309, 394, 411), (50, 309, 595, 623),
        (312, 571, 722, 740), (312, 571, 257, 275), (50, 309, 273, 301), (312, 571, 411, 439),
        (50, 309, 414, 442), (50, 309, 626, 665), (312, 571, 702, 720)],
    8: [(41, 300, 182, 199), (303, 562, 240, 258), (41, 300, 367, 395), (41, 300, 521, 549),
        (303, 562, 673, 702), (41, 300, 714, 732), (41, 300, 201, 219), (303, 562, 260, 299),
        (41, 300, 347, 365), (41, 300, 551, 569), (303, 562, 654, 671), (41, 300, 694, 712)],
}
BOX_COLORS = ('#f2d4cd', '#cbdcec')

# linie podkreśleń w tle (x0, x1, y osi linii; grubość 0,55 pt) – z bg/…pdf (pdfplumber)
ULINES = {
    5: [(69.58, 121.84, 86.44), (332.23, 384.49, 86.44), (69.58, 110.12, 224.84), (332.23, 372.78, 264.54),
        (316.66, 369.96, 313.14), (69.58, 121.84, 338.84), (69.58, 110.12, 526.64), (54.00, 125.65, 562.04)],
    6: [(320.56, 358.73, 507.85), (57.91, 107.79, 640.02)],
    7: [(332.23, 372.78, 86.44), (332.23, 384.49, 311.34), (332.23, 372.78, 470.84), (69.58, 121.84, 484.60),
        (316.66, 369.96, 506.24)],
    8: [(60.58, 112.84, 86.44), (323.23, 375.49, 86.44), (307.66, 388.66, 121.84), (60.58, 101.12, 253.74),
        (60.58, 112.84, 427.24), (323.23, 363.78, 593.83), (60.58, 101.12, 600.74), (307.66, 392.79, 629.23)],
}


def whiteouts(P):
    """białe prostokąty na liniach podkreśleń z tła: jednostka lines z białym tekstem „xxx…” podświetlonym
    na biało (<hl #ffffff>, ok. 3,7 pt wysokości), wstawiona na początek listy (rysowana pod tekstem);
    szerokość linii + 0,5 pt z każdej strony („x” w LSerifCn = 0,455 em)"""
    for k, (x0, x1, y) in enumerate(ULINES[P.page]):
        a, b = x0 - 0.5, x1 + 0.5
        w = b - a
        NB = 0.2275                       # szerokość twardej spacji w LSerifCn (em); tekst niewidoczny w warstwie tekstu
        n = max(1, round(w / (NB * 3.0)))
        size = round(w / (n * NB), 3)
        base = round(y + 0.45 * size / 3.0 + 0.05, 2)
        ln = {'en': '\u00a0' * n, 'font': 'MinionPro-Cn', 'size': size, 'color': '#ffffff', 'x0': a, 'x1': b,
              'top': round(y - 2, 2), 'bottom': round(y + 1.5, 2), 'base': base, 'rot': 0, 'bg': '#ffffff',
              'maxRight': b, 'maxLeft': a, 'align': 'left', 'hl': '#ffffff'}
        P.lay['units'].insert(k, {'id': f'u{901 + k}', 'kind': 'lines', 'x0': a, 'top': ln['top'], 'x1': b,
                                  'bottom': ln['bottom'], 'maxBottom': ln['bottom'], 'maxRight': b, 'maxLeft': a,
                                  'bg': '#ffffff', 'fixscale': 1.0, 'lines': [ln]})


# QA runda 3: kwestie s. 7 u24, u25 do x = 565 (jak w EN: tekst do 563) – pełny stopień 9 pt
BOX_RIGHT = {(7, 'u25'): 565.0, (7, 'u24'): 565.0}


def boxes(P):
    """dialogi w kolorowych ramkach: szerokość tekstu do prawej krawędzi ramki (wcięcie jak z lewej)"""
    for u in P.lay['units']:
        if u['kind'] != 'flow' or u.get('bg') not in BOX_COLORS:
            continue
        for (bx0, bx1, by0, by1) in BOXES[P.page]:
            if by0 - 1 <= u['top'] and u['bottom'] <= by1 + 1 and bx0 <= u['x0'] <= bx1:
                r = BOX_RIGHT.get((P.page, u['id']), bx1 - 8.5)
                u['maxRight'] = r
                if not u.get('nowrap'):
                    u['x1'] = r
                break
        else:
            raise SystemExit(f's. {P.page} {u["id"]}: brak ramki dialogu')


def clear_boxes(P, gap=4.0):
    """jednostki tekstu nad ramką dialogu: dół najwyżej gap pt nad górną krawędzią ramki (unitize daje 0,8 pt –
    polskie litery z ogonkami i kursywa dotykały ramki; QA 26.10: 4 pt – w oryginale 5–8 pt odstępu)"""
    for u in P.lay['units']:
        if u['kind'] != 'flow' or u.get('bg') in BOX_COLORS or u.get('role'):
            continue
        mb = u.get('maxBottom', u['bottom'])
        for (bx0, bx1, by0, by1) in BOXES[P.page]:
            if bx0 - 5 <= u['x0'] <= bx1 and mb - 3 <= by0 <= mb + 3:
                u['maxBottom'] = round(min(mb, by0 - gap), 2)


def hdr(P, uid, icon_l, icon_r, hs=None, gap_l=1.8, gap_r=1.8):
    """nagłówek „ARn (…)”/„Ręka …” między ikonami (icon_l – prawa krawędź lewej ikony, icon_r – lewa krawędź
    prawej ikony; z tła): od icon_l + gap_l (1,8 pt; QA 26.10: było 1,3 – litera dotykała ikony) do icon_r − 1,8 pt, jeden wiersz, osobna skala (nie wpływa na skalę tekstu głównego)"""
    u = P._u(uid)
    p = u['paras'][0]
    x0, r = round(icon_l + gap_l, 2), round(icon_r - gap_r, 2)
    u.update(x0=x0, maxLeft=x0, x1=r, maxRight=r, nowrap=True, body=False)
    p.update(left=0.0, right=0.0, hang=0.0, indent=0.0, x0=x0)
    p.pop('cuts', None)
    if hs:
        p['hs'] = hs


def fix_x0(P, uid, x0):
    """jednostka prawego łamu z x0 zawyżonym przez żywą paginę (259,4): x0 = lewa krawędź łamu;
    wcięcia akapitów i szerokości obrazków opływanych pomniejszone o różnicę"""
    u = P._u(uid)
    dx = x0 - u['x0']
    if abs(dx) < 0.01:
        return u
    u['x0'] = x0
    u['maxLeft'] = x0
    for p in u['paras']:
        p['left'] = round(max(0.0, p.get('left', 0) - dx), 2)
        for c in p.get('cuts', []):
            c['w'] = round(c['w'] - dx, 2)
    return u


def shift_from(u, i, dy):
    for p in u['paras'][i:]:
        for k in ('top', 'bottom', 'base', 'lastbase'):
            p[k] = round(p[k] + dy, 2)


def set_gap(u, i, g):
    """odstęp (pt) linii bazowych: ostatni wiersz akapitu i-1 -> pierwszy wiersz akapitu i"""
    cur = u['paras'][i]['base'] - u['paras'][i - 1]['lastbase']
    shift_from(u, i, round(g - cur, 2))
    u['paras'][i]['gap'] = g


def kind_of(p):
    t = p['en'].lstrip()
    if t.startswith('◊'):
        return 'dia'
    if t.startswith('•'):
        return 'bul'
    if t.startswith('<u>'):
        return 'sub'
    if t.startswith(('Card:', 'US:', 'USSR:')):
        return 'card'
    return 'txt'


# odstępy w blokach przykładu (oryginał: karta->opis 15,5; ->punktor 17,7; punktor->punktor 16,5–17,7;
# punktor->tekst 14–16)
GAPS = {('card', 'txt'): 13.5, ('card', 'sub'): 15.0, ('card', 'bul'): 15.0, ('sub', 'bul'): 15.0,
        ('sub', 'txt'): 14.0, ('txt', 'bul'): 15.0, ('bul', 'bul'): 14.5, ('bul', 'txt'): 13.0,
        ('txt', 'txt'): 13.0, ('txt', 'dia'): 13.5, ('dia', 'dia'): 12.5, ('dia', 'txt'): 14.0}


# s. 8 (najgęstsza): odstępy jeszcze nieco mniejsze
TIGHT = {('card', 'txt'): 12.5, ('card', 'bul'): 13.5, ('txt', 'bul'): 13.5, ('bul', 'bul'): 13.5,
         ('bul', 'txt'): 12.0, ('sub', 'bul'): 14.0, ('txt', 'txt'): 12.0}


# QA runda 3 (27.10): bloki z luką nad ramką dialogu (tekst w skali < 1 krótszy niż w oryginale) – odstępy
# między akapitami bloku powiększone o tyle pt (wartość w layout; w składzie × skala strony), żeby dół bloku
# stał ok. 6–8 pt nad ramką jak w oryginale (zmierzone na podglądzie)
EXTRA = {(5, 'u21'): 4.45, (5, 'u14'): 2.75, (7, 'u28'): 2.7, (7, 'u27'): 2.0, (7, 'u14'): 0.85, (8, 'u21'): 4.35,
         (8, 'u17'): 1.6, (8, 'u25'): 5.8}


def compact(P, uid, start=1, gaps=None):
    u = P._u(uid)
    g = dict(GAPS)
    g.update(gaps or {})
    ex = EXTRA.get((P.page, u['id']), 0.0)
    for i in range(max(1, start), len(u['paras'])):
        a, b = kind_of(u['paras'][i - 1]), kind_of(u['paras'][i])
        if (a, b) in g:
            set_gap(u, i, round(g[(a, b)] + ex, 2))


def split_para(P, uid, i, en_head, en_tail, tail, gap):
    """akapit i scalony przez unitize z dwóch wierszy o różnych stylach -> dwa akapity
    (tail: pola stylu drugiego akapitu)"""
    u = P._u(uid)
    p = u['paras'][i]
    q = copy.deepcopy(p)
    q.pop('cuts', None)
    p.update(en=en_head, nlines=1, lastbase=p['base'], bottom=round(p['base'] + 0.27 * p['size'], 2))
    q.update(tail)
    q.update(en=en_tail, nlines=1, base=round(p['base'] + gap, 2), gap=gap)
    q['lastbase'] = q['base']
    q['top'] = round(q['base'] - 0.73 * q['size'], 2)
    q['bottom'] = round(q['base'] + 0.27 * q['size'], 2)
    u['paras'].insert(i + 1, q)


def bullet_para(p, left, hang=13.5):
    p.update(font='MinionPro-Cn', size=11.0, align='left', pitch=13.2, left=left, hang=hang, indent=0.0, right=0.0)


def diamonds_to_flow(P, uid, col_x0, dx_diamond, dx_text, pitch):
    """lista kart (jednostka lines: „◊”, tytuł, …) -> jednostka flow, akapit na kartę (◊ wysunięty, tytuł
    od wcięcia; dłuższy tytuł łamie się z wcięciem)"""
    u = P._u(uid)
    rows = [ln for ln in u['lines'] if ln['en'] != '◊']
    paras = []
    for k, ln in enumerate(rows):
        base = round(rows[0]['base'] + k * pitch, 2)
        paras.append({'en': '◊ ' + ln['en'], 'font': ln['font'], 'size': ln['size'], 'color': ln['color'],
                      'align': 'left', 'pitch': pitch, 'nlines': 1, 'left': dx_diamond, 'right': 0.0,
                      'indent': 0.0, 'hang': dx_text - dx_diamond, 'top': round(base - 7.3, 2),
                      'bottom': round(base + 2.7, 2), 'base': base, 'lastbase': base, 'x0': col_x0 + dx_diamond,
                      'x1': ln['x1'], 'bg': '#ffffff', 'gap': None if k == 0 else pitch})
    new = {'id': u['id'], 'kind': 'flow', 'x0': col_x0, 'top': paras[0]['top'], 'x1': u.get('maxRight', u['x1']),
           'bottom': paras[-1]['bottom'], 'base': paras[0]['base'], 'maxBottom': u.get('maxBottom', u['bottom']),
           'maxRight': u.get('maxRight', u['x1']), 'maxLeft': col_x0, 'bg': '#ffffff', 'body': True,
           'nowrap': False, 'paras': paras}
    u.clear()
    u.update(new)
    return u


def shift_lines(P, uid, dx, maxright=None):
    """lista kart (lines) przesunięta w poziomie o dx; prawa granica tytułów = maxright"""
    u = P._u(uid)
    for ln in u['lines']:
        ln['x0'] = round(ln['x0'] + dx, 2)
        ln['x1'] = round(ln['x1'] + dx, 2)
        ln['maxLeft'] = round(ln.get('maxLeft', ln['x0']) + dx, 2)
        if ln['en'] != '◊' and maxright:
            ln['maxRight'] = maxright
        else:
            ln['maxRight'] = round(ln['maxRight'] + dx, 2)
    u['x0'] = round(u['x0'] + dx, 2)
    u['x1'] = round(u['x1'] + dx, 2)


def body(P, *uids):
    for uid in uids:
        P.set(uid, body=True)


def card_lines(P, uid):
    """wiersz „Karta: …” – po polsku zwykle dwuwierszowy: wyrównanie do lewej (justowanie dawało dziury);
    QA runda 3 (wariant ustalony dla całego Przykładu): drugi wiersz wcięty pod początek tekstu „Karta:” –
    zamiast obrazka opływanego (trójkąt z tła) lewe wcięcie całego akapitu o jego szerokość"""
    u = P._u(uid)
    for p in u['paras']:
        if kind_of(p) == 'card':
            p['align'] = 'left'
            cuts = p.pop('cuts', [])
            if cuts:
                p['left'] = round(p.get('left', 0.0) + max(c['w'] for c in cuts), 2)


# przybliżona skala tekstu głównego stron (wynik fit.py) – do wcięć wiszących punktorów
PSCALE = {5: 0.91, 7: 0.89, 8: 0.875}


def hang_scaled(P, uid):
    """(QA 26.10: punktory „•” składa teraz render.py w polu o szerokości wcięcia wiszącego – tu tylko „◊”)
    romb „◊” + odstęp EM to w polskim tekście znaki skalowane razem z tekstem, a wcięcie wiszące
    (hang) – stałe; przy skali strony < 1 drugi wiersz punktu zaczynałby się o (1 − s)·13,5 pt dalej niż
    tekst pierwszego wiersza – wcięcie wiszące = szerokość „• ” / „◊  ” w skali strony"""
    k = PSCALE.get(P.page, 1.0)
    u = P._u(uid)
    for p in u['paras']:
        kd = kind_of(p)
        if kd == 'dia':
            p['hang'] = round(15.4 * k, 2)


def justify_txt(P, uid):
    """opisy kursywą (w EN jednowierszowe, wyrównane do lewej) – po polsku wielowierszowe: justowanie
    jak w wielowierszowych opisach oryginału"""
    u = P._u(uid)
    for p in u['paras']:
        if kind_of(p) == 'txt' and 'It' in p['font'] and p.get('align') == 'left':
            p['align'] = 'justify'


DESC = {'font': 'MinionPro-CnIt', 'size': 10.0, 'align': 'justify', 'pitch': 11.0}


# ====================================================================== strony
def s5(P):
    for uid, il, ir in (('u2', 67, 124), ('u5', 67, 112), ('u8', 67, 124), ('u13', 67, 112),
                        ('u17', 330, 386), ('u20', 330, 375)):
        hdr(P, uid, il, ir, hs=0.92 if ir - il < 50 else 0.96, gap_r=2.4 if ir - il < 50 else 1.8)
    # u3: wiersz karty i opis kursywą scalone przez unitize w jeden akapit
    split_para(P, 'u3', 0, 'Card: <b><i>Socialist Governments</i></b> (USSR Event)',
               'Remove 3 US Influence from Western Europe.', DESC, 15.5)
    P.para('u3', 0, font='MinionPro-Cn', align='left', pitch=13.2)
    for uid in ('u3', 'u9'):
        P.set(uid, x1=304.7)
    # u9 + „• Finland” (osobna jednostka lines) + „COMECON is a starred Event…” – jeden blok
    P.lines_to_flow('u10', align='left')
    P.merge('u9', 'u10')
    bullet_para(P.unit('u9')['paras'][5], 13.5)
    P.merge('u9', 'u11')
    P.para('u9', 6, **DESC)
    fix_x0(P, 'u18', 316.66)
    P.para('u18', 1, hs=0.975)         # QA 26.10: rozstrzelony 3. wiersz opisu – inne łamanie
    # u23: nagłówek „END OF TURN ONE” osobno (jeden wiersz); wymóg i wiersz ZSRR – osobne akapity;
    # u24 („Score at end…”) dołączone – może zająć wolne miejsce nad kośćmi (do y = 625)
    h = P.split('u23', 1)
    P.set('u23', nowrap=True, body=False, maxRight=567.0)
    split_para(P, h, 0, 'Military Operations requirement (DEFCON 2 → need 2)', 'USSR: 5 Military Ops <b>☑</b>',
               {'font': 'MinionPro-Cn', 'size': 11.0, 'align': 'left', 'pitch': 15.5, 'left': 36.0,
                'hang': 0.0}, 15.5)
    P.para(h, 0, hang=0.0, align='left')
    P.merge(h, 'u24')
    P.set(h, x1=567.0, body=True)
    for uid in ('u3', 'u6', 'u9', 'u14', 'u18', 'u21'):
        body(P, uid)
        compact(P, uid)                  # QA 26.10: u6 zyskało wiersz – zwykłe odstępy
        justify_txt(P, uid)
        card_lines(P, uid)
        hang_scaled(P, uid)


def s6(P):
    hdr(P, 'u16', 56, 110)
    hdr(P, 'u21', 318, 361, hs=0.92, gap_l=2.5, gap_r=2.5)   # „Ręka USA”: odstępy od gwiazd jak w oryginale
    P.set('u10', maxRight=299.0)       # podpis mapy: nie dalej niż do ikony „US Hand” w prawym łamie
    P.set('u15', maxRight=300.0)       # nagłówek: nie dalej niż do łamu („Nikita examines…” z prawej)
    # lista ZSRR: 25 pt w lewo (najdłuższy tytuł z EN mieści się w łamie w pełnym stopniu)
    shift_lines(P, 'u17', -25.0, maxright=303.0)   # QA runda 3: najdłuższy tytuł w pełnym stopniu
    # lista USA: „Pakt o wzajemnej obronie USA/Japonia (US/Japan Mutual Defense Pact)” w dwóch wierszach;
    # 9 wierszy w miejscu 8 (odstęp 12,57 -> 11,6 pt), prawa granica = łam (560)
    u = P.unit('u22')
    rows = u['lines']
    k = [i for i, ln in enumerate(rows) if ln['en'].startswith('US/Japan')][0]
    extra = copy.deepcopy(rows[k])
    extra['en'] = '(US/Japan Mutual Defense Pact)'
    rows[k]['en'] = 'US/Japan Mutual Defense Pact'
    rows.insert(k + 1, extra)
    b0 = rows[0]['base']
    row = 0
    for i, ln in enumerate(rows):
        if i > 0 and not (ln['en'] != '◊' and rows[i - 1]['en'] == '◊'):
            row += 1
        ln['base'] = round(b0 + row * 11.6, 2)
        ln['top'] = round(ln['base'] - 6.4, 2)
        ln['bottom'] = round(ln['base'] + 3.6, 2)
        if ln['en'] != '◊':
            ln['maxRight'] = 560.0
    u['bottom'] = rows[-1]['bottom']


def s7(P):
    for uid, il, ir in (('u8', 67, 124),):
        hdr(P, uid, il, ir, hs=0.96)
    # u2: nagłówek „HEADLINE PHASE” osobno (jeden wiersz), treść – osobna jednostka
    t = P.split('u2', 1)
    P.set('u2', nowrap=True, body=False)
    # u23: „AR2 (US)” w jednej jednostce z treścią – osobno
    nu = P.split('u23', 1)
    for uid, il, ir in (('u13', 330, 375), ('u19', 330, 386), ('u23', 330, 375)):
        hdr(P, uid, il, ir, hs=0.92 if ir - il < 50 else 0.96, gap_r=2.4 if ir - il < 50 else 1.8)
    # prawy łam u góry: karta CIA + lista kart ZSRR + „Jack uses…” – jeden blok (tekst przelewa się)
    fix_x0(P, 'u14', 316.66)
    P.set('u14', nowrap=False, x1=567.0)
    diamonds_to_flow(P, 'u15', 316.66, 30.0, 47.0, 12.5)
    P.merge('u14', 'u15')
    P.set('u16', nowrap=False, x1=567.0)
    P.merge('u14', 'u16')
    for uid in (t, 'u4', 'u9', 'u14', 'u20', nu):
        body(P, uid)
        compact(P, uid)
        justify_txt(P, uid)
        card_lines(P, uid)
        hang_scaled(P, uid)


def s8(P):
    for uid, il, ir in (('u2', 58, 115), ('u8', 58, 103), ('u12', 58, 115), ('u16', 58, 103),
                        ('u20', 321, 377), ('u24', 321, 366)):
        hdr(P, uid, il, ir, hs=0.92 if ir - il < 50 else 0.96, gap_r=2.4 if ir - il < 50 else 1.8)
    # u3 + u5 (punktory „Die roll…”, „USSR Military Ops”; punktor u4 – w tekście)
    P.set('u3', x1=295.3)
    P.merge('u3', 'u5')
    u = P.unit('u3')
    for i in (3, 4):
        bullet_para(u['paras'][i], 4.85)
    P.set('u25', x1=552.4)
    # QA 26.10: opis AR4 (ZSRR) na granicy 2/3 wierszy – minimalne ścieśnienie (−0,75%), żeby nad ramką
    # dialogu został odstęp jak w oryginale
    P.para('u13', 1, hs=0.985)
    # „• Malaysia: (1/1)” (osobna jednostka lines) dołączone do u25 – skaluje się z tekstem bloku
    P.lines_to_flow('u26', align='left')
    P.merge('u25', 'u26')
    bullet_para(P.unit('u25')['paras'][2], 13.5)
    for uid in ('u3', 'u9', 'u13', 'u17', 'u21', 'u25'):
        body(P, uid)
        # QA 26.10: AR4 (ZSRR) i AR4 (USA) zyskały wiersz – zwykłe odstępy (miejsce nad ramką dialogu)
        compact(P, uid, gaps=None if uid in ('u13', 'u17') else TIGHT)
        justify_txt(P, uid)
        card_lines(P, uid)
        hang_scaled(P, uid)


for pg in range(5, 9):
    P = Patch(D, pg)
    P.restore()
    globals()[f's{pg}'](P)
    boxes(P)
    clear_boxes(P)
    whiteouts(P)
    P.save()
