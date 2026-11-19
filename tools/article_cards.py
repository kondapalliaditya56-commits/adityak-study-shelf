#!/usr/bin/env python3
"""Embed the enriched 'Today's 5 articles' data (about, key clauses, amendments, Supreme Court cases, mnemonics) into index.html.
usage: python3 tools/article_cards.py data/article_cards.json   (idempotent: replaces the artx block, CSS and renderer)"""
import sys, os, re, json
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(sys.argv[1], encoding='utf8'))
p = os.path.join(root, 'index.html'); s = open(p, encoding='utf8').read()
CSS = """/*artx-css*/.hwm+.ab{margin-top:2px}.ab{font:400 14px/1.55 var(--sans);color:var(--ink);background:var(--acc-soft);border-radius:10px;padding:8px 10px}.ab b{color:var(--acc)}
.sub2{display:grid;gap:4px}.sub2 h5,.amd h5{margin:0;font:700 11px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.cl{display:grid;grid-template-columns:auto 1fr;gap:8px;font:400 13.5px/1.5 var(--sans);align-items:baseline}.cl code{font:700 12.5px ui-monospace,Menlo,monospace;background:var(--surface2);border:1px solid var(--line);border-radius:6px;padding:0 6px;white-space:nowrap;color:var(--acc)}
.amd{display:grid;gap:4px;border-left:3px solid var(--blue);padding-left:8px}.am{font:400 13.5px/1.5 var(--sans)}.am b.n{color:var(--blue)}
.cs{border:1px solid var(--line);border-radius:10px;padding:0;margin:0}.cs>summary{cursor:pointer;list-style:none;padding:8px 10px;font:700 13.5px var(--sans);color:var(--acc);display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.cs>summary::-webkit-details-marker{display:none}.cs>summary:before{content:'\\25B8'}.cs[open]>summary:before{content:'\\25BE'}.cs .cn{font:600 12px var(--sans);color:var(--muted);margin-left:auto}
.kc{border-top:1px dashed var(--line);padding:8px 10px;display:grid;gap:3px}.kc h4{margin:0;font:700 14.5px/1.35 var(--serif,Georgia,serif);color:var(--ink)}.kc h4 span{font:600 12px var(--sans);color:var(--saf);margin-left:6px}
.kr{display:grid;grid-template-columns:78px 1fr;gap:6px;font:400 13.5px/1.5 var(--sans)}.kr i{font-style:normal;font:700 11px/1.9 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.kr.h i{color:var(--good)}.kr.h div{background:var(--good-soft);border-radius:6px;padding:2px 6px}.kx{font:italic 400 12.5px/1.45 var(--sans);color:var(--saf)}
.pq{display:inline-block;font:700 11px var(--sans);background:var(--red-soft);color:var(--red);border-radius:99px;padding:2px 8px}
.mnl{border-top:1px dashed var(--line);padding:8px 10px}.mnl b.t{display:block;font:700 11px var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}.mnl ul{margin:0;padding-left:18px;font:400 13px/1.5 var(--sans)}.mnl li{margin:2px 0}
.nc{font:400 13px/1.5 var(--sans);color:var(--muted);border-left:3px solid var(--line);padding:2px 8px}.nl{font:600 12.5px var(--sans)}
.mnb{border:1.5px dashed var(--saf);background:var(--saf-soft);border-radius:10px;padding:7px 10px;display:grid;gap:5px}.mnb .mw{font:800 15px/1.35 var(--serif,Georgia,serif);color:var(--saf)}.mnb .mx{font:400 13px/1.5 var(--sans);color:var(--ink)}
.mnb .ms{font:700 10.5px var(--sans);letter-spacing:.05em;text-transform:uppercase;border-radius:99px;padding:1px 7px;display:inline-block;margin-left:4px;vertical-align:2px}.ms.new{background:var(--blue-soft);color:var(--blue)}.ms.old{background:var(--good-soft);color:var(--good)}
.mnb .mi+.mi{border-top:1px dotted var(--saf);padding-top:5px}#h-art.hwg{grid-template-columns:repeat(auto-fill,minmax(min(100%,420px),1fr))}
@media (max-width:520px){.kr{grid-template-columns:1fr;gap:0}}/*/artx-css*/"""
s = re.sub(r'/\*artx-css\*/.*?/\*/artx-css\*/', '', s, flags=re.S)
s = s.replace('</style>', CSS + '</style>', 1)
blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
s = re.sub(r'<script type="application/json" id="artx">.*?</script>', '', s, flags=re.S)
s = s.replace('<script type="application/json" id="artdata">', '<script type="application/json" id="artx">' + blob + '</script><script type="application/json" id="artdata">', 1)
JS = r"""function arHtml(x,d,j){
  var on=((H.art[d]||{})[j]||0)>0,e=AX[x.n]||{},h;
  var t=esc(x.t).replace(/\*\*(.+?)\*\*/g,'<mark>$1</mark>');
  h='<div class="hw'+(on?' on':'')+'"><div class="hwt"><b>Art. '+esc(x.n)+'</b><span class="pill L">Part '+esc(x.p)+'</span>'+(e.pyq?'<span class="pq">PYQ</span>':'')+'</div><div class="hwm">'+t+'</div>';
  if(e.about)h+='<div class="ab"><b>What it says.</b> '+e.about+'</div>';
  if(e.clauses&&e.clauses.length){h+='<div class="sub2"><h5>Key clauses to read</h5>';e.clauses.forEach(function(c){h+='<div class="cl"><code>'+c[0]+'</code><div>'+c[1]+'</div></div>'});h+='</div>'}
  if(e.amend&&e.amend.length){h+='<div class="amd"><h5>Amendments</h5>';e.amend.forEach(function(c){h+='<div class="am"><b class="n">'+c[0]+'</b>: '+c[1]+'</div>'});h+='</div>'}
  h+='<div class="hwe" style="font-style:normal;color:var(--ink)"><b>Why it matters.</b> '+esc(x.w)+'</div>';
  if(e.pyq)h+='<div><span class="pq">Asked: '+e.pyq+'</span></div>';
  var K=e.key||[],M=e.minor||[];
  if(K.length||M.length){h+='<details class="cs"><summary>⚖️ Supreme Court cases<span class="cn">'+K.length+' landmark · '+M.length+' to know</span></summary>';
    K.forEach(function(k){h+='<div class="kc"><h4>'+k.c+'<span>'+k.y+'</span></h4>'+(k.pyq?'<div><span class="pq">PYQ '+k.pyq+'</span></div>':'')+
      '<div class="kr"><i>Issue</i><div>'+k.issue+'</div></div><div class="kr"><i>Question</i><div>'+k.q+'</div></div><div class="kr h"><i>Held</i><div>'+k.held+'</div></div>'+(k.exam?'<div class="kx">Exam angle: '+k.exam+'</div>':'')+'</div>'});
    if(M.length){h+='<div class="mnl"><b class="t">Also know (one line each)</b><ul>';M.forEach(function(m){h+='<li><b>'+m.c+'</b> ('+m.y+'): '+m.pt+'</li>'});h+='</ul></div>'}
    h+='</details>'}
  else if(e.none)h+='<div class="nc">⚖️ '+e.none+'</div>';
  if(e.mn&&e.mn.length){h+='<div class="mnb">';e.mn.forEach(function(m){h+='<div class="mi"><div class="mw">🧠 '+m.w+' '+(m.src==='new'?'<span class="ms new">New</span>':'<span class="ms old">From your notes · '+m.src+'</span>')+'</div><div class="mx">'+m.x+'</div></div>'});h+='</div>'}
  h+='<div class="hwe">Hook: '+esc(x.h)+'</div>';
  if(e.link)h+='<div class="nl">📖 In your notes: <a href="'+e.link[0]+'">'+e.link[1]+'</a></div>';
  return h+'<button class="hb sm'+(on?' on':'')+'" type="button" data-act="arw" data-d="'+d+'" data-j="'+j+'" aria-pressed="'+on+'">'+(on?'✓ Learned':'Got it')+'</button></div>'}"""
i = s.find('function arHtml(x,d,j){'); k = s.find('function renderArt(){')
assert i > 0 and k > i
s = s[:i] + JS + '\n' + s[k:]
if 'var AX=' not in s:
    s = s.replace("function arDay(d){", "var AX={};try{AX=JSON.parse(document.getElementById('artx').textContent)}catch(e){AX={}}\nfunction arDay(d){", 1)
open(p, 'w', encoding='utf8').write(s); print('index.html: article cards for', len(data), 'articles')
