#!/usr/bin/env python3
"""Handwritten-style current-affairs addenda. Usage: python3 tools/ca_handwritten.py sep26 [...]
Builds one addendum PDF per handwritten subject (A4, 19mm binding, 42mm blank right column), appends it to the subject's latest
version and publishes it as the next version (tools/publish_notes.py). Subjects without a handwritten set go to notes/current-affairs."""
import sys, os, re, json, html, subprocess, shutil, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, os.path.join(ROOT, 'src-gov', 'handnotes'))
os.chdir(ROOT)
import ca_integrate as ci
import hwlib
from hwlib import B, S, box, pg, P, H
from weasyprint import HTML
e = ci.e
TARGETS = [  # (subject id, title, nb prefixes, root pdf or None)
 ('governance', 'Governance', ['gov'], 'Governance-Handwritten-Notes-Print.pdf'),
 ('gs3', 'GS Paper III', ['gs3'], 'GS3-Handwritten-Notes-Print.pdf'),
 ('international-relations', 'International Relations', ['ir'], 'IR-Handwritten-Notes-Print.pdf'),
 ('polity-gs2', 'Polity', ['pol', 'pg2'], 'Polity-Handwritten-Notes-Print.pdf'),
 ('current-affairs', 'Current Affairs', ['ca', 'eco', 'mi'], None),
]
def item_pg(it):
    tg = {'P': 'PRELIMS', 'M': 'MAINS', 'PM': 'PRELIMS + MAINS'}[it['tag']]
    o = [S('%s &nbsp;%s' % (e(it['id']), e(it['t'])), 'r' if it['tag'] == 'PM' else 'b' if it['tag'] == 'M' else 'g').replace('class="sub', 'id="%s" class="sub' % ci.slug(it['id'])),
         '<span class="pyq">%s</span>' % tg]
    o.append(box('ye', '<b>What:</b> %s' % e(it['ctx'])))
    heads, plain = [], []
    for p in it['pts']:
        m = re.match(r'^([^:]{3,30}):\s(.*)$', p)
        (heads if m else plain).append((m.group(1), m.group(2)) if m else p)
    for h, t in heads: o.append(B(e(h), [e(t)]))
    if plain: o.append(B('POINTS', [e(t) for t in plain]))
    if it['pro']: o.append(box('gr', '<b>PRELIMS FODDER</b><br>' + '<br>'.join('&bull; ' + e(t) for t in it['pro'])))
    mm = list(it['mains'])
    if it['kw'] and not any(x.startswith('Keywords') for x in mm): mm.append('Keywords: ' + it['kw'])
    if mm: o.append(box('bl', '<b>MAINS FODDER</b><br>' + '<br>'.join('&bull; ' + e(t) for t in mm)))
    if it['pyq']: o.append(box('pk', '<b>PYQ:</b> ' + e(it['pyq'])))
    return ''.join(o)

def build(months, sid, title, prefixes, out):
    sec = []
    for M in months:
        its = [i for i in M['items'] if any(p in i['nb'] for p in prefixes)]
        if its: sec.append((M, its))
    if not sec: return None
    n = sum(len(x[1]) for x in sec)
    label = ' + '.join(M['label'] for M, _ in sec)
    toc = ''
    body = ''
    for M, its in sec:
        toc += '<div class="pt" style="background:#fff9c4">%s</div>' % e(M['label'])
        for i in its:
            toc += '<a href="#%s">%s &nbsp;%s</a>' % (ci.slug(i['id']), e(i['id']), e(i['t']))
        body += '<div class="partpg" style="padding-top:60mm"><h1>%s</h1><div class="s">%s</div></div>' % (e(M['label']), e(title))
        for i in its: body += '<div class="chap">' + item_pg(i) + '</div>'
    cover = ('<div class="cov"><h1>CURRENT AFFAIRS</h1><div class="s">%s &middot; %s</div><div class="bx">%d items</div><div class="t">Built only from the Sarrthi IAS monthly current-affairs magazine.<br>Red tag = Prelims + Mains, blue = Mains, green = Prelims.<br>Right-hand column is blank for your own notes.</div></div>' % (e(title), e(label), n))
    doc = '<html><head><meta charset="utf-8"><style>%s@page{@bottom-right{content:"%s" counter(page)}}.chap{break-before:auto}.chap+.chap{margin-top:3mm}.partpg{break-after:page}</style></head><body>%s<div class="pg"></div><div class="toc"><h2>Index</h2>%s</div>%s</body></html>' % (
        hwlib.CSS, ('Current Affairs · ' if title != 'Current Affairs' else '') + 'Current Affairs · ' if False else (e(title) + ' · Current Affairs · ' if title != 'Current Affairs' else 'Current Affairs · '), cover, toc, body)
    HTML(string=doc, base_url=ROOT).write_pdf(out)
    return n

def main(codes):
    months = [ci.load_month(c) for c in codes]
    os.makedirs('/tmp/ca_hw', exist_ok=True)
    for sid, title, prefixes, rootpdf in TARGETS:
        add = '/tmp/ca_hw/%s_add.pdf' % sid
        n = build(months, sid, title, prefixes, add)
        if not n: print('skip', sid); continue
        mp = 'notes/%s/manifest.json' % sid
        final = '/tmp/ca_hw/%s_final.pdf' % sid
        if os.path.exists(mp):
            m = json.load(open(mp)); cur = 'notes/%s/%s' % (sid, m['versions'][0]['file'])
            base_pdf = '/tmp/ca_hw/%s_base.pdf' % sid
            # strip a previous addendum for the same month set: version note marks it
            shutil.copy(cur, base_pdf)
            subprocess.run(['qpdf', '--empty', '--pages', base_pdf, add, '--', final], check=True)
        else:
            shutil.copy(add, final)
        opt = final + '.opt.pdf'
        subprocess.run(['qpdf', '--object-streams=generate', '--compress-streams=y', '--recompress-flate', '--compression-level=9', final, opt], check=True); shutil.move(opt, final)
        note = 'Current affairs addendum: %s (%d items)' % (', '.join(M['label'] for M in months), n)
        cmd = ['python3', 'tools/publish_notes.py', sid, final, note]
        if sid == 'current-affairs': cmd += ['--title', 'Current Affairs handwritten notes']
        subprocess.run(cmd, check=True)
        if rootpdf: shutil.copy(final, rootpdf)
        print(sid, n, 'items', subprocess.run(['pdfinfo', final], capture_output=True, text=True).stdout.split('Pages:')[1].split()[0], 'pages')

if __name__ == '__main__': main(sys.argv[1:])
