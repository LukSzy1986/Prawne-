#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Rule_Book_WEB, s. 17–20 (redaktor tr17_20, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Rule_Book_WEB'


def box(P, u, base, maxb, fixscale=None, pitch=None):
    """ramka UWAGA/PRZYKŁAD (QA 26.10, S1): tekst wyśrodkowany w pionie w tle ramki – pierwsza linia
    bazowa `base`, dół tekstu do `maxb` (odstęp od górnej i dolnej krawędzi tła ok. 6–9 pt); opcjonalnie
    stała skala i interlinia akapitu (zmiana interlinii: −3%…+4%)"""
    P.move_to(u, base=base)
    P.set(u, maxBottom=maxb)
    if fixscale:
        P.set(u, fixscale=fixscale)
    if pitch:
        P.para(u, 0, pitch=pitch)

# s. 17 – punktory 10.3.1: bez sztucznego prawego wcięcia (wiersze postrzępione w oryginale);
# akapit 11.1 przechodzi z lewej łamy (u6) do prawej (u7) – ostatni wiersz w u6 justowany
PAGE19 = 0.864                   # skala tekstu głównego s. 19 (fit.py) – dla nagłówka 13.3
VENEER = 'MyriadPro-BoldCond'    # zastępnik kroju Veneer-TwoRegular (nagłówki rozdziałów), zob. niżej

# Nagłówki rozdziałów w kroju Veneer-TwoRegular (bardzo wąski krój wystawowy, wersaliki): render.py nie
# ma dla niego zastępnika (składa go jak LSerif – o ok. 50% szerzej niż oryginał; „11.0 WARIANT „CHIŃSKA
# WOJNA DOMOWA”” wymagałby skali 0,68). Na s. 17–20 wszystkie takie nagłówki dostają krój wąskiego
# groteskowego zastępnika MyriadPro-BoldCond (HerosCnN pogrubiony) – bliższy oryginałowi i jednolity
# w partii (tak samo s. 21–23, łatka tr21_24). Do decyzji: to samo mapowanie dla całego dokumentu.

P = Patch(D, 17); P.restore()
u5 = P.find('11.0 THE CHINESE CIVIL WAR VARIANT')
P.para(u5, 0, font=VENEER)
P.set(u5, x1=301.5, maxRight=301.5)                  # QA3: nagłówek nie dalej niż prawa krawędź łamy (304,4)
# polski tekst 10.3 wypełnia lewą łamę do y ≈ 590 – nagłówek 11.0 i tekst pod nim 6 pt niżej (odstęp
# nad nagłówkiem); w lewej łamie 2 wiersze akapitu 11.1 (reszta w prawej łamie)
u6 = P.find('From C3i #21')
P.move_to(u5, base=613.12)
P.move_to(u6, base=626.32)
P.set(u6, maxBottom=753.7)
u = P.find('Automatic victory is achieved')
for i, p in enumerate(u['paras']):
    if p['en'].startswith('•'):
        P.para(u, i, right=0.0)
u = P.find('The only action for the Chinese')
P.para(u, len(u['paras']) - 1, lastjust=True)
P.save()

# s. 18 – lewa łama: akapit „Turn Zero cannot be used…” rozbity przez unitize na dwa akapity
# (pierwszy wiersz w kroju BoldCnIt) – akapit 0 dostaje krój tekstu i geometrię całości (tekst PL
# w akapicie 0, akapit 1 pusty); jednostki u5 + u6 (nagłówek 12.1) + u7 scalone, żeby dłuższy
# polski tekst przelewał się w łamie (obrazek kart opływany jak w oryginale – cuts na miejscu).
# Prawa łama: u8 + u9 (12.4) scalone – tekst może zejść do zdjęcia (y = 571).
P = Patch(D, 18); P.restore()
P.para(P.find('12. TURN ZERO EXPANSION'), 0, font=VENEER)
u5 = P.find('Turn Zero cannot be used')
P.para(u5, 0, font='MinionPro-Cn', align='justify', nlines=4, bottom=247.08, lastbase=243.12)
P.merge(u5, P.find('12.1 Turn Zero Components'))
P.merge(u5, P.find('Turn Zero consists of six'))
# obrazek kart (12.1) sięga w tle do y ≈ 378 – opływanie do tej wysokości (unitize: do 350,9,
# bo tam kończył się tekst EN); dłuższy tekst PL schodzi niżej
# QA 26.10: granica opływania schodkowa wzdłuż lewej krawędzi obróconych kart (tło 1 pt = 1 px:
# x ≈ 200–211 do y 318, ≈ 205 do y 340, ≈ 210–221 niżej; odstęp tekstu od kart ok. 6 pt) – szersze
# wiersze 12.1 obok kart, mniej rozstrzelone
for i, p in enumerate(u5['paras']):
    if p.get('cuts'):
        P.para(u5, i, cuts=[{'side': 'r', 'top': 272.77, 'bottom': 318.0, 'w': 101.5},
                            {'side': 'r', 'top': 318.0, 'bottom': 340.0, 'w': 96.5},
                            {'side': 'r', 'top': 340.0, 'bottom': 379.0, 'w': 91.5}])
P.set(u5, maxBottom=746.0)                   # QA: ostatni wiersz lewej łamy nie niżej niż w oryginale (744)
u8 = P.find('Cross-reference the result')
P.merge(u8, P.find('Where a Crisis result'))
# punkt 4 z 12.3 w całości w prawej łamie (w PL lewa łama jest pełna już po punkcie 3):
# akapit 0 prawej łamy jako pełny punkt listy (wcięcie wiszące numeru jak w punktach 1–3)
P.para(u8, 0, left=18.0, hang=9.0)
# UWAGA DO ROZGRYWKI – tło 147,4–188,2; 3 wiersze: skala 0,855, interlinia −3% -> odstępy ok. 5,8/5,8 pt
box(P, P.find('Due to the large number'), 160.68, 183.5, fixscale=0.855, pitch=11.64)
P.save()

# s. 19 – lewa łama: u4 + u5 scalone (punktor drugiego wypunktowania – osobna jednostka lines u6 –
# wchodzi do tekstu akapitu: wcięcie wiszące jak w pozostałych punktorach; u6 w trans = skip);
# punktory bez sztucznego prawego wcięcia; akapit 13.2 przechodzi do prawej łamy (u8 -> u9).
# Prawa łama: u13 + u15 scalone (punktor u14 – do tekstu, skip), granica dolna nad stopką.
P = Patch(D, 19); P.restore()
P.para(P.find('13.0 OPTIONAL RULES'), 0, font=VENEER)
u4 = P.find('13.1 Alternate Space Race Track')
u5 = P.find('Upon reaching space 4')
P.para(u5, 0, left=4.49, hang=13.5)
P.merge(u4, u5)
for i, p in enumerate(u4['paras']):
    if i >= 2:
        P.para(u4, i, right=0.0)
u8 = P.find('13.2 Promotional Cards')
P.para(u8, 1, lastjust=True)
P.set(u8, maxBottom=746.0)                   # QA: dół lewej łamy jak w oryginale (743), nie przy stopce
# UWAGA HISTORYCZNA – tło 601,9–678,2; 5 wierszy: skala 0,94, interlinia +4% -> odstępy ok. 9,5/9,5 pt
box(P, P.find('The abbreviations used on this track'), 619.68, 669.2, fixscale=0.94, pitch=12.5)
# UWAGA DO ROZGRYWKI – tło 243,8–320,2; 6 wierszy: skala 0,905, interlinia −2% -> odstępy ok. 6,7/6,7 pt
box(P, P.find('You may have to experiment'), 258.42, 314.0, fixscale=0.905, pitch=11.76)
P.set(P.find('13.3 Designers'), fixscale=PAGE19)  # QA S4: nagłówek w stopniu nagłówków 13.1/13.2 (skala strony)
u13 = P.find('We tried many variations')
u15 = P.find('Operations points may be used to purchase')
P.merge(u13, u15)
P.para(u13, 4, left=13.5, hang=13.5)
for i in (2, 3):
    P.para(u13, i, right=0.0)
P.para(u13, 3, align='left')                 # punktor 2 jak pozostałe punktory (do lewej)
P.set(u13, maxBottom=753.7)
P.save()

# s. 20 – lewa łama: u2 + u3 scalone (tekst 13.4 przelewa się do akapitu „Additional Influence…”);
# prawa łama: wstęp scenariusza (u6) dłuższy w PL – lista Etapów (u7) i dalszy tekst (u8) niżej
# o DY pt (u8 ma w oryginale ok. 40 pt wolnego miejsca nad znakiem promieniowania); u6 może zejść
# o DY6 pt niżej (odstęp nad listą jak w oryginale – linia bazowa ok. 16 pt nad pierwszą pozycją)
DY = 19.0
DY6 = 14.0
P = Patch(D, 20); P.restore()
u5 = P.unit('u5'); assert u5['paras'][0]['en'] == 'A LATE WAR SCENARIO'
P.para(u5, 0, font=VENEER)
u2 = P.find('13.4 Bidding for Sides')
P.merge(u2, P.find('Additional Influence received'))
box(P, P.find('Setup is complete and the US player'), 445.35, 499.8)  # PRZYKŁAD – tło 430,6–507,4
u6 = P.find('By Volko Ruhnke')
u7 = P.find('Turn 1 = 1945')
u8 = P.find('Thus, the Late War period')
P.move_to(u7, base=round(u7['lines'][0]['base'] + DY, 2))
P.move_to(u8, base=round(u8['paras'][0]['base'] + DY, 2))
P.set(u6, maxBottom=round(u6['maxBottom'] + DY6, 2))
P.set(u7, maxBottom=round(u7['maxBottom'] + DY, 2))
P.save()

# ---------------------------------------------------------------- QA runda 3 (27.10): rozstrzelone wiersze
# Lekkie zwężenie odstępów liter (hs ≥ 0,96) w akapitach z rozstrzelonymi wierszami (stretch.py) – przesuwa
# miejsca przełamania; 12.4 justowany jak sąsiednie akapity (uwaga kontroli). Wartości bezwzględne.
QA3 = {
    17: [('u4', 2, dict(hs=0.97)),            # 10.3.1 – 1. wiersz „…(Automatic Victory). Automa-”
         ('u7', 0, dict(hs=0.97)),            # 11.1 (ciąg dalszy) obok pola mapy
         ('u7', 2, dict(hs=0.98))],           # 11.2
    18: [('u5', 3, dict(hs=0.96)),            # 12.1 obok kart
         ('u5', 7, dict(hs=0.97)),            # 12.2 pkt 3
         ('u8', 0, dict(hs=0.97)),            # 12.3 pkt 4
         ('u8', 2, dict(hs=0.97)),            # „Powtórz te kroki…”
         ('u8', 5, dict(align='justify', hs=0.98))],   # 12.4 – justowany jak reszta strony
    19: [('u4', 1, dict(hs=0.97)),            # 13.1 – 1. wiersz
         ('u9', 0, dict(hs=0.955)),           # 13.2 (ciąg dalszy w prawej łamie)
         ('u9', 2, dict(hs=0.98))],           # „Karty te można stosować…”
    20: [('u2', 8, dict(hs=0.97))],           # „Dodatkowe Wpływy…”
}
for pg, items in QA3.items():
    P = Patch(D, pg)
    for uid, i, kw in items:
        P.para(uid, i, **kw)
    P.save()
