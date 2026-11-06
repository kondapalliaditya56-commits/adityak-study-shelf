# -*- coding: utf-8 -*-
"""Fidelity check for one subject chapter file: python3 check.py SUBJECT chapter_file.py
Prints per-chapter: words written vs source words, coverage of fact tokens (numbers, Articles, acronyms, case names), and the missing ones."""
import sys, os, re, html, importlib.util, glob
HERE = os.path.dirname(os.path.abspath(__file__)); HN = os.path.dirname(HERE)
sys.path.insert(0, HN); os.chdir(HN)
import hwlib, dsl
from dsl import *
SRC = '/tmp/claude-0/-home-claude/df387ce8-ff12-544e-98c5-89269dc3a785/scratchpad/found/src/'
def plain(h): return html.unescape(re.sub(r'<[^>]+>', ' ', h))
def norm(s): return re.sub(r'\s+', ' ', s.replace('​', '').replace('–', '-').replace('—', '-').replace('’', "'").replace('“', '"').replace('”', '"')).lower()
def facts(s):
    s = s.replace('**', '')
    out = set()
    for m in re.finditer(r'\b(?:Art(?:icle)?s?\.?|Sections?|Sec\.|Schedule)\s*\d+[A-Za-z]*(?:\(\w+\))*', s): out.add(norm(re.sub(r'(?i)^art(icle)?s?\.?\s*', 'art ', re.sub(r'(?i)^sec(tion)?s?\.?\s*', 'sec ', m.group(0)))))
    for m in re.finditer(r'(?<![\w.])\d[\d,]*(?:\.\d+)?(?:%|st|nd|rd|th)?(?![\w])', s):
        v = m.group(0).replace(',', '')
        if len(v) >= 2 or '%' in v: out.add(v)
    for m in re.finditer(r'\b[A-Z][A-Za-z]+ v\.? [A-Z][A-Za-z\.]+', s): out.add(norm(m.group(0)))
    for m in re.finditer(r'(?<![A-Za-z])[A-Z]{3,}(?![a-z])', s): out.add(m.group(0).lower())
    return out
def node_text(n):
    k = n[0]
    if k == 'tree': return n[1] + ' ' + ' '.join(node_text(x) if isinstance(x, tuple) else x for x in n[2])
    if k == 'sec': return n[1]
    if k in ('bx',): return n[2]
    if k == 'tb': return ' '.join(n[1]) + ' ' + ' '.join(' '.join(r) for r in n[2])
    if k == 'mn': return n[1] + ' ' + n[2]
    if k == 'fl': return (n[2] or '') + ' ' + ' '.join(n[1])
    if k == 'hub': return n[1] + ' ' + ' '.join(n[2]) + ' ' + (n[3] or '')
    if k == 'tl': return ' '.join(a + ' ' + b for a, b in n[1])
    if k == 'two': return ' '.join(node_text(x) for x in n[1] + n[2])
    if k == 'sw': return n[1]
    return ''
def main(subj, f):
    spec = importlib.util.spec_from_file_location('chk', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    ok = True
    for ch in m.CHS:
        for key in ('id', 'title', 'nodes', 'icon', 'simple', 'recall'):
            if key not in ch: print('FAIL chapter', ch.get('id'), 'missing key', key); ok = False
        # render must work
        try: hw = ''.join((dsl.r_hw(n) or '') for n in ch['nodes'] if n[0] != 'stl')
        except Exception as e: print('FAIL chapter', ch['id'], 'render error', repr(e)); ok = False; continue
        text = plain(' '.join(node_text(n) for n in ch['nodes']) + ' ' + ch.get('simple', '') + ' ' + ch.get('pyq', '') + ' ' + ' '.join(q + ' ' + a for q, a in ch.get('recall', [])))
        src = open(SRC + '%s/ch%02d.md' % (subj, ch['id'])).read()
        sw, tw = len(src.split()), len(text.split())
        fs = facts(src); ft = norm(text); ftok = facts(text)
        miss = sorted(x for x in fs if x not in ftok and x not in ft)
        cov = 100 * (1 - len(miss) / max(1, len(fs)))
        print('chapter %s: written %d words (%d%% of %d source words, about %.1f A4 pages) | fact tokens covered %.0f%% (%d of %d)' % (ch['id'], tw, 100 * tw // max(1, sw), sw, tw / 430.0, cov, len(fs) - len(miss), len(fs)))
        if miss: print('  missing:', ', '.join(miss[:70]))
    print('OK' if ok else 'ERRORS')
if __name__ == '__main__': main(sys.argv[1], sys.argv[2])
