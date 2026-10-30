#!/usr/bin/env python3
# Łatki layoutu: TS_20th_Ann_Background_Book_WEB, s. 13–24 (redaktor tb13_24, 2026-10-26)
# Idempotentny: każda strona startuje od stanu z unitize (P.restore()).
import copy
import sys
sys.path.insert(0, '/home/claude/lay')
from laypatch import Patch
D = 'TS_20th_Ann_Background_Book_WEB'

ICON_BASE = 670.5      # linia bazowa wiersza z ikoną ☢ (s. 16) – zgodna z ostatnim wierszem akapitu (pomiar w renderze)
LIST_SCALE = 0.85      # wspólna stała skala wszystkich 13 pozycji listy pułapek DEFCON (s. 16)


def flow_to_lines(P, uid, bases):
    """akapit flow z kilkoma pozycjami listy (EN: jeden akapit) -> jednostka lines, jeden wiersz na
    pozycję, na liniach bazowych punktorów (stała pozycja jak w oryginale)"""
    u = P.unit(uid)
    if u['kind'] == 'lines':
        return u
    p = u['paras'][0]
    lines = []
    for b in bases:
        lines.append({'en': '', 'font': p['font'], 'size': p['size'], 'color': p.get('color', '#000000'),
                      'x0': p['x0'], 'x1': p['x1'], 'top': round(b - 0.73 * p['size'], 2),
                      'bottom': round(b + 0.27 * p['size'], 2), 'base': b, 'rot': 0,
                      'bg': p.get('bg', '#ffffff'), 'maxRight': u['maxRight'], 'maxLeft': p['x0'],
                      'align': 'left'})
    lines[0]['en'] = p['en']
    new = {'id': u['id'], 'kind': 'lines', 'x0': u['x0'], 'top': u['top'], 'x1': u['maxRight'],
           'bottom': lines[-1]['bottom'], 'maxBottom': u.get('maxBottom', u['bottom']),
           'maxRight': u['maxRight'], 'maxLeft': u.get('maxLeft', u['x0']), 'bg': u.get('bg', '#ffffff'),
           'lines': lines}
    u.clear()
    u.update(new)
    return u


def set_cut(P, uid, i, **kw):
    """zmiana opływanego obrazka (cuts) akapitu i: wartości bezwzględne"""
    para = P.unit(uid)['paras'][i]
    para['cuts'][0].update(kw)


def set_cut_new(P, uid, i, **kw):
    """nowy obszar opływania (cuts) akapitu i"""
    P.unit(uid)['paras'][i]['cuts'] = [dict(kw)]


def join_paras(P, uid, i):
    """akapit i+1 (dalszy ciąg akapitu i, rozbity w EN na dwa – np. wiersz z punktorem i reszta punktu)
    dołączony do akapitu i: jeden akapit z wcięciem wiszącym akapitu i"""
    u = P.unit(uid)
    a, b = u['paras'][i], u['paras'][i + 1]
    a['en'] = (a['en'] + ' ' + b['en']).strip()
    a['nlines'] = a.get('nlines', 1) + b.get('nlines', 1)
    for k in ('bottom', 'lastbase'):
        a[k] = b[k]
    a['x1'] = max(a['x1'], b['x1'])
    a['right'] = 0.0
    del u['paras'][i + 1]


def split_para_left(P, uid, i, head=False):
    """akapit i -> dwa akapity: i (strefa opływu karty, wyrównany do lewej) + i+1 (ciąg dalszy, justowany,
    w następnym wierszu – odstęp = interlinia); tekst dzielony w trans (koniec strefy opływu).
    head=True: dodatkowo wiersz nad kartą jako osobny akapit justowany na pełną szerokość (lastjust)"""
    u = P._u(uid)
    if head:
        h = copy.deepcopy(u['paras'][i])
        h.pop('cuts', None)
        h['lastjust'] = True
        h['lastbase'] = h['base']
        u['paras'].insert(i, h)
        nx = u['paras'][i + 1]
        d = round(h['base'] + h['pitch'] - nx['base'], 2)
        for k in ('base', 'lastbase', 'top', 'bottom'):
            nx[k] = round(nx[k] + d, 2)
        for c in nx.get('cuts', []):
            pass
        i += 1
    a = u['paras'][i]
    b = copy.deepcopy(a)
    b.pop('cuts', None)
    d = round(a['lastbase'] + a['pitch'] - b['base'], 2)    # render: odstęp = base(i+1) − lastbase(i)
    for k in ('base', 'lastbase', 'top', 'bottom'):
        b[k] = round(b[k] + d, 2)
    b['gap'] = b['pitch']
    a['align'] = 'left'
    u['paras'].insert(i + 1, b)


def split_head(P, uid, i):
    """akapit i -> wiersze nad kartą (osobny akapit justowany do pełnej szerokości, lastjust) + reszta
    obok karty (z opływem, wyrównana do lewej) w następnym wierszu; tekst dzielony w trans"""
    u = P._u(uid)
    a = u['paras'][i]
    h = copy.deepcopy(a)
    h.pop('cuts', None)
    h['lastjust'] = True
    h['lastbase'] = h['base']
    u['paras'].insert(i, h)
    d = round(h['base'] + h['pitch'] - a['base'], 2)
    for k in ('base', 'lastbase', 'top', 'bottom'):
        a[k] = round(a[k] + d, 2)
    a['align'] = 'left'


def tighten(P, uid, pitch=None, gaps=None):
    """zagęszczenie łamu: interlinia tekstu (pitch, ≤ 3 % mniej) i odstępy między akapitami (gaps:
    {stary odstęp: nowy}); odstęp liczony jak w render.py: base akapitu − lastbase poprzedniego.
    Odstępy porównywane z wartościami sprzed zmian; przesunięcie kumulowane (pozostałe odstępy bez zmian)"""
    u = P._u(uid)
    ps = u['paras']
    orig = [(p['base'], p['lastbase']) for p in ps]
    shift = 0.0
    for i, p in enumerate(ps):
        if pitch and p['font'].startswith('MinionPro') and abs(p['pitch'] - 13.2) < 0.05:
            p['pitch'] = pitch
        if i > 0 and gaps:
            g = round(orig[i][0] - orig[i - 1][1], 1)
            ng = next((v for k, v in gaps.items() if abs(k - g) < 0.4), None)
            if ng is not None:
                shift += ng - g
        if shift:
            for k in ('base', 'lastbase', 'top', 'bottom'):
                p[k] = round(p[k] + shift, 2)


GAPS = {17.7: 15.5, 18.0: 15.5, 25.8: 23.0}
HEAD_SIZE = 14.0      # nagłówki haseł kart (MyriadPro-BlackCondIt-SC700): w oryginale „fałszywe kapitaliki” –
                      # inicjały 14 pt, pozostałe litery 0,7 × 14 pt; unitize podał 10 albo 14 – ujednolicenie
                      # do 14 pt (interlinia 15 pt), jak na s. 25–36 (redaktor tb25_36)


def bigger_heads(P, size=HEAD_SIZE):
    """nagłówki haseł kart (krój …SC700) w stopniu HEAD_SIZE, bez wcięć (numer hasła ze zwykłą spacją,
    nie w polu wcięcia wiszącego)"""
    for u in P.lay['units']:
        for p in (u.get('paras') or []):
            if 'SC700' in p['font']:
                p.update(size=size, pitch=15.0, hang=0.0, left=0.0, indent=0.0)


def s13(P):
    # „Military Operations requirement…” + wiersz „USSR: …” (w EN dwa wiersze jednego akapitu, drugi
    # wcięty): bez justowania (w oryginale wiersz pierwszy nie jest rozciągany)
    P.para('u2', 1, align='left')
    P.set('u2', x1=304.8)              # pełna szerokość szpalty (jak u3); w EN wiersze krótsze
    P.set('u3', maxBottom=257.3)       # odstęp ok. 5 pt nad ramką KENNEDY (jak w oryginale)
    # „Wynik…” i „Kennedy zakłada ręce…” w stopniu oryginału (skala 1, jak „Chruszczow uśmiecha się…”);
    # tylko akapit kursywą „Sytuacja na planszy…” ma własną skalę
    h = P.split('u3', 1)                     # h = u9: „Sytuacja…”, „Kennedy…”
    P.split(h, 1)                            # u10: „Kennedy zakłada ręce na piersi.”
    P.set(h, maxBottom=241.5)                # „Sytuacja…” w 3 wierszach, bez kolizji z wierszem „Kennedy…”


def s14(P):
    # podpis pionowy „Sytuacja na koniec Etapu 3 (Turn 3)”: dłuższy niż EN – więcej miejsca wzdłuż
    # lewej krawędzi mapy, wyśrodkowany na środku podpisu EN (y ≈ 409,5)
    P.line('u2', 0, len=265.0, oy=536.0, base=536.0, top=270.0, bottom=536.0)


def s16(P):
    # lista 14 kart-pułapek: jednolita stała skala wszystkich pozycji (najdłuższe polskie pozycje,
    # np. „Sowieci zestrzeliwują KAL-007 (Soviets Shoot Down KAL-007, USA)”, nie mieszczą się w łamie
    # przy skali 1); pozycje na liniach bazowych punktorów jak w oryginale
    set_cut(P, 'u3', 3, w=148.0)          # karta Duck and Cover od x ≈ 158 – łam obok niej (odstęp ok. 10 pt; przełamanie bez rozstrzeleń)
    flow_to_lines(P, 'u5', [693.22, 707.72, 722.22, 736.72])
    join_paras(P, 'u11', 6)            # „• Several cards…” + dalszy ciąg punktu
    for uid in ('u5', 'u6'):
        P.set(uid, fixscale=LIST_SCALE)
    # wiersz z ikoną ☢ (y 660–675, x 147–162): akapit „W Twilight Struggle…” (u3, akapit 4) – osobna
    # jednostka u14 w stałej skali 0,86 zakotwiczona tak, że jej 4. wiersz stoi na linii ikony (jak w oryginale);
    # 4. wiersz opływa ikonę – kończy się tuż przed nią (justowany); „dla przypomnienia:” (u4, wiersz 1) za ikoną
    # na tej samej linii bazowej; punktory listy (u4) w stopniu tekstu głównego
    t = P.split('u3', 4)                     # t = u13; tekst prawej szpalty (podział u11 niżej) = u14
    pt = round(13.2 * 0.86, 3)
    P.set(t, body=False, fixscale=0.85, maxBottom=ICON_BASE + 3.0)
    P.move_to(t, base=round(ICON_BASE - 3 * pt, 2))
    P.para(t, 0, lastjust=True, ls=-0.01, cuts=[{'side': 'r', 'top': ICON_BASE - 7.5, 'bottom': 677.0, 'w': 149.6}])
    P.set('u3', maxBottom=round(ICON_BASE - 3 * pt - 8.0 - 6.0, 2))
    # strefa opływu karty Duck and Cover (łam x 45–147, < 110 pt): akapit „Choć to wyjątkowo ponury…”
    # podzielony na część obok karty (do lewej – justowanie dawało odstępy 1–3 em) i ciąg dalszy (justowany)
    split_para_left(P, 'u3', 3, head=True)
    P.set('u4', fixscale=0.86)
    P.line('u4', 1, base=ICON_BASE, top=ICON_BASE - 8.0, bottom=ICON_BASE + 3.0)
    for uid in ('u7', 'u8', 'u9', 'u10'):
        P.set(uid, fixscale=LIST_SCALE)
    # „Tear Down this Wall (US)” (pierwszy akapit u11) – osobna jednostka listy; dalszy tekst prawej
    # szpalty -> nowa jednostka u13 (tekst główny)
    h = P.split('u11', 1)                    # h = u13 (akapity 1–7)
    P.set('u11', nowrap=True, body=False, fixscale=LIST_SCALE)
    P.set('u9', maxRight=561.0)        # najdłuższa pozycja (KAL-007) – 2,5 pt w margines
    P.set(h, body=True)
    # prawa szpalta: dół nie niżej niż w oryginale (y ≈ 743) – mniejsze odstępy między punktami
    tighten(P, h, gaps=GAPS)
    P.set(h, maxBottom=743.5)


def s17(P):
    bigger_heads(P)
    # „Most importantly, keep an eye on the deck and know what cards remain in play”: podkreślenie
    # w oryginale to kreski w TLE (y ≈ 358: x 130–304,5; y ≈ 372: x 54–141) – unitize ich nie usuwa.
    # Akapit zaczyna się w miejscu oryginału (osobna jednostka u6), pierwszy wiersz to osobny akapit
    # justowany do pełnej szerokości, drugi zaczyna się od „karty pozostają w grze” – polskie
    # podkreślenie (<u>) pokrywa się z kreskami tła
    h = P.split('u2', 3)                     # h = u6: akapity 3–7
    p3 = h['paras'][0]
    a = copy.deepcopy(p3)
    a.update({'nlines': 1, 'lastbase': p3['base'], 'bottom': round(p3['top'] + 11.0, 2), 'lastjust': True})
    p3.update({'base': round(p3['base'] + p3['pitch'], 2), 'top': round(p3['top'] + p3['pitch'], 2),
               'nlines': p3['nlines'] - 1, 'gap': p3['pitch']})
    h['paras'].insert(0, a)
    P.para(h, 5, lastjust=True)              # akapit przechodzi do prawej szpalty
    # lewa szpalta: dół nie niżej niż w oryginale (y ≈ 740) – interlinia −2,7 %, mniejsze odstępy akapitów
    tighten(P, 'u2', pitch=12.85, gaps={17.7: 15.5, 25.8: 23.0})   # odstęp po punkcie (18 pt) bez zmian
    tighten(P, 'u6', pitch=12.85, gaps=GAPS)
    tighten(P, 'u4', gaps=GAPS)              # odstępy prawej szpalty jak w lewej (akapity 15,5 pt, nagłówki 23 pt)
    P.set('u6', maxBottom=742.5)
    P.para('u2', 0, align='justify')         # punkt „Bardziej ryzykownym…” justowany jak w oryginale
    # prawa szpalta: w oryginale kończy się na wysokości karty Olympic Games (y ≈ 699), poniżej wolne
    # miejsce do stopki – tekst może sięgać do y = 745; karta (do y ≈ 722) opływana do końca
    P.set('u4', maxBottom=745.0)
    set_cut(P, 'u4', 6, top=572.0, bottom=724.0)   # karta Olympic Games y ≈ 575–722
    # łam obok karty (x 431–567): justowanie dawało odstępy do 1,3 em – część akapitu obok karty do lewej,
    # wiersze nad kartą justowane (osobny akapit)
    split_head(P, 'u4', 6)


def s18(P):
    bigger_heads(P)
    # punkty listy rozbite w EN na wiersz z punktorem i resztę punktu -> jeden akapit z wcięciem wiszącym
    join_paras(P, 'u3', 3)
    join_paras(P, 'u3', 1)
    P.para('u2', 7, lastjust=True)           # akapit przechodzi do prawej szpalty
    # (akapit „Dla gracza USA…” przechodzi na s. 19 po pełnym zdaniu – ostatni wiersz bez justowania)
    # dół obu łamów nie niżej niż w oryginale (y ≈ 741) – interlinia −2,7 %, mniejsze odstępy akapitów
    for uid in ('u2', 'u3', 'u5'):
        tighten(P, uid, pitch=12.82, gaps={17.7: 14.5, 18.0: 14.5, 25.8: 22.0})
    P.set('u2', maxBottom=742.5)
    P.set('u5', maxBottom=742.5)
    P.set('u4', fixscale=0.85, maxRight=450.5)   # nagłówek „Lone Gunman”: musi skończyć się przed kartą (x ≥ 452)
    P.para('u4', 0, size=13.6)               # – stopień 13,6 (wizualnie jak 14 pt × skala strony 0,85)
    # karta Lone Gunman sięga do y ≈ 666 – opływanie do dolnej krawędzi karty
    set_cut(P, 'u5', 0, bottom=668.0, w=113.0)   # karta od x ≈ 452: odstęp ok. 6,5 pt
    set_cut(P, 'u2', 1, w=113.0)             # karta CIA Created do x ≈ 150: odstęp ok. 8 pt
    set_cut(P, 'u2', 2, w=113.0)


def s19(P):
    bigger_heads(P)
    # prawa szpalta: tekst nie może zejść na ozdobnik (sierp i młot / gwiazda NATO, y ≈ 382–400)
    P.set('u4', maxBottom=378.0)
    # karta Tear Down this Wall do x ≈ 422 – łam obok niej o ok. 1–2 pt szerszy (odstęp ≥ 7 pt)
    for i in (1, 2, 3):
        set_cut(P, 'u4', i, w=114.8)
    set_cut(P, 'u4', 1, top=145.0)           # karta Tear Down this Wall y ≈ 148–295
    set_cut(P, 'u4', 3, bottom=296.0)        # dół ramki karty y ≈ 295
    # dół łamów nie niżej niż w oryginale (y ≈ 746) – interlinia −2,7 %, mniejsze odstępy akapitów
    for uid in ('u2', 'u4', 'u6'):
        tighten(P, uid, pitch=12.85, gaps=GAPS)
    # łam obok karty (x 431–567): akapit „Dla USA…” i część akapitu „To w dużej mierze…” obok karty
    # wyrównane do lewej (justowanie dawało odstępy 0,6–0,9 em; dopuszczone w liście poprawek rundy 3),
    # ciąg dalszy „przegląd nie jest…” – justowany na pełnej szerokości łamu
    P.para('u4', 2, align='left')
    split_para_left(P, 'u4', 3)
    P.set('u2', maxBottom=745.0)
    P.set('u6', maxBottom=746.0)
    P.para('u6', 2, size=10.85)             # cytat MacArthura w jednym wierszu jak w oryginale (−1,4 %)


def s20(P):
    # lewa szpalta: karta Article 9 sięga do y ≈ 722 (opływanie do jej dolnej krawędzi), pod nią wolne
    # miejsce do stopki
    P.set('u2', maxBottom=745.0)
    set_cut(P, 'u2', 11, bottom=724.0)
    set_cut(P, 'u2', 10, top=573.0)          # karta Article 9 y ≈ 576–723
    P.para('u3', 11, lastjust=True)          # akapit przechodzi na s. 21


def s21(P):
    # tekst w niebieskiej ramce „Twenty Years of Struggle” nie może dochodzić do dolnej krawędzi ramki
    # (y ≈ 745; w EN ostatni wiersz y ≈ 722) – margines wewnętrzny ≥ 10 pt
    P.set('u6', maxBottom=735.0)
    # karta Dien Bien Phu (y ≈ 88–238): jedno opływanie na całą wysokość karty (w EN dwa fragmenty
    # z przerwą 180–198 i końcem 224 – dłuższy polski tekst wszedłby na kartę)
    set_cut(P, 'u2', 1, top=88.35, bottom=240.0)
    P.unit('u2')['paras'][2]['cuts'] = []


def s22(P):
    # lewa ramka: ostatni wiersz ok. 10 pt nad grafiką z okładkami (góra grafiki y ≈ 630,5), jak w oryginale
    P.set('u2', maxBottom=621.0)


def s23(P):
    P.para('u2', 5, lastjust=True)           # akapit przechodzi do prawej szpalty
    P.set('u2', maxBottom=744.5)              # dół lewego łamu nie niżej niż w oryginale


def s24(P):
    bigger_heads(P)
    # „1. a” + „SIA SCORING” (u4, w EN rozbite na dwa kroje) – jeden nagłówek w u3
    # hasło 4 (nagłówek + tekst) płynie za hasłem 3 (jedna jednostka u3) ze zwykłym odstępem przed nagłówkiem
    # (w PL hasło 3 jest krótsze – w EN dziura ok. 25 pt, było 50 pt); karta Middle East Scoring (y ≈ 364–521)
    # opływana jednym obszarem; hasło 5 (u7 + u8) zostaje na miejscu oryginału
    P.merge('u5', 'u6')
    P.merge('u3', 'u5')
    u3 = P.unit('u3')
    for i, p in enumerate(u3['paras']):
        p.pop('cuts', None)
    set_cut_new(P, 'u3', 5, side='l', top=364.57, bottom=523.0, w=114.59)
    P.set('u3', maxBottom=584.0)
    # nagłówek „5.” obok karty Five-Year Plan (x ≥ 189): dołączony do tekstu hasła (u8) – może się łamać,
    # opływa kartę (y ≈ 590–732)
    P.merge('u7', 'u8')
    P.set('u7', nowrap=False, body=True, maxBottom=741.0)
    u7 = P.unit('u7')
    for p in u7['paras']:
        p.pop('cuts', None)
    set_cut_new(P, 'u7', 0, side='r', top=588.0, bottom=734.0, w=114.71)
    # „7. Socialist Governments” obok Karty Chińskiej: polski nagłówek dłuższy niż miejsce do prawej
    # krawędzi łamu – scalony z akapitem pod nim (może się złamać, opływa kartę)
    P.merge('u10', 'u11')
    P.set('u10', nowrap=False, body=True)
    P.para('u10', 0, left=0.0, hang=0.0, indent=0.0)    # bez wysunięcia (weszłoby na kartę)
    set_cut(P, 'u10', 1, top=218.0)
    set_cut(P, 'u9', 1, top=132.0)           # Karta Chińska y ≈ 135–281
    # karta Vietnam Revolts sięga do y ≈ 625
    set_cut(P, 'u13', 0, bottom=627.0)       # (przed scaleniem z u12)
    # „9. Vietnam Revolts”: polski nagłówek dłuższy – scalony z tekstem hasła, opływa kartę (x ≥ 452)
    P.merge('u12', 'u13')
    P.set('u12', nowrap=False, body=True)
    set_cut(P, 'u12', 1, top=478.0)


# odstępy międzywyrazowe (ws, em) / zwężenie (hs) akapitów przy kartach – dobrane pomiarem rozstrzelenia
# (runda 3 poprawek: wiersze obok kart ≤ ok. 0,5 em); klucz: (jednostka, akapit) po wszystkich łatkach strony;
# s. 17 u6[0] – jednowierszowy akapit z podkreśleniem dopasowanym do kresek tła: lekkie rozstrzelenie liter (ls)
WS = {
    17: {('u6', 0): {'ls': 0.02}},
    19: {('u4', 1): {'hs': 0.98}},
    23: {('u2', 4): {'ws': 0.04}},
}


def apply_ws(P):
    for (uid, i), kv in WS.get(P.page, {}).items():
        P.para(uid, i, **kv)


for pg, fn in [(13, s13), (14, s14), (16, s16), (17, s17), (18, s18), (19, s19), (20, s20), (21, s21),
               (22, s22), (23, s23), (24, s24)]:
    P = Patch(D, pg)
    P.restore()
    fn(P)
    apply_ws(P)
    P.save()
