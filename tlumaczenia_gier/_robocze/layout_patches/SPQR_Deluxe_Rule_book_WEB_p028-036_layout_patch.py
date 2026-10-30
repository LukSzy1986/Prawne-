#!/usr/bin/env python3
# Łatki layoutu: SPQR_Deluxe_Rule_book_WEB, s. 28–36 (redaktor sp28_36, 2026-10-26; poprawki QA 26.10)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'SPQR_Deluxe_Rule_book_WEB'

# Akapity jednowierszowe w EN (punktory, zdania wprowadzające) unitize oznaczył jako wyrównane do lewej;
# w oryginale łam jest justowany – polski tekst, który się zawija, ma być justowany jak sąsiednie akapity.
JUST = {30: [('u13', (3, 5))], 31: [('u4', (1,)), ('u14', (1, 2, 5))], 32: [('u15', (3, 4, 5))],
        33: [('u11', (3, 10, 11))], 34: [('u7', (2, 8))]}

# QA: skala tekstu głównego strony (fit) – nagłówki 12 pt wewnątrz jednostek tekstu głównego dostają
# stopień 12/S, żeby po przeskalowaniu miały 12 pt jak nagłówki w osobnych jednostkach (K.4, QA 26.10)
S = {28: 0.853, 31: 0.856, 34: 0.863, 35: 0.868, 36: 0.854}

# QA (runda 3): ramki z tłem – stopień jak tekst główny strony (skala strony), jednolity w obrębie strony; interlinia
# dobrana tak, by dolny odstęp tekstu od krawędzi tła był zbliżony do górnego (ok. 3–5 pt), najwyżej 1,5
BOXV = {(29, 'This rule (as well as 8.6)'): (0.859, 12.58),
        (29, 'This (and its sister rule'): (0.859, 13.58),
        (30, 'This rule is not used in Beneventum'): (0.87, 11.77),
        (30, 'One of the problems with cavalry'): (0.87, 13.55),
        (31, 'This will usually place the victorious'): (0.856, 12.35),
        (31, 'The routing player, where possible'): (0.856, 13.43),
        (31, 'Despite their drawbacks'): (0.856, 15.0),
        (32, 'Most infantry were trained'): (0.873, 13.35),
        (32, 'Several historians portray'): (0.873, 12.86),
        (33, 'Historically, the mahouts'): (0.861, 13.24),
        (33, 'Elephants did not fight in formations'): (0.861, 12.0),
        (33, 'The argument over which family'): (0.861, 14.81),
        (33, 'Skirmisher units were truly'): (0.861, 13.79),
        (34, 'This reflects the remarkable'): (0.863, 13.65),
        (34, 'To increase the crushing'): (0.863, 13.12),
        (35, 'The major advance in the science'): (0.868, 13.4),
        (36, 'The front side of the counter shows'): (0.854, 11.88),
        (36, 'These rules reflect the capabilities'): (0.854, 12.06),
        (36, 'This rule represents the feared'): (0.854, 13.5),
        (36, 'The chariots used by the Gallic'): (0.854, 13.79),
}

# Runda 3 (27.10): drobne korekty akapitów przeciw rozstrzeleniu wierszy – (strona, fragment EN jednostki, nr akapitu): pola
TUNE = {
        (28, 'The Charge:', 0): dict(hs=0.97),
        (29, 'rounded up to 4:1 since the Ph', 0): dict(hs=0.97),
        (30, '<b>8.61</b> Attacking Cavalry ', 1): dict(hs=0.955),
        (30, 'One of the problems with cavalry', 0): dict(hs=0.97),
        (33, '9.21 Orderly Withdrawal', 0): dict(hs=0.97),
        (33, '9.21 Orderly Withdrawal', 13): dict(hs=0.97),
        (33, '<b>9.15 Cavalry vs. Elephants:', 2): dict(hs=0.98),
        (34, '9.51 Phalanxes', 2): dict(hs=0.97),
        (34, '9.51 Phalanxes', 3): dict(hs=0.97),
        (34, '<b>9.51</b> Phalanxes may use ', 12): dict(hs=0.98),
        (34, 'the interruption is caused by ', 1): dict(hs=0.95),
        (34, 'the interruption is caused by ', 7): dict(hs=0.98),
        (34, 'the interruption is caused by ', 8): dict(hs=0.98),
        (35, '<b>9.61</b> See the Stacking C', 0): dict(hs=0.97),
        (35, '<b>9.61</b> See the Stacking C', 3): dict(hs=0.97),
        (35, '<i>may</i> move sideways into ', 8): dict(hs=0.97),
        (36, '9.8 ARTILLERY', 1): dict(hs=0.97, ws=-0.03),
        (36, '9.83', 2): dict(hs=0.97),
        (36, '9.91 Movement Effects', 1): dict(hs=0.96),
        (36, 'Gallic Chariot (CH) units', 0): dict(hs=0.97),
        (36, 'Gallic Chariot (CH) units', 1): dict(hs=0.97),
        }

FOOT = 743.5      # QA: ostatni wiersz łamu co najmniej ok. 5 pt nad stopką (stopka od y ≈ 749)


def tune(P):
    for (pg, t, i), kw in TUNE.items():
        if pg == P.page:
            P.para(P.find(t), i, **kw)


def justify(P):
    for uid, idx in JUST.get(P.page, []):
        for i in idx:
            P.para(uid, i, align='justify')


def head12(P, u, i, size=12.0):
    p = P.unit(u)['paras'][i] if isinstance(u, str) else u['paras'][i]
    s = S[P.page]
    p['size'] = round(size / s, 3)
    p['pitch'] = round(1.2 * size / s, 3)


def box(P, t, bottom, fix=None, pitch=None):
    """ramka z tłem: tekst we własnej skali, dół tekstu ok. 2,5 pt nad dolną krawędzią tła (kontrola)"""
    u = P.find(t)
    fix, pitch = BOXV.get((P.page, t), (fix, pitch))
    P.set(u, body=False, maxBottom=round(bottom - 2.5, 2))
    if fix:
        P.set(u, fixscale=fix)
    if pitch:
        for i in range(len(u['paras'])):
            P.para(u, i, pitch=pitch)


def foot(P, *uids, mb=FOOT):
    for uid in uids:
        u = P.unit(uid)
        P.set(u, maxBottom=min(u.get('maxBottom', u['bottom']), mb))


# s. 28 – akapity przechodzące do następnej łamy / strony: justowany ostatni wiersz
P = Patch(D, 28); P.restore()
P.para(P.find('The Charge:'), 0, lastjust=True)            # u3 -> u5 (prawa łama)
u = P.find('Leader Casualties:')
P.para(u, 3, lastjust=True)                                # u6[3] -> s. 29
# u6[2] („7. The Carthaginian…”) to dalszy ciąg akapitu u6[1] (w trans scalony, [2] = ""):
# odstęp przed u6[3] liczony od końca u6[2], nie od końca u6[1]
P.para(u, 1, lastbase=u['paras'][2]['lastbase'])
head12(P, 'u2', 0)                                         # tytuł przykładu 12 pt
foot(P, 'u3', mb=741.0)                                    # lewa łama: koniec wyżej (QA)
foot(P, 'u6')
tune(P); P.save()

# s. 29 – 8.51 nad ramką UWAGI PROJEKTANTA (tło od y = 620): prześwit ok. 5 pt; ramki – wypełnienie
P = Patch(D, 29); P.restore()
P.set(P.find('8.51'), maxBottom=615.0)
foot(P, 'u3')
box(P, 'This rule (as well as 8.6)', 489.0)
box(P, 'This (and its sister rule', 718.0)
tune(P); P.save()

# s. 30 – podpisy diagramów wyśrodkowane pod diagramami (polskie podpisy mają inną długość);
# akapity przechodzące: 8.54 (u7 -> u9) i ostatni akapit 8.62 (u13 -> s. 31)
P = Patch(D, 30); P.restore()
justify(P)
for t in ('No Advance', 'Pivot Advance', 'Advance with Wheel'):
    u = P.find(t)
    P.line(u, 0, align='center')
u = P.find('8.53'); P.para(u, 1, lastjust=True)
u = P.find('8.61'); P.para(u, len(u['paras']) - 1, lastjust=True)
# szara ramka UWAGI DO ROZGRYWKI: unitize dał zapas pod ramką (maxBottom 298,8) – tekst nie może
# wyjść poza tło ramki (dolna krawędź tła y = 291,0)
box(P, 'This rule is not used in Beneventum', 292.0)
box(P, 'One of the problems with cavalry', 258.0)  # ramka HIST. 8.6 – tło do y = 258
foot(P, 'u7', 'u13')
tune(P); P.save()

# s. 31 – szare ramki UWAG DO ROZGRYWKI: maxBottom = dolna krawędź tła ramki
P = Patch(D, 31); P.restore()
justify(P)
box(P, 'This will usually place the victorious', 155.0)
box(P, 'The routing player, where possible', 449.0)
# jednostki nad ramkami: zapas z unitize sięgał w tło ramki (u2 – ramka od y = 116, u4 – od y = 374)
u = P.find('the pursuing unit is required to advance')
P.set(u, maxBottom=113.6); P.para(u, 0, pitch=11.65)          # interlinia −3% (prześwit nad ramką)
P.set(P.find('If the routed enemy unit moves off the map'), maxBottom=370.0)
# „DRMs:” (jednostka lines, skala 1) + lista modyfikatorów (u8) -> jedna jednostka flow tekstu
# głównego; QA: scalona też z u6 (8.64–8.66), żeby nie było luki przed „Modyfikatory…”
u7 = P.find('DRMs:')
P.lines_to_flow(u7, align='left')
P.set(u7, body=True)
P.merge(u7, P.find('+1 for Numidian LC.'))
P.merge(P.find('8.64 Off-Map Regroup'), u7)
foot(P, 'u6', 'u14')
head12(P, 'u10', 0)                                        # 8.7 – 12 pt
P.set('u11', x1=565.8, maxRight=565.8)                               # 9.0 – w granicach łamu
P.para('u11', 0, hs=0.91)                                  # 9.0 – mniejsze ścieśnienie liter (QA: ciasno)
box(P, 'Despite their drawbacks', 470.0)
tune(P); P.save()

# s. 32 – ostatni akapit 9.14 przechodzi na s. 33; komórka tabeli „0” – maxBottom = dół tła komórki
P = Patch(D, 32); P.restore()
justify(P)
P.set(P.find('heads in the direction of the nearest friendly unit'), maxBottom=584.2)
P.line(P.find('Die Roll'), 0, maxLeft=51.5, maxRight=89.7, hs=0.94)            # „Rzut kością” – margines od linii kolumny (QA r3)
u = P.find('9.14 Elephant Rampage')
P.set(u, maxBottom=516.2); P.para(u, 0, pitch=11.65)                # nad nagłówkiem tabeli (tło od y = 519)
u = P.find('A rampaging Elephant and any stacked leader'); P.para(u, len(u['paras']) - 1, lastjust=True)
P.set(P.find('Each Elephant Rampage is always resolved'), maxBottom=215.5)   # nad cyframi róży
box(P, 'Most infantry were trained', 218.0)
box(P, 'Several historians portray', 458.0)
foot(P, 'u15')
tune(P); P.save()

# s. 33 – ostatni punktor 9.24 przechodzi na s. 34
P = Patch(D, 33); P.restore()
justify(P)
u = P.find('9.21 Orderly Withdrawal'); P.para(u, len(u['paras']) - 1, lastjust=True)
P.para(P.find('9.2 SKIRMISHERS, VELITES'), 0, align='left')   # nagłówek dwuwierszowy – bez justowania
foot(P, 'u11', mb=741.5)
u = P.find('9.15 Cavalry vs. Elephants')
P.set(u, maxBottom=424.6)                                  # 9.15–9.17: odstęp nad ramką HIST. (tło od y = 429)
for i in range(len(u['paras'])):
    P.para(u, i, pitch=12.3)                               # interlinia +2,5% – luka nad ramką jak w oryginale   # odstęp nad ramką HIST. 9.17 (tło od y = 429)
P.move_to(P.find('Elephants did not fight in formations'), base=439.5)   # ramka jednowierszowa – tekst na środku tła
box(P, 'Historically, the mahouts', 132.0)
box(P, 'Elephants did not fight in formations', 445.0)
box(P, 'The argument over which family', 731.0)
box(P, 'Skirmisher units were truly', 228.0)
tune(P); P.save()

# s. 34 – punktory jednowierszowe w EN justowane jak pozostałe; nagłówki 9.3, 9.4 – 12 pt
P = Patch(D, 34); P.restore()
justify(P)
head12(P, 'u2', 2)
head12(P, 'u2', 6)
P.set('u2', maxBottom=493.3)                                # nad ramką PROJ. 9.4 (tło od y = 497)
foot(P, 'u7', mb=742.8)
box(P, 'This reflects the remarkable', 572.0)
box(P, 'To increase the crushing', 117.0)
tune(P); P.save()

# s. 35 – 9.66 przechodzi z lewej łamy (u7) do prawej (u9)
P = Patch(D, 35); P.restore()
P.para(P.find('9.66 Manipular Line Extension'), 0, lastjust=True)
# podpis dolnego diagramu (flow tekstu głównego) – ten sam stopień co podpis górnego (lines, skala 1):
# osobna skala, jeden wiersz rozszerzany symetrycznie w szerokości łamu
P.set(P.find('After Manipular Line Extension'), body=False, nowrap=True, maxLeft=45.0, maxRight=297.0)
head12(P, 'u9', 4)                                         # 9.7 – 12 pt (2 wiersze)
foot(P, 'u7', 'u9')
box(P, 'The major advance in the science', 166.0)
tune(P); P.save()

# s. 36 – 9.91 (u7 -> u9) i ostatni akapit 9.96 (u15 -> s. 37)
P = Patch(D, 36); P.restore()
box(P, 'The front side of the counter shows', 284.0)
box(P, 'These rules reflect the capabilities', 674.0)
P.set(P.find('9.81'), maxBottom=255.5)                                 # nad szarą ramką (od y = 257)
P.para(P.find('9.91 Movement Effects'), 1, lastjust=True)
u = P.find('Gallic Chariot (CH) units'); P.para(u, 1, lastjust=True)
head12(P, 'u2', 0)                                         # 9.8 – 12 pt
foot(P, 'u7', 'u15')
box(P, 'This rule represents the feared', 216.0)
box(P, 'The chariots used by the Gallic', 620.0)
tune(P); P.save()
