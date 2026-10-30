#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Background_Book_WEB, s. 37–48 (redaktor tb37_48, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import os, sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Background_Book_WEB'


def heads14(P):
    """Nagłówki haseł kart (MyriadPro-BlackCondIt-SC700): w oryginale wersaliki 14 pt, kapitaliki 9,8 pt;
    unitize rozpoznał część nagłówków jako 10 pt (stopień kapitalików) – ujednolicenie do 14 pt
    (kapitaliki składane font-variant: small-caps = 0,7 × 14 pt = 9,8 pt, jak w oryginale).
    Wcięcie wiszące (hang) wykryte w części nagłówków jest pozorne (nagłówki EN są jednowierszowe) –
    zerowane, żeby złamany polski nagłówek (nawias EN w 2. wierszu) zaczynał się od lewej krawędzi łamy."""
    for u in P.lay['units']:
        if u['kind'] != 'flow':
            continue
        for i, p in enumerate(u['paras']):
            if 'SC700' in p['font']:
                P.para(u, i, size=14.0, pitch=16.8, hang=0.0)


def cut(P, uid, i, **kw):
    """granice opływania ilustracji karty (y w pt) – dopasowanie do krawędzi karty na tle"""
    cs = P._u(uid)['paras'][i].get('cuts', [])
    assert len(cs) == 1, (P.page, uid, i, cs)
    cs[0].update(kw)


# QA 27.10: dół tekstu głównego ≥ ok. 5 pt nad stopką (y 753,3) i nie niżej niż najniższa łama oryginału
# na danej stronie (+1 pt): maxBottom jednostek tekstu głównego = min(obecny, BOTTOM[strona])
BOTTOM = {37: 730.6, 38: 746.3, 39: 746.9, 40: 746.9, 41: 746.3, 42: 720.5, 43: 694.1, 44: 745.1, 45: 741.0}


CUTGAP = {
    (37, 'u2', 4): 8.0,
    (38, 'u2', 5): 8.0,
    (39, 'u2', 1): 8.0,
    (39, 'u2', 3): 8.0,
    (40, 'u2', 1): 9.5,
    (40, 'u2', 3): 9.5,
    (40, 'u3', 1): 5.5,
    (41, 'u4', 2): 8.0,
    (42, 'u2', 1): 6.0,
    (42, 'u3', 3): 9.5,
    (43, 'u2', 3): 8.5,
    (43, 'u5', 1): 6.5,
    (43, 'u8', 1): 9.5,
    (44, 'u2', 1): 8.5,
    (44, 'u2', 5): 9.5,
    (44, 'u4', 3): 7.5,
    (45, 'u2', 2): 8.0,
    (45, 'u2', 7): 9.5,
    (45, 'u4', 1): 8.0,
    (46, 'u2', 1): 8.5,
    (46, 'u2', 3): 6.5,
    (46, 'u3', 1): 5.5,
}

# QA 27.10: stała skala tekstu głównego strony (fixscale wszystkich jednostek tekstu głównego) – poprawki
# łamania pojedynczych wierszy nie przelewają wtedy całej strony; wartości = skala strony po poprawkach
FIXSCALE = {37: 0.925, 38: 0.888, 39: 0.908, 40: 0.925, 41: 0.9, 42: 0.901, 43: 0.909, 44: 0.876, 45: 0.884,
            46: 0.897}


def narrow_cuts(P):
    """QA 27.10: opływanie kart – odstęp tekstu od krawędzi karty wg CUTGAP (pt; w unitize ok. 8–10 pt), dobrany
    dla każdej karty tak, by w wąskich łamach obok kart nie było rozstrzelonych wierszy (qa/search.py);
    krawędź karty mierzona na obrazie tła bgimg (1 px = 1 pt)."""
    from PIL import Image
    im = Image.open(f'/home/claude/lay/bgimg/{D}/p-{P.page:02d}.png').convert('L')
    for u in P.lay['units']:
        for i, p in enumerate(u.get('paras', [])):
            for c in p.get('cuts', []):
                gap = CUTGAP.get((P.page, u['id'], i))
                if gap is None:
                    continue
                y0, y1 = int(c['top']) + 4, int(c['bottom']) - 4
                if c['side'] == 'l':
                    xa, xb = int(u['x0']), int(u['x0'] + c['w'])
                else:
                    xa, xb = int(u['x1'] - c['w']), int(u['x1'])
                xs = [x for x in range(xa, xb) if any(im.getpixel((x, y)) < 235 for y in range(y0, y1, 2))]
                if not xs:
                    continue
                if c['side'] == 'l':
                    w = max(xs) + 1 + gap - u['x0']
                else:
                    w = u['x1'] - (min(xs) - gap)
                c['w'] = round(w, 2)


def bottoms(P):
    narrow_cuts(P)
    y = BOTTOM.get(P.page)
    fs = FIXSCALE.get(P.page)
    for u in P.lay['units']:
        if u['kind'] == 'flow' and u.get('body'):
            if y is not None:
                u['maxBottom'] = round(min(u.get('maxBottom', u['bottom']), y), 2)
            if fs is not None and not os.environ.get('FS_OFF'):
                u['fixscale'] = fs


# s. 37–42 – tylko nagłówki haseł
for n in (37, 38, 39, 40, 41, 42):
    P = Patch(D, n); P.restore()
    heads14(P)
    if n == 39:
        # hasło P3 przechodzi do prawej łamy – ostatni wiersz lewej łamy justowany
        P.para(P.find('The Berlin Wall arose'), 3, lastjust=True)
    if n == 41:
        # hasło P12 przechodzi do prawej łamy – ostatni wiersz lewej łamy justowany
        P.para(P.find('The declaration of martial law'), 5, lastjust=True)
    bottoms(P)
    P.save()

# s. 43 – nagłówek działu „KARTY WARIANTU WSCHODZĄCE CZERWONE SŁOŃCE” w dwóch wierszach (polski tytuł
# nie mieści się w jednym wierszu szpalty); hasło RS1 niżej o ok. 11 pt; hasło RS2 („2. ANZUS”) jako osobna
# jednostka niżej o 26,5 pt, żeby nagłówek i pierwsze wiersze stały nad ilustracją karty RS2 (y = 418)
P = Patch(D, 43); P.restore()
heads14(P)
h = P.find('RED SUN RISING VARIANT CARDS')
P.set(h, nowrap=False, maxBottom=112.0)
u = P.find('As the Cold War deepened')
P.move_to(u, base=124.5)                      # QA: odstęp ok. 8 pt pod dwuwierszowym nagłówkiem działu
cut(P, u, 1, top=145.0)                       # opływanie karty RS1 od jej górnej krawędzi (y 147)
n = P.split(u, 2)
P.move_to(n, base=401.0)
P.set(u, maxBottom=379.0)                    # odstęp przed nagłówkiem „2. ANZUS” jak między hasłami
bottoms(P)
P.save()

# s. 44 – nagłówek „3. Chinese Civil War” (osobna jednostka obok ilustracji karty) scalony z tekstem
# lewej łamy; opływanie karty RS3 od górnej krawędzi karty (y = 72), żeby nagłówek nie wchodził na kartę
P = Patch(D, 44); P.restore()
heads14(P)
a = P.find('3. chinese civil War')
b = P.find('Renewed after Japan')
P.merge(a, b)
P.set(a, body=True, nowrap=False, maxBottom=753.7)
cut(P, a['id'], 1, top=72.0)
# karta RS5: opływanie od górnej krawędzi karty (y = 485) – złamany nagłówek „5. …” nie wchodzi obok karty
cut(P, a['id'], 5, top=484.0)
# karta RS7: opływanie do dolnej krawędzi karty (y = 371); hasła 8–10 jako osobna jednostka od miejsca
# pod kartą (nagłówek „8. …” pod kartą, jak w oryginale, a nie złamany na 3 wiersze obok niej)
r = P.find('Relations between Joseph Stalin')
cut(P, r, 3, bottom=375.0)
n = P.split(r, 4)
P.move_to(n, base=388.0)
P.set(r, maxBottom=376.0)
bottoms(P)
P.save()

# s. 45 – nagłówki; hasło 13 (akapit EN rozbity na 2 akapity przy ilustracji) – całość w akapicie 6:
# wcięcie pierwszego wiersza zamiast lewego wcięcia całego akapitu, justowanie; opływanie karty RS13 do
# jej dolnej krawędzi (y = 737), lewa łama do dolnej krawędzi karty (maxBottom 741; w unitize 728,96 –
# ostatni wiersz obok karty, bez osieroconego wiersza pod kartą)
P = Patch(D, 45); P.restore()
heads14(P)
u = P.find('As Cold War tensions spread')
P.para(u, 6, left=0.0, indent=3.18, align='justify')
cut(P, u['id'], 7, bottom=741.0)
P.set(u, maxBottom=741.0)
# karta RS11: opływanie od górnej krawędzi karty (y = 165) – nagłówek „11. Air America” nad kartą
cut(P, u['id'], 2, top=164.5)
# karta RS14: opływanie od górnej do dolnej krawędzi karty (y = 186–334)
cut(P, P.find('The destruction of the Second World War'), 1, top=185.0, bottom=338.0)
bottoms(P)
P.save()

# s. 46 – nagłówki; karta RS17: opływanie od górnej (y = 316) do dolnej krawędzi karty (y = 463)
P = Patch(D, 46); P.restore()
heads14(P)
cut(P, P.find('For years, Ferdinand Marcos'), 3, top=315.0, bottom=467.0)   # QA: zwężenie od górnej krawędzi karty (y 316)
bottoms(P)
P.save()

# s. 47 – Źródła ilustracji: wszystkie pozycje jednakowo wyrównane, bez wcięcia wiszącego (unitize przypisał
# pozycjom jednowierszowym pozorne wcięcie wiszące);
# dolny margines w niebieskiej ramce (ramka do y = 746)
P = Patch(D, 47); P.restore()
u = P.find('Duck and Cover. Civil Defense')
for i in range(len(u['paras'])):
    # QA 27.10: wyrównanie do lewej (bez dzielenia) – przy justowaniu długie, niepodzielne kody licencji
    # i nazwy archiwów dawały rozstrzelone wiersze (16., 33., 36., 41., 58., 67., RS18.)
    P.para(u, i, align='left', hang=0.0, indent=0.0, left=0.0, right=0.0)
P.set(u, maxBottom=726.0)
bottoms(P)
P.save()
