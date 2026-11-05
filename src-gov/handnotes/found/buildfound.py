# -*- coding: utf-8 -*-
"""Handwritten-style revision notes for a foundation subject.
Usage (from anywhere): python3 buildfound.py SUBJECT OUT.pdf [id,id,...]
SUBJECT = polity | economy | geography | modern-india ; chapters live in found/<SUBJECT>/ch_*.py (each defines CHS)."""
import sys, os, glob, importlib.util, re
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
def load(subj, only=None):
    chs = []
    for f in sorted(glob.glob(os.path.join(HERE, subj, 'ch_*.py'))):
        spec = importlib.util.spec_from_file_location('m_' + os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); chs += m.CHS
    chs.sort(key=lambda c: c['id'])
    if only: chs = [c for c in chs if c['id'] in only]
    return chs
def chapter_html(ch):
    ic = hwlib.ICON.get(ch.get('icon', 'bag'), hwlib.ICON['bag'])
    h = '<div class="chap" id="c%s"><div class="ttl">%s&nbsp;%s&nbsp;%s</div>' % (ch['id'], ic, ch['title'], ic)
    if ch.get('pyq'): h += '<div class="pyqline">%s</div>' % hwlib.P(ch['pyq'])
    if ch.get('simple'): h += hwlib.SW(ch['simple'])
    nodes = ch['nodes']; i = 0
    while i < len(nodes):
        n = nodes[i]
        if n[0] == 'sec' and i + 1 < len(nodes):
            h += '<div class="keep">%s%s</div>' % (dsl.r_hw(n), dsl.r_hw(nodes[i + 1])); i += 2
        else: h += dsl.r_hw(n); i += 1
    if ch.get('recall'):
        rc = ch['recall']
        h += '<div class="keep">' + hwlib.S('Recall drill: cover and answer', 'r') + '<table>' + ''.join('<tr>' + ''.join('<td style="width:23%%">%s</td><td style="width:27%%">%s</td>' % qa for qa in rc[i:i+2]) + ('<td></td><td></td>' if len(rc[i:i+2]) == 1 else '') + '</tr>' for i in range(0, len(rc), 2)) + '</table></div>'
    return h + '</div>'
_rhw = dsl.r_hw
def r_hw(n):
    out = _rhw(n)
    return '<div class="keep">%s</div>' % out if n[0] in ('fl', 'hub', 'tl') else out
dsl.r_hw = r_hw
_hub = dsl.svg_hub
dsl.svg_hub = lambda c, s: _hub(c, s).replace('max-width:150mm', 'max-width:118mm')
def build(subj, out, only=None):
    cfg = SUBJ[subj]; chs = load(subj, only)
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
    html = '<html><head><style>%s</style></head><body>%s</body></html>' % (hwlib.CSS + '.chap{break-before:auto;margin-top:5mm}.pyqline,.sw,.ttl{break-after:avoid}.br{orphans:3;widows:3}.br{break-inside:auto}.keep{break-inside:avoid}.keep table{font-size:9pt}.keep td{padding:.2mm 1.4mm}.pyq{font-size:7.6pt}', ''.join(body))
    html = html.replace('</style>', '@page{@bottom-right{content:"%s · Handwritten Notes · " counter(page);font-family:PH;font-size:8pt;color:#888}}</style>' % cfg['title'].title(), 1)
    html = html.replace('</style>', hwstyle.css('handlee', '') + '</style>', 1)
    html = hwstyle.decorate(html)
    import hwextras
    if subj == 'modern-india':
        hwextras.SKIP.add('CIC')  # in Modern India CIC = Commander-in-Chief, not Central Information Commission
    if not os.environ.get('NOEXTRAS'):
        if cfg['ca'] or cfg['gl']:
            html = hwextras.apply(html, cfg['ca'] or ['none'], months=('sep26', 'oct26'))
    d = HTML(string=html, base_url='.').render()
    print('pages', len(d.pages)); d.write_pdf(out)
if __name__ == '__main__':
    only = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
    build(sys.argv[1], sys.argv[2], only)
