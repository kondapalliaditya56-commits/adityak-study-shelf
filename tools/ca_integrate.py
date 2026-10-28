#!/usr/bin/env python3
"""Fold monthly current-affairs digests (ca/<mon><yy>_*.py + ca/remap_<mon><yy>.py) into Study Shelf notebooks.
Idempotent. Usage: python3 tools/ca_integrate.py sep26 [more months, oldest first]
 - <prefix>-ca-YYYY-MM.html per existing notebook (pol, pg2, gov, ir, eco, gs3, mi) with that month's items
 - 'Related current affairs' box injected into mapped chapters (marker <!--ca:YYYY-MM-->)
 - card on each notebook home linking the CA page
 - new Current Affairs notebook (ca-home, ca-ch01..06, ca-search) for subjects with no notebook
 - library.json + libdata in index.html + sw.js file list (cache bumped by caller)"""
import sys, os, re, json, glob, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
MONTHS = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
MN = ['','January','February','March','April','May','June','July','August','September','October','November','December']
NB = {  # prefix: (library id, base, home, search, template chapter, title)
 'pol': ('polity','pol-','pol-home.html','pol-search.html','pol-ch01.html','Polity'),
 'pg2': ('polity-gs2','pg2-','pg2-home.html','pg2-search.html','pg2-ch01.html','Polity (GS-2)'),
 'gov': ('governance','gov-','gov-home.html','gov-search.html','gov-ch01.html','Governance'),
 'ir':  ('international-relations','ir-','ir-home.html','ir-search.html','ir-ch01.html','International Relations'),
 'eco': ('economy','eco-','eco-home.html','eco-search.html','eco-ch01.html','Economy'),
 'gs3': ('gs3','gs3-','gs3-home.html','gs3-search.html','gs3-ch01.html','GS Paper III'),
 'mi':  ('modern-india','','home.html','search.html','ch01.html','Modern Indian History'),
}
CA_SUBJECTS = [('Society & Social Justice','Society and Social Justice','soc'),('Science & Technology','Science and Technology','st'),
 ('Environment','Environment','env'),('Art & Culture','Art and Culture','cul'),('Ethics','Ethics','eth'),('Miscellaneous','Miscellaneous','misc')]
e = lambda s: html.escape(str(s), quote=True)
def slug(i): return 'i-' + re.sub(r'[^0-9a-z]+', '-', i.lower()).strip('-')
def first_sentence(s, n=170):
    s = s.strip(); m = re.match(r'(.+?[.!?])(\s|$)', s)
    t = m.group(1) if m else s
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'
def rich(t):
    t = e(t); m = re.match(r'^([^:]{3,48}):\s(.*)$', t)
    return '<strong>%s:</strong> %s' % (m.group(1), m.group(2)) if m else t
TAGN = {'P':('Prelims','med'),'M':('Mains','med'),'PM':('Prelims + Mains','high')}

def load_month(code):
    mon, yy = code[:3], code[3:]; y = 2000 + int(yy); mo = MONTHS[mon]
    ITEMS = []
    for f in sorted(glob.glob('ca/%s_*.py' % code)): exec(open(f).read(), {'ITEMS': ITEMS})
    rp = 'ca/remap_%s.py' % code; R = {}
    if os.path.exists(rp):
        g = {}; exec(open(rp).read(), g); R = g['REMAP']
    for it in ITEMS:
        if it['id'] in R: it['nb'], it['ch'] = R[it['id']]
        it['nb'] = list(it['nb']); it['ch'] = list(it['ch'])
        for k, d in (('pts', []), ('pro', []), ('mains', []), ('kw', ''), ('pyq', ''), ('ctx', ''), ('tag', 'P')): it.setdefault(k, list(d) if isinstance(d, list) else d)
    return dict(code=code, y=y, mo=mo, ym='%d-%02d' % (y, mo), label='%s %d' % (MN[mo], y), items=ITEMS)

def split_tpl(path):
    s = open(path, encoding='utf-8').read()
    return s

def item_html(it, chtitle):
    tg = TAGN[it['tag']]
    o = ['<h2 id="%s">%s · %s<a class="anchor" href="#%s" aria-label="Link to this section">#</a></h2>' % (slug(it['id']), e(it['id']), e(it['t']), slug(it['id']))]
    o.append('<div class="pills"><span class="ptag %s">%s</span><span class="pill">%s</span></div>' % (tg[1], tg[0], e(it['sub'])))
    o.append('<p>%s</p>' % e(it['ctx']))
    if it['pts']: o.append('<ul class="lst">%s</ul>' % ''.join('<li>%s</li>' % rich(p) for p in it['pts']))
    if it['pro']: o.append('<aside class="callout shortcut"><span class="tag">Prelims fodder</span><ul class="lst">%s</ul></aside>' % ''.join('<li>%s</li>' % rich(p) for p in it['pro']))
    if it['mains'] or it['kw']:
        li = ''.join('<li>%s</li>' % rich(p) for p in it['mains'])
        if it['kw'] and not any(x.startswith('Keywords') for x in it['mains']): li += '<li><strong>Keywords:</strong> %s</li>' % e(it['kw'])
        o.append('<aside class="callout note"><span class="tag">Mains fodder</span><ul class="lst">%s</ul></aside>' % li)
    if it['pyq']: o.append('<aside class="callout"><span class="tag">PYQ connect</span><p>%s</p></aside>' % e(it['pyq']))
    if chtitle: o.append('<p class="gdesc">Read with: %s</p>' % chtitle)
    return ''.join(o)

def build_page(tpl_path, nbid, nbtitle, ch_n, title, eyebrow, lede, secs, body, cards, home, search, footer):
    s = open(tpl_path, encoding='utf-8').read()
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % e(title), s, count=1, flags=re.S)
    bar = re.search(r'<header class="bar">.*?</header>', s, re.S).group(0)
    nb = re.sub(r'<a class="nbtn"[^>]*>.*?</a>', '', bar)
    nb = re.sub(r'<span class="bartitle">.*?</span>', '<span class="bartitle"><b>CA</b> %s</span>' % e(title if len(title) < 40 else nbtitle), nb, flags=re.S)
    nb = re.sub(r'data-ch="\d+"', 'data-ch="%d"' % ch_n, nb)
    nb = re.sub(r'(<a class="home" href=")[^"]*(">Contents)', r'\g<1>%s\2' % home, nb)
    nb = re.sub(r'(<a class="home" href=")[^"]*(">Search)', r'\g<1>%s\2' % search, nb)
    s = s.replace(bar, nb, 1)
    toc = '<aside class="sidetoc"><div class="sth">On this page</div><ol>%s</ol></aside>' % ''.join('<li><a href="#%s">%s</a></li>' % (i, e(t)) for i, t in secs)
    s = re.sub(r'<aside class="sidetoc">.*?</aside>', lambda m: toc, s, count=1, flags=re.S)
    main = ('<main class="page"><div class="chead"><div class="eyebrow">%s</div><h1>%s</h1><p class="lede">%s</p></div><div class="notes">%s'
            '<h2 id="recall">Recall sheet<a class="anchor" href="#recall" aria-label="Link to this section">#</a></h2><p class="gdesc">Read once, hide it, then say what happened and why it matters.</p><ol class="recall">%s</ol></div>'
            '<nav class="pager"><a href="%s"><small>Back to</small>Contents</a></nav><footer>%s</footer></main>') % (
            e(eyebrow), e(title), e(lede), body, ''.join('<li><strong>%s</strong> %s</li>' % (e(c['q']), e(c['a'])) for c in cards), home, footer)
    s = re.sub(r'<main class="page">.*?</main>', lambda m: main, s, count=1, flags=re.S)
    s = re.sub(r'(<script type="application/json" id="data">).*?(</script>)', lambda m: m.group(1) + json.dumps({'mcq': [], 'cards': cards}, ensure_ascii=False) + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'window\.__NB=\{.*?\};', lambda m: 'window.__NB=' + json.dumps({'id': nbid, 'ch': ch_n, 'title': title}) + ';', s, count=1)
    return s

FOOT = 'Current-affairs digests built only from the Sarrthi IAS monthly current-affairs magazine in project knowledge: facts are the magazine\'s. Items marked in the notebook as related chapters are cross-links, not new theory. Copyright belongs to the publisher; keep this private.'

def cards_for(items):
    out = []
    for it in sorted(items, key=lambda x: {'PM': 0, 'M': 1, 'P': 2}[x['tag']])[:24]:
        out.append({'q': '%s: what happened and why does it matter?' % it['t'], 'a': first_sentence(it['ctx'], 220)})
    return out

def chap_title(cid, lib):
    m = re.match(r'^(?:([a-z0-9]+)-)?ch(\d+)$', cid)
    if not m: return None, None
    pre, n = m.group(1) or 'mi', int(m.group(2))
    for pfx, v in NB.items():
        if pfx == pre:
            for l in lib:
                if l['id'] == v[0]:
                    for c in l['chapters']:
                        fn = v[1] + 'ch%02d.html' % n
                        if c['n'] == n and os.path.exists(fn): return fn, c['title']
    return None, None

def main(codes):
    lib = json.load(open('library.json'))
    months = [load_month(c) for c in codes]
    # per-notebook CA pages and chapter boxes
    report = []
    for pfx, (nbid, base, home, search, tplf, nbt) in NB.items():
        for M in months:
            its = [i for i in M['items'] if pfx in i['nb'] and (pfx != 'mi' or any(c.startswith('mi-') for c in i['ch']))]
            if not its: continue
            fn = '%s-ca-%s.html' % (pfx, M['ym'])
            body = []; secs = []
            for i in its:
                links = []
                for c in i['ch']:
                    c2 = c.replace('mi-ch', 'ch') if c.startswith('mi-') else c
                    f, t = chap_title(c2, lib)
                    if f and (c2.startswith(base) or (pfx == 'mi' and c.startswith('mi-'))):
                        links.append('<a href="%s">%s</a>' % (f, e(t)))
                body.append(item_html(i, ' · '.join(links))); secs.append((slug(i['id']), '%s · %s' % (i['id'], i['t'])))
            secs.append(('recall', 'Recall sheet'))
            page = build_page(tplf, nbid, nbt, 900 + M['mo'] if False else 900, '%s: current affairs, %s' % (nbt, M['label']),
                              'Current affairs · %s · %s' % (M['label'], nbt),
                              '%d items from the Sarrthi IAS %s current affairs that belong to %s. Each has the magazine\'s context, key points, prelims and mains fodder and PYQ links.' % (len(its), M['label'], nbt),
                              secs, ''.join(body), cards_for(its), home, search, FOOT)
            open(fn, 'w', encoding='utf-8').write(page)
            # home card
            hp = open(home, encoding='utf-8').read()
            hp = re.sub(r'<!--ca-card:%s-->.*?<!--/ca-card-->' % M['ym'], '', hp, flags=re.S)
            card = ('<!--ca-card:%s--><a class="hwcard" href="%s" style="display:flex;align-items:center;gap:12px;margin:10px 0 4px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--surface);text-decoration:none;color:inherit;font-family:var(--sans)">'
                    '<span style="font-size:24px" aria-hidden="true">&#128240;</span><span style="flex:1"><b style="display:block;font-size:16px">Current affairs: %s</b><small style="color:var(--muted)">%d items mapped to this notebook</small></span><span style="font-weight:700;color:var(--accent)">Open &rsaquo;</span></a><!--/ca-card-->') % (M['ym'], fn, M['label'], len(its))
            if '<p class="prog">' in hp: hp = hp.replace('<p class="prog">', card + '<p class="prog">', 1)
            else: hp = hp.replace('</h1>', '</h1>' + card, 1)
            open(home, 'w', encoding='utf-8').write(hp)
            report.append((fn, len(its)))
    # chapter boxes
    boxes = {}
    for M in months:
        for it in M['items']:
            for c in it['ch']:
                c2 = c.replace('mi-ch', 'ch') if c.startswith('mi-') else c
                f, t = chap_title(c2, lib)
                if not f: report.append(('MISSING CHAPTER %s for %s' % (c, it['id']), 0)); continue
                pfx = 'mi' if c.startswith('mi-') else c.split('-')[0]
                if pfx not in NB: continue
                boxes.setdefault((f, M['ym'], M['label']), []).append((it, pfx))
    done_files = set()
    for (f, ym, label), lst in boxes.items():
        s = open(f, encoding='utf-8').read()
        s = re.sub(r'(<section class="cabox">)?<!--ca:%s-->.*?<!--/ca-->(</section>)?' % ym, '', s, flags=re.S)
        s = s.replace('<section class="cabox"></section>', '')
        li = ''
        for it, pfx in lst:
            tgt = '%s-ca-%s.html' % (pfx, ym) if pfx in NB and any(pfx in x['nb'] for x in [it]) else 'ca-ch01.html'
            if pfx != 'mi' and pfx not in it['nb']: pfx2 = pfx
            li += '<li><a href="%s#%s"><strong>%s</strong></a>: %s</li>' % (tgt, slug(it['id']), e(it['t']), e(first_sentence(it['ctx'], 150)))
        box = '<!--ca:%s--><aside class="callout live"><span class="tag">Current affairs · %s</span><ul class="lst">%s</ul></aside><!--/ca-->' % (ym, label, li)
        if '<h2 id="recall"' in s: s = s.replace('<h2 id="recall"', box + '<h2 id="recall"', 1)
        elif '<nav class="pager">' in s: s = s.replace('<nav class="pager">', '<section class="cabox">' + box + '</section><nav class="pager">', 1)
        else: report.append(('no insertion point in ' + f, 0)); continue
        open(f, 'w', encoding='utf-8').write(s); done_files.add(f)
    # Current Affairs notebook
    subj_items = {}
    for M in months:
        for it in M['items']:
            for key, nm, short in CA_SUBJECTS:
                if it['sub'] == key: subj_items.setdefault(key, []).append((M, it))
    chap_entries = []
    homeCards = []
    for n, (key, nm, short) in enumerate(CA_SUBJECTS, 1):
        pairs = subj_items.get(key, [])
        if not pairs: continue
        fn = 'ca-ch%02d.html' % n
        body = []; secs = []; allits = []
        for M in reversed(months):
            its = [i for (m, i) in pairs if m is M]
            if not its: continue
            body.append('<h2 id="m-%s">%s<a class="anchor" href="#m-%s" aria-label="Link to this section">#</a></h2>' % (M['ym'], e(M['label']), M['ym']))
            secs.append(('m-' + M['ym'], M['label']))
            for i in its:
                links = []
                for c in i['ch']:
                    c2 = c.replace('mi-ch', 'ch') if c.startswith('mi-') else c
                    f, t = chap_title(c2, lib)
                    if f: links.append('<a href="%s">%s</a>' % (f, e(t)))
                body.append(item_html(i, ' · '.join(links))); secs.append((slug(i['id']), '%s · %s' % (i['id'], i['t']))); allits.append(i)
        secs.append(('recall', 'Recall sheet'))
        page = build_page('pg2-ch01.html', 'current-affairs', 'Current Affairs', n, 'Current affairs: ' + nm, 'Current affairs · ' + nm,
                          '%d items on %s from the Sarrthi IAS monthly current-affairs magazine, newest month first.' % (len(allits), nm.lower()),
                          secs, ''.join(body), cards_for(allits), 'ca-home.html', 'ca-search.html', FOOT)
        open(fn, 'w', encoding='utf-8').write(page)
        chap_entries.append({'n': n, 'title': nm, 'sub': '%d items' % len(allits), 'badge': '', 'slides': False, 'pending': False,
                             'secs': [{'id': i, 't': t} for i, t in secs]})
        homeCards.append('<a class="chcard" href="%s" data-ch="%d" data-secs="%d"><span class="chn">%d</span><span class="cht"><b>%s</b><small>%d items</small><span class="cbar"><i></i></span></span><span class="chb"><i class="tick" hidden>Done</i><em>Monthly</em></span></a>' % (fn, n, len(secs), n, e(nm), len(allits)))
    # home
    pg = open('pg2-home.html', encoding='utf-8').read()
    head = pg[:pg.index('<main')]; tail = pg[pg.index('</main>'):]
    head = re.sub(r'<title>.*?</title>', '<title>Current Affairs notebook</title>', head, count=1, flags=re.S)
    head = re.sub(r'<header class="bar">.*?</header>', '<header class="bar"><div class="barin"><a class="home" href="index.html">Library</a><a class="home" href="ca-home.html">Contents</a><span class="bartitle"><b></b> Current Affairs notebook</span><a class="home" href="ca-search.html">Search</a><button class="themebtn" id="themebtn" type="button" aria-label="Change theme">Theme</button></div></header>', head, flags=re.S)
    mainh = ('<main class="page home-page"><div class="chead"><div class="eyebrow">Sarrthi IAS · monthly current affairs</div><h1>Current Affairs</h1><p class="lede">Subjects that have no notebook of their own: society and social justice, science and technology, environment, art and culture, ethics and miscellaneous. Polity, governance, IR, economy, security and agriculture items sit inside those notebooks; this notebook holds the rest.</p>'
             '<a class="hwcard" href="pdfview.html?s=current-affairs" style="display:flex;align-items:center;gap:12px;margin:14px 0 4px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--surface);text-decoration:none;color:inherit;font-family:var(--sans)"><span style="font-size:26px" aria-hidden="true">&#9998;</span><span style="flex:1"><b style="display:block;font-size:16px">Handwritten notes (PDF)</b><small id="hwmeta" style="color:var(--muted)">Opens the latest version in the PDF viewer</small></span><span style="font-weight:700;color:var(--accent)">Open &rsaquo;</span></a><script>fetch("notes/current-affairs/manifest.json",{cache:"no-store"}).then(function(r){return r.json()}).then(function(m){var v=m.versions[0],e=document.getElementById("hwmeta");if(e)e.textContent="Latest: version "+v.v+" \\u00b7 "+v.pages+" pages \\u00b7 "+v.date}).catch(function(){})</script><p class="prog"><span id="progress"></span> of %d chapters marked done.</p><div class="row"><a class="btn pri" href="ca-ch01.html">Start</a><a class="btn" href="ca-search.html">Search</a></div></div><section class="part"><h2>Subjects</h2><div class="chlist">%s</div></section>'
             '<footer>%s</footer>') % (len(chap_entries), ''.join(homeCards), FOOT)
    tail = tail.replace('</main>', '</main>', 1)
    open('ca-home.html', 'w', encoding='utf-8').write(head + mainh + tail)
    # search page (client-side over all CA items)
    idx = []
    for M in months:
        for it in M['items']:
            f = None
            for n, (key, nm, short) in enumerate(CA_SUBJECTS, 1):
                if it['sub'] == key: f = 'ca-ch%02d.html' % n
            if not f:
                for p in ['pol','pg2','gov','ir','eco','gs3']:
                    if p in it['nb']: f = '%s-ca-%s.html' % (p, M['ym']); break
            if not f: continue
            idx.append({'id': it['id'], 'm': M['label'], 'sub': it['sub'], 't': it['t'], 'u': f + '#' + slug(it['id']),
                        'x': ' '.join([it['ctx']] + it['pts'] + it['pro'] + it['mains'] + [it['kw'], it['pyq']])})
    sp = build_page('pg2-ch01.html', 'current-affairs', 'Current Affairs', 99, 'Search current affairs', 'Current affairs · Search',
                    'Type a word to find items from every month and subject in the current-affairs digests.', [('q', 'Search')],
                    '<h2 id="q">Search<a class="anchor" href="#q" aria-label="Link to this section">#</a></h2><input id="cq" type="search" placeholder="Search e.g. BRICS, FATF, tiger reserve" style="width:100%;font:16px var(--sans);padding:12px;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink)"><div id="cres"></div>'
                    '<script>(function(){var D=@@IDX@@;var q=document.getElementById("cq"),r=document.getElementById("cres");function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;","\\"":"&quot;"}[c]})}'
                    'function run(){var w=q.value.toLowerCase().split(/\\s+/).filter(Boolean);if(!w.length){r.innerHTML="<p class=\\"gdesc\\">"+D.length+" items indexed.</p>";return}var out=D.filter(function(d){var h=(d.t+" "+d.sub+" "+d.x).toLowerCase();return w.every(function(k){return h.indexOf(k)>=0})}).slice(0,40);'
                    'r.innerHTML=out.length?out.map(function(d){return "<p><a href=\\""+d.u+"\\"><strong>"+esc(d.id+" · "+d.t)+"</strong></a><br><small>"+esc(d.m+" · "+d.sub)+"</small></p>"}).join(""):"<p>No match.</p>"}q.addEventListener("input",run);run()})();</script>'.replace('@@IDX@@', json.dumps(idx, ensure_ascii=False).replace('</', '<\\/')),
                    [], 'ca-home.html', 'ca-search.html', FOOT)
    sp = re.sub(r'<h2 id="recall".*?</ol>', '', sp, flags=re.S)
    open('ca-search.html', 'w', encoding='utf-8').write(sp)
    # library.json + libdata
    lib = [l for l in lib if l['id'] != 'current-affairs']
    lib.append({'id': 'current-affairs', 'title': 'Current Affairs', 'sub': 'Monthly Sarrthi IAS current affairs for subjects without their own notebook', 'base': 'ca-', 'home': 'home.html', 'search': 'search.html',
                'chapters': chap_entries, 'group': 'Current Affairs'})
    json.dump(lib, open('library.json', 'w'), ensure_ascii=False)
    s = open('index.html', encoding='utf-8').read()
    s = re.sub(r'(<script type="application/json" id="libdata">).*?(</script>)', lambda m: m.group(1) + json.dumps(lib, ensure_ascii=False) + m.group(2), s, count=1, flags=re.S)
    open('index.html', 'w', encoding='utf-8').write(s)
    # sw.js
    sw = open('sw.js', encoding='utf-8').read()
    m = re.search(r'const FILES=(\[.*?\]);', sw, re.S); files = json.loads(m.group(1))
    new = sorted(set(f for f in glob.glob('*-ca-*.html')) | set(glob.glob('ca-*.html')))
    files = sorted(set(files) | set(new) | set(f for f in ['notes/current-affairs/manifest.json'] if os.path.exists(f)))
    sw = sw.replace(m.group(0), 'const FILES=' + json.dumps(files) + ';', 1)
    open('sw.js', 'w', encoding='utf-8').write(sw)
    for r in report: print(*r)
    print('boxes in', len(done_files), 'chapter files')

if __name__ == '__main__':
    main(sys.argv[1:])
