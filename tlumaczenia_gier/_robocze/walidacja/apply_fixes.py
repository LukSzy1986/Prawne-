#!/usr/bin/env python3
"""apply_fixes.py – nanosi zaakceptowane poprawki (TSV) do md i trans JSON.

Użycie: python3 apply_fixes.py FIXES.tsv [--dry] [--log LOG.tsv]
Kolumny TSV (nagłówek): dok, strona, cytat_PL, poprawka_PL, gdzie (md|json|oba), [id], [uwagi]
- md:   /home/claude/tr/out/<dok>/pNNN.md – zamiana dokładnego fragmentu (musi wystąpić dokładnie raz,
        chyba że kolumna occ=all).
- json: /home/claude/lay/trans/<dok>/pNNN.json – zamiana w łańcuchach wartości jednostek (paras/lines);
        fragment musi wystąpić dokładnie raz w pliku (łącznie), chyba że occ=all.
Każda poprawka jest raportowana: OK / BRAK (fragment nie znaleziony) / WIELE (niejednoznaczny).
Przy --dry nic nie zapisuje.
"""
import csv, json, os, sys

TR = '/home/claude/tr/out'
TRANS = '/home/claude/lay/trans'


def count_in_json(obj, s):
    n = 0
    if isinstance(obj, str):
        return obj.count(s)
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.startswith('_'):
                continue
            n += count_in_json(v, s)
    elif isinstance(obj, list):
        for v in obj:
            n += count_in_json(v, s)
    return n


def replace_in_json(obj, old, new):
    if isinstance(obj, str):
        return obj.replace(old, new)
    if isinstance(obj, dict):
        return {k: (v if k.startswith('_') else replace_in_json(v, old, new)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [replace_in_json(v, old, new) for v in obj]
    return obj


def main():
    args = sys.argv[1:]
    dry = '--dry' in args
    log_path = None
    if '--log' in args:
        log_path = args[args.index('--log') + 1]
    tsv = [a for a in args if a.endswith('.tsv') and a != log_path][0]
    rows = list(csv.DictReader(open(tsv, encoding='utf-8'), delimiter='\t'))
    results = []
    md_cache, js_cache = {}, {}
    for r in rows:
        dok, page = r['dok'].strip(), int(r['strona'])
        old, new = r['cytat_PL'], r['poprawka_PL']
        where = r.get('gdzie', 'oba').strip() or 'oba'
        occ_all = (r.get('occ', '') or '').strip() == 'all'
        rid = r.get('id', '') or f'{dok[:4]}-{page}-{len(results)+1}'
        targets = ['md', 'json'] if where == 'oba' else [where]
        for t in targets:
            if t == 'md':
                path = f'{TR}/{dok}/p{page:03d}.md'
                if path not in md_cache:
                    md_cache[path] = open(path, encoding='utf-8').read()
                txt = md_cache[path]
                n = txt.count(old)
                if n == 0:
                    st = 'BRAK'
                elif n > 1 and not occ_all:
                    st = f'WIELE({n})'
                else:
                    md_cache[path] = txt.replace(old, new)
                    st = f'OK({n})'
            else:
                path = f'{TRANS}/{dok}/p{page:03d}.json'
                if path not in js_cache:
                    js_cache[path] = json.load(open(path, encoding='utf-8'))
                obj = js_cache[path]
                n = count_in_json(obj, old)
                if n == 0:
                    st = 'BRAK'
                elif n > 1 and not occ_all:
                    st = f'WIELE({n})'
                else:
                    js_cache[path] = replace_in_json(obj, old, new)
                    st = f'OK({n})'
            results.append((rid, dok, page, t, st, old, new))
            print(f'{st:9s} {dok[:8]} s.{page:2d} {t:4s} {rid}: {old[:60]!r} -> {new[:60]!r}')
    if not dry:
        for path, txt in md_cache.items():
            open(path, 'w', encoding='utf-8').write(txt)
        for path, obj in js_cache.items():
            json.dump(obj, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if log_path:
        new_file = not os.path.exists(log_path)
        with open(log_path, 'a', encoding='utf-8') as fh:
            if new_file:
                fh.write('id\tdok\tstrona\tgdzie\tstatus\tbyło\tjest\n')
            for rid, dok, page, t, st, old, new in results:
                fh.write(f'{rid}\t{dok}\t{page}\t{t}\t{st}\t{old}\t{new}\n')
    bad = [x for x in results if not x[4].startswith('OK')]
    print(f'--- {len(results)} operacji, nieudanych: {len(bad)}' + (' (DRY)' if dry else ''))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
