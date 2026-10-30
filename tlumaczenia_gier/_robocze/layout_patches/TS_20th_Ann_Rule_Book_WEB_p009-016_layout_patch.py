#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Rule_Book_WEB, s. 9–16 (redaktor tr9_16, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
# Ramki przykładów/uwag: maxBottom do krawędzi tła ramki (pomiar z bgimg, 1 px = 1 pt) minus ok. 4 pt.
# Akapity rozbite w EN na kilka akapitów (opływanie kart, wymuszone końce wierszy) – scalone w jeden
# akapit (join), opływanie obrazków kart – pola cuts (float), jak cuts z unitize.
import sys
sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Rule_Book_WEB'
# Nagłówki rozdziałów w kroju Veneer-TwoRegular: render.py składa go zastępnikiem LSerif (szeryfowy,
# ok. 50% szerszy) – jak w łatkach tr17_20 i tr21_24: wąski pogrubiony bezszeryfowy MyriadPro-BoldCond
# (HerosCnN Bold), jednolicie dla nagłówków 5.0, 6.0, 7.0, 8.0, 9.0 i 10.0.
VENEER = 'MyriadPro-BoldCond'


def join(P, uid, i, j):
    """scal akapity i..j jednostki flow w akapit i (tekst EN połączony spacją)"""
    u = P.unit(uid)
    ps = u['paras']
    if j >= len(ps):
        return
    a = ps[i]
    for q in ps[i + 1:j + 1]:
        t = a['en']
        a['en'] = (t[:-1] + q['en']) if (t.endswith('-') and q['en'][:1].islower()) else (t + ' ' + q['en'])
        a['nlines'] = a.get('nlines', 1) + q.get('nlines', 1)
        a['bottom'] = q['bottom']
        a['lastbase'] = q['lastbase']
        a['x1'] = max(a['x1'], q['x1'])
        a['x0'] = min(a['x0'], q['x0'])
    del ps[i + 1:j + 1]


def cut(P, uid, i, *cs):
    """opływanie obrazka: cs = (side, top, bottom, w) we współrzędnych strony"""
    P.para(uid, i, cuts=[{'side': s, 'top': t, 'bottom': b, 'w': w} for s, t, b, w in cs])


def drop(P, uid):
    u = P.unit(uid)
    P.lay['units'].remove(u)


# ---------------------------------------------------------------- s. 9
P = Patch(D, 9); P.restore()
P.set('u8', maxBottom=466.0)                 # PRZYKŁAD 1 – ramka do y = 470
P.set('u9', maxBottom=746.0)                 # PRZYKŁAD 2 – ramka do y = 750
P.set('u5', maxBottom=533.5)                 # UWAGA – ramka do y = 537
P.para('u6', 0, left=0.0, hang=13.5, ls=0)   # pierwszy punktor jak pozostałe: znak „•” w tekście (u7 – skip)
P.para('u3', 0, font=VENEER)                 # 5.0
P.para('u2', 7, align='justify')            # „I.” – po polsku 2 wiersze (w EN 1 wiersz, do lewej)
P.save()

# ---------------------------------------------------------------- s. 10
P = Patch(D, 10); P.restore()
join(P, 'u2', 0, 1)                          # PRZYKŁAD 3 – jeden akapit
P.set('u2', maxBottom=217.0)                 # ramka do y = 221
P.set('u3', maxBottom=376.0)                 # ramka do y = 380
P.set('u5', maxBottom=585.0)                 # ramka do y = 589
join(P, 'u9', 0, 1)                          # PRZYKŁAD (6.1.2) – jeden akapit
P.set('u9', maxBottom=532.5)                 # ramka do y = 536
P.move_to('u9', base=405.5)                  # ramka od y = 391
P.para('u9', 0, pitch=12.47)                 # QA 26.10: interlinia +4% – tekst do ok. 6 pt nad mapą (było 11 pt)
P.set('u10', maxBottom=748.5)                # ramka do y = 752
P.move_to('u10', base=708.0)                 # QA 26.10: 1,7 pt wyżej – odstęp góra/dół ok. 11/7 pt
P.para('u7', 0, font=VENEER)                 # 6.0
P.set('u8', maxBottom=389.5)                 # 6.0–6.1.2: ramka przykładu od y = 391 (unitize: 400 – wchodziło w ramkę)
P.save()

# ---------------------------------------------------------------- s. 11
P = Patch(D, 11); P.restore()
P.set('u3', maxBottom=204.5)                 # ramka do y = 208
P.set('u2', maxBottom=114.0)                 # 6.1.3: ramka przykładu od y = 115 (unitize: 121,5)
P.set('u4', maxBottom=489.5)                 # ramka przykładu od y = 491
P.set('u5', maxBottom=612.5)                 # ramka do y = 616
P.save()

# ---------------------------------------------------------------- s. 12
P = Patch(D, 12); P.restore()
join(P, 'u3', 0, 1)                          # PRZYKŁAD (6.3) – jeden akapit, pełna szerokość
P.para('u3', 0, right=0)
P.set('u3', maxBottom=470.5, x1=290.0)       # ramka 40..300 x 315..474
P.move_to('u3', base=331.5)
P.set('u2', maxBottom=313.8)                 # ramka przykładu od y = 315
P.set('u4', maxBottom=283.0)                 # znaczniki Wyścigu Kosmicznego od y ≈ 284
P.move_to('u6', base=702.0)                  # QA 26.10: 6.4.2 o 3 pt wyżej (obrazek toru do y = 686),
P.set('u6', maxBottom=749.0)                 # ostatni wiersz ≥ 5 pt nad stopką
P.save()

# ---------------------------------------------------------------- s. 13
P = Patch(D, 13); P.restore()
for i in (3, 4):
    P.para('u2', i, align='left')            # punktory 6.4.4 – w EN błędnie wykryte „center”
join(P, 'u9', 3, 4)                          # 7.4 – ostatni wiersz (tytuł karty) w tym samym akapicie
# 7.3: podkreślenie tytułu „Flower Power” jest w EN kreską w tle (x 475–545, y ≈ 148) – po polsku tekst
# leży inaczej, więc kreska przekreślałaby inne słowa; akapit dostaje białe tło (hl #ffffff), które ją
# zasłania (tło strony pod akapitem jest białe), a polski tytuł ma własne podkreślenie (<u>)
P.para('u9', 2, hl='#ffffff')
P.set('u3', maxBottom=421.5)                 # ramka do y = 425
P.set('u2', maxBottom=344.2)                 # ramka przykładu od y = 348 (QA 26.10: odstęp jak w EN)
P.set('u4', maxBottom=462.8)                 # ramka uwagi od y = 464
P.set('u12', maxBottom=617.8)                # ramka przykładu od y = 619
P.set('u5', maxBottom=525.5, x1=300.0)       # UWAGA PROJEKTANTA – ramka 50..309 x 464..529
P.move_to('u5', base=479.8)                  # QA 26.10: 1,5 pt wyżej – 5 wierszy, odstępy góra/dół ok. 8/7 pt
P.set('u13', maxBottom=692.5)                # ramka do y = 696
P.para('u7', 0, font=VENEER)                 # 7.0
# PRZYKŁAD (7.4): dwie części tekstu wokół dwóch kart -> jedna jednostka z opływaniem
u10 = P.unit('u10')
join(P, 'u10', 0, 1)
join(P, 'u11', 0, 1)
P.merge('u10', 'u11')
join(P, 'u10', 0, 1)
P.para('u10', 0, left=0, hang=0)
P.set('u10', x1=564.7, maxRight=567.59, maxBottom=560.5)
cut(P, 'u10', 0, ('r', 290.0, 407.0, 564.7 - 442.0), ('l', 407.0, 566.0, 436.0 - 325.43))
P.save()

# ---------------------------------------------------------------- s. 14
P = Patch(D, 14); P.restore()
P.set('u3', maxBottom=164.5, x1=290.0)       # PRZYKŁAD 1 – ramka 41..300 x 103..168
P.move_to('u3', base=117.5)
P.set('u2', maxBottom=101.8)                 # 7.4.2: ramka przykładu od y = 103
P.set('u11', maxBottom=115.8)                # 8.1.3: ramka uwagi od y = 117
P.set('u4', maxBottom=227.5, x1=292.0)       # PRZYKŁAD 2 – ramka 41..300 x 178..231
P.move_to('u4', base=192.0)
P.para('u4', 0, pitch=11.64)                 # QA 26.10: interlinia −3% (4 wiersze w ramce 53 pt)
P.set('u5', maxBottom=278.5, x1=292.0)       # PRZYKŁAD 3 – ramka 41..300 x 241..282
P.move_to('u5', base=254.2)                  # QA 26.10: górny odstęp ok. 5,5 pt (było 2 pt)
P.para('u5', 0, pitch=11.64)                 # interlinia −3% (3 wiersze w ramce 41 pt)
P.para('u5', 0, align='left')                # w EN justowany, 2 wiersze; PL 3 wiersze – jak pozostałe przykłady
P.para('u9', 0, font=VENEER)                 # 8.0
P.move_to('u9', base=612.4)                  # 8.0 i 8.1 niżej o 4 pt (7.6 po polsku dłuższy; pod 8.1.2 jest miejsce)
P.move_to('u10', base=625.6)
P.set('u7', maxRight=186.0)                  # nagłówek 7.6 nie może wejść na kartę (od x ≈ 190)
P.set('u7', fixscale=0.868)                  # QA 26.10 (S4): stopień jak „8.1” (nagłówek w łamie, skala tekstu strony)
# 7.4.3–7.5 dłuższe po polsku: nagłówek 7.6 i jego akapit niżej o 5 pt (miejsce do nagłówka 8.0 jest)
P.move_to('u7', base=429.8)
P.set('u6', maxBottom=415.5)
# 7.6: akapit rozbity w EN na 6 części (opływanie karty) -> jeden akapit z opływaniem
join(P, 'u8', 0, 5)
P.move_to('u8', base=443.0)
P.para('u8', 0, align='justify')
# QA 26.10: opływanie dokładniej wzdłuż lewej krawędzi karty (bgimg: x 201 przy y 425 → 188 przy y 535,
# dolny róg do y ≈ 550), odstęp tekstu od karty ok. 6 pt – szersze wiersze, mniej rozstrzeleń
cut(P, 'u8', 0, ('r', 428.0, 445.0, 295.12 - 193.0), ('r', 445.0, 465.0, 295.12 - 191.0),
    ('r', 465.0, 485.0, 295.12 - 188.0), ('r', 485.0, 505.0, 295.12 - 186.0),
    ('r', 505.0, 525.0, 295.12 - 183.5), ('r', 525.0, 543.0, 295.12 - 182.0),
    ('r', 543.0, 556.0, 295.12 - 188.0))
# UWAGA DO ROZGRYWKI (8.1.3): ikona ☢ jest w tle w wierszu 6 (x 475–488, linia bazowa 193,82). QA 26.10:
# u12 = wiersze 1–5, u13 = wiersz 6 przed ikoną + <br> + wiersz 7, u14 = wiersz 6 za ikoną; stopień 0,92,
# interlinia 11,4 pt we wszystkich trzech częściach (wiersz 5 → 6 bez luki), wiersz 6 bez justowania
# (tekst dobrany tak, by naturalnie wypełnił miejsce przed ikoną)
PN = 0.92
for uid in ('u12', 'u13', 'u14'):
    P.set(uid, fixscale=PN)
    P.para(uid, 0, pitch=round(11.4 / PN, 3))
P.move_to('u12', base=round(193.82 - 5 * 11.4, 2))
P.set('u12', maxBottom=186.5)
P.para('u13', 0, align='left')
P.set('u13', maxBottom=210.0)
join(P, 'u15', 0, 1)                         # PRZYKŁAD (8.1.3) – jeden akapit
P.set('u15', maxBottom=336.0)                # ramka do y = 340
# UWAGA DO ROZGRYWKI (8.1.5) obok ikony znacznika Ograniczenia DEFCON: jedna jednostka od x = 316,66
# z opływaniem ikony po lewej (w EN dwa akapity + osobny wiersz pod ikoną)
u17 = P.unit('u17')
join(P, 'u17', 0, 1)
p0 = u17['paras'][0]
p0['en'] = p0['en'] + ' ' + P.unit('u18')['lines'][0]['en']
drop(P, 'u18')
P.set('u17', x0=316.66, maxLeft=316.66, x1=556.0, maxRight=556.0, body=False, maxBottom=718.0)   # ramka 360..562
P.move_to('u17', base=667.0)
for i in range(3, 7):
    P.para('u16', i, right=0.0)              # punktory DEFCON 4–1: bez sztucznego prawego wcięcia
P.para('u17', 0, left=0, indent=3.63)
cut(P, 'u17', 0, ('l', 655.0, 693.0, 365.0 - 316.66))   # ikona: x 316–359, y 647–690 (bgimg)
P.save()

# ---------------------------------------------------------------- s. 15
P = Patch(D, 15); P.restore()
P.set('u3', maxBottom=389.5)                 # PRZYKŁAD (8.2.1) – ramka do y = 393
P.set('u2', maxBottom=338.8)                 # ramka przykładu od y = 340
P.set('u4', maxBottom=589.8)                 # ramka przykładu od y = 591
P.set('u5', maxBottom=651.5, x1=299.0)       # PRZYKŁAD (8.2.4) – ramka 50..309 x 591..655
P.move_to('u5', base=605.0)
P.para('u6', 0, font=VENEER)                 # 9.0
# 9.1 i 9.2 opływają kartę The China Card (prawy górny róg): akapity scalone, opływanie
join(P, 'u7', 0, 2)
P.para('u7', 0, align='justify', ls=0)
P.set('u7', maxBottom=180.0)                 # wiersz „limit.” (u8) – w akapicie 9.1 (niżej: scalenie z u9)
# QA 26.10: opływanie wzdłuż lewej krawędzi karty (bgimg: x 491 przy y 68 → 478 przy y 176), odstęp ok. 5 pt
cut(P, 'u7', 0, ('r', 92.0, 125.0, 566.9 - 482.0), ('r', 125.0, 155.0, 566.9 - 478.0),
    ('r', 155.0, 180.0, 566.9 - 474.0))
join(P, 'u9', 0, 2)
P.para('u9', 0, align='justify')
cut(P, 'u9', 0, ('r', 180.0, 187.0, 566.9 - 470.0), ('r', 187.0, 199.0, 566.9 - 508.0))   # dolna krawędź karty: y 185 (x 480) – 197 (x 560)
P.merge('u9', 'u10')                         # 9.5 (drugi punktor) – 9.8 w tej samej jednostce co 9.2–9.5
P.para('u9', 5, left=13.5, hang=13.5)        # drugi punktor 9.5 jak pierwszy (znak „•” w tekście)
# QA 26.10: 9.1 po polsku krótszy niż w EN – 9.2 w tej samej jednostce co 9.1 (bez luki ok. 20 pt);
# odstęp 9.1 → 9.2 jak między pozostałymi punktami (21,3 pt między liniami bazowymi)
P.merge('u7', 'u9')
p7 = P.unit('u7')['paras']
p7[1]['base'] = round(p7[0]['lastbase'] + 21.3, 2)
P.set('u7', maxBottom=512.0)                 # do zdjęcia (od y ≈ 516)
P.save()

# ---------------------------------------------------------------- s. 16
P = Patch(D, 16); P.restore()
P.para('u2', 0, font=VENEER)                 # 10.0
# 10.1.1: podkreślenia „Presence:”, „Domination:”, „Control:” są w EN kreskami w tle (x 45–99,
# y ≈ 262 / 293 / 351) – białe tło akapitów (hl #ffffff) je zasłania; polskie hasła mają własne <u>
for i in (1, 2, 3, 4):
    P.para('u5', i, hl='#ffffff')
# białe tło zasłania kreskę tylko wtedy, gdy kreska wypada w wierszu tekstu (nie w odstępie między
# akapitami): przy skali 0,90 (stała dla całego tekstu głównego strony) i 2/2/5 wierszach akapitów
# 10.1.1/Obecność/Dominacja nagłówek 10.1 na linii bazowej 240 daje wiersze o liniach bazowych
# ok. 264,8 / 292,9 / 356,4, których tło zakrywa kreski y = 262,5–263,0 / 293,4–293,9 / 350,7–351,2
P.move_to('u5', base=240.0)
for uid in ('u3', 'u5', 'u12'):
    P.set(uid, fixscale=0.90)
P.set('u3', maxBottom=159.8)                 # ramka uwagi od y = 161
P.set('u4', x1=292.0, maxRight=292.0, maxBottom=196.5)   # UWAGA DO ROZGRYWKI – ramka 41..300 x 161..202
# QA 26.10 (S1): 3 wiersze w ramce 41 pt – stopień 0,86, interlinia −3%, odstęp góra/dół ok. 5,5/6 pt
P.move_to('u4', base=173.9)
P.para('u4', 0, pitch=11.64)
# PRZYKŁAD (10.1): w EN 6 jednostek (wiersze obok karty Central America Scoring) -> jedna jednostka
for uid in ('u7', 'u8', 'u9', 'u10', 'u11'):
    P.merge('u6', uid)
n = len(P.unit('u6')['paras'])
join(P, 'u6', 0, n - 1)
P.para('u6', 0, align='left', left=0, right=0)
P.set('u6', nowrap=False, x0=315.0, maxLeft=315.0, x1=552.0, maxRight=552.0, maxBottom=269.5)   # ramka 302..562 (pod kartą)
P.move_to('u6', base=92.0)
cut(P, 'u6', 0, ('r', 86.0, 196.0, 552.0 - 447.0))
for u, i in (('u5', 1), ('u12', 0), ('u12', 2)):  # 10.1.1, 10.1.3, 10.1.5 – po polsku 2 wiersze (w EN 1)
    P.para(u, i, align='justify')
P.save()

# ---------------------------------------------------------------- ramki przykładów i uwag (QA 26.10)
# Po kontroli wizualnej: tekst ramki (MinionPro-MediumCnIt) składa się teraz lżej i węziej, więc stała
# skala wspólna dla strony zostawiała pusty dół. Każda ramka ma własną skalę (BOXSCALE – największa
# mieszcząca się, nie większa niż 1,1 × skala tekstu głównego strony, tj. stopień ≤ tekstu głównego),
# a dół tekstu ok. 7 pt nad dolną krawędzią tła ramki (BOXBOT – krawędź z bgimg; gdy pod tekstem jest
# obrazek, a nie krawędź ramki – granica jak dotąd, ok. 4 pt nad obrazkiem).
BOXBOT = {
    9: {'u5': 537 - 7, 'u8': 469 - 7, 'u9': 750 - 7},
    10: {'u2': 221 - 7, 'u3': 380 - 7, 'u5': 589 - 7, 'u9': 532.5, 'u10': 752 - 7},
    11: {'u3': 204.5, 'u5': 616 - 7},
    12: {'u3': 470.5},
    13: {'u3': 425 - 7, 'u5': 529 - 7, 'u10': 564 - 7, 'u13': 696 - 7},
    14: {'u3': 168 - 7, 'u4': 231 - 7, 'u5': 282 - 6.2, 'u15': 336.0, 'u17': 721 - 7},
    15: {'u3': 393 - 7, 'u5': 656 - 7},
    16: {'u6': 269.5},
}
BOXSCALE = {}
for pg, d in BOXBOT.items():
    P = Patch(D, pg)                         # bez restore – kontynuacja łatek strony z sekcji wyżej
    for uid, mb in d.items():
        P.set(uid, maxBottom=float(mb))
        P.unit(uid).pop('fixscale', None)
        if (pg, uid) in BOXSCALE:
            P.set(uid, fixscale=BOXSCALE[(pg, uid)])
    if pg == 16:
        P.set('u4', fixscale=0.85)            # QA S1: stopień 8,5 pt (−0,1 pt; skala ≥ 0,85), 3 wiersze, odstęp góra/dół ok. 5,5/6,5 pt
    P.save()

# ---------------------------------------------------------------- RUNDA 3 (27.10): rozstrzelenia, stopnie w ramkach
R3 = {}


def r3(pg):
    """Patch strony bez restore – kontynuacja (sekcje wyżej zaczynają od restore)"""
    return Patch(D, pg)


# s. 13 – ramki po lewej: tekst wyżej (odstęp górny ok. 6,5 pt jak w EN), interlinia −3%, dół 6 pt nad krawędzią
# (większy stopień pisma: ramki na s. 13 miały 8,5 pt wobec 9,0–9,6 pt na s. 12 i 14); 7.1 – odstęp
# międzywyrazowy −0,05 em, żeby „(Event)” zmieściło się w 2. wierszu (rozstrzelony wiersz 0,72 em)
P = r3(13)
for uid, base, mb in (('u3', 363.6, 419.0), ('u5', 477.8, 523.0), ('u13', 634.2, 690.0)):
    P.move_to(uid, base=base)
    P.set(uid, maxBottom=mb)
    P.para(uid, 0, pitch=11.64)
P.para('u8', 2, ws=-0.05)
P.save()

# ramki – stopień pisma: po rundzie 2 każda ramka miała własną skalę (różnice do 1 pt na stronie). Runda 3:
# skala ramki = min(skala wyliczona przez fit, najmniejsza skala ramki na stronie + 0,04, 1,1 × skala tekstu
# głównego strony) – stopnie w ramkach jednej strony różnią się najwyżej o 0,4 pt i nie przekraczają tekstu
# głównego. Wartości stałe (pomiar fit.py 27.10). Wyjątek: s. 14 u12–u14 (UWAGA z ikoną ☢, trzy części
# jednej uwagi) – 0,92, bo przy mniejszym stopniu wiersz z ikoną nie wypełnia miejsca przed ikoną.
BOXFIX = {
    9: {'u5': 0.915, 'u8': 0.955, 'u9': 0.955},
    10: {'u2': 0.936, 'u3': 0.936, 'u5': 0.936, 'u9': 0.896, 'u10': 0.936},
    11: {'u3': 0.874, 'u5': 0.914},
    12: {'u3': 0.898},
    13: {'u3': 0.89, 'u5': 0.922, 'u10': 0.882, 'u13': 0.91},
    14: {'u3': 0.877, 'u4': 0.877, 'u5': 0.871, 'u15': 0.902, 'u17': 0.862},
    15: {'u3': 0.927, 'u5': 0.887},
    16: {'u4': 0.85, 'u6': 0.89},
}
for pg, d in BOXFIX.items():
    P = r3(pg)
    for uid, sc in d.items():
        P.set(uid, fixscale=sc)
    P.save()

# s. 13 – prawa łama 7.2–7.4: po polsku (skala 0,87) kończy się ok. 37 pt nad ramką przykładu (w EN ok. 14 pt).
# Odstępy rozłożone jak w EN: interlinia akapitów +3%, odstęp przed nagłówkiem 7.3 i przed 7.4 większy
# o 6 i 7 pt (przed skalowaniem) – koniec 7.4 ok. 15 pt nad ramką.
P = r3(13)
u9 = P.unit('u9')
for i in (0, 2, 3):
    P.para('u9', i, pitch=13.6)
P.para('u9', 1, base=round(u9['paras'][0]['lastbase'] + 25.8 + 6.0, 2))
P.para('u9', 3, base=round(u9['paras'][2]['lastbase'] + 21.3 + 7.0, 2))
P.set('u9', maxBottom=262.0)
P.save()

# s. 14 – nagłówek 8.0: krój zastępczy szerszy niż Veneer; „8.0 STATUS DEFCON I OPERACJE WOJSKOWE” w jednym
# wierszu ma 15,1 pt (inne nagłówki rozdziałów 17,6–18 pt). Tracking hs 0,94 → ok. 16 pt (17,5 pt nie mieści się
# w łamie 250 pt bez łamania nagłówka, a pod 8.1.2 nie ma miejsca na drugi wiersz).
# 7.6 obok karty: pierwszy wiersz rozstrzelony (0,6 em) – poprawione w trans („W talii jest 5 Wydarzeń
# Wojennych (War…” wypełnia pierwszy wiersz).
P = r3(14)
P.para('u9', 0, hs=0.94)
P.save()

# s. 15 – 8.2.3: odstęp międzywyrazowy −0,03 em (wiersz „zagrano kartę Wydarzenia Wojennego (War Event card; np.
# WOJNA” miał 0,5 em; po zmianie 0,22 em)
P = r3(15)
P.para('u4', 1, ws=-0.03)
P.save()
# s. 15 – 9.7: odstęp międzywyrazowy −0,03 em (wiersz „Wartość Operacyjna (Operations value) KARTY CHIŃSKIEJ (THE”
# 0,58 em → 0,23 em)
P = r3(15)
P.para('u7', 8, ws=-0.03)
P.save()

# ---------------------------------------------------------------- ts_naglowki (30.10): nagłówki rozdziałów jak Phalanx
# s. 14 – „8.0 STATUS DEFCON ORAZ OPERACJE WOJSKOWE” (dłuższy o „ORAZ”): nagłówek może wejść w odstęp między łamami
# (prawa łama w tej wysokości zaczyna się punktorem w x ≈ 321), tracking 0,92 – stopień ok. 15,6 pt (było 16,2 pt).
P = r3(14)
P.set('u9', maxRight=310.0)
P.para('u9', 0, hs=0.92)
P.save()
# s. 16 – „10.0 ROZSTRZYGNIĘCIE I WARUNKI ZWYCIĘSTWA” w jednym wierszu miałby ok. 14 pt (ramka PRZYKŁAD od x ≈ 305):
# dwa wiersze jak w Phalanx („10.0 ROZSTRZYGNIĘCIE / I WARUNKI ZWYCIĘSTWA”, podział <br> w trans), stała skala 0,9
# (16,2 pt), drugi wiersz na linii bazowej oryginału (85,3), pierwszy 16,5 pt wyżej – nad nim pagina (do y ≈ 54).
P = r3(16)
u = P.unit('u2')
P.set(u, nowrap=False, fixscale=0.9)
P.para(u, 0, pitch=round(16.5 / 0.9, 3), nlines=2)
P.move_to(u, base=round(85.32 - 16.5, 2))
P.para(u, 0, lastbase=85.32)
P.set(u, bottom=89.68, maxBottom=89.68)
P.save()
# s. 15 – „9.0 KARTA CHIŃSKA (CHINA)” sięgał na ilustrację karty THE CHINA CARD (lewa krawędź karty w wysokości
# nagłówka x ≈ 494): nagłówek do x = 488 (stopień ok. 16,5 pt).
P = r3(15)
P.set('u6', x1=488.0, maxRight=488.0)
P.save()
