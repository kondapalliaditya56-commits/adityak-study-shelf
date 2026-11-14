# -*- coding: utf-8 -*-
"""Detailed layer for the Geography handwritten notes.
Keeps the existing revision DSL (trees, tables, mnemonics) as the 'revision map' of each topic and adds, at the same topic:
  - 'Understand it first' (plain words; analogies are memory aids, no new facts)
  - the FULL handout notes with the handout's own pictures, maps and tables (taken from the Study Shelf chapter page,
    which is built from the handout PDF), plus the quick-revise cards
MAP[chapter] = {dsl section number: first Shelf anchor id of that topic}; UND[chapter] = {dsl section number: text}."""
import re, os, html as H
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
CSS = (".hd{margin:1mm 0 2mm}.hd p{margin:.6mm 0 1mm}.hd ul{margin:.3mm 0 .8mm;padding-left:5mm}.hd li{margin:.35mm 0}"
       ".hd ul ul{list-style:circle}.hd ul ul ul{list-style:square}"
       ".hd .h3{font-family:KB;font-size:11.6pt;color:#c62828;border-bottom:1.4px solid #c62828;margin:2.4mm 0 1mm;break-after:avoid}"
       ".hd .h4{font-family:KB;font-size:10.8pt;color:#1565c0;margin:1.8mm 0 .6mm;break-after:avoid}"
       ".hd .h4:before{content:'\\25B8  '}"
       ".hd .red{color:#c62828}.hd .grn{color:#2e7d32}.hd mark{background:#fff176;color:#111}"
       ".hfig{text-align:center;margin:1.6mm 0;break-inside:avoid}.hfig img{max-width:100%;max-height:105mm;border:1px solid #bbb;border-radius:2px}"
       ".hfig.tbl img{max-height:235mm}"
       ".qk{border:1.6px solid #ef6c00;border-left-width:2mm;background:#fff8ec;border-radius:3px;padding:1mm 2.4mm;margin:1.6mm 0;color:#333}"
       ".qk .qh{font-family:KB;color:#e65100;font-size:10pt;margin-bottom:.4mm;break-after:avoid}.qk table{font-size:9.6pt;margin:1mm 0}.qk p{margin:.5mm 0}.qk ul{margin:.3mm 0;padding-left:5mm}"
       ".qk blockquote{margin:1mm 0;padding-left:2mm;border-left:2px solid #ef6c00}.qk h3,.qk h4{font-family:KB;font-size:10.4pt;margin:1mm 0 .4mm;color:#e65100}"
       ".und{border:1.8px solid #00838f;background:#e0f7fa;border-radius:3px;padding:1mm 2.4mm;margin:1.2mm 0;color:#004d57;break-inside:avoid}.und b{color:#006064}"
       ".fh{font-family:KB;font-size:9.4pt;color:#555;border-top:1.4px dashed #999;margin:2mm 0 .6mm;padding-top:.6mm;break-after:avoid}"
       ".glo2{border:1.8px solid #6a1b9a;background:#f8f0fb;border-radius:3px;padding:1mm 2.4mm;margin:2.4mm 0}.glo2 .gh{font-family:KB;color:#6a1b9a;font-size:10.4pt;margin-bottom:.8mm}.glo2 .gc{column-count:2;column-gap:5mm;font-size:9.8pt}.glo2 .ge{break-inside:avoid;margin:.4mm 0}"
       ".pics{display:flex;flex-wrap:wrap;gap:2mm 3mm;align-items:flex-start;margin:1mm 0 2mm}.pic{flex:0 0 47%;max-width:47%;text-align:center;break-inside:avoid}.pic.w{flex:0 0 100%;max-width:100%}"
       ".pic.s{flex:0 0 30%;max-width:30%}.pic img{max-width:100%;max-height:62mm;border:1px solid #bbb;border-radius:2px}.pic.w img{max-height:100mm}.pic.t img{max-height:225mm}.pic .cp{font-size:8.6pt;color:#555;line-height:1.1;margin-top:.3mm}"
       ".ph{font-family:KB;font-size:9.4pt;color:#00695c;margin:1.4mm 0 .4mm;break-after:avoid}"
       ".pq{font-size:9.6pt}.pq p{margin:.4mm 0}.pq ul{margin:.2mm 0 .6mm;padding-left:5mm}.pq .h3{font-size:10.6pt}.pq .h4{font-size:10pt;margin:1.6mm 0 .3mm;color:#c62828}.pq .h4:before{content:''}"
       ".rm{font-family:KB;font-size:9.4pt;color:#555;margin:1mm 0 0;break-after:avoid}")
WORDS = set()
def _words(maps):
    for n in maps:
        t = H.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'src="data:[^"]*"', '', _main(n))))
        WORDS.update(w for w in re.findall(r"[a-z]{2,}", t))
def _main(n):
    t = open(os.path.join(ROOT, 'geo-ch%02d.html' % n), encoding='utf8').read()
    m = t[t.index('<main'):t.index('<nav class="pager"')]
    return m
def _conv(s):
    s = re.sub(r'<a class="anchor"[^>]*>.*?</a>', '', s, flags=re.S)
    s = re.sub(r'<h2[^>]*>(.*?)</h2>', lambda m: '<div class="h3">%s</div>' % m.group(1), s, flags=re.S)
    s = re.sub(r'<h3[^>]*>(.*?)</h3>', lambda m: '<div class="h3">%s</div>' % m.group(1), s, flags=re.S)
    s = re.sub(r'<h4[^>]*>(.*?)</h4>', lambda m: '<div class="h4">%s</div>' % m.group(1), s, flags=re.S)
    def fig(m):
        cls = 'hfig tbl' if 'tbl' in m.group(1) else 'hfig'
        w = float(m.group(2)); src = m.group(3)
        mm = min(134.0, w * 0.3528 * (1.0 if 'tbl' in m.group(1) else 0.9))
        return '<div class="%s"><img src="%s" style="width:%.1fmm"></div>' % (cls, src, mm)
    s = re.sub(r'<figure class="([^"]*)" style="--w:([\d.]+)px"><img[^>]*src="([^"]+)"[^>]*></figure>', fig, s)
    def qr(m):
        lab = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        body = m.group(2).replace('<div class="tw">', '').replace('</table></div>', '</table>')
        return ''  # quick-revise cards are not handout text; the revision map at each topic already carries them
    s = re.sub(r'<details class="qr"[^>]*><summary><b>[^<]*</b><span>(.*?)</span></summary><div class="quick">(.*?)</div></details>', qr, s, flags=re.S)
    s = s.replace('<div class="tw">', '').replace('</table></div>', '</table>')
    s = re.sub(r'\s(loading|alt)="[^"]*"', '', s)
    return s
def split(n):
    """-> (lens_html, {anchor id: html from that anchor up to the next anchor}, [ids in order], recall_html)"""
    m = _main(n)
    heads = [(x.start(), x.group(2)) for x in re.finditer(r'<(h2|h3|h4)[^>]*\sid="([^"]+)"', m)]
    ids = [i for _, i in heads]; segs = {}
    for k, (pos, i) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(m)
        segs[i] = m[pos:end]
    return segs, ids
def _txt(x): return re.sub(r'\s+', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()
TOK = re.compile(r'<(h2|h3|h4)[^>]*>(.*?)</\1>|<li>\s*<b>(.*?)</b>|<p>\s*<b>(.*?)</b>|<figure class="([^"]*)" style="--w:([\d.]+)px"><img[^>]*src="([^"]+)"[^>]*></figure>', re.S)
def pics(seg):
    """Handout figures of a topic, each captioned with the handout heading / label it sits under."""
    seg = re.sub(r'<details class="qr".*?</details>', '', seg, flags=re.S)
    out = []; hd = ''; lab = ''
    for m in TOK.finditer(seg):
        if m.group(1): hd = re.sub(r'^\d+\s*·\s*', '', _txt(re.sub(r'<a class="anchor".*?</a>', '', m.group(2), flags=re.S))).rstrip(':# '); lab = ''
        elif m.group(3) or m.group(4):
            l = _txt(m.group(3) or m.group(4)).rstrip(': ')
            if 2 < len(l) < 48 and not re.match(r'(Q\.|Answer|Ans|Explanation|Which|Select|Statement)', l): lab = l
        else:
            cls, w, src = m.group(5), float(m.group(6)), m.group(7)
            cap = hd.title() if hd.isupper() else hd
            if lab and lab.lower() not in cap.lower(): cap = (cap + ' · ' if cap else '') + lab
            k = 'pic t w' if 'tbl' in cls else ('pic w' if w > 345 else ('pic s' if w < 190 else 'pic'))
            out.append('<div class="%s"><img src="%s"><div class="cp">%s</div></div>' % (k, src, H.escape(cap)))
    return out
ISPYQ = re.compile(r'^\s*(\d+\s*·\s*)?PYQs?\s*:?\s*$', re.I)
PYQBX = re.compile(r'^\s*<b>\s*(Mains|Prelims|PYQ)?\s*(19|20)\d\d')
def attach(chs, maps, und, GL={}, IGNORE=()):
    for ch in chs:
        n = ch['id']
        if n not in maps: continue
        if not WORDS: _words(maps)
        m = _main(n)
        heads = [(x.start(), x.group(2), _txt(re.sub(r'<a class="anchor".*?</a>', '', x.group(3), flags=re.S))) for x in re.finditer(r'<(h2|h3|h4)[^>]*\sid="([^"]+)"[^>]*>(.*?)</\1>', m, re.S)]
        segs = {}; order = []; pyq_ids = []
        for k, (pos, i, ttl) in enumerate(heads):
            segs[i] = m[pos:heads[k + 1][0] if k + 1 < len(heads) else len(m)]; order.append(i)
            if ISPYQ.match(ttl): pyq_ids.append(i)
        body = [i for i in order if i not in ('exam-lens', 'recall', 'traps') and i not in pyq_ids]
        # topic start points: 'sid' or 'sid@keyword' (keyword = text inside that anchor's block where the topic starts)
        secs = [x for x in ch['nodes'] if x[0] == 'sec']
        mp = maps[n]; assert len(mp) == len(secs), ('map length', n, len(mp), len(secs))
        pts = []  # (body index, offset in that seg, sec ordinal)
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
        npic = 0; out = []; tail = []; k = -1; cur_pyq = False; pend = None
        def flush():
            nonlocal npic
            if pend is not None and pend in rng:
                pp = pics(rng[pend]); npic += len(pp)
                if pp: out.append(('raw', '<div class="ph">\U0001F5BC From the handout: pictures, maps and tables of this topic</div><div class="pics">%s</div>' % ''.join(pp)))
        for nd in ch['nodes']:
            if nd[0] == 'sec':
                flush(); k += 1; pend = k
                cur_pyq = bool(re.search(r'PYQ BANK|MISSED PYQ', re.sub(r'<[^>]+>', '', nd[1]), re.I))
                if cur_pyq: tail.append(('bx', 'bl', '<b>%s</b>' % re.sub(r'<[^>]+>', '', nd[1]))); continue
                out.append(nd)
                if k in und.get(n, {}): out.append(('raw', '<div class="und"><b>Understand it first:</b> %s</div>' % und[n][k]))
            elif cur_pyq: tail.append(nd)
            elif nd[0] == 'bx' and PYQBX.match(nd[2]): tail.append(nd)
            else: out.append(nd)
        flush()
        total = len(pics(''.join(segs[i] for i in body)))
        if npic != total: print('PICTURES ch%d: placed %d of %d' % (n, npic, total))
        # chapter end: recall drill, then PYQs, then abbreviation column
        if ch.get('recall'):
            rc = ch['recall']; ch['recall'] = None
            out.append(('sec', 'RECALL DRILL: COVER AND ANSWER', 'r'))
            out.append(('raw', '<table>' + ''.join('<tr>' + ''.join('<td style="width:23%%">%s</td><td style="width:27%%">%s</td>' % qa for qa in rc[i:i + 2]) + ('<td></td><td></td>' if len(rc[i:i + 2]) == 1 else '') + '</tr>' for i in range(0, len(rc), 2)) + '</table>'))
        out.append(('sec', 'PYQs OF THIS CHAPTER', 'r'))
        if 'exam-lens' in segs: out.append(('raw', '<div class="hd pq">%s</div>' % _conv(re.sub(r'^<h2.*?</h2>', '', segs['exam-lens'], flags=re.S))))
        if tail:
            out.append(('raw', '<div class="ph">★ PYQ answers in one line (asked year and the key)</div>')); out += tail
        if pyq_ids:
            out.append(('raw', '<div class="ph">✍ The PYQs as printed in the handout, with answers</div>'))
            out.append(('raw', '<div class="hd pq">%s</div>' % _conv(''.join(re.sub(r'^<(h2|h3|h4)[^>]*>.*?</\1>', '', segs[i], count=1, flags=re.S) for i in pyq_ids))))
        txt = _txt(re.sub(r'src="data:[^"]*"', '', m)) + ' ' + _txt(' '.join(str(x) for x in out if x[0] != 'raw'))
        found = sorted(set(re.findall(r'(?<![A-Za-z])(?:[A-Z][a-z]?[A-Z][A-Za-z0-9\-]*|[A-Z]{2,})(?![A-Za-z])', _txt(re.sub(r'src="data:[^"]*"', '', ' '.join(str(x) for x in out))).replace('\\u', ' '))))
        have = [a for a in found if a in GL]
        for a in GL:
            if a not in have and not a.isupper() and re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(a), txt): have.append(a)
        un = [a for a in found if a not in GL and a not in IGNORE and not (a.isupper() and a.lower() in WORDS)]
        if un: print('UNEXPANDED ABBREVIATIONS ch%d:' % n, ' '.join(un))
        if have:
            rows = ''.join('<div class="ge"><b>%s</b> = <u>%s</u>%s</div>' % (a, GL[a][0], (' — ' + GL[a][1]) if GL[a][1] else '') for a in sorted(have, key=str.lower))
            out.append(('raw', '<div class="glo2"><div class="gh">\U0001F524 ABBREVIATION COLUMN <i>(full forms as the handout gives them where it does; the one-line meanings are plain-language aids, verify)</i></div><div class="gc">%s</div></div>' % rows))
        ch['nodes'] = out
