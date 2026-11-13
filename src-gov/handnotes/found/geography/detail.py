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
def attach(chs, maps, und, GL={}, IGNORE=()):
    for ch in chs:
        n = ch['id']
        if n not in maps: continue
        if not WORDS: _words(maps)
        segs, ids = split(n); mp = maps[n]; U = und.get(n, {})
        body = [i for i in ids if i not in ('exam-lens', 'recall', 'traps')]
        starts = sorted(((body.index(a), k) for k, a in mp.items()))
        assert starts[0][0] == 0, 'first topic must start at the first handout anchor'
        rng = {}
        for j, (p, k) in enumerate(starts):
            e = starts[j + 1][0] if j + 1 < len(starts) else len(body)
            rng[k] = ''.join(segs[i] for i in body[p:e])
        out = []; cur = None; first_sec = True
        def flush(k):
            if k in rng:
                out.append(('raw', '<div class="fh">✍ Full handout notes with its pictures (nothing dropped)</div><div class="hd">%s</div>' % _conv(rng[k])))
        for nd in ch['nodes']:
            if nd[0] == 'sec':
                if cur is not None: flush(cur)
                mnum = re.match(r'\s*(\d+)\s', re.sub(r'<[^>]+>', '', nd[1])); cur = int(mnum.group(1)) if mnum else -1
                if first_sec and 'exam-lens' in segs:
                    lens = re.sub(r'^<h2.*?</h2>', '', segs['exam-lens'], flags=re.S)
                    out.append(('sec', 'EXAM LENS AND PYQ MAP', 'r')); out.append(('raw', '')); out.append(('raw', '<div class="hd">%s</div>' % _conv(lens)))
                first_sec = False
                out.append(nd)
                if cur in U: out.append(('raw', '<div class="und"><b>Understand it first:</b> %s</div>' % U[cur]))
                if cur in rng: out.append(('raw', '<div class="rm">★ Revision map (cover the full notes and recall from this)</div>'))
            else: out.append(nd)
        if cur is not None: flush(cur)
        missing = [k for k in rng if not any(x[0] == 'sec' and re.match(r'\s*%d\s' % k, re.sub(r'<[^>]+>', '', x[1])) for x in ch['nodes'])]
        assert not missing, ('unmapped', n, missing)
        for extra in ('traps', 'recall'):
            if extra in segs: out.append(('raw', '<div class="hd">%s</div>' % _conv(segs[extra])))
        txt = H.unescape(re.sub(r'<[^>]+>', ' ', re.sub(r'src="data:[^"]*"', '', ''.join(segs.values())))) + ' ' + H.unescape(re.sub(r'<[^>]+>', ' ', repr(ch['nodes'][:0]) + ' '.join(str(x) for x in out if x[0] != 'raw')))
        found = sorted(set(re.findall(r'(?<![A-Za-z])(?:[A-Z][a-z]?[A-Z][A-Za-z0-9\-]*|[A-Z]{2,})(?![A-Za-z])', txt)))
        have = [a for a in found if a in GL]
        for a in GL:
            if a not in have and not a.isupper() and re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(a), txt): have.append(a)
        un = [a for a in found if a not in GL and a not in IGNORE and not (a.isupper() and a.lower() in WORDS)]
        if un: print('UNEXPANDED ABBREVIATIONS ch%d:' % n, ' '.join(un))
        if have:
            rows = ''.join('<div class="ge"><b>%s</b> = <u>%s</u>%s</div>' % (a, GL[a][0], (' \u2014 ' + GL[a][1]) if GL[a][1] else '') for a in sorted(have, key=str.lower))
            out.append(('raw', '<div class="glo2"><div class="gh">\U0001F524 ABBREVIATION COLUMN <i>(full forms as the handout gives them where it does; the one-line meanings are plain-language aids, verify)</i></div><div class="gc">%s</div></div>' % rows))
        ch['nodes'] = out
