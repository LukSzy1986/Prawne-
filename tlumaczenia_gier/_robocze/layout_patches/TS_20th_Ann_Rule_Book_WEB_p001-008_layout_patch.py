#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Rule_Book_WEB, s. 1–8 (redaktor tr1_8, 2026-10-26)
# Idempotentna: każda strona startuje od stanu z unitize (P.restore()).
import copy
import sys
sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Rule_Book_WEB'


def zero_right(P, uid):
    """sztuczne prawe wcięcia (right) z poszarpanych wierszy EN – zerowane we wszystkich akapitach jednostki"""
    u = P.unit(uid)
    for i, p in enumerate(u['paras']):
        if p.get('right'):
            P.para(u, i, right=0.0)


def add_line(P, uid, src, dy, en='', **kw):
    """nowy wiersz jednostki lines: kopia wiersza src przesunięta o dy (pt) w dół – polski podpis w dwóch wierszach"""
    u = P.unit(uid)
    ln = copy.deepcopy(u['lines'][src])
    for k in ('top', 'bottom', 'base'):
        ln[k] = round(ln[k] + dy, 2)
    ln['en'] = en
    ln.update(kw)
    u['lines'].append(ln)
    u['bottom'] = max(u['bottom'], ln['bottom'])
    u['maxBottom'] = max(u.get('maxBottom', u['bottom']), ln['bottom'])
    return ln


def center_lines(P, uid, c, half):
    """wiersze wyśrodkowane w x = c, miejsce ±half"""
    u = P.unit(uid)
    for i, l in enumerate(u['lines']):
        w = l['x1'] - l['x0']
        P.line(u, i, x0=round(c - w / 2, 2), x1=round(c + w / 2, 2), align='center',
               maxLeft=round(c - half, 2), maxRight=round(c + half, 2))


def s3(P):
    # podpisy elementów: nazwa polska + EN w drugim wierszu (wiersz dodany łatką); karty Wydarzeń – EN scalone
    # z numerami („(Event Cards, #…)”), środek podpisu przesunięty tak, by nie nachodził na sąsiednie elementy
    add_line(P, 'u4', 0, 9.2, '[PL: (Statecraft Cards)]')
    add_line(P, 'u6', 0, 9.2, '[PL: (Crisis Cards)]')
    add_line(P, 'u13', 0, 9.2, '[PL: (Player Aids)]')
    center_lines(P, 'u5', 240.0, 44.0)        # obok stosu kart Kryzysów (prawa krawędź x ≈ 197)
    center_lines(P, 'u15', 476.0, 46.0)       # obok nakładki (prawa krawędź x ≈ 432)
    center_lines(P, 'u12', 480.1, 46.0)
    center_lines(P, 'u8', 209.3, 46.0)
    center_lines(P, 'u6', 164.4, 40.0)
    # QA: drugie wiersze podpisów jednym krojem (jak „(Player Aids)”): kursywa zwykła 9 pt; numery kart pogrubione jak w EN
    for uid in ('u5', 'u8', 'u12', 'u15'):
        P.line(uid, 1, font='MyriadPro-CondIt', size=9.0)
    # podpisy obrócone: dłuższy tekst – miejsce wzdłuż linii bazowej (len) i początek przesunięty w lewo
    P.line('u2', 0, len=58.0)
    P.line('u10', 0, ox=430.0, oy=101.5, len=104.0)
    P.line('u16', 0, ox=364.5, oy=591.7, len=63.0)
    # nagłówki sekcji (krój zastępczy Veneer szerszy): wyśrodkowane na środku nagłówka EN
    # kolor: w oryginale szary, fakturowany (w PDF zapisany jako #231f20) – średni kolor z obrazu strony
    for uid in ('u9', 'u3', 'u7', 'u14'):
        u = P.unit(uid)
        if u['kind'] == 'flow':
            P.para(u, 0, align='center', color='#978c84')
        else:
            P.line(u, 0, align='center', color='#978c84')
    P.set('u3', maxLeft=60.0, maxRight=322.0)
    P.line('u7', 0, maxLeft=70.0, maxRight=363.0)
    # SCENARIUSZ WSCHODZĄCE CZERWONE SŁOŃCE – dwa wiersze nad nakładką (wyżej wolne pole)
    u = P.unit('u14')
    P.set(u, nowrap=False, x0=318.0, x1=545.0, maxLeft=318.0, maxRight=545.0)
    P.para(u, 0, align='center', pitch=19.0, nlines=2)
    P.move_to(u, base=391.7)
    P.set(u, maxBottom=416.0)


def line_unit(P, src_uid, src_para, new_id, x0, x1, base, align='justify', lastjust=True):
    """jednowierszowa jednostka flow (kopia akapitu src) zakotwiczona linią bazową w y = base, x0–x1 –
    fragment wiersza między ikonami (żółte kółka z numerami w tle); dodawana za jednostką źródłową"""
    if any(x['id'] == new_id for x in P.lay['units']):
        raise ValueError(new_id)
    src = P.unit(src_uid)
    par = copy.deepcopy(src['paras'][src_para])
    par.update({'en': f'[fragment wiersza, EN: {src_uid}]', 'align': align, 'lastjust': lastjust, 'nlines': 1, 'ls': 0.0, 'ws': 0.0, 'hs': 1.0,
                'left': 0.0, 'right': 0.0, 'indent': 0.0, 'hang': 0.0, 'cuts': [], 'gap': None, 'cont': False,
                'base': base, 'lastbase': base, 'top': round(base - 7.04, 2), 'bottom': round(base + 3.96, 2),
                'x0': x0, 'x1': x1})
    u = {k: copy.deepcopy(v) for k, v in src.items() if k != 'paras'}
    u.update({'id': new_id, 'x0': x0, 'x1': x1, 'top': par['top'], 'bottom': par['bottom'], 'base': base,
              'maxBottom': round(base + 4.0, 2), 'maxRight': x1, 'maxLeft': x0, 'body': True, 'nowrap': False,
              'paras': [par]})
    u.pop('fixscale', None)
    P.lay['units'].insert(P.lay['units'].index(src) + 1, u)
    return u


S6 = 0.9    # s. 6: stała skala tekstu 3.1–3.4 (wiersze z ikonami i ich dalszy ciąg)


def s6(P):
    # 3.1–3.4: tekst przerywany ikonami ①–⑩ (tło). Każdy wiersz z ikoną = osobna jednostka (lub akapit) zakotwiczona
    # linią bazową oryginału, od lewego marginesu do ikony albo od ikony do prawego marginesu, justowana
    # z ostatnim wierszem (lastjust), żeby polski tekst dochodził do ikony. Stała skala S6 dla wszystkich fragmentów;
    # interlinia i odstępy akapitów podzielone przez S6, żeby wiersze stały na liniach bazowych oryginału.
    def keep_grid(uid):
        u = P.unit(uid)
        prev = None
        for i, p in enumerate(u['paras']):
            n = p.get('nlines', 1)
            pitch = round(p['pitch'] / S6, 3)
            if prev is not None:
                g = p['base'] - prev['lastbase']
                p['base'] = round(prev['lastbase'] + g / S6, 3)
            p['pitch'] = pitch
            p['lastbase'] = round(p['base'] + (n - 1) * pitch, 3)
            prev = p
        P.set(u, fixscale=S6)

    P.para('u4', 0, align='justify')                           # 3.1 ① … (2 wiersze)
    P.line('u3', 0, size=round(11.0 * S6, 2))                 # QA: „3.1” w stopniu numerów 3.2–3.4 (11 pt × S6)
    P.para('u5', 0, align='justify', lastjust=True, right=round(295.31 - 172.0, 2))   # … ②
    P.para('u5', 1, align='justify')
    P.set('u5', maxBottom=160.0)
    P.para('u6', 0, align='justify', lastjust=True)            # ② …
    P.set('u6', x0=189.3, maxLeft=189.3)                       # QA: wąski odstęp po kółku ②
    P.para('u7', 0, align='justify', lastjust=True, right=round(295.37 - 188.4, 2))   # 3.2 … ③
    P.para('u7', 1, align='justify', hs=0.96)                # R3: „1 w Iraku,” w 1. wierszu (bez luki po „1 w Syrii,”)
    P.set('u7', maxBottom=220.5)
    P.para('u8', 0, align='justify', lastjust=True)            # ③ …
    P.para('u9', 0, align='justify', lastjust=True, right=round(295.41 - 189.0, 2), ls=0.0)    # 3.3 … ④ (R3: bez rozstrzelenia liter)
    P.para('u9', 1, align='justify')
    P.set('u9', maxBottom=294.5)
    P.para('u9', 1, hs=0.98)                                   # QA: twarde spacje „1 w …” – ciaśniej o 1%
    P.para('u10', 0, align='justify', lastjust=True)           # ④ …
    for uid in ('u6', 'u8', 'u10', 'u14'):
        u = P.unit(uid)
        P.set(u, maxBottom=round(u['paras'][0]['base'] + 4.0, 2))
    # 3.4
    u11 = P.unit('u11')
    del u11['paras'][1:]
    P.para(u11, 0, align='justify', lastjust=True, right=round(295.33 - 232.3, 2))      # 3.4 … ⑤
    P.set(u11, bottom=316.16, maxBottom=316.2)
    P.lines_to_flow('u12', align='justify')                    # ⑤ … (w EN: wiersz „in the Space”)
    P.set('u12', x0=249.8, x1=295.4, maxLeft=249.8, maxRight=295.4, maxBottom=316.2)   # QA: odstęp po ⑤
    P.para('u12', 0, align='left', lastjust=False, indent=0.0, x0=249.8, x1=295.4, ls=0.0, ws=0.15)   # R3: krótki fragment do lewej
    line_unit(P, 'u11', 0, 'u18', 45.0, 295.33, 325.4)         # wiersz bez ikony
    line_unit(P, 'u18', 0, 'u19', 60.0, 295.33, 339.58)        # ⑥ …
    u13 = P.unit('u13')
    del u13['paras'][1:]
    P.para(u13, 0, align='left', lastjust=False, right=round(163.25 - 110.9, 2), ls=0.0, ws=0.15)     # … ⑦ (R3: do lewej, bez rozstrzelenia)
    P.set(u13, bottom=357.72, maxBottom=357.8)
    P.para('u14', 0, align='justify', lastjust=True)           # ⑦ …
    P.set('u14', x0=128.0, maxLeft=128.0)                      # QA: wąski odstęp po kółku ⑦
    line_unit(P, 'u13', 0, 'u20', 45.0, 162.6, 367.94)         # … ⑧
    line_unit(P, 'u20', 0, 'u21', 45.0, 150.2, 382.6)          # … ⑨
    line_unit(P, 'u21', 0, 'u22', 45.0, 155.0, 397.86)         # … ⑩
    line_unit(P, 'u22', 0, 'u23', 45.0, 295.4, 411.06, align='left', lastjust=False)   # koniec 3.4
    u15 = P.unit('u15')                                        # ⑧ … (dalsze wiersze – nowe jednostki)
    P.set(u15, x0=182.2, x1=295.36, maxLeft=182.2, bottom=371.9, maxBottom=371.9)   # QA: odstęp po ⑧
    P.para(u15, 0, align='justify', lastjust=True, cuts=[], nlines=1, lastbase=367.94, x0=182.2)
    line_unit(P, 'u15', 0, 'u24', 168.4, 295.36, 382.6)        # ⑨ … (QA: +1,5 pt odstępu po kółku)
    line_unit(P, 'u24', 0, 'u25', 173.8, 295.36, 397.86)       # ⑩ …
    for u in P.lay['units']:
        if u['kind'] == 'flow' and not u.get('role') and u['id'] not in ('u2', 'u16'):
            if u['id'] in ('u18', 'u19', 'u20', 'u21', 'u22', 'u23', 'u24', 'u25'):
                u['maxBottom'] = round(u['paras'][0]['base'] + 4.0, 2)
            keep_grid(u['id'])
    # ts_naglowki (30.10): przywrócone poprawki walidacji tsr_1_8#3/#5 – „, rozmieszczając 15/25 znacz-” (koniec „ników”
    # w następnym wierszu) i „Oba znaczniki Wyścigu Kosmicznego (Space Race)” przed ikoną ⑤: ścieśnienie (hs) fragmentów
    # przy ikonach ③ ④ ⑤ oraz 3.3 (u9[1]) – podział wierszy 3.3 bez dzielenia „Kana-dzie”, „Filipi-nach”
    for uid in ('u8', 'u10'):
        P.para(uid, 0, hs=0.94)
    P.para('u9', 1, hs=0.96)
    P.para('u11', 0, hs=0.93)


def s8(P):
    for uid in ('u5', 'u7'):
        zero_right(P, uid)
    P.para('u5', 3, align='left')          # QA: punkty w C. jednolicie z wolną prawą krawędzią (jak pozostałe)
    # R3 (QA/stretch): rozstrzelone wiersze – tracking akapitu (4.2, 4.3, A, B, C, D)
    for uid, i, hs in (('u3', 1, 0.97), ('u3', 2, 0.96), ('u3', 15, 0.95), ('u3', 17, 0.97), ('u5', 1, 0.97), ('u7', 3, 0.97)):
        P.para(uid, i, hs=hs)
    # R3 (QA: ramka UWAGA DO ROZGRYWKI 8,3 pt): wcięcie lewe 9 → 6 pt (ramka od x ≈ 40,7), tracking 0,95 – ok. 9 pt
    P.para('u4', 0, hs=0.95, left=6.0)


HEAD2 = 14.0   # R3 (QA pkt 8): nagłówki 2.x jak w oryginale – 14 pt efektywnie (runda 2: 12,2 pt)


def s5(P):
    zero_right(P, 'u2')
    P.set('u5', fixscale=round(HEAD2 / 14.0, 3))                # 2.2 KARTY
    P.para('u17', 1, size=round(HEAD2 / 0.931, 2))              # 2.3 ZNACZNIKI (w akapicie o skali strony 0,931)
    # 2.2.1: między panelem przykładowej karty (do y = 629) a ramką uwagi (od y = 684) – 4 wiersze po polsku
    P.move_to('u6', base=642.5)
    P.set('u6', maxBottom=682.0)
    # 2.2.2: punktory z gwiazdami – polski tekst przed ikoną gwiazdy (x ≈ 431) dłuższy niż EN: punktory
    # w x = 326 (wcięcie wiszące 8,5 pt, w tekście spacja półfiretowa), fragmenty przy ikonach o stałej skali 0,9
    for uid in ('u10', 'u12'):
        P.set(uid, x0=326.0, maxLeft=326.0)
        P.para(uid, 0, hang=8.5)
    P.set('u10', x1=429.5)                  # do ikony czerwonej gwiazdy (x ≈ 431)
    P.para('u14', 0, left=9.34, hang=8.5)
    # QA: tekst punktu kończy się ok. 2 pt przed ikoną gwiazdy (justowanie z ostatnim wierszem)
    P.set('u12', x1=432.0)
    for uid in ('u10', 'u12'):
        P.para(uid, 0, align='justify', lastjust=True)
    P.para('u14', 0, align='justify', lastjust=True, right=round(567.11 - 428.8, 2), ls=0.025)
    P.set('u15', x0=447.0, x1=567.6)
    for uid in ('u10', 'u11', 'u12', 'u13', 'u15'):
        P.set(uid, fixscale=0.9)
    P.para('u14', 2, align='justify')      # 2.2.3 – po polsku dwa wiersze (w EN jeden), jak inne punkty
    # R3 (QA): odstęp ok. 4 pt po obu stronach ikon gwiazd (czerwona x 431,3–444,6; niebieska 434,2–447,5; szara 431–445);
    # fragmenty przed gwiazdą wyrównane do lewej (bez justowania), tracking 0,97 we wszystkich fragmentach wierszy z gwiazdami
    P.set('u10', x1=427.0, maxRight=427.0)
    P.set('u12', x1=430.0, maxRight=430.0)
    for uid in ('u10', 'u12'):
        P.para(uid, 0, align='left', lastjust=False, hs=0.97)
    P.para('u14', 0, align='left', lastjust=False, right=round(567.11 - 427.0, 2), hs=0.97)
    for uid, x in (('u11', 448.8), ('u13', 451.7), ('u15', 449.0)):
        P.set(uid, x0=x, maxLeft=x)
        P.para(uid, 0, hs=0.97, x0=x)
    # R3 (QA: ostatni wiersz 2.1.8 prawie dotyka nagłówka 2.2 KARTY): tracking 0,95 – 2.1.8 w 5 wierszach jak w EN
    P.para('u4', 0, hs=0.95)
    P.para('u14', 4, hs=0.97)              # R3: 2.2.5 – rozstrzelony 2. wiersz
    # R3 (QA: ramka UWAGA przy 2.2.5 – 8,5 pt wobec 9,3–9,9 pt w innych ramkach): tekst do x = 562 (ramka do x ≈ 571,6),
    # tracking 0,95 – stopień efektywny ok. 9,3 pt (dwa wiersze jak w EN)
    P.set('u16', x1=562.0, maxRight=562.0)
    P.para('u16', 0, hs=0.95)


def s2(P):
    # nota „Od redakcji” (K.1; glosariusz TS 9.2): nowy akapit u4[6] pod tekstem 1.0 – krój tekstu, kursywa 9,5 pt
    u = P.unit('u4')
    if len(u['paras']) == 6:
        n = copy.deepcopy(u['paras'][5])
        base = round(n['lastbase'] + 18.0, 2)          # odstęp jak między akapitami (render liczy go z base)
        n.update({'en': '[Od redakcji – nota dodana w składzie PL]', 'font': 'MinionPro-CnIt', 'size': 9.5,
                  'pitch': 11.4, 'gap': 18.0, 'nlines': 5, 'cuts': [], 'base': base, 'top': round(base - 7.0, 2),
                  'lastbase': round(base + 4 * 11.4, 2), 'bottom': round(base + 4 * 11.4 + 2.5, 2)})
        u['paras'].append(n)
    zero_right(P, 'u6')
    # QA: nota nie niżej niż dolna krawędź zdjęcia w prawej łamie (y = 747); interlinia noty −3%
    P.set(u, maxBottom=747.0)
    P.para(u, 6, pitch=11.06, lastbase=round(u['paras'][6]['base'] + 4 * 11.06, 2))
    # R3 (QA: rozstrzelone wiersze 1.0): cała lewa łama 1.0 z trackingiem 0,97 (−0,015 em) – inne przełamania, odstępy ≤ 0,45 em
    for i in range(7):
        P.para(u, i, hs=0.97)


def s1(P):
    # spis treści: polskie tytuły mogą sięgać do numerów stron (kropki wiodące z tła zakrywa <hl> w kolorze ramki)
    u = P.unit('u1')
    for i, l in enumerate(u['lines']):
        if not l['en'][:1].isdigit():
            P.line(u, i, maxRight=426.0)
    P.set('u1', maxRight=426.0)
    for uid in ('u2', 'u5'):
        P.set(uid, x1=426.0, maxRight=426.0)
        P.para(uid, 0, align='left', right=0.0)
    for uid in ('u3', 'u4'):
        P.set(uid, maxRight=426.0)
    # QA: ogonek „Ę” w „KSIĘGA ZASAD” przecinał górną linię ramki spisu – stopień 46 pt, linia bazowa 2 pt wyżej
    P.line('u6', 0, size=46.0)
    P.move_to('u6', base=359.2)


# QA (26.10): ramki UWAGA / PRZYKŁAD – dolny margines wewnętrzny ok. 7 pt (dół tła ramki − 7 = maxBottom)
BOX_BOTTOM = {4: {'u3': 366, 'u5': 717}, 5: {'u3': 314, 'u16': 418, 'u7': 749, 'u8': 123},
              6: {'u16': 461}, 8: {'u6': 347, 'u4': 744}}


BOX_SIZE = {5: {'u16': 9.7}, 6: {'u16': 9.7}, 8: {'u4': 9.7}}   # stopień −0,3 pt (QA, pkt 4)
BOX_PITCH = {5: {'u16': 13.2}, 6: {'u16': 13.2}, 8: {'u4': 13.4, 'u6': 12.8}}    # dwa wiersze w ramce 40 pt – interlinia wypełnia ramkę równomiernie


def boxes(P):
    for uid, yb in BOX_BOTTOM.get(P.page, {}).items():
        P.set(uid, maxBottom=yb - 7.0)
    for uid, sz in BOX_SIZE.get(P.page, {}).items():
        P.para(uid, 0, size=sz)
    for uid, pt in BOX_PITCH.get(P.page, {}).items():
        P.para(uid, 0, pitch=pt)


def s4(P):
    P.para('u2', 0, size=round(HEAD2 / 0.919, 2))               # 2.1 MAPA GRY (skala strony 0,919)
    P.para('u4', 2, hs=0.97)                                     # R3: 2.1.4 – rozstrzelone wiersze (tracking −0,015 em)


PAGES = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 8: s8}

if __name__ == '__main__':
    only = [int(a) for a in sys.argv[1:]]
    for p, fn in sorted(PAGES.items()):
        if only and p not in only:
            continue
        P = Patch(D, p)
        P.restore()
        fn(P)
        boxes(P)
        P.save()
