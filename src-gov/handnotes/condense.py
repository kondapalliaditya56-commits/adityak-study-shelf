# -*- coding: utf-8 -*-
"""Middle-path condenser for the handwritten print notes only (shelf and book keep the full text).
Drops the least important whole clauses of over-long strings; never rewrites words."""
import re
FRAC = 0.62
SPLIT = re.compile(r'(; | · |(?<!incl)(?<!e\.g)(?<!i\.e)(?<!etc)(?<!vs)(?<!No)(?<!Sec)(?<!Art)(?<!Dr)(?<=[a-z0-9\)>\'])\. (?=[A-Z<(\'"0-9]))')
def _bal(s): return s.count('<b>') == s.count('</b>') and s.count('<i>') == s.count('</i>') and s.count('<span') == s.count('</span>')
def _clauses(s):
    parts = SPLIT.split(s); out = []; i = 0
    while i < len(parts):
        c = parts[i]; sep = parts[i+1] if i+1 < len(parts) else ''
        out.append([c, sep]); i += 2
    # merge to keep tags balanced
    m = []; buf = None
    for c, sep in out:
        if buf is None: buf = [c, sep]
        else: buf[0] += buf[1] + c; buf[1] = sep
        if _bal(buf[0]): m.append(buf); buf = None
    if buf: m.append(buf)
    return m
def _score(c, first):
    s = 0
    if first: s += 100
    if '<b>' in c: s += 3
    if re.search(r'\d', c): s += 3
    if re.search(r'\b(not|never|only|must|cannot|no)\b', c): s += 1
    if re.search(r'\b(e\.g\.|example|for instance)\b', c, re.I): s -= 2
    s -= len(c) / 120.0
    return s
def shorten(s, budget):
    if not isinstance(s, str) or len(re.sub(r'<[^>]+>', '', s)) <= budget * 1.15: return s
    if 'own mnemonic' in s or 'verify' in s.lower() or 'class="tag"' in s: return s
    cl = _clauses(s)
    full = len(re.sub(r'<[^>]+>', '', s)); budget = max(budget, FRAC * full)
    if len(cl) < 3: return s
    order = sorted(range(len(cl)), key=lambda i: -_score(cl[i][0], i == 0))
    keep = set(); used = 0
    for i in order:
        L = len(re.sub(r'<[^>]+>', '', cl[i][0]))
        if i == 0 or used + L <= budget: keep.add(i); used += L
    res = ''; last = None
    for i, (c, sep) in enumerate(cl):
        if i in keep:
            if res: res += last if last else '; '
            res += c; last = sep if sep.strip() else '; '
        else: last = sep if sep.strip() else '; '
    res = res.rstrip()
    L = lambda x: len(re.sub(r'<[^>]+>', '', x))
    if L(res) > budget * 1.3:   # stage 2: drop long parenthetical examples without numbers
        res2 = re.sub(r'\s*\((?:(?!\d)[^()<>]){30,}\)', '', res)
        if _bal(res2): res = res2
    return res
def condense(n, kb=150, bb=300, tcb=130):
    k = n[0]
    if k == 'tree':
        kids = [condense(x, kb, bb, tcb) if isinstance(x, tuple) else shorten(x, kb) for x in n[2]]
        return ('tree', n[1], kids, n[3], n[4])
    if k == 'bx':
        if n[1] in ('qt', 'ca'): return n
        return ('bx', n[1], shorten(n[2], bb))
    if k == 'tb':
        if n[1] and 'PYQ' in str(n[1][-1]): return n
        return ('tb', n[1], [[shorten(c, tcb) for c in r] for r in n[2]])
    if k == 'tl': return ('tl', [(a, shorten(b, tcb)) for a, b in n[1]])
    if k == 'two': return ('two', [condense(x, kb, bb, tcb) for x in n[1]], [condense(x, kb, bb, tcb) for x in n[2]])
    return n
