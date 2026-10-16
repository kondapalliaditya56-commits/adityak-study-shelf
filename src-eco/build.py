import json, re, os, shutil
from lib import *
import importlib
MODS=[]
for i in range(14):
    try: MODS.append(importlib.import_module('ch%d'%i))
    except ModuleNotFoundError: pass

OUT = 'out'
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT + '/img')
chs = [m.c for m in MODS]
for f in os.listdir('img'):
    if f.startswith('eco-'):
        shutil.copy('img/' + f, OUT + '/img/' + f)

def name(n): return '%sch%02d.html' % (PFX, n)

written = [c for c in chs]
for i, c in enumerate(chs):
    prev = (chs[i-1].n, chs[i-1].title) if i > 0 else None
    nxt = (chs[i+1].n, chs[i+1].title) if i + 1 < len(chs) else None
    open(OUT + '/' + name(c.n), 'w').write(chap_page(c, prev, nxt, len(chs)))

summ = {
 0: 'Box colours, how to study, which handout feeds which chapter, and the priority map.',
 1: 'Poverty: well-being, why and how it is measured, the poverty line committees, India\'s progress, World Bank lines and PPP, global and National MPI with the worked example, and depth and severity (PGI, SPG).',
 2: 'Inequality: Kuznets, Lorenz and Gini (with four shortcomings), why inequality exists (natural, Marx, modern, rule of law), and trickle-down versus inclusive growth.'}

CSS = STYLE
def shell(title, bar_title, body, js=''):
    bar = '<header class="bar"><div class="barin"><a class="home" href="index.html">Library</a><a class="home" href="%shome.html">Contents</a><span class="bartitle">%s</span><a class="home" href="%ssearch.html">Search</a><a class="home" href="%stimeline.html">Timeline</a><button class="themebtn" id="themebtn" type="button" aria-label="Change theme">Theme</button></div></header>' % (PFX, bar_title, PFX, PFX)
    return HEAD.replace('@@T@@', esc(title)) + '<body>' + bar + body + '<script>' + STORE_JS + js + '</script><script src="hl.js" defer></script></body></html>'

# ---- home
cards = ''
for c in chs:
    n = len(all_sections(c))
    badge = 'Start here' if c.n == 0 else 'Handout only'
    cards += '<a class="chcard" href="%s" data-ch="%d" data-secs="%d"><span class="chn">%d</span><span class="cht"><b>%s</b><small>%s</small></span><span class="chb"><i class="tick" hidden>Done</i><em>%s</em></span></a>' % (name(c.n), c.n, n, c.n, esc(c.title), esc((getattr(c,'summary',None) or summ.get(c.n,''))), badge)
ALL = {1:'Poverty',2:'Inequality',3:'Unemployment',4:'Basic Concepts of Economics',5:'National Income Accounting',6:'Inflation',7:'Banking and NBFCs',8:'Money and Monetary Policy',9:'Capital Markets',10:'External Sector and Balance of Payments',11:'GST',12:'Government Budgeting and Fiscal Policy',13:'NABARD, NBFCs, Chit Funds and Ponzi Schemes'}
PARTS = [('Part 1 · Poverty, inequality and employment',[1,2,3]),('Part 2 · Concepts and national income',[4,5]),('Part 3 · Prices, money and finance',[6,7,8,9]),('Part 4 · External sector, GST and the budget',[10,11,12]),('Part 5 · Rural and climate finance',[13])]
byn = {c.n:c for c in chs}
def card(c):
    n = len(all_sections(c))
    badge = 'Start here' if c.n == 0 else 'Handout only'
    return '<a class="chcard" href="%s" data-ch="%d" data-secs="%d"><span class="chn">%d</span><span class="cht"><b>%s</b><small>%s</small><span class="cbar"><i></i></span></span><span class="chb"><i class="tick" hidden>Done</i><em>%s</em></span></a>' % (name(c.n), c.n, n, c.n, esc(c.title), esc(getattr(c,'summary',None) or summ.get(c.n,'')), badge)
parts_html = ''
for ptitle, ns in PARTS:
    cl = ''
    for n in ns:
        cl += card(byn[n]) if n in byn else '<div class="chcard pending"><span class="chn">%d</span><span class="cht"><b>%s</b><small>Coming</small></span></div>' % (n, esc(ALL[n]))
    parts_html += '<section class="part"><h2>%s</h2><div class="chlist">%s</div></section>' % (esc(ptitle), cl)
nw = len([c for c in chs if c.n > 0]); npend = 13 - nw
home_body = '<main class="page home-page"><div class="chead"><div class="eyebrow">Sarrthi IAS · GS Foundation · Aditya Kalia</div><h1>Economy</h1><p class="lede">Your personal Economy notebook. Each chapter keeps the handout facts and adds an exam lens, tables, redrawn flows, timelines, recall sheets, quizzes and flashcards. Handout only, nothing added from outside.</p><p class="prog"><span id="progress"></span> of %d written chapters marked done.%s</p><div class="row"><a class="btn pri" href="%sch00.html">Start here</a><a class="btn" href="%ssearch.html">Search</a><a class="btn" href="%stimeline.html">Master timeline</a><a class="btn" href="%spyq.html">PYQ bank</a></div></div><section class="part"><h2>How to read</h2><div class="chlist">%s</div></section>%s</main>' % (nw, (' %d more on the way.' % npend) if npend else '', PFX, PFX, PFX, PFX, card(byn[0]), parts_html)
home_js = r'''
(function(){var S=NBS;function upd(){var done=0;document.querySelectorAll('a.chcard[data-ch]').forEach(function(a){var n=+a.dataset.ch,t=+a.dataset.secs,p=S.pct('economy',n,t),rec=(S.get().nb.economy||{})[n],d=rec&&rec.dt?!!rec.done:p>=.999;var bar=a.querySelector('.cbar i');if(bar)bar.style.width=Math.round(p*100)+'%';var tk=a.querySelector('.tick');if(tk)tk.hidden=!d;if(d&&n>0)done++});var el=document.getElementById('progress');if(el)el.textContent=done}upd();S.onChange(upd);setTimeout(upd,2500)})();
'''
# add progress bars to cards
open(OUT + '/%shome.html' % PFX, 'w').write(shell('Economy notebook', '<b></b> Economy notebook', home_body, home_js))

# ---- search
idx = []
for c in chs:
    for s in c.secs:
        txt = re.sub(r'\s+', ' ', ' '.join(s['plain']))
        idx.append({'ch': c.n, 'cht': c.title, 'id': s['id'], 't': re.sub(r'<[^>]+>', '', s['title']), 'x': txt})
    if c.n > 0 and (chapter_pyqs(c)[0] or chapter_pyqs(c)[1]):
        idx.append({'ch': c.n, 'cht': c.title, 'id': 'pyq', 't': 'Past-year questions', 'x': pyq_plain(c)})
idx.append({'ch': 0, 'cht': 'PYQ bank', 'id': '', 't': 'PYQ bank: topics outside the 13 chapters', 'x': bank_plain(), 'href': PFX + 'pyq.html'})
sdata = json.dumps(idx, ensure_ascii=False).replace('</', '<\\/')
search_body = '<main class="page"><div class="chead"><div class="eyebrow">Economy notebook</div><h1>Search</h1><p class="lede">Search every section of the written chapters.</p></div><input class="sbox" id="q" type="search" placeholder="Try: Tendulkar, Gini, PPP, MPI, trickle-down" autocomplete="off"><div class="count" id="cnt"></div><div class="results" id="res"></div></main><script type="application/json" id="idx">' + sdata + '</script>'
search_js = r'''
(function(){var D=JSON.parse(document.getElementById('idx').textContent),q=document.getElementById('q'),res=document.getElementById('res'),cnt=document.getElementById('cnt');
function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function run(){var v=q.value.trim().toLowerCase();res.innerHTML='';if(v.length<2){cnt.textContent='';return}
var ws=v.split(/\s+/),out=[];D.forEach(function(d){var t=(d.t+' '+d.x).toLowerCase(),ok=ws.every(function(w){return t.indexOf(w)>=0});if(!ok)return;var i=t.indexOf(ws[0]),sn=(d.t+'. '+d.x),j=Math.max(0,sn.toLowerCase().indexOf(ws[0])-60);out.push({d:d,sn:sn.substr(j,200)})});
cnt.textContent=out.length+' section'+(out.length===1?'':'s');
out.slice(0,40).forEach(function(o){var h=document.createElement('div');h.className='hit';var s=esc(o.sn);ws.forEach(function(w){s=s.replace(new RegExp('('+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>')});h.innerHTML='<a href="'+(o.d.href||('eco-ch'+(o.d.ch<10?'0':'')+o.d.ch+'.html#'+o.d.id))+'">'+(o.d.ch?('Ch '+o.d.ch+' · '):'')+esc(o.d.t)+'</a><br><small>'+esc(o.d.cht)+'</small><br>'+s+'…';res.appendChild(h)})}
q.addEventListener('input',run);var p=new URLSearchParams(location.search).get('q');if(p){q.value=p;run()}})();
'''
open(OUT + '/%ssearch.html' % PFX, 'w').write(shell('Economy search', '<b></b> Search', search_body, search_js))

# ---- timeline
items = []
for c in chs:
    for lab, txt, star in c.timeline:
        items.append((c.n, lab, txt, star))
def key(it):
    m = re.search(r'(\d{4})', it[1])
    return (int(m.group(1)) if m else 9999, it[0])
items.sort(key=key)
SHORT={1:'Poverty',2:'Inequality',3:'Unemployment',4:'Basic concepts',5:'National income',6:'Inflation',7:'Banking',8:'Money',9:'Capital markets',10:'External',11:'GST',12:'Budget',13:'NABARD'}
tl = '<div class="chips" id="chips" style="flex-wrap:wrap"><button class="chip on" data-f="0" type="button">All</button>' + ''.join('<button class="chip" data-f="%d" type="button">Ch %d %s</button>' % (c.n, c.n, SHORT.get(c.n,'')) for c in chs if c.timeline) + '<button class="chip" data-f="s" type="button">★ High-yield</button></div><ol class="timeline">'
for n, lab, txt, star in items:
    tl += '<li class="tl %s" data-ch="%d"><time class="yr">%s</time><span class="pin"></span><div class="tlbody">%s%s <a class="sref" href="%s#chapter-timeline">Ch %d</a></div></li>' % ('high' if star else '', n, esc(lab), md(txt), '<span class="star">★</span>' if star else '', name(n), n)
tl += '</ol>'
tl_body = '<main class="page"><div class="chead"><div class="eyebrow">Economy notebook</div><h1>Master timeline</h1><p class="lede">Dated entries and number checkpoints from the written chapters.</p></div>' + tl + '</main>'
tl_js = r'''
(function(){var ch=document.querySelectorAll('.chip');ch.forEach(function(b){b.addEventListener('click',function(){ch.forEach(function(x){x.classList.toggle('on',x===b)});var f=b.dataset.f;document.querySelectorAll('.tl').forEach(function(li){li.hidden=!(f==='0'||(f==='s'?li.classList.contains('high'):li.dataset.ch===f))})})})})();
'''
open(OUT + '/%stimeline.html' % PFX, 'w').write(shell('Economy timeline', '<b></b> Timeline', tl_body, tl_js))

# ---- PYQ bank page
open(OUT + '/%spyq.html' % PFX, 'w').write(shell('Economy PYQ bank', '<b></b> PYQ bank', bank_body({c.n: c.title for c in chs}), ''))

# ---- libdata entry
lib = {'id': 'economy', 'title': 'Economy (GS Foundation)', 'sub': 'Sarrthi IAS handouts by Aditya Kalia', 'base': PFX, 'home': 'home.html', 'search': 'search.html', 'timeline': 'timeline.html', 'chapters': []}
for c in chs:
    lib['chapters'].append({'n': c.n, 'title': c.title, 'slides': False, 'pending': False, 'secs': [{'id': s['id'], 't': re.sub(r'<[^>]+>', '', s['title'])} for s in all_sections(c)]})
for n in range(1,14):
    if n not in byn:
        lib['chapters'].append({'n': n, 'title': ALL[n], 'slides': False, 'pending': True, 'secs': []})
lib['chapters'].sort(key=lambda x:x['n'])
json.dump(lib, open(OUT + '/lib_entry.json', 'w'), ensure_ascii=False)
print('built', os.listdir(OUT))
