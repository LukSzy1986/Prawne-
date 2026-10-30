#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Background_Book_WEB, s. 25–36 (redaktor tb25_36, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
#
# 1. Nagłówki haseł kart (MyriadPro-BlackCondIt-SC700): w oryginale „fałszywe kapitaliki” – inicjały,
#    cyfry i akronimy 14 pt, pozostałe litery 9,8 pt (= kapitaliki 0,7 × 14 pt). unitize podał stopień
#    10 albo 14 niekonsekwentnie – ujednolicenie: 14 pt (render: font-variant small-caps), bez wcięć.
# 2. Prawe łamy stron nieparzystych 27, 29, 31: jednostki z x0 = 259,43 (od żywej paginy) i sztucznym
#    lewym wcięciem 57,23 pt / fikcyjnymi wycięciami szer. 57,23 – sprowadzone do x0 = 316,66 łamu.
# 3. Nagłówki w osobnych jednostkach jednowierszowych (nowrap) obok ilustracji kart: polski tytuł z EN
#    nie mieści się w wierszu – nagłówek dołączony do następnej jednostki tekstu (może się łamać).
# 4. Wycięcia (cuts) ilustracji kart: unitize kończy je na ostatnim zwężonym wierszu EN (np. s. 25
#    karta 16: do y = 204, a karta sięga y = 220) – dłuższy tekst polski wchodził na karty. Wycięcia
#    wyznaczone od nowa z ramek kart na obrazie tła (bgimg p-NN.png, 1 px = 1 pt), w pionie +1/+1 pt,
#    szerokość = karta + 8 pt odstępu od tekstu (jak w oryginale, ok. 114,6 pt).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Background_Book_WEB'
SC = 'MyriadPro-BlackCondIt-SC700'
RX0 = 316.66          # lewa krawędź prawego łamu stron nieparzystych
GAP = 8.0             # odstęp tekstu od karty

# ramki kart (x0, y0, x1, y1) w pt, z obrazu tła
CARDS = {
    25: [(54, 146, 160, 294), (462, 71, 568, 220), (462, 590, 568, 739)],
    26: [(189, 229, 296, 378), (45, 550, 151, 699), (452, 119, 558, 267), (452, 556, 558, 705)],
    27: [(198, 294, 305, 443), (316, 121, 423, 269), (462, 489, 568, 638)],
    28: [(45, 551, 151, 700), (307, 261, 414, 410)],
    29: [(198, 76, 305, 224), (54, 564, 160, 713), (462, 514, 568, 663)],
    30: [(45, 143, 151, 292), (452, 323, 558, 472)],
    31: [(198, 71, 305, 220)],
    32: [(189, 418, 296, 566)],
    33: [(54, 301, 160, 449)],
    34: [(189, 80, 296, 229), (307, 394, 414, 543)],
    35: [(188, 215, 294, 364)],
    36: [(45, 116, 151, 265)],
}


def headings(P):
    for u in P.lay['units']:
        if u['kind'] != 'flow':
            continue
        for p in u['paras']:
            if p['font'] == SC:
                p.update(size=14.0, pitch=15.0, hang=0.0, left=0.0, indent=0.0)


def fix_x0(P, uid):
    """jednostka prawego łamu od x0 = 259,43 -> 316,66; bez sztucznych wcięć"""
    u = P.unit(uid)
    u['x0'] = RX0
    u['maxLeft'] = RX0 - 0.5
    for p in u['paras']:
        p['left'] = 0.0


def head_merge(P, uh, ub):
    """nagłówek uh (nowrap) + jednostka tekstu ub -> jedna jednostka flow tekstu głównego"""
    h = P.merge(P.unit(uh), P.unit(ub))
    P.set(h, body=True, nowrap=False)
    return h


# QA 26.10: światło międzywyrazowe akapitów w wąskich łamach obok kart – drobna zmiana światła
# międzyliterowego (ls, em) zmienia łamanie wierszy; klucz: strona -> {początek tekstu EN akapitu: ls}
TRACK = {
    25: {"(1947) King Michael I,": -0.005, "(1948–49, 1956, 1967, ": -0.005, "(1955) A reaction to p": -0.005, "(1947) Before a joint ": -0.005},
    26: {"(1949) The second part": -0.025},
    27: {"(1956–1989) Captured m": 0.005, "(1945–1989) Sparked by": 0.015, "(1963–?) The first Nuc": -0.01, "(1947–?) Also characte": -0.005},
    28: {"(1947–1989) The arms r": 0.005, "(1964–1975) It is hard": 0.005},
    29: {"(1979–1992) In an era ": 0.015, "(1964) As the reality ": -0.005},
    30: {"(1974) Portugal was th": -0.005, "(1969) An ardent socia": 0.005},
    31: {"(1966–1977) While prim": 0.005, "(1960) Starting in 195": 0.005},
    33: {"(1973) Personalized di": 0.005, "(1969) After years of ": 0.01, "(1961) The seminal lin": 0.005},
    34: {"(1961– 1969) After yea": -0.005, "(1979–1990) In many wa": 0.005, "(1986) After the fall ": -0.015, "(1983–?) More properly": 0.015},
    35: {"(1985—1991) Successor ": -0.005},
    36: {"(1985) In an effort to": -0.005, "(1986) The Chernobyl a": 0.005, "(1985–1994) The first ": -0.005},
}


def track(P):
    for pre, v in TRACK.get(P.page, {}).items():
        hit = [p for u in P.lay['units'] for p in (u.get('paras') or []) if p['en'].startswith(pre)]
        assert len(hit) == 1, (P.page, pre)
        hit[0]['ls'] = v


def col_bottom(P, y=747.5):
    """QA 26.10: łamy kończą się nie niżej niż w oryginale (ok. 744–748), ≥ 5 pt nad stopką (753,3)"""
    for u in P.lay['units']:
        if u['kind'] == 'flow' and not u.get('role') and u.get('maxBottom', 0) > y:
            u['maxBottom'] = max(y, round(u['bottom'], 2))


def set_cuts(P):
    """wycięcia wszystkich jednostek flow od nowa – z ramek kart"""
    flows = [u for u in P.lay['units'] if u['kind'] == 'flow' and not u.get('role') and not u.get('nowrap')]
    for u in flows:
        for p in u['paras']:
            p.pop('cuts', None)
    for (cx0, cy0, cx1, cy1) in CARDS[P.page]:
        top, bot = cy0 + 1.0, cy1 + 1.0     # QA: wiersz, którego pole tylko muska górę karty, nie jest skracany
        for u in flows:
            if not (u['x0'] - 1 <= (cx0 + cx1) / 2 <= u['x1'] + 1):
                continue                                  # inny łam
            if u.get('maxBottom', u['bottom']) < top or u['top'] > bot:
                continue                                  # jednostka poza zasięgiem karty
            if cx0 - u['x0'] < u['x1'] - cx1:
                cut = {'side': 'l', 'top': top, 'bottom': bot, 'w': round(cx1 - u['x0'] + GAP, 2)}
            else:
                cut = {'side': 'r', 'top': top, 'bottom': bot, 'w': round(u['x1'] - cx0 + GAP, 2)}
            u['paras'][0].setdefault('cuts', []).append(cut)


# s. 25 – nagłówki 12 (obok karty 11) i 16 (obok karty 16)
P = Patch(D, 25); P.restore(); headings(P)
head_merge(P, 'u3', 'u4')
head_merge(P, 'u6', 'u7')
P.merge('u2', 'u3')            # lewy łam 11–15 jako jeden ciąg (bez dziury przy karcie 11)
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 26 – nagłówki 25 (obok karty 24) i 28 (obok karty 28); 21. NATO zostaje w swojej jednostce
P = Patch(D, 26); P.restore(); headings(P)
head_merge(P, 'u6', 'u7')
head_merge(P, 'u8', 'u9')
P.merge('u6', 'u8')            # prawy łam 25–28 jako jeden ciąg (akapit 27 dochodzi do karty 28)
P.merge('u5', 'u6')            # … razem z hasłem 24 (bez dziury przy karcie 24)
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 27 – nagłówki 31 (obok karty 31), 34 (prawy łam, x0), 37 (obok karty 36)
P = Patch(D, 27); P.restore(); headings(P)
fix_x0(P, 'u6')
head_merge(P, 'u3', 'u4')
head_merge(P, 'u6', 'u7')
head_merge(P, 'u12', 'u13')
P.merge('u6', 'u9')            # akapit 36 przerwany w unitize wierszami z karty 36 – jeden ciągły łam
u = P.unit('u6')               # akapit 36 (cały tekst) kończy się tam, gdzie część z u9 – odstęp do 37
i36 = next(i for i, p in enumerate(u['paras']) if p['en'].startswith('(1947–?) Also characterized'))
u['paras'][i36]['lastbase'] = u['paras'][i36 + 1]['lastbase']
P.merge('u2', 'u3')            # lewy łam 29–33 jako jeden ciąg
P.merge('u6', 'u12')           # prawy łam 34–37 jako jeden ciąg
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 28 – nagłówki, wycięcia
P = Patch(D, 28); P.restore(); headings(P); set_cuts(P); col_bottom(P); track(P); P.save()

# s. 29 – nagłówki 44 (obok karty 44) i 50 (obok karty 50); prawy łam od x0 = 316,66
P = Patch(D, 29); P.restore(); headings(P)
for uid in ('u5', 'u6', 'u7'):
    fix_x0(P, uid)
head_merge(P, 'u2', 'u3')
head_merge(P, 'u6', 'u7')
P.merge('u5', 'u6')            # prawy łam 47–50 jako jeden ciąg
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 30 – nagłówek 52 (obok karty 51)
P = Patch(D, 30); P.restore(); headings(P)
head_merge(P, 'u3', 'u4')
P.merge('u2', 'u3')              # lewy łam 51–54 jako jeden ciąg
P.para('u2', -1, lastjust=True)  # akapit 54 przechodzi do prawego łamu
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 31 – nagłówki 58 (obok karty 58) i 62 (prawy łam); prawy łam od x0 = 316,66
P = Patch(D, 31); P.restore(); headings(P)
for uid in ('u5', 'u6', 'u7'):
    fix_x0(P, uid)
head_merge(P, 'u2', 'u3')
head_merge(P, 'u6', 'u7')
P.merge('u5', 'u6')              # prawy łam: dokończenie akapitu 61 i hasła 62–64 jako jeden ciąg
P.para('u2', -1, lastjust=True)  # akapit 61 przechodzi do prawego łamu
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 32 – nagłówek 67 (obok karty 67)
P = Patch(D, 32); P.restore(); headings(P)
head_merge(P, 'u3', 'u4')
P.merge('u2', 'u3')              # lewy łam 65–68 jako jeden ciąg
P.para('u2', -1, lastjust=True)  # akapit 68 przechodzi do prawego łamu
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 33 – nagłówki, wycięcia
P = Patch(D, 33); P.restore(); headings(P); set_cuts(P); col_bottom(P); track(P); P.save()

# s. 34 – nagłówek 80 (obok karty 80)
P = Patch(D, 34); P.restore(); headings(P)
head_merge(P, 'u2', 'u3')
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 35 – nagłówek 87 (obok karty 87)
P = Patch(D, 35); P.restore(); headings(P)
head_merge(P, 'u3', 'u4')
P.merge('u2', 'u3')              # lewy łam 86–89 jako jeden ciąg
P.para('u2', -1, lastjust=True)  # akapit 89 przechodzi do prawego łamu
set_cuts(P); col_bottom(P); track(P); P.save()

# s. 36 – nagłówki, wycięcia
P = Patch(D, 36); P.restore(); headings(P)
P.para('u2', -1, lastjust=True)  # akapit 96 przechodzi do prawego łamu
P.para('u3', -1, lastjust=True)  # akapit 100 przechodzi na s. 37
set_cuts(P); col_bottom(P); track(P); P.save()
