# -*- coding: utf-8 -*-
"""v6: pictures sit at the node they belong to; every handout point the revision map does not carry is added under 'More points' with its own pictures in place."""
import re, html as H, sys
sys.path.insert(0, '..')
import cover, detail as D
STATS = {}
CSS = (".pics{display:block!important}.pics:after{content:'';display:block;clear:both}.pic{display:inline-block!important;vertical-align:top;width:47%!important;max-width:47%!important;margin:0 1% 2mm 0}.pic.w,.pic.t{display:block!important;width:100%!important;max-width:100%!important}.pic.s{width:30%!important;max-width:30%!important}.xt{border-left:1.6mm solid #ef6c00;padding-left:2.4mm;margin:1.4mm 0 2mm;background:#fffaf2}.xt .xh{font-family:KB;font-size:9.8pt;color:#e65100;margin:.6mm 0}"
       ".xt .h4{font-family:KB;font-size:10.4pt;color:#1565c0;margin:1.4mm 0 .3mm;break-after:avoid}.xt .h4:before{content:'\\25B8  '}"
       ".xt ul{margin:.2mm 0 .6mm;padding-left:5mm}.xt li{margin:.3mm 0}.xt ul ul{list-style:circle}.xt ul ul ul{list-style:square}.xt p{margin:.5mm 0}"
       ".xt .red{color:#c62828}.xt .grn{color:#2e7d32}.xt mark{background:#fff176}.xt table{font-size:9.4pt}")
def _figs(frag_blocks):
    """-> [(caption, heading+label text, html, order)] from a topic's blocks"""
    out = []; hd = ''; lab = ''
    for kind, d, t, h in frag_blocks:
        if kind == 'h': hd = re.sub(r'^\d+\s*·\s*', '', t).rstrip(':# '); lab = ''
        elif kind in ('li', 'p'):
            l = t.strip().rstrip(': ')
            if kind == 'li' and 2 < len(l) < 48 and re.search(r'<b>', h) and not re.match(r'(Q\.|Answer|Ans|Explanation|Which|Select|Statement)', l): lab = l
        elif kind == 'fig':
            m = re.search(r'class="([^"]*)" style="--w:([\d.]+)px"><img[^>]*src="([^"]+)"', h)
            if not m: continue
            cls, w, src = m.group(1), float(m.group(2)), m.group(3)
            cap = hd.title() if hd.isupper() else hd
            if lab and lab.lower() not in cap.lower(): cap = (cap + ' · ' if cap else '') + lab
            k = 'pic t w' if 'tbl' in cls else ('pic w' if w > 345 else ('pic s' if w < 190 else 'pic'))
            out.append((cap, hd + ' ' + lab, '<div class="%s"><img src="%s"><div class="cp">%s</div></div>' % (k, src, H.escape(cap)), len(out), (w, src, H.escape(cap), 'tbl' in cls, hd)))
    return out
def _nodetext(nd):
    return ' '.join(re.sub(r'<[^>]+>', ' ', x) if isinstance(x, str) else ' '.join(re.sub(r'<[^>]+>', ' ', str(y)) for y in x) if isinstance(x, (list, tuple)) else str(x) for x in nd[1:])
def _ul(items):
    """items: [(depth, html)] -> nested ul"""
    out = []; cur = -1
    for d, h in items:
        d = min(d, cur + 1) if cur >= 0 else 0
        while cur < d: out.append('<ul>'); cur += 1
        while cur > d: out.append('</li></ul>'); cur -= 1
        out.append('</li>' if out and out[-1].startswith('<li') or (out and out[-1].endswith('</li>') is False and out[-1] not in ('<ul>',) and False) else '')
        out.append('<li>%s' % h)
    while cur >= 0: out.append('</li></ul>'); cur -= 1
    return ''.join(out).replace('</li></li>', '</li>')
def extras(blocks, have, placed):
    """-> (groups, miss): groups = [{'head': heading text, 'items': [(depth, html)], 'raw': [html tables]}] of everything the map does not carry"""
    miss = 0; own = []
    for i, (kind, d, t, h) in enumerate(blocks):
        if kind not in ('li', 'p', 'tbl'): own.append(False); continue
        has_kids = kind == 'li' and i + 1 < len(blocks) and blocks[i + 1][0] == 'li' and blocks[i + 1][1] > d
        unc = not cover.covered(t, have)
        own.append(unc and (not has_kids or len(cover.toks(t)) >= 4))
    emit = list(own)
    for i in range(len(blocks) - 1, -1, -1):
        kind, d = blocks[i][0], blocks[i][1]
        if kind == 'li':
            j = i + 1
            while j < len(blocks) and blocks[j][0] == 'li' and blocks[j][1] > d:
                if emit[j]: emit[i] = True
                j += 1
    # buckets keyed by (main heading, sub heading); main = h2/h3, sub = h4
    buckets = []; cur = None; main = ''; sub = None; key = None
    def clean_h(x):
        x = re.sub(r'^\d+\s*·\s*', '', D._txt(x)).strip(': #'); return x.title() if x.isupper() else x
    for i, (kind, d, t, h) in enumerate(blocks):
        if kind == 'h':
            if d <= 3: main = clean_h(h); sub = None
            else: sub = clean_h(h)
            continue
        if kind == 'fig' or not emit[i]: continue
        miss += 1
        if (main, sub) != key:
            key = (main, sub); cur = {'main': main, 'sub': sub, 'items': [], 'raw': []}; buckets.append(cur)
        if kind == 'li': cur['items'].append((d, re.sub(r'\s+', ' ', h).strip()))
        elif kind == 'p': cur['items'].append((0, re.sub(r'\s+', ' ', h).strip()))
        else: cur['raw'].append(h)
    return buckets, miss
def _flat(items):
    """[(depth, html)] -> flat arrow bullets (sub-points get a dash); never a nested side-box"""
    out = []
    for d, h in items:
        out.append(h if d == 0 else ('\u2013 ' if d == 1 else '\u00b7 ') + h)
    return out
def _trees(items, main):
    """top-level points of a main heading: a short label with sub-points -> one side-box; plain points -> plain arrow list"""
    res = []; plain = []; i = 0
    def fl():
        nonlocal plain
        if plain: res.append(('plain', plain)); plain = []
    while i < len(items):
        d, h = items[i]; j = i + 1
        while j < len(items) and items[j][0] > d: j += 1
        ch = items[i + 1:j]; lab = re.sub(r'<[^>]+>', '', h).strip()
        if ch and len(lab) <= 64:
            fl(); res.append(('tree', h.rstrip(': '), _flat([(dd - d - 1, hh) for dd, hh in ch])))
        else:
            plain.append(h); plain += _flat([(dd - d, hh) for dd, hh in ch])
        i = j
    fl(); return res
def _float(p):
    w, src, cap, tbl, hd = p
    mm = max(28.0, min(62.0, w * 0.2646 * 0.8))
    return '<div class="sw fp" style="float:right;width:%.0fmm"><img src="%s"><div class="cp">%s</div></div>' % (mm, src, cap)
import importlib, os
OPENERS = {}
sys.path.insert(0, os.path.join(D.ROOT, 'src-geo')); sys.path.insert(0, os.path.join(D.ROOT, 'src-gov', 'book'))
try:
    OPENERS[3] = importlib.import_module('chap.ch3')
except Exception as e: print('no opener', e)
def _b(t): return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', H.escape(t, quote=False))
OCSS = (".ob{border:2px solid #2e7d32;background:#f1f8e9;border-radius:3px;padding:1.2mm 2.8mm;margin:1.6mm 0;break-inside:avoid}.ob .oh{font-family:KB;color:#2e7d32;font-size:11pt;margin-bottom:.6mm}"
        ".ob.p{border-color:#6a1b9a;background:#f8f0fb}.ob.p .oh{color:#6a1b9a}.ob.b{border-color:#1565c0;background:#e8f1fb}.ob.b .oh{color:#1565c0}.ob.r{border-color:#c62828;background:#fdecea}.ob.r .oh{color:#c62828}"
        ".ob ul{margin:.3mm 0;padding-left:5mm}.ob li{margin:.4mm 0}.ob table{font-size:9.6pt}.two2{display:flex;gap:3mm}.two2>div{flex:1}"
        ".nums{display:flex;flex-wrap:wrap;gap:1.6mm}.nums span{border:1.6px solid #1565c0;border-radius:5px;padding:.4mm 2mm;background:#fff}.nums b{color:#c62828}.nums i{font-size:9pt;color:#555}")
def _opening(n):
    S = OPENERS[n]; import viz
    o = []
    o.append(('raw', '<div class="ob"><div class="oh">The chapter in 60 seconds</div><ul>%s</ul></div>' % ''.join('<li>%s</li>' % _b(x) for x in S.SIMPLE)))
    o.append(('raw', '<div class="ob b"><div class="oh">Words you need first</div><table><tr><th>Word</th><th>Meaning</th></tr>%s</table></div>' % ''.join('<tr><td><b>%s</b></td><td>%s</td></tr>' % (H.escape(a), H.escape(b)) for a, b in S.TERMS)))
    o.append(('raw', '<div class="ob p"><div class="oh">One line to carry</div>%s</div>' % H.escape(S.REMEMBER)))
    L = S.LENS
    o.append(('raw', '<div class="ob p"><div class="oh">What the exam asks</div><div class="two2"><div><b>Prelims hooks</b><ul>%s</ul></div><div><b>Mains hooks</b><ul>%s</ul></div></div><i>%s</i></div>' % (''.join('<li>%s</li>' % H.escape(x) for x in L['prelims']), ''.join('<li>%s</li>' % H.escape(x) for x in L['mains']), H.escape(L['close']))))
    o.append(('raw', '<div class="ob b"><div class="oh">Chapter map</div>%s</div>' % viz.render(S.VISUALS[0])))
    return o
def _closing(n):
    S = OPENERS[n]; o = [('sec', 'NUMBER CARD, TRAPS AND SELF-TEST', 'r')]
    o.append(('raw', '<div class="ob"><div class="oh">Number card</div><div class="nums">%s</div></div>' % ''.join('<span><b>%s</b> <i>%s</i></span>' % (H.escape(a), H.escape(b)) for a, b in S.NUMBERS)))
    o.append(('raw', ''.join('<div class="ob r"><div class="oh">%s: %s</div>%s <i>%s</i></div>' % (H.escape(t['k']), H.escape(t['t']), H.escape(t['d']), H.escape(t['r'])) for t in S.TRAPS)))
    o.append(('raw', '<div class="ob b"><div class="oh">Self-test (answers at the end of the box)</div>%s<p><b>Answers:</b> %s</p></div>' % (''.join('<p><b>Q%d.</b> %s<br>%s</p>' % (i + 1, H.escape(q['q']), ' &nbsp; '.join('(%s) %s' % ('abcd'[j], H.escape(x)) for j, x in enumerate(q['o']))) for i, q in enumerate(S.QUIZ)), ', '.join('Q%d %s' % (i + 1, 'abcd'[q['a']]) for i, q in enumerate(S.QUIZ)))))
    return o
def attach(chs, maps, und, GL={}, IGNORE=()):
    for ch in chs:
        n = ch['id']
        if n not in maps: continue
        if not D.WORDS: D._words(maps)
        m = D._main(n)
        heads = [(x.start(), x.group(2), D._txt(re.sub(r'<a class="anchor".*?</a>', '', x.group(3), flags=re.S))) for x in re.finditer(r'<(h2|h3|h4)[^>]*\sid="([^"]+)"[^>]*>(.*?)</\1>', m, re.S)]
        segs = {}; order = []; pyq_ids = []
        for k, (pos, i, ttl) in enumerate(heads):
            segs[i] = m[pos:heads[k + 1][0] if k + 1 < len(heads) else len(m)]; order.append(i)
            if D.ISPYQ.match(ttl): pyq_ids.append(i)
        body = [i for i in order if i not in ('exam-lens', 'recall', 'traps') and i not in pyq_ids]
        secs = [x for x in ch['nodes'] if x[0] == 'sec']
        mp = maps[n]; assert len(mp) == len(secs), ('map length', n, len(mp), len(secs))
        pts = []
        for k, a in enumerate(mp):
            if not a: continue
            sid, _, kw = a.partition('@'); off = 0
            if kw:
                off = segs[sid].find(kw); assert off > 0, ('keyword', n, a)
            pts.append((body.index(sid), off, k))
        assert pts == sorted(pts), ('map order', n)
        def cut(a, b):
            (i0, o0), (i1, o1) = a, b; s = ''
            for j in range(i0, min(i1, len(body) - 1) + 1):
                seg = segs[body[j]]; lo = o0 if j == i0 else 0; hi = o1 if j == i1 else len(seg)
                if j == i1 and o1 == 0: break
                s += seg[lo:hi]
            return s
        rng = {}
        for j, (bi, off, k) in enumerate(pts):
            nxt = (pts[j + 1][0], pts[j + 1][1]) if j + 1 < len(pts) else (len(body), 0)
            rng[k] = cut((bi, off), nxt)
        # split nodes into groups by sec
        groups = []; tail = []; cur = None; cur_pyq = False; k = -1
        for nd in ch['nodes']:
            if nd[0] == 'sec':
                k += 1; cur_pyq = bool(re.search(r'PYQ BANK|MISSED PYQ', re.sub(r'<[^>]+>', '', nd[1]), re.I))
                if cur_pyq: tail.append(('bx', 'bl', '<b>%s</b>' % re.sub(r'<[^>]+>', '', nd[1]))); cur = None; continue
                cur = {'k': k, 'sec': nd, 'nodes': []}; groups.append(cur)
            elif cur_pyq: tail.append(nd)
            elif nd[0] == 'bx' and D.PYQBX.match(nd[2]): tail.append(nd)
            elif cur is not None: cur['nodes'].append(nd)
            else: groups.append({'k': -1, 'sec': None, 'nodes': [nd]})
        out = []; st = dict(blocks=0, miss=0, figs=0, placed=0)
        for g in groups:
            if g['sec'] is None: out += g['nodes']; continue
            k = g['k']; out.append(g['sec'])
            if k in und.get(n, {}): out.append(('raw', '<div class="und"><b>Understand it first:</b> %s</div>' % und[n][k]))
            nodes = g['nodes']
            if k not in rng: out += nodes; continue
            bl = cover.blocks(rng[k])
            have = set(cover.stems(' '.join(_nodetext(x) for x in nodes))) | cover.stems(und.get(n, {}).get(k, ''))
            figs = _figs(bl); st['figs'] += len(figs)
            ntoks = [(cover.stems(_nodetext(x)) if x[0] not in ('sec', 'stl') else set()) for x in nodes]
            bks, miss = extras(bl, have, None)
            st['blocks'] += sum(1 for b_ in bl if b_[0] in ('li', 'p', 'tbl')); st['miss'] += miss
            xn = []; lastm = None  # ordered nodes: dict(kind, main, sub, ...)
            for bk in bks:
                if bk['main'] and bk['main'] != lastm:
                    xn.append({'k': 'mh', 'main': bk['main'], 'sub': None}); lastm = bk['main']
                if bk['sub']: xn.append({'k': 'tree', 'main': bk['main'], 'sub': bk['sub'], 'label': bk['sub'], 'kids': _flat(bk['items']), 'fl': []})
                else:
                    for kd in _trees(bk['items'], bk['main']):
                        if kd[0] == 'plain': xn.append({'k': 'plain', 'main': bk['main'], 'sub': None, 'kids': kd[1], 'fl': []})
                        else: xn.append({'k': 'tree', 'main': bk['main'], 'sub': None, 'label': kd[1], 'kids': kd[2], 'fl': []})
                for r in bk['raw']: xn.append({'k': 'raw', 'main': bk['main'], 'sub': None, 'html': r})
            floats = {}; blocks_after = {}; left = []
            def tk(x): return set(cover.toks(x or ''))
            for cap, ctx, html, i, meta in figs:
                w, src, capt, istbl, hd = meta
                small = (w <= 345 and not istbl)
                ct = set(cover.toks(ctx)); best = None; bs = 0
                for j, nt in enumerate(ntoks):
                    if not nt or not ct: continue
                    sc = len(ct & nt) / len(ct)
                    if sc > bs + 1e-9: bs, best = sc, j
                if best is not None and bs >= 0.4:
                    if small and nodes[best][0] == 'tree': floats.setdefault(best, []).append(_float(meta))
                    else: blocks_after.setdefault(best, []).append(html)
                    st['placed'] += 1; continue
                hk = tk(hd); done = False
                if small and hk:
                    cand = [x for x in xn if x['k'] in ('tree', 'plain') and x['sub'] and len(hk & tk(x['sub'])) / max(len(hk), len(tk(x['sub'])) or 1) >= 0.7]
                    cand = cand or [x for x in xn if x['k'] in ('tree', 'plain') and x['main'] and len(hk & tk(x['main'])) / max(len(hk), len(tk(x['main'])) or 1) >= 0.7]
                    if cand: cand[0]['fl'].append(_float(meta)); done = True; st['placed'] += 1
                if not done: left.append(html)
            for j, nd in enumerate(nodes):
                if j in floats and nd[0] == 'tree': nd = ('tree', nd[1], floats[j] + list(nd[2]), nd[3], nd[4])
                out.append(nd)
                if j in blocks_after: out.append(('raw', '<div class="pics">%s</div>' % ''.join(blocks_after[j])))
            for x in xn:
                if x['k'] == 'mh': out.append(('raw', '<div class="mh">%s</div>' % H.escape(x['main'])))
                elif x['k'] == 'tree': out.append(('tree', x['label'], x['fl'] + x['kids'], None, 24))
                elif x['k'] == 'plain': out.append(('raw', '<div class="pl">%s%s</div>' % (''.join(x['fl']), ''.join('<div class="kid">%s</div>' % y for y in x['kids']))))
                else: out.append(('raw', '<div class="hd">%s</div>' % D._conv(x['html'])))
            if left: out.append(('raw', '<div class="pics">%s</div>' % ''.join(left)))
        STATS[n] = st
        if n in OPENERS:
            out = _opening(n) + out
        print('ch%d: handout blocks %d, added as more points %d, pictures %d (at their node %d, rest in the topic flow)' % (n, st['blocks'], st['miss'], st['figs'], st['placed']))
        if ch.get('recall'):
            rc = ch['recall']; ch['recall'] = None
            out.append(('sec', 'RECALL DRILL: COVER AND ANSWER', 'r'))
            out.append(('raw', '<table>' + ''.join('<tr>' + ''.join('<td style="width:23%%">%s</td><td style="width:27%%">%s</td>' % qa for qa in rc[i:i + 2]) + ('<td></td><td></td>' if len(rc[i:i + 2]) == 1 else '') + '</tr>' for i in range(0, len(rc), 2)) + '</table>'))
        out.append(('sec', 'PYQs OF THIS CHAPTER', 'r'))
        if 'exam-lens' in segs: out.append(('raw', '<div class="hd pq">%s</div>' % D._conv(re.sub(r'^<h2.*?</h2>', '', segs['exam-lens'], flags=re.S))))
        if tail:
            out.append(('raw', '<div class="ph">★ PYQ answers in one line (asked year and the key)</div>')); out += tail
        if pyq_ids:
            out.append(('raw', '<div class="ph">✍ The PYQs as printed in the handout, with answers</div>'))
            out.append(('raw', '<div class="hd pq">%s</div>' % D._conv(''.join(re.sub(r'^<(h2|h3|h4)[^>]*>.*?</\1>', '', segs[i], count=1, flags=re.S) for i in pyq_ids))))
        if n in OPENERS: out += _closing(n)
        txt = D._txt(re.sub(r'src="data:[^"]*"', '', m)) + ' ' + D._txt(' '.join(str(x) for x in out if x[0] != 'raw'))
        found = sorted(set(re.findall(r'(?<![A-Za-z])(?:[A-Z][a-z]?[A-Z][A-Za-z0-9\-]*|[A-Z]{2,})(?![A-Za-z])', D._txt(re.sub(r'src="data:[^"]*"', '', ' '.join(str(x) for x in out))).replace('\\u', ' '))))
        have2 = [a for a in found if a in GL]
        for a in GL:
            if a not in have2 and not a.isupper() and re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(a), txt): have2.append(a)
        un = [a for a in found if a not in GL and a not in IGNORE and not (a.isupper() and a.lower() in D.WORDS)]
        if un: print('UNEXPANDED ABBREVIATIONS ch%d:' % n, ' '.join(un))
        if have2:
            rows = ''.join('<div class="ge"><b>%s</b> = <u>%s</u>%s</div>' % (a, GL[a][0], (' — ' + GL[a][1]) if GL[a][1] else '') for a in sorted(have2, key=str.lower))
            out.append(('raw', '<div class="glo2"><div class="gh">\U0001F524 ABBREVIATION COLUMN <i>(full forms as the handout gives them where it does; the one-line meanings are plain-language aids, verify)</i></div><div class="gc">%s</div></div>' % rows))
        ch['nodes'] = out
CSS += OCSS

CSS += (".sw.fp{background:none!important;border:0!important;padding:0!important;margin:0 0 1.4mm 3mm!important;font-size:8pt;color:#555;text-align:center;break-inside:avoid}"
        ".sw.fp img{width:100%;border:1px solid #bbb;border-radius:2px}.sw.fp .cp{line-height:1.1}.kids:after{content:'';display:block;clear:both}")

CSS += (".mh{font-family:CB;font-size:12.6pt;color:#1565c0;border-bottom:2px solid #1565c0;margin:2.6mm 0 1.2mm;break-after:avoid}"
        ".pl{margin:.6mm 0 1.4mm 1mm}.pl:after{content:'';display:block;clear:both}.pl .kid{margin:.7mm 0}.pl .kid:before{content:'\\2192  ';color:#999}")
CSS += (".sub{display:block!important;max-width:none!important;width:auto;margin-right:1.6mm!important}"
        ".mh{display:block;background:linear-gradient(90deg,#dbeafe 0%,#f4f9ff 70%,#fff 100%);border:2px solid #1565c0;border-radius:3px;padding:.5mm 3mm .7mm 0;font-family:CB;font-size:13.4pt;color:#0d47a1;box-shadow:1.1mm 1.1mm 0 #1565c0;margin:3.2mm 1.6mm 2.2mm 0!important;border-bottom:2px solid #1565c0!important;break-after:avoid;letter-spacing:.4px}"
        ".mh:before{content:'\\25C6';display:inline-block;background:#1565c0;color:#fff;padding:.5mm 2.6mm;margin:-.5mm 3mm -.7mm 0;font-size:11pt}")
CSS += (".sub{display:flex!important;align-items:center;flex-wrap:nowrap;gap:2.6mm;text-align:left!important;justify-content:flex-start}.sub svg,.sub img{flex:none}.sub .pyq{margin-left:0!important;flex:none}"
        ".mh{background:linear-gradient(90deg,#ef6c00 0%,#fb8c00 55%,#ffb74d 100%)!important;color:#fff!important;border:2px solid #4e342e!important;border-bottom:2px solid #4e342e!important;border-radius:3px 16px 16px 3px!important;box-shadow:1.3mm 1.3mm 0 #4e342e!important;text-shadow:.35mm .35mm 0 rgba(78,52,46,.55);padding:.7mm 4mm .8mm 2.4mm!important;letter-spacing:.5px}"
        ".mh:before{content:'\\25B6'!important;display:inline-block;background:#4e342e!important;color:#ffcc80!important;border-radius:50%;width:5.6mm;height:5.6mm;line-height:5.6mm;text-align:center;font-size:8pt!important;padding:0!important;margin:0 3mm 0 0!important;vertical-align:middle;text-shadow:none}")
CSS += (".sub{display:block!important;text-align:left!important;white-space:normal}.sub .pic{display:inline-block;margin-right:2.6mm}.sub .pyq{display:inline-block;margin:0 0 0 2.4mm!important;vertical-align:middle}")
CSS += (".sub .pic{display:inline-block!important;width:7.6mm;overflow:hidden;white-space:nowrap;vertical-align:middle;text-indent:0;margin-right:1.6mm!important}")
CSS += (".sub i.pic{width:7.6mm!important;max-width:7.6mm!important;flex:none!important;text-align:left!important;display:inline-block!important}")
CSS += (".sub,.sub.b,.sub.r,.sub.g{background:linear-gradient(100deg,#4a148c,#ad1457 60%,#ff7043)!important;color:#fff!important;border:2px solid #2b0f3a!important;border-radius:2mm!important;box-shadow:1.2mm 1.2mm 0 #2b0f3a!important;letter-spacing:1px;text-shadow:0 1px 0 rgba(0,0,0,.35)}"
        ".sub .pyq{background:#fff3c4!important;color:#6a1b00!important;border-color:#ffd54f!important;text-shadow:none}")
CSS += (".sub,.sub.b,.sub.r,.sub.g{background:#e8f1fb!important;color:#1f3a5a!important;border:1.4px solid #7f9fc4!important;border-left:5mm solid #9db8d8!important;border-radius:1.5mm!important;box-shadow:none!important;text-shadow:none!important;letter-spacing:.6px}"
        ".sub .pyq{background:#fff!important;color:#6b4e00!important;border:1px solid #d9b95a!important}"
        ".mh{background:#fdf1dc!important;color:#5a3b12!important;border:1.2px solid #d8b27a!important;box-shadow:none!important;text-shadow:none!important}"
        ".mh *{color:#5a3b12!important;text-shadow:none!important}")
