# -*- coding: utf-8 -*-
"""Build the IR handwritten-style print notes. Run from this folder: python3 buildhw.py OUT.pdf"""
import sys, os, glob, importlib
os.chdir(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.getcwd())
from weasyprint import HTML
import hwlib
from dsl import *
import dsl

def chapter_hw_ir(ch):
    """Like dsl.chapter_hw, but a section heading is glued to the block after it (no orphan headings)."""
    ic = hwlib.ICON.get(ch.get('icon', 'bag'), hwlib.ICON['bag'])
    h = '<div class="chap" id="c%s"><div class="ttl">%s&nbsp;%s&nbsp;%s</div>' % (ch['id'], ic, ch['title'], ic)
    if ch.get('pyq'): h += '<div class="pyqline">%s</div>' % hwlib.P(ch['pyq'])
    if ch.get('simple'): h += hwlib.SW(ch['simple'])
    nodes = ch['nodes']; i = 0
    while i < len(nodes):
        n = nodes[i]
        if n[0] == 'sec' and i + 1 < len(nodes):
            h += '<div class="keep">%s%s</div>' % (r_hw(n), r_hw(nodes[i + 1])); i += 2
        else:
            h += r_hw(n); i += 1
    if ch.get('recall'):
        h += '<div class="keep">' + hwlib.S('Recall drill: cover and answer', 'r') + '<table>' + ''.join('<tr>' + ''.join('<td style="width:23%%">%s</td><td style="width:27%%">%s</td>' % qa for qa in ch['recall'][i:i+2]) + ('<td></td><td></td>' if len(ch['recall'][i:i+2]) == 1 else '') + '</tr>' for i in range(0, len(ch['recall']), 2)) + '</table></div>'
    return h + '</div>'

import condense as _cd
LEVEL = (150, 300, 130)
_rhw = dsl.r_hw
def r_hw(n):
    if n[0] in ('tree', 'bx', 'tb', 'tl', 'two'): n = _cd.condense(n, *LEVEL)
    out = _rhw(n)
    return '<div class="keep">%s</div>' % out if n[0] in ('fl', 'hub', 'tl') else out
dsl.r_hw = r_hw
_hub = dsl.svg_hub
dsl.svg_hub = lambda c, s: _hub(c, s).replace('max-width:150mm', 'max-width:118mm')

PARTS = [('Module 1', 'Civil Services, Transparency, Accountability, Citizen\'s Charter, RTI', '#e0f2f1'), ('Module 2', 'Corruption, Social Audit, CBI, CVC, Lokpal, Whistleblower, PCA', '#fff3e0'), ('Module 3', 'Governance, E-Governance, Data Protection, Emerging Tech', '#ede7f6'), ('Module 4', 'Civil Society, NGOs, SHGs, Pressure Groups, CAG', '#fce4ec'), ('Module 5', 'Regulatory Bodies, FSSAI, CCI', '#e8f5e9')]

ONLY = None
def all_chapters():
    chs = []
    for f in sorted(glob.glob('ch_*.py')):
        chs += importlib.import_module(f[:-3]).CHS
    chs.sort(key=lambda c: c['id'])
    if ONLY: chs = [c for c in chs if c['id'] in ONLY]
    for c in chs:
        c['no'] = c['id']
    return chs

def build(out):
    chs = all_chapters()
    body = ['<div class="cov"><div class="s">UPSC CSE Mains 2027 · GS Paper II</div><h1>GOVERNANCE</h1>'
            '<div class="s">Civil services · RTI · Corruption · Lokpal · E-governance · Civil society · CAG · Regulators</div>'
            '<div><span class="bx">Handwritten-style notes</span></div>'
            '<div class="t">Built from the Sarrthi IAS GS-2 Governance handouts (Modules 1-5).<br>'
            'Bracket trees · diagrams · mnemonics · PYQ tags · current affairs<br>'
            'Right column and left binding margin are kept blank for your own use.<br><br>Personal study edition · for printing</div></div>']
    toc = '<div class="partpg" style="padding:0;break-before:page"><div class="toc"><h2>INDEX</h2>'
    cur = -1
    for c in chs:
        pi = 0 if c['id'] <= 14 else 1 if c['id'] <= 19 else 2 if c['id'] <= 24 else 3 if c['id'] <= 29 else 4
        if pi != cur:
            cur = pi; l, t_, bg = PARTS[pi]; toc += '<div class="pt" style="background:%s">%s · %s</div>' % (bg, l, t_)
        toc += '<a href="#c%s">%s &nbsp;%s</a>' % (c['id'], c['no'], c.get('toc', c['title']))
    body.append(toc + '</div></div>')
    for c in chs:
        body.append(chapter_hw_ir(c))
    html = '<html><head><style>%s</style></head><body>%s</body></html>' % (hwlib.CSS + '.chap{break-before:auto;margin-top:5mm}.pyqline,.sw,.ttl{break-after:avoid}.br{orphans:3;widows:3}.br{break-inside:auto}.keep{break-inside:avoid}.keep table{font-size:9pt}.keep td{padding:.2mm 1.4mm}', ''.join(body))
    d = HTML(string=html, base_url='.').render()
    print('pages', len(d.pages))
    d.write_pdf(out)

if __name__ == '__main__':
    if len(sys.argv) > 2: ONLY = [int(x) for x in sys.argv[2].split(',')]
    build(sys.argv[1] if len(sys.argv) > 1 else 'Governance_Handwritten_Notes.pdf')
