#!/usr/bin/env python3
# Łatki layoutu: SPQR_Deluxe_Rule_book_WEB, s. 1–9 (redaktor sp1_9, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'SPQR_Deluxe_Rule_book_WEB'

# s. 1 – spis treści: bez rozstrzelenia liter (ls z oryginału dotyczyło kropek wiodących)
P = Patch(D, 1); P.restore()
for uid in ('u4', 'u7'):
    u = P.unit(uid)
    for i in range(len(u['paras'])):
        # (qa 26.10) wiersze spisu justowane do pełnej szerokości: kropki kończą się stałym odstępem przed numerem
        P.para(u, i, ls=0.0, align='justify', lastjust=True)
u = P.unit('u8')
for i in range(len(u['lines'])):
    P.line(u, i, ls=0.0)
P.line(u, 1, align='right')                  # „Ruch …… 14”, „Indeks zasad …… 42”: numer strony
P.line(u, 2, align='right')                  # w jednej kolumnie z numerami z u4/u7
P.save()

# s. 2 – łamy kończą się nad stopką (jak w oryginale, ok. y = 738), nie na 748; akapity przechodzące
# do następnej łamy/strony justowane do końca
P = Patch(D, 2); P.restore()
P.set('u3', maxBottom=741.0)
P.set('u7', maxBottom=741.0)
P.para('u3', 5, lastjust=True)               # „Dla tych, którzy…” – ciąg dalszy w u5
P.para('u7', 17, lastjust=True)              # 2.23 – ciąg dalszy na s. 3
# (qa) prawa łama: koniec 1.0 („…wodzem.”) wypada wyżej niż w oryginale – nagłówek 2.0 i tekst pod nim
# o 26 pt wyżej (odstęp ok. 20 pt jak w oryginale)
P.move_to('u6', base=118.63)               # (qa3) prawa łama s. 2 krótsza o wiersz (podział p2_dla n=77)
P.set('u6', maxBottom=142.24)
P.move_to('u7', base=150.97)
P.save()

# s. 3 – diagram 2.25: podpisy, do których linia odnośnika dochodzi z prawej, wyrównane do prawej
# krawędzi z oryginału (polskie podpisy są dłuższe); dwuwierszowy podpis słonia szerszy (do ramki)
P = Patch(D, 3); P.restore()
P.line('u5', 0, align='right')                         # „Liczebność” (falanga)
P.line('u8', 0, align='right', maxLeft=457.0)          # „Liczebność” (Thrace) – odstęp od „Typ oddziału”
P.line('u11', 0, align='right', maxLeft=455.0)         # „Klasa oddziału” (Seleucid) – odstęp od „Nazwa/ozn.”
P.line('u11', 1, align='right', maxLeft=457.0)         # „Liczebność” (Seleucid)
# (qa) 8 pt sprawdzone: przy 8 pt podpisy nachodzą na „Rodzaj pocisku”/„Typ oddziału” – zostaje ok. 7,3 pt
P.para('u7', 0, ls=-0.02)                                            # „Nazwa/oznacz.” (piechota) do linii odnośnika
P.set('u14', x1=563.0)                                 # „Osłona łuczników / Rodzaj pocisku”
for i in range(2, 6):                                  # podpisy falangi: jednostka nowrap pomija „cuts”,
    P.para('u4', i, left=113.4)                        # więc wcięcie jak w oryginale (x = 437,4)
P.para('u7', 4, align='left')                          # „Zdolność ruchu / Jakość wojsk (TQ)”
P.para('u10', 3, align='left')
P.set('u2', maxBottom=741.0)
P.set('u17', maxBottom=741.0)
# (qa) stała skala tekstu głównego 0,935 (s. 3 tworzy rozkładówkę ze s. 2 – 0,894; bez tego tekst skakałby do 0,98)
P.set('u2', fixscale=0.935)
P.set('u17', fixscale=0.935)
P.save()

# s. 4–6 – hasła 2.4 z ilustracją żetonu (obrazek opływany): każde hasło z żetonem w osobnej jednostce
# zakotwiczonej w miejscu oryginału, żeby opis stał obok swojego żetonu (polski tekst jest dłuższy);
# łamy kończą się nad stopką (y = 741)
def split_at(P, uid, idx):
    u = P.unit(uid)
    for i in sorted(idx, reverse=True):
        P.split(u, i)

P = Patch(D, 4); P.restore()
P.set('u2', maxBottom=741.0)
P.set('u4', maxBottom=741.0)                 # pod hasłem „Triarii” w oryginale wolne miejsce do stopki
split_at(P, 'u4', [5, 6, 7])                 # Velites, Hastati, Principes (+ Triarii)
# (qa3) jak w oryginale: nazwa hasła przy górnej krawędzi żetonu („Principes” 638,73, „Triarii” 704,13 – linie
# bazowe z oryginału); po „Hastati” zostaje wolne miejsce (polski tekst krótszy). „Triarii”: na s. 4 trzy wiersze
# obok żetonu, dalszy ciąg (2 wiersze) na s. 5 – podział w src/splits.py (p4_triarii)
pr_u = P.find('Principes: The third line')
tr_u = P.split(pr_u, 1)
P.move_to(pr_u, base=638.73)
P.move_to(tr_u, base=704.13)
P.set(pr_u, maxBottom=round(tr_u['top'] - 1, 2))
P.para(tr_u, 0, lastjust=True)               # „Triarii” – ciąg dalszy (2 wiersze) na s. 5, jak w oryginale
P.save()

B5_MN = 262.5                                # s. 5 L: „Manipuł” (bez żetonu) – w połowie wolnego miejsca
P = Patch(D, 5); P.restore()
P.set('u2', maxBottom=741.0)
P.set('u4', maxBottom=741.0)
# (qa3) lewa łama: u2 = dokończenie „Triarii” (2 wiersze), dalej hasła w osobnych jednostkach; nazwy haseł przy
# górnej krawędzi żetonów (linie bazowe z oryginału); „Manipuł” (bez żetonu) w połowie wolnego miejsca między
# „Alae” a „Ciężką piechotą”
split_at(P, 'u2', [1, 2, 3, 4, 5])           # Alae, Maniple, Heavy Inf., Phalanx, Legion Inf.
S5L = [('Alae Sociorum: The', 90.33), ('Maniple: Each line', B5_MN), ('Heavy Infantry: Descendants', 341.13),
       ('Phalanx: A formation', 418.53), ('Legion Infantry: A game', 615.93)]
s5u = [P.move_to(P.find(en), base=b) for en, b in S5L]
P.set('u2', maxBottom=round(s5u[0]['top'] - 1, 2))   # dokończenie „Triarii”
for a, b in zip(s5u, s5u[1:]):
    P.set(a, maxBottom=round(b['top'] - 1, 2))
P.set(s5u[-1], maxBottom=741.0)
split_at(P, 'u4', [1, 2, 4, 5, 6, 7])        # Barbarian Inf., Light Inf. (+Skirmishers), Javelinists, Archers, Slingers, Light Cav.
P.para(P.find('Light Cavalry: Essentially'), 0, lastjust=True)   # „Light Cavalry” – ciąg dalszy na s. 6
# (qa) prawa łama: koniec hasła ok. 8 pt nad żetonem następnego hasła (było 1–3 pt)
for en in ('Barbarian Infantry:', 'Light Infantry: A gener', 'Javelinists:', 'Archers: Light', 'Slingers:',
           'Light Cavalry: Essentially'):
    nxt = P.find(en)
    ctop = min(c['top'] for pa in nxt['paras'] for c in pa.get('cuts', []))
    prev = P.lay['units'][P.lay['units'].index(nxt) - 1]
    P.set(prev, maxBottom=round(ctop - 6.0, 2))
P.save()

P = Patch(D, 6); P.restore()
P.set('u2', maxBottom=741.0)
P.set('u8', maxBottom=741.0)
split_at(P, 'u2', [1, 2, 3, 4, 5])           # Lancers, Heavy Cav., Roman Cav., Elephants, Scorpio
# (qa3) „Skorpion” – nazwa hasła przy górnej krawędzi żetonu, jak w oryginale (po „Słoniach” wolne miejsce)
sc_u = P.move_to(P.find('Scorpio: A Scorpio'), base=631.93)
P.set(P.find('Elephants: By this time'), maxBottom=round(sc_u['top'] - 1, 2))
# (qa) ramka UWAGA HISTORYCZNA: interlinia +3% i tekst o 2 pt niżej – równe marginesy górny i dolny
u = P.find('HISTORICAL NOTE: Roman battles')
P.para(u, 0, pitch=12.36)
P.move_to(u, base=377.3)
P.save()

# s. 7 – przykładowy żeton dowódcy: tytuł wyśrodkowany nad żetonem jak w oryginale (polski dłuższy);
# „Oznaczenie inicjatywy / elitarnej” wyrównane do prawej (linia odnośnika od prawego końca);
# „Współczynnik / rozkazów liniowych” o 4,5 pt w prawo (odstęp od „Inicjatywa”)
P = Patch(D, 7); P.restore()
P.para('u6', 1, left=80.7)
# (qa) tytuł „Przykładowy żeton dowódcy” – osobna jednostka w stałym stopniu 8 pt na linii oryginału
P.set(P.split('u6', 1), fixscale=1.0)
P.set('u8', x0=320.0)
P.para('u8', 0, align='right')
P.line('u7', 2, align='right')
for i in (6, 8):
    ln = P.unit('u7')['lines'][i]
    P.line('u7', i, x0=round(ln['x0'] + 4.5, 2), x1=round(ln['x1'] + 4.5, 2))
P.set('u3', maxBottom=741.0)
P.set('u11', maxBottom=741.0)
P.merge('u2', 'u3')                          # lewa łama: faza B i etap starcia – tekst przepływa (pod u3 wolne miejsce)
P.save()

# s. 8 – nagłówek „4.3 LEADER CAPABILITIES: LINE COMMANDS” (12 pt, pogrubiony) scalony w units z akapitem
# 4.31 – wydzielony jako osobny akapit (krój, stopień i odstępy jak nagłówek 4.2 nad 4.21)
import copy
P = Patch(D, 8); P.restore()
u = P.unit('u2')
src = u['paras'][10]
if src['en'].startswith('<b>4.3 LEADER CAPABILITIES: LINE COMMANDS 4.31</b>'):
    h = copy.deepcopy(u['paras'][0])
    h.update(top=src['top'], bottom=round(src['top'] + 12.0, 2), base=src['base'], lastbase=src['base'],
             nlines=1, right=0.0, gap=src['gap'], x1=297.13,
             en='<b>4.3 LEADER CAPABILITIES: LINE COMMANDS</b>')
    src.update(en=src['en'].replace('<b>4.3 LEADER CAPABILITIES: LINE COMMANDS 4.31</b>', '<b>4.31</b>'),
               base=round(src['base'] + 14.0, 2), top=round(src['base'] + 14.0 - 6.93, 2),
               nlines=src['nlines'] - 1, gap=14.0)
    u['paras'].insert(10, h)
P.set('u2', maxBottom=741.0)
P.set('u6', maxBottom=741.0)
P.save()

# s. 9 – ostatni akapit (4.56) przechodzi na s. 10 (carry): justowany do końca łamu; łam kończy się nad stopką
P = Patch(D, 9); P.restore()
# 4.4: (qa) punkt 1 listy zaczyna się pod żetonem wodza (wcięcie opływu kończy się na 329,1) – większy odstęp
# przed listą; odstępy między punktami jak w oryginale (lista mieści się nad ramką uwagi historycznej)
for pa in P.unit('u4')['paras'][2:]:          # odstęp liczony z linii bazowych: przesuwamy całą listę
    for k in ('top', 'bottom', 'base', 'lastbase'):
        pa[k] = round(pa[k] + 4.5, 2)
P.set('u9', maxBottom=741.0)
P.para('u9', 2, lastjust=True)
P.para('u4', 4, align='justify')             # (qa) 4.4 pkt 3 – dwa wiersze, justowanie z dzieleniem
P.save()

# s. 6–9 – granice jednostek przy ramkach uwag (tło): unitize dawał maxBottom sięgające ramki lub poza nią;
# tekst nad ramką kończy się ok. 4 pt nad jej górną krawędzią, tekst w ramce – ok. 2,5 pt nad dolną
# (ramki zmierzone na tle: s. 6 364–452, s. 7 555–630, s. 8 218–294, s. 9 170–257, 479,5–615,5, 503,5–554,5)
for pg, lims in ((6, {'u4': 360.0, 'u5': 449.5}),
                 (7, {'u9': 551.0, 'u10': 627.5}),
                 (8, {'u4': 214.0, 'u5': 292.4}),
                 (9, {'u2': 166.0, 'u3': 254.5, 'u4': 475.5, 'u5': 613.0, 'u7': 499.5, 'u8': 552.0})):
    P = Patch(D, pg)                         # bez restore – uzupełnia łatki stron powyżej
    for uid, mb in lims.items():
        P.set(uid, maxBottom=mb)
    P.save()

# (qa 26.10) nagłówki X.Y i nagłówki faz (12 pt pogrubione) wewnątrz jednostek tekstu głównego mają mieć
# 12 pt niezależnie od skali strony: stopień i interlinia = wartość z oryginału / skala strony (H12 – skale
# stron ustalone pomiarem fit.py po wszystkich zmianach)
H12 = {2: 0.894, 3: 0.935, 6: 0.904, 7: 0.886, 8: 0.854, 9: 0.856}
for pg, sc in H12.items():
    P = Patch(D, pg)                         # bez restore – uzupełnia łatki stron powyżej
    for u in P.lay['units']:
        if u['kind'] != 'flow' or not u.get('body'):
            continue
        for pa in u['paras']:
            if pa['font'] == 'TimesNewRomanPS-BoldMT' and (pa.get('h12') or abs(pa['size'] - 12.0) < 0.01):
                pa.update(size=round(12.0 / sc, 3), pitch=round(14.4 / sc, 3), h12=True)
    P.save()

# (qa 26.10) ramki uwag – równe marginesy tekstu w tle ramki (zasada 4 kontroli): s. 7 tekst niżej; s. 8 interlinia
# −3% i tekst wyśrodkowany (ostatni wiersz dotykał dolnej krawędzi); s. 9 (UWAGA PROJEKTANTA, UWAGA HISTORYCZNA)
# za duży pusty dół – interlinia +10% (stopień bez zmian = tekst główny) i tekst wyśrodkowany w ramce; s. 9 UWAGA DO
# ROZGRYWKI – tekst niżej
FR7, FR8, FR9A, FR9B = 2.35, -0.85, 1.65, 2.65
FRAME = {7: {'u10': (None, FR7)}, 8: {'u5': (11.64, FR8)}, 9: {'u3': (13.2, FR9A), 'u5': (13.2, FR9B), 'u8': (None, 1.75)}}
for pg, units in FRAME.items():
    P = Patch(D, pg)                         # bez restore – uzupełnia łatki stron powyżej
    for uid, (pitch, dy) in units.items():
        u = P.unit(uid)
        if pitch:
            P.para(u, 0, pitch=pitch)
        P.move_to(u, base=round(u['paras'][0]['base'] + dy, 2))
    P.save()

# (qa3 27.10) nagłówki główne 18 pt (1.0, 2.0, 3.0, 4.0): tracking z oryginału (hs 0,889 ≈ −1 pt) zjadał odstęp
# międzywyrazowy („SEKWENCJA GRY”, „WPROWADZENIE”) – tracking ok. −0,3 pt (hs 0,967)
for pg, uid in ((2, 'u2'), (2, 'u6'), (6, 'u7'), (7, 'u5')):
    P = Patch(D, pg)                         # bez restore – uzupełnia łatki stron powyżej
    P.para(uid, 0, hs=0.967)
    P.save()

# (qa3) rozstrzelone wiersze (stretch.py ≥ 0,7 em): lekkie zwężenie odstępów liter (hs ≥ 0,94) w pojedynczych akapitach
import re as _re
SPACING = {2: [('For Those Who Have Not', 0.97)],
           4: [('Leader:</b> Interchangeable', 0.97)],
           5: [('Phalanx:</b> A formation', 0.97), ('Javelinists:</b> Skirmishers', 0.97)],
           6: [('HISTORICAL NOTE: Roman battles', 0.97)],
           7: [('DESIGN NOTE: This rating', 0.97)]}
for pg, items in SPACING.items():
    P = Patch(D, pg)                         # bez restore – uzupełnia łatki stron powyżej
    for en, hs in items:
        hits = [(u, i) for u in P.lay['units'] if u['kind'] == 'flow'
                for i, pa in enumerate(u['paras']) if _re.sub(r'<[^>]+>', '', pa['en']).startswith(_re.sub(r'<[^>]+>', '', en))]
        assert len(hits) == 1, (pg, en, len(hits))
        P.para(hits[0][0], hits[0][1], hs=hs)
    P.save()
