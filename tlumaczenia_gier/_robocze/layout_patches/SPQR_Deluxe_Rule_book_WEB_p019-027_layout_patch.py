#!/usr/bin/env python3
# Łatki layoutu: SPQR_Deluxe_Rule_book_WEB, s. 19–27 (redaktor sp19_27, 2026-10-26)
# Idempotentna: każda strona startuje od kopii z unitize (P.restore()).
import copy
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'SPQR_Deluxe_Rule_book_WEB'


def pidx(P, uid, en):
    """indeks akapitu jednostki po początku tekstu EN"""
    hits = [i for i, p in enumerate(P.unit(uid)['paras']) if p['en'].startswith(en)]
    if len(hits) != 1:
        raise KeyError(f'{uid}: „{en}” – {len(hits)}')
    return hits[0]


def absorb(P, uid, en_from, en_to):
    """akapit en_from obejmuje (geometria EN) kolejne akapity aż do en_to włącznie – te są w trans
    puste, więc odstęp do następnego akapitu liczy się od ostatniego wiersza en_to"""
    u = P.unit(uid)
    i, j = pidx(P, uid, en_from), pidx(P, uid, en_to)
    P.para(uid, i, lastbase=u['paras'][j]['lastbase'])
    return i, j


def justify_single(P, skip=()):
    """akapity tekstu (10 pt) jednowierszowe w oryginale, wyrównane do lewej – po polsku zwykle
    zajmują więcej wierszy; justowanie (ostatni wiersz i tak do lewej) jak w akapitach wielowierszowych"""
    for u in P.lay['units']:
        if u['kind'] != 'flow' or u.get('nowrap') or u.get('role') or u['id'] in skip:
            continue
        for p in u['paras']:
            if p.get('align') == 'left' and p.get('size') == 10.0 and p.get('nlines', 1) == 1:
                p['align'] = 'justify'


def p20(P):
    # 7.2: nagłówek + pierwszy wiersz definicji ZOC (u18) i dalszy ciąg (u19) – jedna jednostka;
    # definicja w całości w akapicie u18[1], u19[0] pusty; diagram ZOC opływany jednym wycięciem
    u = P.find('7.2 ZONES OF CONTROL')
    P.merge(u, 'u19')
    i, j = absorb(P, u['id'], 'ZOC are those hexes', 'the hex occupied')
    P.para(u, i, align='justify')
    for p in u['paras']:
        p.pop('cuts', None)
    P.para(u, i, cuts=[{'side': 'r', 'top': 242.0, 'bottom': 349.0, 'w': 121.47}])
    # etykiety „Flank” po lewej stronie diagramów: wyrównanie do prawej (polski napis dłuższy)
    for uid in ('u5', 'u10'):
        P.line(uid, 0, align='right')


def p22(P):
    # 8.17: punktor oszczepników rozbity w oryginale na dwa akapity (obok znaczników) – jeden akapit;
    # wycięcie obejmuje oba znaczniki (MISSILE No i MISSILE LOW)
    u = P.find('Each different missile type')
    i, j = absorb(P, u['id'], '• Javelinists, other than LG', 'sile Low whenever')
    P.para(u, i, align='justify')
    k = pidx(P, u['id'], '• Archers, Slingers')
    P.para(u, k, cuts=[{'side': 'r', 'top': 452.0, 'bottom': 531.0, 'w': 45.43}])
    # 8.15 przechodzi z lewego łamu do prawego (u7[0]) – ostatni wiersz lewego łamu justowany
    P.para(P.find('8.15 Missile Fire Resolution'), 0, lastjust=True)


def p24(P):
    # przykład [Beneventum]: ostatni akapit rozbity w oryginale przed „Z.” – jeden akapit
    u = P.find('The Macedon LC')
    absorb(P, u['id'], 'The Macedon LC', '<b>Z</b>. Whichever')


def p26(P):
    # lista modyfikatorów rzutu: 6 pozycji („+1 dla …”), wcięcie wiszące do początku tekstu po „+1” (x ≈ 61)
    u = P.find('The above DR is modified')
    ps = u['paras']
    tmpl = ps[1]
    bases = [(ps[1]['base'], ps[2]['base']), (ps[3]['base'], ps[4]['base']),
             (ps[5]['base'], ps[5]['base']), (ps[5]['base'] + 14.16, ps[5]['base'] + 14.16),
             (ps[5]['lastbase'], ps[5]['lastbase']), (ps[6]['base'], 182.61)]
    items = []
    en = ['+1 Elephant/PH-HI', '+1 African/Indian', '+1 attacked by DD Phalanx', '-1 DD Phalanx attacked',
          '-1 BI Ferocity', '+2 attacked by BI Ferocity (9.94).']
    prev = ps[0]['lastbase']
    for (b0, b1), e in zip(bases, en):
        p = copy.deepcopy(tmpl)
        p.update({'en': e, 'left': 2.68, 'hang': 13.46, 'indent': 0.0, 'right': 0.0, 'pitch': 12.0,
                  'align': 'justify', 'base': round(b0, 2), 'lastbase': round(b1, 2),
                  'top': round(b0 - 6.93, 2), 'bottom': round(b1 + 3.07, 2),
                  'nlines': 1 + round((b1 - b0) / 12.0), 'gap': round(b0 - prev, 2)})
        prev = b1
        items.append(p)
    u['paras'] = [ps[0]] + items
    u['bottom'] = 185.68
    u['maxBottom'] = 190.0
    P.lay['units'].remove(P.unit('u3'))


def p21(P):
    # wyjątki 7.33: pierwszy punktor prawego łamu („Routed units and units In Column…”) przeniesiony
    # na koniec lewego łamu (u4) – po polsku prawy łam nad ramką uwagi (u7) się nie mieści
    u4, u6 = P.unit('u4'), P.unit('u6')
    if not u6['paras'][0]['en'].startswith('• Routed units'):
        return
    b = copy.deepcopy(u6['paras'][0])
    last = u4['paras'][-1]
    dy = (last['lastbase'] + 13.44) - b['base']
    for k in ('top', 'bottom', 'base', 'lastbase'):
        b[k] = round(b[k] + dy, 2)
    b['gap'] = 13.44
    b['x0'], b['x1'] = last['x0'], last['x1']
    u4['paras'].append(b)
    u4['bottom'] = b['bottom']
    first = u6['paras'].pop(0)
    sh = u6['paras'][0]['base'] - first['base']
    for p in u6['paras']:
        for k in ('top', 'bottom', 'base', 'lastbase'):
            p[k] = round(p[k] - sh, 2)
    u6['paras'][0]['gap'] = None
    u6['base'] = u6['paras'][0]['base']
    # 8.11 obok żetonów (łam ok. 91 pt): część akapitu w wąskim pasie jako osobny akapit wyrównany
    # do lewej (runda 3 – justowanie dawało odstępy > 1 em), dalszy ciąg tego samego akapitu
    # justowany, bez odstępu i wcięcia (trans: u12[0] – wąski pas, u12[1] – ciąg dalszy)
    u12 = P.unit('u12')
    if len(u12['paras']) == 2:
        a = u12['paras'][0]
        b = copy.deepcopy(a)
        a['align'] = 'left'
        b['en'] = '(8.11 – ciąg dalszy)'
        b['gap'] = a['pitch']
        b['base'] = round(a['lastbase'] + a['pitch'], 2)   # render liczy odstęp z base − poprzedni lastbase
        b['indent'] = 0.0
        b.pop('cuts', None)
        u12['paras'].insert(1, b)
    # ramka uwagi do rozgrywki (szare tło x 315–566): tekst o 2 pt szerzej z każdej strony
    P.set('u7', x0=317.0, x1=565.0, maxRight=565.0)


PAGES = {20: p20, 21: p21, 22: p22, 24: p24, 26: p26}

# Granice dolne (maxBottom) przy ramkach uwag (kolorowe tło w bgimg 72 dpi, pomiar 26.10):
# tekst w ramce – dół ramki − 1 pt; tekst nad ramką/grafiką – górna krawędź ramki − 2 pt
# (unitize liczy maxBottom do następnej jednostki, a ta zaczyna się dopiero pod brzegiem ramki).
# Poprawki po kontroli wizualnej (QA 26.10): odstęp nad diagramem (s. 19 u2, s. 20 u3) i dół łamów
# blisko dołu łamu oryginału, ≥ 5 pt nad stopką (s. 20 u12, s. 21 u4, s. 22 u5, s. 26 u8).
MAXB = {
    19: {'u2': 334.0},
    20: {'u3': 178.0, 'u12': 728.0, 'u14': 90.0, 'u15': 119.0, 'u16': 176.0, 'u17': 216.0, 'u18': 609.0,
         'u24': 637.0},
    21: {'u3': 187.0, 'u4': 742.0, 'u6': 121.0, 'u7': 173.0, 'u11': 442.0, 'u13': 656.0},
    22: {'u3': 579.0, 'u4': 619.0, 'u5': 729.0, 'u8': 256.0},
    23: {'u2': 320.0, 'u3': 524.0, 'u6': 504.0, 'u8': 551.0},
    24: {'u2': 340.0, 'u4': 475.5, 'u3': 404.0, 'u9': 513.0, 'u10': 596.0, 'u11': 671.0, 'u12': 725.0},
    25: {'u2': 104.0, 'u3': 222.0},
    26: {'u6': 526.0, 'u7': 602.0, 'u8': 737.0},
    27: {'u2': 201.0, 'u3': 229.0, 'u6': 471.0, 'u7': 547.0},
}

# Runda 3 (27.10): tekst w ramkach uwag w skali tekstu głównego strony (jak w oryginale – 10 pt
# wszędzie; w rundzie 2 ramki miały własną skalę, co dawało różne stopnie na jednej stronie).
# BOX: uid → (górna, dolna krawędź tła ramki, pt). Tekst ramki: body, maxBottom = dół tła − 4 pt.
# BOXFIT: uid → (interlinia nominalna, przesunięcie dy) – wypełnienie tła: interlinia ≤ ~+10 %,
# reszta wolnego miejsca rozdzielona po równo nad i pod tekstem (dy).
BOX = {
    20: {'u15': (92, 120), 'u17': (178, 217), 'u24': (611, 638)},
    21: {'u3': (137, 188), 'u7': (123, 174), 'u11': (342, 443), 'u13': (629, 657)},
    22: {'u4': (581, 620), 'u8': (122, 257)},
    23: {'u2': (54, 321), 'u3': (328, 525), 'u8': (524, 552)},
    24: {'u3': (342, 405), 'u9': (439, 514), 'u10': (522, 597)},
    25: {'u2': (54, 105), 'u3': (112, 223)},
    26: {'u7': (528, 603)},
    27: {'u3': (203, 230), 'u7': (473, 548)},
}
BOXFIT = {
    21: {'u3': (13.2, 0.3), 'u7': (13.01, 0.0), 'u11': (13.2, 1.7)},
    22: {'u8': (12.46, 0.0)},
    23: {'u2': (13.2, 16.6), 'u3': (13.15, 0.0)},
    24: {'u3': (12.99, 0.0), 'u9': (13.08, 0.0), 'u10': (13.2, 0.2)},
    25: {'u2': (13.03, 0.0), 'u3': (13.2, 0.4)},
    26: {'u7': (13.2, 1.0)},
    27: {'u7': (13.2, 0.7)},
}


# QA: nagłówki 12 pt (bez wspólnej skali strony) – nagłówek wydzielony w osobną jednostkę
# (początek EN, ścieśnienie hs dla zbyt długich polskich nagłówków)
HEADS = {
    19: [('6.8 PRE-ARRANGED', 0.95)],
    20: [('7.1 FACING', None), ('7.2 ZONES OF CONTROL', None)],
    21: [('7.3 SHOCK REQUIREMENTS', None)],
    23: [('8.2 REACTION FIRE', None)],
}


# Runda 3 (27.10): drobne ustawienia akapitów (początek EN akapitu → pola akapitu: hs/ws/align …)
# przeciw rozstrzelonym wierszom w wąskich łamach
PARA = {
    20: [('7.0 FACING AND', {'hs': 0.967})],
    21: [('8.0 COMBAT', {'hs': 0.967, 'ws': 0.04})],
}


def head_split(P, en):
    hits = [(u, i) for u in P.lay['units'] if u['kind'] == 'flow' and not u.get('nowrap')
            for i, p in enumerate(u['paras']) if p['en'].startswith(en)]
    if len(hits) != 1:
        raise KeyError(f'nagłówek „{en}” – {len(hits)}')
    u, i = hits[0]
    if i + 1 < len(u['paras']):
        P.split(u, i + 1)
    h = P.split(u, i) if i > 0 else u
    P.set(h, body=False, nowrap=True, maxRight=u.get('maxRight', u['x1']))
    return h


def p21_anchor(P):
    # 7.32: akapit zakotwiczony w miejscu oryginału (podział jednostki) – numer akapitu
    # i pierwszy wiersz obok znacznika SHOCK, jak w oryginale
    for en in ('<b>7.32</b>',):
        hits = [(u, i) for u in P.lay['units'] if u['kind'] == 'flow'
                for i, p in enumerate(u['paras']) if p['en'].startswith(en)]
        u, i = hits[0]
        if i > 0:
            P.split(u, i)


for n in range(19, 28):
    P = Patch(D, n); P.restore()
    justify_single(P)
    if n in PAGES:
        PAGES[n](P)
    for uid, mb in MAXB.get(n, {}).items():
        P.set(uid, maxBottom=mb)
    for uid, (bt, bb) in BOX.get(n, {}).items():
        P.set(uid, body=True, maxBottom=bb - 4.0)
        u = P.unit(uid)
        if uid in BOXFIT.get(n, {}):
            pitch, dy = BOXFIT[n][uid]
            for i in range(len(u['paras'])):
                P.para(uid, i, pitch=pitch)
            P.move_to(uid, base=round(u['paras'][0]['base'] + dy, 2))
            P.set(uid, maxBottom=bb - 4.0)
    for en, hs in HEADS.get(n, []):
        h = head_split(P, en)
        if hs:
            P.para(h, 0, hs=hs)
    if n == 19:
        # podpis pod diagramem: jak w oryginale do lewej (po polsku dwa wiersze – bez rozstrzelenia)
        P.para(P.find('A Phalanx column moves'), 0, align='left')
    if n == 21:
        p21_anchor(P)
    for en, kw in PARA.get(n, []):
        hits = [(u, i) for u in P.lay['units'] if u['kind'] == 'flow'
                for i, p in enumerate(u['paras']) if p['en'].startswith(en)]
        if len(hits) != 1:
            raise KeyError(f's. {n}: akapit „{en}” – {len(hits)}')
        P.para(hits[0][0], hits[0][1], **kw)
    P.save()
