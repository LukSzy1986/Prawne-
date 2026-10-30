#!/usr/bin/env python3
"""render.py DOK [strony] [--pages A-B] [--png] [--tag TAG] [--out PLIK.pdf] [--keep-html]

Skład przekładu na tle oryginału.
Dla każdej strony buduje HTML (bloki jednostek pozycjonowane absolutnie w pt, @font-face z lokalnymi
fontami), renderuje go w Chromium (playwright, page.pdf o rozmiarze strony oryginału, bez marginesów),
nakłada wynik na stronę tła /home/claude/lay/bg/DOK.pdf (pikepdf, overlay) i zapisuje
/home/claude/final/base_DOK.pdf (bez etykiet – te nakłada apply_labels.py z build_doc.sh).

  strony / --pages A-B  tylko wskazane strony; gdy base_DOK.pdf istnieje, są w nim podmieniane,
                        gdy nie – powstaje base z nałożonym tekstem tylko na tych stronach
  --png                 TRYB PODGLĄDU: base_DOK.pdf NIE jest zmieniany; PNG 100 dpi stron do
                        /tmp/fit_DOK_TAG/pNNN.png (TAG z --tag, domyślnie „render”)
  --out PLIK.pdf        zapisz wynik (tylko renderowane strony) do wskazanego pliku
  --keep-html           zostaw pliki HTML stron w /home/claude/lay/html/DOK/ (do diagnozy)

Źródła: layout/DOK/pNNN.json (geometria), trans/DOK/pNNN.json (przekład; brak pliku lub jednostki
= tekst oryginału), carry/DOK/pNNN.json (tekst wstawiany w miejsce @@CARRY@@).
Dopasowanie: skrypt JS mierzy jednostki; tekst główny (jednostki flow w kroju tekstu głównego) ma
WSPÓLNĄ skalę strony (zmienna CSS --s: stopień i interlinia), pozostałe jednostki skalują się osobno.
Skala < 0,85 = „do sprawdzenia”. Wynik pomiarów: /home/claude/final/fit_DOK.json.
"""
import html as htmlmod
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from laylib import (FINAL, ROOT, carry_path, font_face_css, fontcss, layout_path, load_json,  # noqa: E402
                    norm_text, page_count, parse_pages, save_json, tokenize, trans_path)
from plhyph import hyph_word  # noqa: E402
from enhyph import hyph_en  # noqa: E402

MIN_OK = 0.85          # najmniejsza akceptowalna skala
MIN_SCALE = 0.5        # poniżej tej skali tekst już nie jest zmniejszany (nadmiar zostaje)
AUTO_KEEP_ROLES = ('header', 'pageno', 'footer', 'slug')

# Żywa pagina: jednostki flow z jednym akapitem równym kluczowi (porównanie bez znaczników
# i niezależne od rodzaju kresek/spacji) są – przy „keep” lub braku wpisu w trans – składane po polsku.
# Znacznik stylu z wartości (np. <i>) jest zamieniany na znacznik użyty w oryginale (np. <f Font>).
HEADER_MAP = {
    'Space Empires: All Good Things - <i>Master Rule Book - Version 1.0</i>':
        'Space Empires: All Good Things – <i>Główna księga zasad – wersja 1.0</i>',
    '<b>Space Empires: All Good Things - </b>Competitive Scenario Book - Version 1.0':
        '<b>Space Empires: All Good Things – </b>Księga scenariuszy rywalizacyjnych – wersja 1.0',
    'SPACE EMPIRES — Scenario Book': 'SPACE EMPIRES — Księga scenariuszy',
    'SPACE EMPIRES — Rules of Play': 'SPACE EMPIRES — Zasady gry',
    'SPACE EMPIRES — Close Encounters Expansion': 'SPACE EMPIRES — dodatek Close Encounters',
    'REPLICATORS — Rules of Play': 'REPLICATORS — Zasady gry',
}
_HMAP = {norm_text(k): v for k, v in HEADER_MAP.items()}

PL_LETTERS = 'A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż'
_PROT = '\ue000'


# ====================================================================== tekst
def header_text(en):
    """tłumaczenie żywej paginy albo None; przenosi znacznik stylu z oryginału"""
    pl = _HMAP.get(norm_text(en))
    if pl is None:
        return None
    t_en = [t for t in tokenize(en) if t[0] == 'o']
    t_pl = [t for t in tokenize(pl) if t[0] == 'o']
    if len(t_en) == 1 and len(t_pl) == 1 and (t_en[0][1], t_en[0][2]) != (t_pl[0][1], t_pl[0][2]):
        n0, a0 = t_pl[0][1], t_pl[0][2]
        n1, a1 = t_en[0][1], t_en[0][2]
        op0 = f'<{n0} {a0}>' if a0 else f'<{n0}>'
        op1 = f'<{n1} {a1}>' if a1 else f'<{n1}>'
        pl = pl.replace(op0, op1, 1).replace(f'</{n0}>', f'</{n1}>', 1)
    return pl


_OFF = set(os.environ.get('QA_OFF', '').split(','))   # diagnostyka: wyłączanie reguł typografii
NOHYPH = {'formed', 'carter'}


_PL_ASCII = None


def _pl_ascii_words():
    """polskie wyrazy zapisane samymi literami ASCII (np. „inicjatywa”, „Rzymianie”), występujące w przekładach POZA nawiasami –
    wyrazy takie w nawiasie dzielimy po polsku, a nie wzorcami angielskimi"""
    global _PL_ASCII
    if _PL_ASCII is None:
        words = set()
        base = os.path.join(ROOT, 'trans')
        try:
            for d in os.listdir(base):
                dp = os.path.join(base, d)
                if not os.path.isdir(dp):
                    continue
                for fn in os.listdir(dp):
                    if not fn.endswith('.json'):
                        continue
                    try:
                        raw = open(os.path.join(dp, fn), encoding='utf-8').read()
                    except OSError:
                        continue
                    raw = re.sub(r'<[^<>]*>', '', raw)
                    depth = 0
                    buf = []
                    for ch in raw:
                        if ch == '(':
                            depth += 1
                        elif ch == ')':
                            depth = max(0, depth - 1)
                        elif depth == 0:
                            buf.append(ch)
                            continue
                        buf.append(' ')
                    for w in re.findall(r'[A-Za-z]{6,}', ''.join(buf)):
                        words.add(w.lower())
        except OSError:
            pass
        _PL_ASCII = words
    return _PL_ASCII


_PL_FUNC = {'i', 'w', 'z', 'na', 'do', 'od', 'po', 'za', 'ze', 'we', 'lub', 'oraz', 'albo', 'zob', 'np', 'tzw', 'tj', 'czyli',
            'jest', 'nie', 'się', 'dla', 'przy', 'pod', 'nad', 'bez', 'jak', 'oraz', 'jeśli', 'gdy', 'tylko', 'też', 'także',
            'ale', 'lecz', 'który', 'która', 'które', 'kolumna', 'heks', 'heksy', 'oddział', 'oddziały'}


def _paren_is_polish(s, a, b):
    """czy nawias okrągły, w którym stoi wyraz s[a:b], jest polskim wtrąceniem (a nie angielską glosą terminu):
    polskie litery diakrytyczne albo polskie wyrazy funkcyjne w obrębie tego nawiasu (poprawka 30.10.2026 –
    np. „(inicjatywa 6)”, „(Rzymianie)”, „(ilustracje poniżej)” dzielone dotąd wzorcami angielskimi)"""
    lo = s.rfind('(', 0, a)
    hi = s.find(')', b)
    seg = s[lo + 1:hi if hi >= 0 else len(s)]
    seg = re.sub(r'<[^<>]*>', ' ', seg)
    if re.search('[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', seg):
        return True
    words = set(re.findall(r'[a-ząćęłńóśźż]+', seg.lower()))
    return bool(words & _PL_FUNC)


def _hyph_sub(s):
    """dzielenie wyrazów: angielskie słowa (ASCII) w nawiasach okrągłych dzielimy wg wzorców angielskich (chyba że to polski wyraz
    ASCII znany z tekstu poza nawiasami); wyrazy z NOHYPH – wcale; wyrazy z ręcznym miękkim łącznikiem (U+00AD) zostawiamy bez zmian"""
    def f(m):
        w = m.group(0)
        if '\u00ad' in w:
            return w                           # ręczny podział ma pierwszeństwo i blokuje automat w całym wyrazie
        pre = s[:m.start()]
        if 'paren' not in _OFF and pre.count('(') > pre.count(')') and w.isascii():
            if w.lower() in _pl_ascii_words() or _paren_is_polish(s, m.start(), m.end()):
                return hyph_word(w)
            return hyph_en(w)                  # angielskie słowa w nawiasach: wzorce angielskie, nie polskie
        if w.lower() in NOHYPH:
            return w
        return hyph_word(w)
    return re.sub(rf'[{PL_LETTERS}\u00ad]+', f, s)


def polish_typo(text, hyph=False):
    """twarde spacje po jednoliterowych spójnikach/przyimkach, po liczbach i przed półpauzą, niełamliwe
    zakresy liczb; miękkie łączniki (akapity justowane)"""
    tags = []

    def prot(m):
        tags.append(m.group(0))
        return _PROT
    s = re.sub(r'<[^<>]*>', prot, text)
    s = re.sub(rf'(?<![{PL_LETTERS}0-9\u00ad])([aiouwzAIOUWZ]) (?=\S)', '\\1\u00a0', s)
    if 'num' not in _OFF:
        s = re.sub(rf'(\d) (?=[{PL_LETTERS}])', '\\1\u00a0', s)           # 75 jardów, 3 heksy
    if 'caps' not in _OFF:
        s = re.sub(r'(?<![A-Za-z])([A-Z]{2,}) (?=\d)', '\\1\u00a0', s)      # DEFCON 3, SA 4.0
    s = re.sub(r'(?<![A-Za-z])(CC) (?=BY)', '\\1\u00a0', s)
    if 'dot' not in _OFF:
        s = re.sub(rf'(?<=[{PL_LETTERS}0-9]) (\d{{1,2}}\.)(?= [a-ząćęłńóśźż])', '\u00a0\\1', s)   # zasad 4. wydania
    s = re.sub(rf'(?<![{PL_LETTERS}])([IVX]{{1,4}}) (?=[a-ząćęłńóśźż])', '\\1\u00a0', s)      # II wojny
    s = re.sub(rf'(?<=[A-ZŁŚŻŹĆ][a-ząćęłńóśźż]) (?=[IVX]{{2,4}}(?![{PL_LETTERS}]))', '\u00a0', s)  # Paweł II
    s = re.sub(r'\bJan Paweł\b', 'Jan\u00a0Paweł', s)
    if 'dash' not in _OFF:
        s = re.sub(r'(?<=\S) ([–—]) ', '\u00a0\\1 ', s)                       # półpauza nie zaczyna wiersza
    if hyph:
        s = _hyph_sub(s)
    it = iter(tags)
    return re.sub(_PROT, lambda m: next(it), s)


def tags_to_html(s):
    """znaczniki składu -> HTML (tekst poza znacznikami jest escapowany)"""
    out = []
    stack = []
    for tok in tokenize(s):
        k = tok[0]
        if k == 't':
            out.append(htmlmod.escape(htmlmod.unescape(tok[1]), quote=False))
        elif k == 'br':
            out.append('<br>')
        elif k == 'o':
            name, arg = tok[1], tok[2]
            if name in ('b', 'i'):
                out.append(f'<{name}>')
            elif name == 'sc':
                out.append('<span class="sc">')
            elif name == 'u':
                out.append('<span class="ul">')
            elif name in ('sup', 'sub'):
                out.append(f'<span class="{name}">')
            elif name == 'c':
                col = arg if re.fullmatch(r'#[0-9a-fA-F]{6}', arg) else '#000000'
                out.append(f'<span style="color:{col}">')
            elif name == 'f':
                out.append(f'<span style="{fontcss(arg)}">')
            elif name == 'hl':
                col = arg if re.fullmatch(r'#[0-9a-fA-F]{6}', arg or '') else '#cfe8f6'
                out.append(f'<span class="hl" style="background-color:{col}">')
            stack.append(name)
        elif k == 'c':
            name = tok[1]
            if name not in stack:
                continue
            while stack:
                n = stack.pop()
                out.append(f'</{n}>' if n in ('b', 'i') else '</span>')
                if n == name:
                    break
    while stack:
        n = stack.pop()
        out.append(f'</{n}>' if n in ('b', 'i') else '</span>')
    return ''.join(out)


LEADER = re.compile(r'^(.*?)\s*(?:\.\s*){4,}(\S{1,8})\s*$')


_MARK = (r'(?:[•●▪■◦‣∙·]|\(?[A-Za-z]\)|\(?[0-9]{1,2}\)|[A-Za-z][.)]|[0-9]{1,2}[.)])')
_BUL_HTML = re.compile(rf'^((?:<(?:b|i|span)[^>]*>)*)({_MARK})((?:</(?:b|i|span)>)*)(?:\s|&nbsp;|\u00a0)+')


def bullet_box(html_s, hang):
    """punkt listy: znacznik i odstęp w polu o stałej szerokości = wcięcie wiszące (tekst pierwszego wiersza
    zaczyna się dokładnie tam, gdzie wiersze dalsze; odstęp po znaczniku nie rozciąga się przy justowaniu)"""
    m = _BUL_HTML.match(html_s)
    if not m or hang < 1.0:
        return html_s
    if len(re.findall(r'<(?:b|i|span)\b', m.group(1))) != len(re.findall(r'</(?:b|i|span)>', m.group(3))):
        return html_s
    box = (f'<span class="bsp" style="min-width:{hang:.2f}pt">{m.group(1)}{m.group(2)}{m.group(3)}</span>')
    return box + html_s[m.end():]


_NB = re.compile(r'(?<![\w.,])((?:[A-Za-z]{0,4}\d+(?:[.,]\d+)?|[A-Z]{2,6})[–-][A-Za-z]{0,4}\d+(?:[.,]\d+)?%?|BY-SA)(?![\w])')


def nb_ranges(html_s):
    """zakresy liczb (104–110, 20–40%) i „BY-SA” w jednym kawałku – bez łamania wiersza w środku"""
    parts = re.split(r'(<[^>]*>)', html_s)
    return ''.join(x if x.startswith('<') else _NB.sub(r'<span class="nb">\1</span>', x) for x in parts)


def para_inner(text, align, hang=0):
    """HTML akapitu ze znacznikami bazowej linii (bm/em) i obsługą kropek wiodących (spis treści)"""
    m = LEADER.match(text)
    if m and '<' not in m.group(2):
        t = tags_to_html(polish_typo(m.group(1)))
        return (f'<span class="lt"><i class="bm"></i>{t}</span><span class="ld"></span>'
                f'<span class="ln_">{tags_to_html(m.group(2))}<i class="em"></i></span>'), True
    t = tags_to_html(polish_typo(text, hyph=(align == 'justify')))
    t = nb_ranges(t)
    if hang and 'bul' not in _OFF:
        t = bullet_box(t, hang)
    return f'<i class="bm"></i>{t}<i class="em"></i>', False


# ====================================================================== dane stron
def load_trans(doc, p):
    return load_json(trans_path(doc, p)) or {}


def carry_text(doc, p):
    c = load_json(carry_path(doc, p))
    if isinstance(c, dict):
        return c.get('text', '')
    if isinstance(c, str):
        return c
    return None


def unit_texts(doc, p, u, tr, warn):
    """lista tekstów (akapitów albo wierszy) do złożenia; None = jednostka pominięta"""
    entry = tr.get(u['id'])
    kind = u['kind']
    items = u['paras'] if kind == 'flow' else u['lines']
    if entry is None:
        if u.get('role') not in AUTO_KEEP_ROLES:
            warn.append(f"{u['id']}: brak w trans – złożono oryginał")
        entry = 'keep'
    if entry == 'skip':
        return None
    if entry == 'keep':
        texts = [it['en'] for it in items]
        if kind == 'flow' and len(texts) == 1:
            h = header_text(texts[0])
            if h is not None:
                texts = [h]
        return texts
    if isinstance(entry, dict):
        key = 'paras' if kind == 'flow' else 'lines'
        texts = entry.get(key)
        if not isinstance(texts, list):
            warn.append(f"{u['id']}: brak pola {key} – złożono oryginał")
            return [it['en'] for it in items]
        texts = list(texts) + [''] * (len(items) - len(texts))
        texts = texts[:len(items)]
        out = []
        for t in texts:
            t = t if isinstance(t, str) else ''
            if '@@CARRY@@' in t:
                ct = carry_text(doc, p)
                if ct is None:
                    warn.append(f"{u['id']}: brak pliku carry dla @@CARRY@@")
                    ct = ''
                t = t.replace('@@CARRY@@', ct)
            out.append(t)
        return out
    warn.append(f"{u['id']}: nieznana wartość w trans – złożono oryginał")
    return [it['en'] for it in items]


# ====================================================================== HTML
CSS = r"""
@page{size:%(W).3fpt %(H).3fpt;margin:0}
html,body{margin:0;padding:0;background:transparent}
html{width:%(W).3fpt;height:%(H).3fpt;overflow:hidden}
body{width:%(W).3fpt;height:%(H).3fpt;position:relative;overflow:hidden}
.u{position:absolute;box-sizing:border-box;margin:0;padding:0}
.p{margin:0;padding:0;box-sizing:border-box;hyphens:manual;-webkit-hyphens:manual;overflow-wrap:normal;
   word-break:normal;font-kerning:normal;text-rendering:geometricPrecision;font-synthesis:weight style small-caps}
.nw .p{white-space:nowrap}
.bsp{display:inline-block;white-space:nowrap;text-indent:0}
.nb{white-space:nowrap}
.bm,.em{display:inline-block;width:0;height:0;vertical-align:baseline;font-style:normal}
b{font-weight:700} i{font-style:italic}
.sc{font-variant:small-caps}
.ul{text-decoration:underline;text-decoration-thickness:0.06em;text-underline-offset:0.12em}
.sup{font-size:0.68em;vertical-align:0.38em;line-height:0}
.sub{font-size:0.68em;vertical-align:-0.18em;line-height:0}
.hl{box-decoration-break:clone;-webkit-box-decoration-break:clone;padding:0.07em 0}
.cf{height:0;margin:0;padding:0}
.ldr{display:flex;align-items:baseline;white-space:nowrap}
.ldr .lt{flex:0 1 auto;overflow:hidden;text-overflow:clip}
.ldr .ld{flex:1 1 0;overflow:hidden;white-space:nowrap;margin:0 0.15em}
.ldr .ld::before{content:". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."}
.ldr .ln_{flex:none}
.lu{position:absolute;left:0;top:0;width:0;height:0}
.l{position:absolute;white-space:nowrap;margin:0;padding:0;line-height:1.15}
.rot{position:absolute;width:0;height:0;transform-origin:0 0}
"""


def ls_em(item):
    """dodatkowy letter-spacing (em): rozstrzelenie z oryginału (ls) + zwężenie hs<1"""
    v = float(item.get('ls', 0) or 0)
    hs = item.get('hs')
    if hs and hs < 0.985:
        v += (hs - 1.0) * 0.5
    return v


def build_html(doc, p, lay, tr, warn):
    W, H = lay['width'], lay['height']
    body_font = (lay.get('body') or {}).get('font')
    parts = []
    meta = []
    for u in lay.get('units', []):
        texts = unit_texts(doc, p, u, tr, warn)
        if texts is None:
            continue
        if u['kind'] == 'flow':
            ps = []
            prev_last = None
            paras_html = []
            for para, t in zip(u['paras'], texts):
                if not t or not t.strip():
                    continue
                gap = None if prev_last is None else round(para['base'] - prev_last, 3)
                prev_last = para['lastbase']
                if para.get('hl') and not LEADER.match(t):
                    t = f"<hl {para['hl']}>{t}</hl>"       # akapit podświetlony w całości
                inner, is_ldr = para_inner(t, para.get('align', 'left'), para.get('hang', 0) or 0)
                al = para.get('align', 'left')
                hang = para.get('hang', 0) or 0
                indent = para.get('indent', 0) or 0
                pad_l = (para.get('left', 0) or 0) + hang
                ti = indent - hang
                pad_r = max(0.0, para.get('right', 0) or 0)
                css = (f"padding-left:{pad_l:.2f}pt;padding-right:{pad_r:.2f}pt;text-indent:{ti:.2f}pt;"
                       f"text-align:{al};font-size:calc({para['size']}pt * var(--s,1));"
                       f"line-height:calc({para['pitch']}pt * var(--s,1));color:{para.get('color', '#000000')};"
                       + fontcss(para['font'], ls_em(para)))
                if para.get('ws'):
                    css += f"word-spacing:{para['ws']}em;"
                if al == 'justify' and para.get('lastjust'):
                    css += 'text-align-last:justify;'
                cls = 'p ldr' if is_ldr else 'p'
                paras_html.append(f'<div class="{cls}" style="{css}">{inner}</div>')
                ps.append({'gap': gap, 'size': para['size'], 'base': para['base']})
            if not ps:
                continue
            nowrap = bool(u.get('nowrap'))
            group = 'body' if u.get('body') else 'own'
            cls = 'u fl nw' if nowrap else 'u fl'
            m = {'id': u['id'], 'kind': 'flow', 'group': group, 'x0': u['x0'], 'x1': u['x1'],
                 'base': ps[0]['base'], 'maxBottom': u.get('maxBottom', u['bottom']),
                 'maxRight': max(u.get('maxRight', u['x1']), u['x1']),
                 'maxLeft': min(u.get('maxLeft', u['x0']), u['x0']), 'nowrap': nowrap,
                 'align': u['paras'][0].get('align', 'left'), 'paras': ps,
                 'cuts': [] if nowrap else [c for para in u['paras'] for c in para.get('cuts', [])]}
            if u.get('fixscale'):
                m['fixscale'] = float(u['fixscale'])
            meta.append(m)
            parts.append(f'<div class="{cls}" id="{u["id"]}">' + ''.join(paras_html) + '</div>')
        else:
            lhtml = []
            lmeta = []
            for i, (ln, t) in enumerate(zip(u['lines'], texts)):
                if not t or (not t.strip() and '\u00a0' not in t):
                    continue
                css = (f"font-size:{ln['size']}pt;color:{ln.get('color', '#000000')};"
                       + fontcss(ln['font'], ls_em(ln)))
                if ln.get('hl'):
                    t = f"<hl {ln['hl']}>{t}</hl>"
                inner = f'<i class="bm"></i>{tags_to_html(polish_typo(t))}'
                rot = ln.get('rot', 0) or 0
                if rot:
                    lhtml.append(f'<div class="rot" id="{u["id"]}_r{i}" style="left:{ln["ox"]}pt;top:{ln["oy"]}pt;'
                                 f'transform:rotate({-rot}deg)"><div class="l" id="{u["id"]}_{i}" style="{css}">'
                                 f'{inner}</div></div>')
                else:
                    lhtml.append(f'<div class="l" id="{u["id"]}_{i}" style="{css}">{inner}</div>')
                lmeta.append({'i': i, 'size': ln['size'], 'x0': ln['x0'], 'x1': ln['x1'], 'base': ln['base'],
                              'align': ln.get('align', 'left'), 'maxLeft': min(ln.get('maxLeft', ln['x0']), ln['x0']),
                              'maxRight': max(ln.get('maxRight', ln['x1']), ln['x1']), 'rot': rot,
                              'len': ln.get('len', ln['x1'] - ln['x0'])})
            if not lmeta:
                continue
            meta.append({'id': u['id'], 'kind': 'lines', 'lines': lmeta, 'same': bool(u.get('same_scale')),
                         'fixscale': u.get('fixscale')})
            parts.append(f'<div class="lu" id="{u["id"]}">' + ''.join(lhtml) + '</div>')
    css = CSS % {'W': W, 'H': H}
    doc_html = (f'<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><style>{font_face_css()}\n{css}</style>'
                f'</head><body>\n' + '\n'.join(parts) +
                f'\n<script>window.__META__={json.dumps(meta, ensure_ascii=False)};window.__MIN__={MIN_SCALE};'
                f'window.__OK__={MIN_OK};</script>\n<script>{FIT_JS}</script></body></html>')
    return doc_html, meta


# ====================================================================== dopasowanie (JS)
FIT_JS = r"""
const PX = 4/3;                       // 1 pt = 4/3 px CSS
function bmY(el){ return el.getBoundingClientRect().bottom; }
function layoutFlow(m, s){
  const el = document.getElementById(m.id);
  el.style.setProperty('--s', s);
  for (const f of el.querySelectorAll(':scope > .cf')) f.remove();
  const ps = [...el.querySelectorAll(':scope > .p')];
  // pudełko
  let left = m.x0, width = m.x1 - m.x0;
  if (m.nowrap){
    if (m.align === 'center'){
      const e = Math.max(0, Math.min(m.x0 - m.maxLeft, m.maxRight - m.x1));
      left = m.x0 - e; width = (m.x1 - m.x0) + 2*e;
    } else if (m.align === 'right'){
      left = m.maxLeft; width = m.x1 - m.maxLeft;
    } else { width = m.maxRight - m.x0; }
  }
  el.style.left = (left*PX)+'px'; el.style.width = (width*PX)+'px'; el.style.top = '0px';
  ps.forEach(p => p.style.marginTop = '0px');
  // pomiar położeń linii bazowych wewnątrz akapitów
  const info = ps.map(p => {
    const r = p.getBoundingClientRect();
    const b = p.querySelector('.bm'), e = p.querySelector('.em');
    const b1 = b ? bmY(b) - r.top : r.height*0.8;
    const bl = e ? r.bottom - bmY(e) : r.height*0.2;
    return {b1, bl};
  });
  for (let i = 1; i < ps.length; i++){
    const g = (m.paras[i].gap == null ? m.paras[i].size*1.2 : m.paras[i].gap) * s * PX;
    ps[i].style.marginTop = (g - info[i-1].bl - info[i].b1) + 'px';
  }
  const top = m.base*PX - info[0].b1;
  el.style.top = top + 'px';
  // obrazki opływane tekstem: floaty od początku jednostki, we współrzędnych strony; kolejność
  // według położenia (górna krawędź floatu nie może być wyżej niż floatu wcześniejszego w DOM)
  if (m.cuts && m.cuts.length){
    const cs = [...m.cuts].sort((a,b) => a.top - b.top);
    const sideY = {l: 0, r: 0}; let cur = 0; const frag = [];
    for (const c of cs){
      const t = c.top*PX - top, bt = c.bottom*PX - top;
      const y0 = Math.max(sideY[c.side], cur);
      const t1 = Math.max(t, y0);
      const h = bt - t1;
      if (h <= 0) continue;
      frag.push([c.side, t1 - y0, 0.01]); frag.push([c.side, h, c.w*PX]);
      sideY[c.side] = t1 + h; cur = t1;
    }
    const first = el.firstChild;
    for (const f of frag){
      const d = document.createElement('div'); d.className = 'cf';
      d.style.cssFloat = f[0] === 'l' ? 'left' : 'right';
      d.style.clear = f[0] === 'l' ? 'left' : 'right';
      d.style.height = f[1]+'px'; d.style.width = f[2]+'px';
      el.insertBefore(d, first);
    }
  }
  // wynik
  const last = ps[ps.length-1];
  const e = last.querySelector('.em');
  const lastBase = e ? bmY(e) : last.getBoundingClientRect().bottom;
  const ink = lastBase + 0.22*m.paras[m.paras.length-1].size*s*PX;
  let overV = ink - m.maxBottom*PX;
  let overH = 0;
  if (m.nowrap){
    for (const p of ps){ overH = Math.max(overH, p.scrollWidth - p.clientWidth); }
  } else {
    for (const p of ps){ overH = Math.max(overH, p.scrollWidth - p.clientWidth - 0.5*PX); }
    overH = Math.max(0, overH - 2*PX);   // pojedyncze długie słowo – tolerancja
  }
  return {ok: overV <= 0.6*PX && overH <= 0.6*PX, overV: overV/PX, overH: overH/PX};
}
function layoutLine(m, l, s){
  const el = document.getElementById(m.id + '_' + l.i);
  el.style.fontSize = (l.size*s) + 'pt';
  el.style.left = '0px'; el.style.top = '0px';
  // pomiar w układzie elementu (offset*), niezależny od obrotu rodzica
  const w = el.scrollWidth;
  const b = el.querySelector('.bm');
  const off = b ? b.offsetTop + b.offsetHeight : el.offsetHeight*0.8;
  let avail;
  if (l.rot){
    el.style.left = '0px'; el.style.top = (-off)+'px';
    avail = l.len*1.08*PX;
  } else {
    let x;
    if (l.align === 'center'){
      const c = (l.x0 + l.x1)/2;
      avail = 2*Math.min(c - l.maxLeft, l.maxRight - c)*PX; x = c*PX - w/2;
    } else if (l.align === 'right'){
      avail = (l.x1 - l.maxLeft)*PX; x = l.x1*PX - w;
    } else {
      avail = (l.maxRight - l.x0)*PX; x = l.x0*PX;
    }
    el.style.left = x + 'px'; el.style.top = (l.base*PX - off) + 'px';
  }
  return {ok: w <= avail + 0.6*PX, over: (w - avail)/PX, w: w};
}
function fitLines(m){
  const res = {}; let mn = 1, over = 0;
  const scales = m.lines.map(l => {
    if (m.fixscale){ layoutLine(m, l, m.fixscale); return m.fixscale; }
    let r = layoutLine(m, l, 1);
    if (r.ok) return 1;
    let lo = window.__MIN__, hi = 1;
    if (!layoutLine(m, l, lo).ok){ return lo; }
    for (let k = 0; k < 9; k++){ const mid = (lo+hi)/2; if (layoutLine(m, l, mid).ok) lo = mid; else hi = mid; }
    return lo;
  });
  let common = Math.min(...scales);
  m.lines.forEach((l, k) => {
    const s = m.same ? common : scales[k];
    if (s < window.__OK__){ const r = layoutLine(m, l, window.__OK__); over = Math.max(over, r.over); }
    layoutLine(m, l, s); mn = Math.min(mn, s);
  });
  return {scale: mn, over: Math.max(0, over)};
}
function search(test){
  if (test(1).ok) return 1;
  let lo = window.__MIN__, hi = 1;
  if (!test(lo).ok) return lo;
  for (let k = 0; k < 10; k++){ const mid = (lo+hi)/2; if (test(mid).ok) lo = mid; else hi = mid; }
  return Math.floor(lo*1000)/1000;
}
function fitPage(){
  const M = window.__META__; const out = {units:{}, page_scale:1};
  const body = M.filter(m => m.kind === 'flow' && m.group === 'body' && !m.fixscale);
  const own = M.filter(m => m.kind === 'flow' && (m.group !== 'body' || m.fixscale));
  const allFit = s => { let ok = true; for (const m of body){ if (!layoutFlow(m, s).ok) ok = false; } return {ok}; };
  let ps = 1;
  if (body.length){ ps = search(allFit); allFit(ps); }
  out.page_scale = ps;
  const record = (m, s) => {
    let over = 0;
    const r = layoutFlow(m, s);
    if (!r.ok || s < window.__OK__){
      const r2 = layoutFlow(m, Math.max(s, window.__OK__));
      over = Math.max(0, r2.overV, r2.overH);
      layoutFlow(m, s);
    }
    out.units[m.id] = {scale: s, over: Math.round(over*10)/10};
  };
  // skala strony: każda jednostka tekstu głównego potrzebuje własnej skali tylko do raportu
  for (const m of body){
    const own_s = search(s => layoutFlow(m, s));
    out.units[m.id] = {scale: Math.min(ps, own_s), need: own_s, over: 0};
  }
  allFit(ps);
  for (const m of body){
    const u = out.units[m.id];
    if (u.need < window.__OK__){
      const r2 = layoutFlow(m, window.__OK__); u.over = Math.round(Math.max(0, r2.overV, r2.overH)*10)/10;
    }
    layoutFlow(m, ps); u.scale = ps;
  }
  for (const m of own){
    const s = m.fixscale ? m.fixscale : search(t => layoutFlow(m, t));
    record(m, s);
  }
  for (const m of M.filter(m => m.kind === 'lines')){
    out.units[m.id] = fitLines(m);
  }
  return out;
}
"""


# ====================================================================== render
def chromium():
    os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
    from playwright.sync_api import sync_playwright
    return sync_playwright()


def render_pages(doc, pages, keep_html=False, quiet=False):
    """renderuje strony; zwraca (pdf_bytes per strona, wyniki dopasowania, ostrzeżenia, czas)"""
    import pikepdf  # noqa: F401
    htmldir = f'{ROOT}/html/{doc}'
    os.makedirs(htmldir, exist_ok=True)
    pdfs, results, warns = {}, {}, {}
    t0 = time.time()
    with chromium() as pw:
        browser = pw.chromium.launch()
        ctx = browser.new_context()
        page = ctx.new_page()
        for p in pages:
            lay = load_json(layout_path(doc, p))
            if lay is None:
                warns[p] = ['brak pliku layout (uruchom unitize.py)']
                continue
            if not lay.get('units'):
                results[p] = {'units': {}, 'page_scale': 1}
                continue
            tr = load_trans(doc, p)
            warn = []
            doc_html, meta = build_html(doc, p, lay, tr, warn)
            hp = f'{htmldir}/p{p:03d}.html'
            with open(hp, 'w', encoding='utf-8') as fh:
                fh.write(doc_html)
            page.goto('file://' + hp)
            page.evaluate('document.fonts.ready.then(() => true)')
            res = page.evaluate('fitPage()')
            W, H = lay['width'], lay['height']
            pdfs[p] = page.pdf(width=f'{W / 72:.5f}in', height=f'{H / 72:.5f}in', print_background=True,
                               margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
                               prefer_css_page_size=True)
            results[p] = res
            warns[p] = warn
            if not keep_html:
                os.remove(hp)
        browser.close()
    return pdfs, results, warns, time.time() - t0


_INVIS_SPAN = re.compile(rb'/Span\s*<<\s*/ActualText\s*<FEFF(?:00AD|2060)>\s*>>\s*BDC(.*?)EMC\s*', re.S)
_SHOW_OP = re.compile(rb'(?:<[0-9A-Fa-f]*>|\[[^\]]*\]|\([^)]*\))\s*(?:Tj|TJ)\s*')


def strip_invisible_spans(data):
    """Chromium zapisuje miękki łącznik (U+00AD) i WJ (U+2060) jako zerowy glif w bloku ActualText.
    Usuwamy sam glif, zostawiając operatory ustawiania pozycji (Td/Tm) – wygląd strony bez zmian,
    a w warstwie tekstowej nie zostają niewidoczne znaki (wyszukiwanie i kopiowanie działają na całych wyrazach)."""
    def sub(m):
        inner = _SHOW_OP.sub(b'', m.group(1))
        return inner.strip() + b'\n'
    return _INVIS_SPAN.sub(sub, data)


def overlay_into(target_pdf, target_index, pdf_bytes):
    import pikepdf
    ov = pikepdf.open(io.BytesIO(pdf_bytes))
    if not len(ov.pages):
        return
    if not os.environ.get('KEEP_SHY'):
        pg0 = ov.pages[0]
        conts = pg0.obj.get('/Contents')
        streams = list(conts) if isinstance(conts, pikepdf.Array) else [conts]
        raw = b'\n'.join(st.read_bytes() for st in streams)
        pg0.obj['/Contents'] = ov.make_stream(strip_invisible_spans(raw))
    pg = target_pdf.pages[target_index]
    form = target_pdf.copy_foreign(ov.pages[0].as_form_xobject())
    mb = [float(v) for v in pg.mediabox]
    pg.add_overlay(form, pikepdf.Rectangle(*mb))


def compose_subset(doc, pages, pdfs, out_path):
    """PDF tylko z renderowanymi stronami (tło + tekst)"""
    import pikepdf
    bg = pikepdf.open(f'{ROOT}/bg/{doc}.pdf')
    keep = [p for p in pages if 1 <= p <= len(bg.pages)]
    out = pikepdf.new()
    for p in keep:
        out.pages.append(bg.pages[p - 1])
    for k, p in enumerate(keep):
        if p in pdfs:
            overlay_into(out, k, pdfs[p])
    out.save(out_path)
    return keep


def compose_base(doc, pages, pdfs, out_path):
    """base_DOK.pdf: aktualizacja istniejącego pliku albo nowy z tła"""
    import pikepdf
    bg = pikepdf.open(f'{ROOT}/bg/{doc}.pdf')
    n = len(bg.pages)
    full = set(pages) >= set(range(1, n + 1))
    if os.path.exists(out_path) and not full:
        base = pikepdf.open(out_path)
        if len(base.pages) != n:
            base = pikepdf.open(f'{ROOT}/bg/{doc}.pdf')
        else:
            for p in pages:
                base.pages[p - 1] = bg.pages[p - 1]     # świeża strona tła
    else:
        base = pikepdf.open(f'{ROOT}/bg/{doc}.pdf')
    for p in pages:
        if p in pdfs:
            overlay_into(base, p - 1, pdfs[p])
    tmp = out_path + '.tmp'
    base.save(tmp)
    base.close()
    os.replace(tmp, out_path)


def update_fit(doc, results, warns):
    import fcntl
    os.makedirs(FINAL, exist_ok=True)
    with open(f'{FINAL}/.fit_{doc}.lock', 'w') as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        return _update_fit(doc, results, warns)


def _update_fit(doc, results, warns):
    path = f'{FINAL}/fit_{doc}.json'
    data = load_json(path, {}) or {}
    for p, r in results.items():
        units = r.get('units', {})
        chk = sorted([k for k, v in units.items() if v.get('scale', 1) < MIN_OK - 1e-6 or v.get('over', 0) > 0.5
                      and v.get('scale', 1) <= MIN_SCALE + 1e-6], key=lambda x: int(x[1:]))
        data[f'p{p:03d}'] = {'page_scale': r.get('page_scale', 1),
                             'units': {k: {kk: (round(vv, 3) if isinstance(vv, float) else vv)
                                           for kk, vv in v.items()} for k, v in units.items()},
                             'check': chk, 'warn': warns.get(p, [])}
    os.makedirs(FINAL, exist_ok=True)
    save_json(path, dict(sorted(data.items())))
    return data


def page_report(p, r, warn):
    units = r.get('units', {})
    bad = [(k, v) for k, v in units.items() if v.get('scale', 1) < MIN_OK - 1e-6]
    bad.sort(key=lambda kv: int(kv[0][1:]))
    if not bad and not warn:
        return f's. {p}: OK'
    msg = []
    if bad:
        msg.append('do sprawdzenia: ' + ', '.join(f"{k} (skala {v['scale']:.2f}, nadmiar {v.get('over', 0):.1f} pt)"
                                                 for k, v in bad))
    if warn:
        msg.append('uwagi: ' + '; '.join(warn))
    return f's. {p}: ' + ' | '.join(msg)


def pngs(pdf_path, pages, outdir, dpi=100):
    os.makedirs(outdir, exist_ok=True)
    for k, p in enumerate(pages, 1):
        tmp = f'{outdir}/_t{p}'
        subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(k), '-l', str(k), '-png', '-singlefile', pdf_path, tmp],
                       check=True, capture_output=True)
        os.replace(tmp + '.png', f'{outdir}/p{p:03d}.png')


def run(doc, pages=None, png=False, tag=None, out=None, keep_html=False, quiet=False):
    n = page_count(doc)
    plist = parse_pages(pages, n) if pages else list(range(1, n + 1))
    pdfs, results, warns, dt = render_pages(doc, plist, keep_html=keep_html, quiet=quiet)
    update_fit(doc, results, warns)
    os.makedirs(FINAL, exist_ok=True)
    if png or out:
        tmpdir = tempfile.mkdtemp(prefix=f'render_{doc[:20]}_', dir=f'{ROOT}/html' if os.path.isdir(f'{ROOT}/html') else None)
        sub = out or f'{tmpdir}/sub.pdf'
        keep = compose_subset(doc, plist, pdfs, sub)
        if png:
            outdir = f'/tmp/fit_{doc}_{tag or "render"}'
            pngs(sub, keep, outdir)
        if not out:
            shutil.rmtree(tmpdir, ignore_errors=True)
    else:
        compose_base(doc, plist, pdfs, f'{FINAL}/base_{doc}.pdf')
    lines = [page_report(p, results[p], warns.get(p, [])) for p in plist if p in results]
    for p in plist:
        if p not in results and warns.get(p):
            lines.append(f's. {p}: ' + '; '.join(warns[p]))
    if not quiet:
        for l in lines:
            print(l)
        rendered = len(pdfs)
        print(f'czas: {dt:.1f} s ({dt / max(1, rendered):.2f} s/stronę)')
    return results, warns, lines


def main(argv):
    args = []
    opts = {'png': False, 'tag': None, 'out': None, 'keep_html': False, 'pages': None}
    it = iter(argv)
    for a in it:
        if a == '--png':
            opts['png'] = True
        elif a == '--tag':
            opts['tag'] = next(it)
        elif a == '--out':
            opts['out'] = next(it)
        elif a == '--pages':
            opts['pages'] = next(it)
        elif a == '--keep-html':
            opts['keep_html'] = True
        elif a in ('-h', '--help'):
            print(__doc__)
            return 1
        else:
            args.append(a)
    if not args:
        print(__doc__)
        return 1
    doc = args[0]
    pages = opts['pages'] or (args[1] if len(args) > 1 else None)
    run(doc, pages, png=opts['png'], tag=opts['tag'], out=opts['out'], keep_html=opts['keep_html'])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
