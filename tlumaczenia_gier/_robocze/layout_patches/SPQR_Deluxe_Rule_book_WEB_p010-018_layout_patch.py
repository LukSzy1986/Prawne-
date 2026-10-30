#!/usr/bin/env python3
# Łatki layoutu: SPQR_Deluxe_Rule_book_WEB, s. 10–18 (redaktor sp10_18, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'SPQR_Deluxe_Rule_book_WEB'

# akapity tekstu (10 pt), które w oryginale mają jeden wiersz i dlatego unitize oznaczył je „left” –
# po polsku łamią się na kilka wierszy, a łam oryginału jest justowany
KEEP_LEFT = ('EXAMPLE #1 (Voluntary)', 'EXAMPLE #2 (Rout/Retreat)')


def justify_single(P):
    for u in P.lay['units']:
        if u['kind'] != 'flow' or u.get('role') or not u.get('body'):
            continue
        for p in u['paras']:
            if (p['align'] == 'left' and p.get('nlines') == 1 and p['size'] <= 10.5
                    and 'Bold' not in p['font'] and p['en'] not in KEEP_LEFT):
                p['align'] = 'justify'


def clamp_boxes(P):
    """ramki z kolorowym tłem (UWAGA…): tekst ramki nie może wyjść poza jej tło, a tekst nad ramką
    nie może na nią wejść – granice tła odczytane z obrazu tła (bgimg, 1 px = 1 pt)"""
    from PIL import Image
    im = Image.open(f'/home/claude/lay/bgimg/{D}/p-{P.page:02d}.png').convert('RGB')
    flows = [u for u in P.lay['units'] if u['kind'] == 'flow' and not u.get('role')]
    for b in flows:
        if b.get('bg', '#ffffff') == '#ffffff':
            continue
        x = int(b['x0'] + 20)
        t = int(b['top'])
        while t > 0 and sum(im.getpixel((x, t))) < 740:
            t -= 1
        e = int(b['bottom'])
        while e < im.height - 1 and sum(im.getpixel((x, e))) < 740:
            e += 1
        top, bot = t + 1, e - 1
        b['maxBottom'] = round(min(b.get('maxBottom', b['bottom']), bot + 0.5), 2)
        for u in flows:
            if u is b or u['x0'] > b['x1'] or u['x1'] < b['x0'] or u['bottom'] > b['top']:
                continue
            if u.get('maxBottom', u['bottom']) > top - 1.0:
                u['maxBottom'] = round(top - 1.0, 2)


# Skala strony (wynik fit.py) – do kompensacji stopnia nagłówków wewnątrz jednostek tekstu (QA 26.10:
# nagłówki X.Y mają 12 pt, rozdziałów 18 pt, niezależnie od skali tekstu strony). Po zmianie trans
# sprawdzić page_scale w fit i w razie potrzeby uaktualnić.
HEAD65_BASE = 472.5   # s. 15: linia bazowa nagłówka 6.5 (QA r3: odstęp nad nagłówkiem ok. 12 pt)
HEAD_S = {10: 0.862, 11: 0.857, 12: 0.859, 13: 0.87, 14: 0.873, 15: 0.867, 16: 0.863, 17: 0.88, 18: 0.859}


def fix_headings(P):
    """nagłówki (Bold >= 12 pt): w osobnych jednostkach – własna skala (12/18 pt, bez skali strony);
    wewnątrz jednostek tekstu – stopień i interlinia podzielone przez skalę strony (po skalowaniu = 12 pt)"""
    s = HEAD_S[P.page]
    for u in P.lay['units']:
        if u['kind'] != 'flow' or u.get('role'):
            continue
        heads = [p for p in u['paras'] if 'Bold' in p['font'] and p['size'] >= 12]
        if not heads:
            continue
        if len(heads) == len(u['paras']):
            u['body'] = False
            continue
        for p in heads:
            p['size'] = round(p['size'] / s, 3)
            p['pitch'] = round(p['pitch'] / s, 3)


# QA 26.10 (zasada 4): ramki z kolorowym tłem – dolny odstęp tekstu od krawędzi tła ≈ górny. Tekst w ramce
# ma stopień tekstu głównego (skala strony), więc puste dno wypełnia większa interlinia (×f, najwyżej 1,2)
# i ewentualne przesunięcie w dół (dy, pt). Wartości z pomiaru podglądów (boxfill.py, redaktor sp10_18).
BOXFILL = {
    10: [('HISTORICAL DIGRESSION: It seem', 1.135, 0.0), ('DESIGN NOTE: A single named Tr', 1.119, 0.0)],
    12: [('PLAY NOTE: Momentum (and Trump', 1.091, 0.0)],
    13: [('DESIGN NOTE: This is a game me', 1.2, 4.4), ('PLAY NOTE: The No-Momentum res', 1.149, 0.0)],
    14: [('PLAY NOTE: We have provided so', 1.2, 1.7), ('HISTORICAL NOTE: As with previ', 1.11, 0.0), ('PLAY NOTE: Players should neve', 1.102, 0.0)],
    15: [('HISTORICAL NOTE: What the game', 1.2, 6.3), ('DESIGN NOTE: Because of its le', 1.117, 0.0), ('PLAY NOTE: Orderly Withdrawal ', 1.119, 0.0)],
    16: [('PLAY NOTE: Yes, it says within', 1.088, 0.0), ('HISTORICAL NOTE: Orderly Withd', 1.2, 4.0), ('PLAY NOTE: As noted in 6.51, t', 1.091, 0.0)],
    17: [('DESIGN NOTE: The stacking rule', 1.089, 0.0)],
    18: [('DESIGN NOTE: The vaunted Roman', 1.044, 0.0), ('DESIGN NOTE: On the battlefield', 1.141, 0.0)],
}


def fill_boxes(P):
    for en, f, dy in BOXFILL.get(P.page, []):
        u = P.find(en)
        for i, p in enumerate(u['paras']):
            P.para(u, i, pitch=round(p['pitch'] * f, 3))
        if dy:
            P.move_to(u, base=round(u['paras'][0]['base'] + dy, 2))


def clamp_bottom(P, ymax=739.5):
    """QA 26.10: ostatni wiersz łamu nie niżej niż dół łamu oryginału (ok. 735–740 pt) i ≥ 5 pt nad stopką"""
    for u in P.lay['units']:
        if u['kind'] == 'flow' and not u.get('role') and u.get('maxBottom', u['bottom']) > ymax:
            u['maxBottom'] = max(ymax, u['bottom'])


PAGES = {}


def page(n):
    def deco(fn):
        PAGES[n] = fn
        return fn
    return deco


@page(10)
def p10(P):
    # „4.7 DOWÓDCY A ODDZIAŁY BOJOWE WROGA” w 12 pt jest o ok. 6% szerszy od łamu – ścieśniony (hs 0,92; w trans spacja włoskowa przed „A” – optycznie znikał odstęp Y A;
    # QA r3: najmniejsze ścieśnienie, przy którym zostaje w jednym wierszu jak w oryginale)
    P.para(P.find('4.7 LEADERS & ENEMY COMBAT UNITS'), 0, hs=0.92)


@page(11)
def p11(P):
    # „5.0 …” – sztuczne prawe wcięcie nagłówka dwuwierszowego (ściskało litery)
    P.para(P.find('5.0 LEADER ACTIVATION AND ORDERS'), 0, right=0)
    # QA r3: tracking nagłówka 18 pt ok. −0,3 pt (hs 0,967) zamiast −1 pt z oryginału (znikały odstępy)
    P.para(P.find('5.0 LEADER ACTIVATION AND ORDERS'), 0, hs=0.967)
    # pierwszy punktor 4.91 od miejsca z oryginału (pod żetonem dowódcy słoni) – inaczej przy skali
    # strony < 1 jego pierwszy wiersz wpada na obrazek opływany tekstem
    u = P.find('4.9 ELEPHANT COMMAND')
    n = P.split(u, 3)
    # QA r3: nagłówek 4.9 (12 pt, dwa wiersze – trans <br>) w miejscu z oryginału (odstęp nad nim jak
    # w oryginale); drugi wiersz „(ZASADA OPCJONALNA)” opływa żeton dowódcy słoni; punktory tuż pod żetonem
    P.move_to(n, base=180.0)
    # QA r3: odstęp nad „5.0” za duży (tekst strony w skali < 1 kończy się wyżej niż w oryginale) –
    # nieco większe odstępy między akapitami 4.92–4.94 (+2,3 pt przed każdym akapitem bez punktora)
    # i nagłówek 5.0 ze wstępem wyżej o 3 pt (ramka WAŻNE jest w tle – zostaje)
    add = 0.0
    for i, p in enumerate(n['paras']):
        if i and not p['en'].startswith('•'):
            add += 2.3
        if add:
            P.para(n, i, base=round(p['base'] + add, 2), lastbase=round(p['lastbase'] + add, 2),
                   top=round(p['top'] + add, 2), bottom=round(p['bottom'] + add, 2))
    for key in ('5.0 LEADER ACTIVATION AND ORDERS', 'Combat units may move and fight'):
        h = P.find(key)
        mb = h.get('maxBottom', h['bottom'])
        P.move_to(h, base=round(h['paras'][0]['base'] - 3.0, 2))
        P.set(h, maxBottom=round(mb - 3.0, 2))


@page(12)
def p12(P):
    # nagłówek „5.3 IMPET (MOMENTUM)” w miejscu z oryginału – tuż nad ramką UWAGA DO ROZGRYWKI
    P.split(P.find('5.3 MOMENTUM'), 7)
    # drugi akapit 5.26 przechodzi do prawego łamu po pełnym zdaniu („…z impetu (Momentum).”) –
    # lewy łam o wiersz krótszy (QA: nie niżej niż dół łamu oryginału), mniejsza luka nad 5.3


@page(13)
def p13(P):
    # QA r3: „Wyjątek” (5.34) w trzech wierszach jak w oryginale – odstęp nad nagłówkiem 5.4 ok. 11 pt
    # (lekko ciaśniejszy skład akapitu: hs 0,96, ws −0,05 em; trans: bez nawiasów (Elite rule), (Game Turn))
    P.para(P.find('A leader first activated by the Elite rule'), 0, hs=0.96, ws=-0.05)
    # przykład do 5.53 przechodzi na s. 14 (po „Za drugim razem Leliusz ma”) – ostatni wiersz łamu
    # wypełniony w ok. 85%, bez justowania (QA r3)


@page(14)
def p14(P):
    # QA r3: tracking nagłówka 18 pt ok. −0,3 pt (hs 0,967)
    P.para(P.find('6.0 MOVEMENT'), 0, hs=0.967)
    # „6.2 TEREN (TERRAIN)” – nagłówek z nawiasem EN może sięgać do prawej krawędzi łamu
    u = P.lines_to_flow(P.find('6.2 TERRAIN'), align='left')
    P.set(u, maxRight=567.0, nowrap=True)


@page(15)
def p15(P):
    # odstęp nad nagłówkiem „6.4 ODDZIAŁY FALANGI” (bez niego ostatni wiersz 6.32 dotykał nagłówka)
    P.set(P.find('6.27 The Movement Cost Chart'), maxBottom=269.5)
    # QA: luka przed ramką UWAGA DO ROZGRYWKI (tło ramki stałe) – nagłówek 6.5 ze wstępem jako osobna
    # jednostka, dosunięta do ramki; wolne miejsce przechodzi nad nagłówek (przerwa między punktami)
    n = P.split(P.find('6.5 ORDERLY WITHDRAWAL'), 4)
    P.move_to(n, base=HEAD65_BASE)
    # 6.51 przechodzi na s. 16 (po „wycofuje się (withdraws)”) – ostatni, pełny wiersz łamu justowany
    P.para(P.find('During an enemy Movement and Missile Fire Segment, or at any time'), 0, lastjust=True)


@page(17)
def p17(P):
    # przykład nr 1 do 6.63 przechodzi na s. 18 – ostatni (pełny) wiersz łamu justowany jak w oryginale
    P.para(P.find('EXAMPLE #1 (Voluntary)'), 1, lastjust=True)


@page(18)
def p18(P):
    # 6.66 przechodzi do prawego łamu po zdaniu „…(wyjątkiem jest 9.66).” – mniejsza luka nad 6.7 (QA)
    # 6.73 przechodzi na s. 19 – ostatni wiersz BEZ justowania (wypełniony w ok. 90%; justowany był
    # rozstrzelony > 0,9 em – QA)
    # QA: ramka UWAGA PROJEKTANTA (lewa) – tekst dotykał dolnej krawędzi tła; stopień −0,25 pt (po skali)
    P.para(P.find('The vaunted Roman flexibility'), 0, size=9.7)


for n in range(10, 19):
    P = Patch(D, n)
    P.restore()
    justify_single(P)
    if n in PAGES:
        PAGES[n](P)
    fix_headings(P)
    fill_boxes(P)
    clamp_boxes(P)
    clamp_bottom(P)
    P.save()
