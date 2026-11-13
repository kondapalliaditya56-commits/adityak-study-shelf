# -*- coding: utf-8 -*-
"""Handwritten-style revision notes for a foundation subject.
Usage (from anywhere): python3 buildfound.py SUBJECT OUT.pdf [id,id,...]
SUBJECT = polity | economy | geography | modern-india ; chapters live in found/<SUBJECT>/ch_*.py (each defines CHS)."""
import re, sys, os, glob, importlib.util, re
HERE = os.path.dirname(os.path.abspath(__file__)); HN = os.path.dirname(HERE)
os.chdir(HN); sys.path.insert(0, HN)
from weasyprint import HTML
import hwlib, dsl, hwstyle
from dsl import *
SUBJ = {
 'polity': dict(title='POLITY', sub='Preamble · Sources · Union and territory · Citizenship · Fundamental Rights · DPSP · Duties · Amendment · Executive · Parliament · Judiciary · States · Federalism · Emergency · Elections', cap='Built from the Sarrthi IAS GS Foundation Polity handouts (Parts 1 to 3) with Lakshmikanth tables and current affairs.', pre='pol', ca=['pol'], gl=True),
 'economy': dict(title='ECONOMY', sub='Basics · National income · Growth · Money and banking · Inflation · Budget and taxes · External sector · Agriculture · Industry · Poverty and development', cap='Built from the Sarrthi IAS GS Foundation Economy handouts (Aditya Kalia) with Sept and Oct 2026 current affairs.', pre='eco', ca=['eco'], gl=True),
 'geography': dict(title='GEOGRAPHY', sub='Geomorphology · Climatology · Oceanography · Indian geography · Human geography · Economic geography', cap='Built from the Sarrthi IAS GS Foundation Geography handouts (pictures and the mind-map pages are in the textbook edition).', pre='geo', ca=[], gl=False),
 'modern-india': dict(title='MODERN INDIAN HISTORY', sub='Eighteenth-century India · British conquest · Revolt of 1857 · Reforms · Moderates and Extremists · Gandhian era · Constitutional developments', cap='Built from the Sarrthi IAS handout and Himanshu Khatri class slides. Reign-year codes are kept exactly as taught.', pre='mi', ca=['mi'], gl=False),
}

def apply_cn(subj, chs):
    """Class-note additions: found/<subj>/cn/cn_*.py define ADD = {chapter_id: [dict(after='section title keyword', nodes=[...]), ...]}.
    Each block goes at the end of the section whose title contains `after` (else before the recall drill = end of nodes)."""
    adds = {}; rec = {}
    for f in sorted(glob.glob(os.path.join(HERE, subj, 'cn', 'cn_*.py'))):
        spec = importlib.util.spec_from_file_location('cn_' + os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for cid, blocks in m.ADD.items(): adds.setdefault(cid, []).extend(blocks)
        for cid, qa in getattr(m, 'RECALL', {}).items(): rec.setdefault(cid, []).extend(qa)
    for ch in chs:
        if rec.get(ch['id']): ch['recall'] = list(ch.get('recall') or []) + rec[ch['id']]; ch['cn_recall'] = list(rec[ch['id']])
        for blk in adds.get(ch['id'], []):
            nodes = ch['nodes']; kw = (blk.get('after') or '').lower(); pos = len(nodes)
            if kw:
                for i, n in enumerate(nodes):
                    if n[0] == 'sec' and kw in re.sub(r'<[^>]+>', '', n[1]).lower():
                        pos = i + 1
                        while pos < len(nodes) and (nodes[pos][0] != 'sec' or re.sub(r'<[^>]+>', '', nodes[pos][1]).startswith('CLASS')): pos += 1
                        break
            ch['nodes'] = nodes[:pos] + list(blk['nodes']) + nodes[pos:]
            ch.setdefault('cn_blocks', []).append(blk)

def load(subj, only=None):
    chs = []
    for f in sorted(glob.glob(os.path.join(HERE, subj, 'ch_*.py'))):
        spec = importlib.util.spec_from_file_location('m_' + os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); chs += m.CHS
    chs.sort(key=lambda c: c['id'])
    apply_cn(subj, chs)
    if only: chs = [c for c in chs if c['id'] in only]
    return chs

import json as _json, html as _html
STORY_CSS = (".sty{border:1.6px solid #d9a400;background:#fffbe6;border-radius:3mm;padding:2mm 3mm;margin:2mm 0;break-inside:auto}"
 ".sty .sty-h{font-family:PH;font-size:12pt;color:#a06b00;margin-bottom:.6mm}.sty .sty-sp{font-weight:700;margin:0 0 1.2mm 0}"
 ".sty .sty-bt{display:flex;gap:2mm;margin:.9mm 0 0 0;break-inside:avoid}.sty .sty-bn{flex:none;width:5mm;height:5mm;border-radius:50%;background:#d9a400;color:#fff;text-align:center;font-size:8.5pt;line-height:5mm}"
 ".sty .sty-bb{flex:1}.sty .sty-bb b{color:#7a4f00}.sty .sty-br{font-size:8.6pt;color:#8a6d1f;font-style:italic;margin:0 0 0 7mm}.sty .sty-cast{font-size:9pt;margin-top:1.4mm;border-top:1px dashed #d9a400;padding-top:1mm}"
 ".stl{border-left:1.8mm solid #d9a400;background:#fff8dc;padding:.6mm 2mm;margin:1mm 0 1.2mm 0;font-size:9.4pt;break-inside:avoid}.stl b{color:#7a4f00}")
def _clean(x): return _html.escape(x.replace('\n', ' ').strip(), quote=False)
def load_story(subj):
    d = os.path.join(HERE, subj); data = {}
    f = os.path.join(d, 'story.json')
    if os.path.exists(f):
        for k, v in _json.load(open(f, encoding='utf8')).items(): data[int(k)] = v
    shorts = {}
    for g in sorted(glob.glob(os.path.join(d, 'story_short_*.json'))):
        for k, v in _json.load(open(g, encoding='utf8')).items(): shorts[int(k)] = v
    return data, shorts
def story_html(cid, data, shorts):
    st = data.get(cid)
    if not st: return ''
    sh = shorts.get(cid)
    h = '<div class="sty"><div class="sty-h">\U0001F4D6 THE STORY FIRST (same story as the textbook)</div><div class="sty-sp">%s</div>' % _clean(st['spine'])
    for i, b in enumerate(st['beats'], 1):
        parts = b.split('\n'); title = parts[0].rstrip('.')
        bridge = parts[-1] if parts[-1].startswith('\u2192') else ''
        body = (sh[i - 1] if sh and len(sh) == len(st['beats']) else ' '.join(parts[1:-1] if bridge else parts[1:])[:200])
        h += '<div class="sty-bt"><div class="sty-bn">%d</div><div class="sty-bb"><b>%s.</b> %s</div></div>' % (i, _clean(title), _clean(body))
        if bridge and i < len(st['beats']): h += '<div class="sty-br">%s</div>' % _clean(bridge)
    ch = [c for c in st.get('chars', [])[1:] if len(c) >= 3]
    if ch: h += '<div class="sty-cast"><b>Cast:</b> ' + ' · '.join('%s = %s' % (_clean(c[0]), _clean(c[2])) for c in ch) + '</div>'
    return h + '</div>'
_STORY = {}

FIX_CSS = (".arrow{flex-wrap:wrap}.arrow>div{flex:1 1 18.5%;min-width:18.5%;max-width:100%;overflow-wrap:anywhere;box-sizing:border-box;margin-bottom:1.2mm}"
           ".lab{overflow-wrap:anywhere;word-break:normal}")
def fit_labels(html):
    """Side-heading labels are fixed-width boxes: widen and shrink the font when the longest word would spill out (overlap with the text beside it)."""
    def f(m):
        w = int(m.group(1)); inner_html = m.group(3)
        txt = re.sub(r'<[^>]+>', ' ', _html.unescape(inner_html))
        words = [x for x in re.split(r'[\s/\u2013-]+', txt) if x]
        L = max([len(x) for x in words] or [1])
        p = 10.5; ww = w
        def need(wmm): return (wmm - 5.0) / (L * 0.205)
        if need(ww) < p:
            ww = min(w + 6, 36)
            p = max(7.4, min(10.5, need(ww)))
        sty = ' style="max-width:%dmm;min-width:%dmm%s"' % (ww, ww, ';font-size:%.1fpt' % p if p < 10.5 else '')
        return '<div class="lab"%s>%s</div>' % (sty, inner_html)
    return re.sub(r'<div class="lab" style="max-width:(\d+)mm;min-width:(\d+)mm">(.*?)</div>', f, html, flags=re.S)
def chapter_html(ch):
    ic = hwlib.ICON.get(ch.get('icon', 'bag'), hwlib.ICON['bag'])
    h = '<div class="chap" id="c%s"><div class="ttl">%s&nbsp;%s&nbsp;%s</div>' % (ch['id'], ic, ch['title'], ic)
    if ch.get('pyq'): h += '<div class="pyqline">%s</div>' % hwlib.P(ch['pyq'])
    if ch.get('simple'): h += hwlib.SW(ch['simple'])
    h += story_html(ch['id'], *_STORY.get('d', ({}, {})))
    nodes = ch['nodes']; i = 0
    while i < len(nodes):
        n = nodes[i]
        if n[0] == 'sec' and i + 2 < len(nodes) and nodes[i + 1][0] == 'stl':
            h += '<div class="keep">%s%s%s</div>' % (dsl.r_hw(n), dsl.r_hw(nodes[i + 1]), dsl.r_hw(nodes[i + 2])); i += 3
        elif n[0] == 'sec' and i + 1 < len(nodes):
            h += '<div class="keep">%s%s</div>' % (dsl.r_hw(n), dsl.r_hw(nodes[i + 1])); i += 2
        else: h += dsl.r_hw(n); i += 1
    if ch.get('recall'):
        rc = ch['recall']
        h += '<div class="keep">' + hwlib.S('Recall drill: cover and answer', 'r') + '<table>' + ''.join('<tr>' + ''.join('<td style="width:23%%">%s</td><td style="width:27%%">%s</td>' % qa for qa in rc[i:i+2]) + ('<td></td><td></td>' if len(rc[i:i+2]) == 1 else '') + '</tr>' for i in range(0, len(rc), 2)) + '</table></div>'
    return h + '</div>'
_rhw = dsl.r_hw
def r_hw(n):
    if n[0] == 'stl': return '<div class="stl"><b>\U0001F4D6 Story link \u00b7 beat %s:</b> %s</div>' % (n[1], n[2])
    out = _rhw(n)
    return '<div class="keep">%s</div>' % out if n[0] in ('fl', 'hub', 'tl') else out
dsl.r_hw = r_hw
_hub = dsl.svg_hub
dsl.svg_hub = lambda c, s: _hub(c, s).replace('max-width:150mm', 'max-width:118mm')
def build(subj, out, only=None):
    cfg = SUBJ[subj]; chs = load(subj, only)
    _STORY['d'] = load_story(subj)
    import listify; listify.apply(chs)
    cov = ('<div class="cov"><div class="s">UPSC CSE 2027 · GS Foundation</div><h1>%s</h1><div class="s">%s</div><div><span class="bx">Handwritten revision notes</span></div>'
           '<div class="t">%s<br>Bracket trees · diagrams · mnemonics · PYQ tags · current affairs<br>Right column and left binding margin are kept blank for your own use.<br><br>Personal study edition · for printing</div></div>') % (cfg['title'], cfg['sub'], cfg['cap'])
    toc = '<div class="partpg" style="padding:0;break-before:page"><div class="toc"><h2>INDEX</h2>'
    cur = None
    for c in chs:
        pt = c.get('part_name')
        if pt and pt != cur: cur = pt; toc += '<div class="pt" style="background:%s">%s</div>' % (c.get('part_bg', '#e3f2fd'), pt)
        toc += '<a href="#c%s">%s &nbsp;%s</a>' % (c['id'], c['id'], c.get('toc', c['title']))
    toc += '</div></div>'
    body = [cov, toc] + [chapter_html(c) for c in chs]
    html = '<html><head><style>%s</style></head><body>%s</body></html>' % (hwlib.CSS + STORY_CSS + FIX_CSS + '.chap{break-before:auto;margin-top:5mm}.pyqline,.sw,.ttl{break-after:avoid}.br{orphans:3;widows:3}.br{break-inside:auto}.keep{break-inside:avoid}.keep table{font-size:9pt}.keep td{padding:.2mm 1.4mm}.pyq{font-size:7.6pt}', ''.join(body))
    html = html.replace('</style>', '@page{@bottom-right{content:"%s · Handwritten Notes · " counter(page);font-family:PH;font-size:8pt;color:#888}}</style>' % cfg['title'].title(), 1)
    html = html.replace('</style>', hwstyle.css('handlee', '') + '</style>', 1)
    html = hwstyle.decorate(html)
    import hwextras
    if subj == 'modern-india':
        hwextras.SKIP.add('CIC')  # in Modern India CIC = Commander-in-Chief, not Central Information Commission
    if not os.environ.get('NOEXTRAS'):
        if cfg['ca'] or cfg['gl']:
            html = hwextras.apply(html, cfg['ca'] or ['none'], months=('sep26', 'oct26'))
    html = fit_labels(html)
    d = HTML(string=html, base_url='.').render()
    print('pages', len(d.pages)); d.write_pdf(out)
if __name__ == '__main__':
    only = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
    build(sys.argv[1], sys.argv[2], only)
