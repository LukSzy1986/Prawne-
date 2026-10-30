#!/usr/bin/env python3
# Łatki layoutu: SPQR_Deluxe_Rule_book_WEB, s. 37–44 (redaktor sp37_44, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import sys; sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'SPQR_Deluxe_Rule_book_WEB'

# s. 37 – prawa łama: 10.12 (dokończenie) + 10.13 + punktory + reszta 10.13–10.15 w jednej jednostce
# (u6 + u7 + u9), żeby polski tekst mógł się przelewać; punktory 10.13 jako tekst akapitu
# („• ”, wcięcie wiszące 9 pt jak w pozostałych punktorach strony) – osobne kropki u8 pomijane w trans
P = Patch(D, 37); P.restore()
P.merge('u6', 'u7')
P.merge('u6', 'u9')
for i in (2, 3):
    P.para('u6', i, left=0.0, hang=9.0)
P.para('u6', 3, hs=0.97)                      # 2. punktor 10.13: lżejsze zwężenie zamiast rozstrzelonego wiersza
# lewa łama: koniec 9.96 nie może dochodzić do samego nagłówka 10.0 (18 pt) – odstęp ok. 10 pt
P.set('u2', maxBottom=383.0)
# nagłówek 10.0 (18 pt): bez zwężenia hs z oryginału – przy kroju zastępczym litery zachodziły na siebie
P.para('u3', 0, hs=1.0)
# 10.12 przechodzi z lewej łamy do prawej: ostatni wiersz lewej łamy justowany
P.para('u4', 5, lastjust=True)
# nagłówek 10.1 jako osobna jednostka poza skalą strony (12 pt jak pozostałe nagłówki tego rzędu):
# u4 = wstęp 10.0, u12 = nagłówek 10.1, u13 = tekst 10.1–10.12 (od miejsca z oryginału)
h = P.split('u4', 1)                          # u12: nagłówek + reszta
t = P.split(h, 1)                             # u13: tekst od 10.1
P.set(h, body=False, nowrap=True)
P.set(t, maxBottom=742.0)                     # dół łamu jak w oryginale (ok. 740 pt)
# odstęp nad nagłówkiem 10.1 jak w oryginale (ok. 6,5 pt): 10.0 i wstęp o 1,5 pt wyżej, wstęp z interlinią −3%,
# nagłówek 10.1 o 0,6 pt niżej
P.move_to('u3', base=404.6)
P.move_to('u4', base=418.95)
P.para('u4', 0, pitch=11.64)
P.move_to(h, base=479.0)
P.set('u4', maxBottom=470.0)
P.save()

# s. 38 – UWAGA DO ROZGRYWKI: tekst nie może wyjść poza beżowoszarą ramkę tła (480–651 pt)
P = Patch(D, 38); P.restore()
P.set('u8', maxBottom=649.0)
# lewa łama: koniec 10.16 z odstępem od nagłówka 10.2
P.set('u2', maxBottom=553.0)
# prawa łama: 10.22 w jednej jednostce aż do ramki UWAGI (480 pt); ostatni akapit opływa znacznik ROUTED
# tam, gdzie wypadnie (bez luki przed nim)
P.set('u7', maxBottom=478.0)
# UWAGA DO ROZGRYWKI ze skalą własną – wypełnia ramkę równomiernie
P.set('u8', body=False)
P.para('u4', 0, ws=-0.04)                     # UWAGA HISTORYCZNA: węższe odstępy – mniej rozstrzelone wiersze
# 10.21: akapity punktorów z interlinią 12 pt (w oryginale jednowierszowe miały 13,44 pt)
for i in range(4):
    P.para('u5', i, pitch=12.0)
P.para('u5', 3, align='justify')              # ostatni punktor 10.21 ma 2 wiersze – pierwszy justowany
P.save()

# s. 39 – 10.23 przechodzi do prawej łamy na granicy zdania („…zostają wyeliminowane.” | „Wszystkie pozostałe…”)
P = Patch(D, 39); P.restore()
P.set('u2', maxBottom=739.0)                  # lewa łama nie niżej niż w oryginale (736 pt)
# prawa łama: odstęp od stopki; opływanie znacznika RALLIED od jego górnej krawędzi (608 pt)
P.set('u4', maxBottom=741.0)
P.para('u4', 14, cuts=[{'side': 'r', 'top': 606.5, 'bottom': 644.0, 'w': 47.0}])
P.save()

# s. 40 – nagłówek 10.4 jako osobna jednostka jednowierszowa 12 pt (poza skalą strony): „10.4 ZWIĄZANIE WALKĄ
# (OPCJONALNE)” – znacznik ENGAGED pod nagłówkiem jak w oryginale; tekst 10.41–10.43 w nowej jednostce u9
P = Patch(D, 40); P.restore()
n = P.split('u7', 1)
P.set('u7', nowrap=True, body=False, fixscale=1.0)
# lewa łama: koniec 10.29 z odstępem od nagłówka 10.3
P.set('u2', maxBottom=255.0)
P.save()

# s. 41 – tytuł ramki Liwiusza: oba wiersze wyśrodkowane w ramce (w oryginale wcięcia dobrane do EN)
P = Patch(D, 41); P.restore()
for i in (0, 1):
    P.para('u6', i, align='center', left=0.0)
# nagłówek 11.0 (dwa wiersze) do lewej – justowany pierwszy wiersz miałby duże odstępy; bez zwężenia hs
# (litery zachodziły na siebie)
P.para('u2', 0, align='left', hs=1.0)
# ramki (UWAGA PROJEKTANTA, Liwiusz) ze skalą własną – tekst główny i nagłówki 11.1/11.2 w 100% (12 pt);
# ramka Liwiusza wypełnia tło równomiernie (dolny odstęp jak w oryginale)
P.set('u3', body=False)
P.set('u7', body=False, fixscale=0.984)          # ostatni wiersz ok. 6 pt nad dolną krawędzią ramki (737 pt)
P.save()

# >>> INDEKS (dane generowane: /home/claude/work/sp37_44/gen/index_gen.py – nie edytować ręcznie)
INDEX_SCALE = 0.97
INDEX_ROWS = {
 (42, 'u2'): (96.93, [
  ('Cohesion Hits: 10.1', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Cause Elimination of routed unit: 9.16, 10.27 (5th bullet)', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('(cont.) Cause Elimination of routed unit: 9.16, 10.27 (5th bullet)', 18.0, 6.02, 'left', False, True, 1.0, 0.0),
  ('Cause Rout: 6.53, 8.43, 8.47, 9.16, 10.14, 10.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('For Cavalry adjacent to Elephants: 9.15, 9.16', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Changing Facing: 7.14-7.16', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('For Double-Depth Phalanxes: 9.52, 9.53', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Elephant Rampage: 9.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Missile Hits: 8.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Movement: 6.13, 6.22, 6.41–6.44', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Orderly Withdrawal: 6.52, 9.21', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Phalanx standing instead of routing: 8.43, 8.47', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Rally: 10.28', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Shock Combat: 8.43, 8.46, 8.47, 9.53, 10.13', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('From Stacking: 6.63, 6.68', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Recovery From: 10.16', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Depletion: 10.3', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Facing: 7.1', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Advance After Combat Change: 8.52 – 8.53', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Change restricted: 7.24, 10.41', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Changing: 7.12-16, 9.65, 9.71', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Changing at completion of Orderly Withdrawal: 6.52', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Cohesion Hits for Changing: [See Cohesion hits: From Changing Facing]', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('(cont.) Cohesion Hits for Changing: [See Cohesion hits: From Changing Facing]', 18.0, 6.02, 'left', False, True, 1.0, 0.0),
  ('In-Column Units: 6.73', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Reaction Facing Change: 7.15-7.16', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Stacked units: 6.67', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Leaders: 4.0', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Activation: 5.11 – 5.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Adjacent to enemy combat unit while alone in hex: 4.72', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Carthaginian Command: 4.6', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Casualty: 4.73, 8.19', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Charisma: 4.1, 5.26, 8.46', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Combat: 4.7, 4.83', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Command Range: 4.1, 4.21, 4.32–4.34, 5.26, 5.45, 5.51, 7.33, 10.41', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('(cont.) Command Range: 4.1, 4.21, 4.32–4.34, 5.26, 5.45, 5.51, 7.33, 10.41', 18.0, 6.02, 'left', False, True, 1.0, 0.0),
  ('Die Roll of Doom: 5.33', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Elite Commander Initiative: 5.5', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Enemy ZOCs: 4.21, 4.24, 4.32, 4.4, 4.71–4.72, 4.83, 5.26, 5.31, 5.46, 7.23', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('(cont.) Enemy ZOCs: 4.21, 4.24, 4.32, 4.4, 4.71–4.72, 4.83, 5.26, 5.31, 5.46, 7.23', 18.0, 6.02, 'left', False, True, 1.0, 0.0),
  ('Facing: 4.85, 6.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Finished: 5.15, 5.26, 5.32-5.33, 5.41– 5.42, 5.44, 6.83', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Inactive: 5.11, 5.41-5.42, 5.44, 5.52', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Initiative: 4.1, 4.22, 4.91, 5.12, 5.21, 5.32, 5.41-5.42, 5.51, 6.81, 10.28, 11.1', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('(cont.) Initiative: 4.1, 4.22, 4.91, 5.12, 5.21, 5.32, 5.41-5.42, 5.51, 6.81, 10.28, 11.1', 18.0, 6.02, 'left', False, True, 1.0, 0.0),
  ('Killed: 4.56, 4.74, 4.84, 8.44, 8.46', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
 ]),
 (42, 'u7'): (103.68, [
  ('Leader Elephants: 4.8, 6.14-6.15, 6.61, 7.21, 9.12, 9.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Line Commands: 4.3, 4.31, 4.33–4.34, 4.4–4.6, 4.91, 5.23, 5.25, 6.66, 8.14, 9.24, 9.52, 9.66', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('(cont.) Line Commands: 4.3, 4.31, 4.33–4.34, 4.4–4.6, 4.91, 5.23, 5.25, 6.66, 8.14, 9.24, 9.52, 9.66', 18.0, 6.02, 'left', False, True, 1.0, 0.0),
  ('Momentum: [See Momentum]', 18.0, 6.02, 'left', False, False, 1.0, 0.0),
  ('Movement: 4.1, 5.24, 6.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Orderly Withdrawal: 6.54', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Overall Commanders: 4.4', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Proconsuls: 4.56', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Replacement: 4.4, 4.74, 11.1', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Rout: 9.14, 10.26', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Strategy Rating: 4.1, 4.33, 4.56, 4.6', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Tribunes/Praefects: 4.51-4.55, 4.74, 11.1', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Trump: [See Trump]', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Wounded: 4.73', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Missile Combat: 8.1', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Against Leaders: 8.19', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Cohesion Hits from: 8.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Depleted unit DRM: 10.32', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Die Roll Modifiers: 8.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Elephant Screens & Javelinists: 9.12-9.13', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Elephants take two Hits from: 8.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Extended Range: 8.16', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Firing During Movement: 8.11, 8.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Harassment and Dispersal Tactics: 8.3, 9.22, 9.31', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Line of Sight: 8.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Missile Low/No: 8.17-8.18, 10.28', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Missile Fire: 8.11-8.13', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Reaction Fire: 5.25, 8.2, 8.33, 8.55, 9.12–9.13, 9.16, 9.86', 18.0, 6.02, 'justify', True, False, 0.97, -0.06),
  ('Scorpios: 9.8', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('When Missile Units Fire: 8.12', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Withdrawal Fire: 6.55', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Momentum: 5.3, 5.14, 5.26, 5.42, 5.44, 5.52', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Movement: 6.0', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Cohesion Hits From: 6.13, 6.22, 6.41-6.45, 7.14', 18.0, 6.02, 'justify', True, False, 0.97, 0.0),
  ('Column Movement: 6.7', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Double-Depth Phalanxes: 9.52', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Elephant Pass-Thru: 9.11', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Elephant Rampage: 4.84, 9.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Facing and Movement: 6.32, 6.43, 6.52, 6.73, 7.13', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Leader Elephants: 4.83', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Manipular Line Extension: 9.68', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Movement Allowance: 6.11, 6.14', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Phalanxes (Two-Hex units): 6.4', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Restrictions: 6.12, 6.25, 6.3, 9.52, 9.61', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Terrain: 6.2, 6.42, 6.72, 10.27', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
 ]),
 (43, 'u2'): (60.93, [
  ('Triarii Restrictions: 9.71', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Orderly Withdrawal: 6.5', 0.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Cavalry Line Withdrawal: 6.57', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Cohesion Hits from: 6.52', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Elephants moving adjacent to Cavalry: 9.16', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Elephant Rampage – OW resolved before: 9.14', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('In-Column units restricted: 6.77', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Leaders: 4.72, 6.14, 6.54, 6.65', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Manipular Line Extension: 9.67', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Missile Fire from mounted archers: 8.12, 6.55', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Pre-arranged Withdrawal: 6.8', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Procedure: 6.51– 6.52', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Skirmishers: 6.51-6.52, 9.21-9.22, 6.52', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Orders: 4.2, 5.2, 6.64, 6.66', 0.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rout and Rally: 10.2', 0.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Automatic Depletion from Rally: 10.31', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Cohesion Hits after Rally: 10.28', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Eliminating units from Rout: 10.21, 10.24, 10.27', 18.0, 0.0, 'justify', True, False, 0.97, 0.0),
  ('Initial two-hex Rout: 10.22', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rally Attempt: 10.28', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rally Order: 5.22, 10.28', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rally Table: 10.29', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rallying a Depleted unit: 10.33', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rout from Shock: 8.43, 8.47', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rout Movement: 10.22–10.26', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rout Procedure: 10.21', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Rout Effects: 10.27', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Stacked units: 6.68', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('When all units would Rout: 10.15', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Shock Combat: 8.4', 0.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Advance After Combat: 6.13, 8.5, 8.62', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Depletion: 10.32', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Cavalry Pursuit: 8.47, 8.61-8.62', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Cohesion Hits: 8.43, 8.46, 10.1', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Collapse: 8.47', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Column Shifts: 6.26, 8.46, 9.41, 10.32', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Die roll Modifiers: 8.46', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
  ('Double-Depth Phalanxes: 9.53', 18.0, 0.0, 'justify', True, False, 1.0, 0.0),
 ]),
 (43, 'u4'): (60.93, [
  ('Elephant Pass-Thru: 9.11', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Elephant vs. Elephant: 9.17, 9.19', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Leaders: 4.71– 4.73, 8.44', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Phalanx Defense: 9.4', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Pre-Shock Procedure: 7.3, 8.42, 9.19, 9.23', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Pre-Shock TQ Check: 8.43, 9.11, 9.19, 9.23', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Resolution: 8.43 – 8.47', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Size Adjustments: 6.68, 8.46, 9.62', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Simultaneous Rout: 10.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Skirmishers: 9.23', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Stacking & Combat: 6.68, 9.53, 9.62', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Superiority: 8.46, 8.54, 8.72, 9.15, 9.17', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Terrain: 6.26', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Who Must/May Shock: 7.3, 8.41', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Stacking: 6.6', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Changing Top/Bottom unit: 6.66', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Double-Depth Phalanxes: 9.51', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Facing: 6.67', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Leader Elephants: 4.85', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Leaders in Stacks: 6.64- 6.65', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Moving Stacks: 6.64, 9.52', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Non-Roman: 6.61', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Roman Legion: 6.63, 9.61', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Trump: 5.15, 5.4', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Zones of Control (ZOCs): 7.2', 0.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Cavalry Move into Elephant ZOC: 9.15', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Condition of Collapse Die roll: 8.47', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Extent of: 7.21-7.22', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Leaders in Enemy ZOCs: 4.24, 4.33, 4.71– 4.72, 5.26, 5.31', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Column Restrictions: 6.71', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('MLE Restrictions: 9.66', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Movement Into: 7.23', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Movement Out of: 7.23', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Phalanxes In: 6.44 – 6.45', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Rout Restrictions: 10.22 – 10.24', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Withdrawal Restrictions: 6.55', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Shock Requirements: 8.42', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
  ('Skirmishers and Velites: 7.21', 18.0, 6.02, 'justify', True, False, 1.0, 0.0),
 ]),
}
# <<< INDEKS


def index_column(P, uid, base0, rows):
    """kolumna indeksu: jeden akapit na wiersz (hasło z kropkami wiodącymi albo jego dalszy ciąg);
    odstęp między hasłami 14,16 pt, w obrębie hasła 12 pt – jak w oryginale"""
    u = P.unit(uid)
    tpl = dict(u['paras'][0])
    for k in ('cuts', 'cont', 'hl', 'ls', 'hs', 'lastjust'):
        tpl.pop(k, None)
    paras, b = [], base0
    for i, (en, left, right, align, lastjust, cont, hs, ws) in enumerate(rows):
        if i:
            b = round(b + (12.0 if cont else 14.16), 2)
        p = dict(tpl)
        p.update(en=en, font='TimesNewRomanPSMT', size=10.0, align=align, pitch=12.0, nlines=1,
                 left=left, right=right, indent=0.0, hang=0.0, base=b, lastbase=b,
                 top=round(b - 6.93, 2), bottom=round(b + 3.07, 2),
                 x0=round(u['x0'] + left, 2), x1=round(u['x1'] - right, 2),
                 gap=None if i == 0 else (12.0 if cont else 14.16))
        if lastjust:
            p['lastjust'] = True
        if hs < 1.0:
            p['hs'] = hs                          # lekkie zwężenie: hasło w jednym wierszu jak w oryginale
        if ws:
            p['ws'] = ws                          # i węższe odstępy między wyrazami (hasło z długą listą numerów)
        paras.append(p)
    u['paras'] = paras
    mb = u.get('maxBottom', u['bottom'])          # granica z oryginału zostaje (bez poszerzania)
    u['base'], u['top'], u['bottom'] = paras[0]['base'], paras[0]['top'], paras[-1]['bottom']
    u['maxBottom'] = mb
    u['fixscale'] = INDEX_SCALE                   # stała skala (liczba kropek dobrana do tej skali)


# s. 42–43 – indeks zasad: każde hasło (lub jego dalszy ciąg) jako osobny akapit jednowierszowy,
# kropki wiodące i numery do prawej krawędzi łamy (justowanie wiersza; liczba kropek z pomiaru – generator)
P = Patch(D, 42); P.restore()
P.merge('u2', 'u3')                           # lewa łama w jednej jednostce (u4 „Cause Rout:” – skip w trans)
for uid in ('u2', 'u7'):
    index_column(P, uid, *INDEX_ROWS[(42, uid)])
P.save()

P = Patch(D, 43); P.restore()
for uid in ('u2', 'u4'):
    index_column(P, uid, *INDEX_ROWS[(43, uid)])
P.save()

# s. 44 – tylna okładka: adres w dwóch wyśrodkowanych wierszach jak w oryginale (bez wcięcia wiszącego
# z unitize; łama poszerzona symetrycznie, żeby „…CA 93232–1308” nie łamało się; podział wierszy <br> w trans)
P = Patch(D, 44); P.restore()
P.para('u2', 0, hang=0.0)
P.set('u2', x0=206.0, x1=406.0)
P.save()
