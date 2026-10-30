#!/usr/bin/env python3
"""select_fixes.py – buduje TSV poprawek z TSV walidatora wg decyzji.
Użycie: python3 select_fixes.py VAL.tsv OUT.tsv 'IDX[:gdzie][=nowa_poprawka]' ...
IDX – numer wiersza (1..n) w VAL.tsv; opcjonalnie :md|:json|:oba nadpisuje kolumnę gdzie; =tekst nadpisuje poprawkę.
"""
import csv, sys
val, out = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(val, encoding='utf-8'), delimiter='\t'))
tag = val.split('/')[-1][4:-4]
sel = []
for spec in sys.argv[3:]:
    new = None
    if '=' in spec:
        spec, new = spec.split('=', 1)
    where = None
    if ':' in spec:
        spec, where = spec.split(':', 1)
    r = dict(rows[int(spec) - 1])
    if where: r['gdzie'] = where
    if new is not None: r['poprawka_PL'] = new
    r['id'] = f'{tag}#{spec}'
    sel.append(r)
import os
exists = os.path.exists(out)
with open(out, 'a', encoding='utf-8') as fh:
    if not exists:
        fh.write('dok\tstrona\tcytat_PL\tpoprawka_PL\tgdzie\tid\tuwagi\n')
    for r in sel:
        fh.write('\t'.join([r['dok'], r['strona'], r['cytat_PL'], r['poprawka_PL'], r['gdzie'], r['id'], f"{r['kategoria']}/{r['waga']}"]) + '\n')
print(f'{len(sel)} poprawek -> {out}')
