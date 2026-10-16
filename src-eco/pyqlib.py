import json,re,html
PYQ=json.load(open('/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad/pyq_final.json'))
def _e(s): return html.escape(str(s),quote=False)
def _norm(s): return re.sub(r'\s+',' ',re.sub(r'[-–—/]',' ',s.lower())).strip()
def _has(text,k):
    k=_norm(k)
    if k in text: return True
    if k.endswith('s') and k[:-1] in text: return True
    return (k+'s') in text
GENERIC=set('requirements status challenges challenge reasons reason measures differences merits demerits progress features factors components changes policies arguments agree analyse analyze discuss trend pattern scope significance problems improvements achievements success rationale determinants steps types objectives implementation criticism constraints difficulty effectiveness outcomes improve investment production income'.split())
BANKS=[('agri','Agriculture, food security and farm policy'),('industry','Industry, MSME, trade and investment policy'),('infra','Infrastructure, energy and PPP'),('hrd','Human development: health, education, census'),('planning','Planning, NITI Aayog and reforms'),('misc','Outside economy (polity, history, geography, IR) filed under Economy in the PDF')]
BANKNAME=dict(BANKS)

def _blocks(lines):
    out=[]
    for l in lines:
        if not out or re.match(r'^(\d+[\.\)]\s|\([ivx]+\)\s|Select\b|Which of the (statements|above|following)\b.*\?$|How many|Answer|Statement|Choose|Code)',l) and not (out and out[-1][0]=='p' and re.search(r'(the|of|to|a|and|or|with|in|by|that|which)$',out[-1][1])):
            kind='s' if re.match(r'^\d+[\.\)]\s',l) else 'p'
            out.append([kind,re.sub(r'^\d+[\.\)]\s*','',l) if kind=='s' else l])
        else:
            out[-1][1]+=' '+l
    return out

def prelim_html(r):
    bl=_blocks(r['stem'])
    h='<div class="pq"><div class="pqh"><span class="yr">%s</span><span class="qno">Q%d</span></div>'%(_e(r['year'] or 'year not stated'),r['id'])
    inlist=False
    for k,t in bl:
        if k=='s':
            if not inlist: h+='<ol class="pqst">';inlist=True
            h+='<li>%s</li>'%_e(t)
        else:
            if inlist: h+='</ol>';inlist=False
            h+='<p class="pqs">%s</p>'%_e(t)
    if inlist: h+='</ol>'
    h+='<ol class="opts" type="a">'+''.join('<li>%s</li>'%_e(r['opts'][k]) for k in 'abcd' if k in r['opts'])+'</ol>'
    a=r['ans']
    h+='<details class="ans"><summary>Show answer</summary><p><strong>(%s)</strong> %s</p></details></div>'%(a,_e(r['opts'].get(a,'')))
    return h

def mains_html(m,chtext=None):
    chips=[];seen=set()
    qn=_norm(m['q'])
    for k in m['kw']:
        if k.lower() in seen: continue
        seen.add(k.lower())
        inq=_has(qn,k)
        generic = _norm(k) in GENERIC
        inn=bool(chtext) and not generic and _has(chtext,k)
        if inn: chips.append(('n',k))
        elif inq: chips.append(('q',k))
    chips.sort(key=lambda c:c[0]!='n')
    h='<article class="mq"><div class="mqh"><span class="yr">%s</span><span class="mk">%s marks</span><span class="tp">%s</span></div><p class="mqt">%s</p>'%(_e(m['year']),_e(m['marks']),_e(m['topic']),_e(m['q']))
    if chips:
        h+='<div class="kw"><span class="kwl">Keywords</span>'+''.join('<span class="kc %s">%s</span>'%(c,_e(k)) for c,k in chips)+'</div>'
    return h+'</article>', chips

def _secs_for(ch):
    # map section number -> (id,title)
    out={}
    for s in ch.secs:
        m=re.match(r'^(\d+)\s*·',re.sub(r'<[^>]+>','',s['title']))
        if m: out[int(m.group(1))]=(s['id'],s['title'])
        elif s['id']=='slide-only-topics': out[12]=(s['id'],s['title'])
    return out

def chapter_pyqs(ch):
    pre=[r for r in PYQ['prelims'] if r.get('ch')==ch.n]
    mn=[m for m in PYQ['mains'] if m.get('ch')==ch.n]
    return pre,mn

def counts_by_section(ch):
    pre,mn=chapter_pyqs(ch);d={}
    for r in pre: d.setdefault(r['sec'],[0,0])[0]+=1
    for m in mn: d.setdefault(m['sec'],[0,0])[1]+=1
    return d

def pyq_section(ch):
    pre,mn=chapter_pyqs(ch)
    if not pre and not mn: return ''
    secs=_secs_for(ch)
    chtext=_norm(' '.join(' '.join(s['plain']) for s in ch.secs))
    groups=sorted(set([r['sec'] for r in pre]+[m['sec'] for m in mn]))
    yrs=sorted({r['year'] for r in pre if r['year']}|{m['year'] for m in mn})
    h='<section id="pyq"><h2 id="pyq-top">Past-year questions<a class="anchor" href="#pyq-top">#</a></h2>'
    h+='<p class="gdesc">%d Prelims and %d Mains questions for this chapter, from the Saarthi subject-wise PYQ sheets (Prelims 2004–2024, Mains GS-III 2013–2025). Each group sits under the notes topic it tests. Try the question first, then open the answer.</p>'%(len(pre),len(mn))
    h+='<p class="gdesc kwkey"><span class="kc n">solid chip</span> keyword that appears in this chapter’s notes &nbsp; <span class="kc q">outline chip</span> keyword taken from the question itself.</p>'
    h+='<div class="row"><button class="btn" type="button" onclick="document.querySelectorAll(\'#pyq details.pqgrp\').forEach(function(d){d.open=true})">Open all topics</button><button class="btn" type="button" onclick="document.querySelectorAll(\'#pyq details.pqgrp\').forEach(function(d){d.open=false})">Close all</button></div>'
    for g in groups:
        sid,stitle=secs.get(g,('',str(g)))
        p=[r for r in pre if r['sec']==g]; m=[x for x in mn if x['sec']==g]
        h+='<details class="pqgrp" id="pyq-%s" open><summary><span class="gt">%s</span><span class="gc">%d Prelims · %d Mains</span></summary>'%(sid,_e(re.sub(r'<[^>]+>','',stitle)),len(p),len(m))
        if sid: h+='<p class="gotonotes"><a class="xref" href="#%s">Read the notes for this topic</a></p>'%sid
        if p:
            h+='<h4 class="pqk">Prelims</h4>'+''.join(prelim_html(r) for r in sorted(p,key=lambda r:r['year'] or '0',reverse=True))
        if m:
            h+='<h4 class="pqk">Mains (GS-III)</h4>'
            for x in sorted(m,key=lambda x:x['year'],reverse=True):
                h+=mains_html(x,chtext)[0]
        h+='</details>'
    return h+'</section>'

def pyq_plain(ch):
    pre,mn=chapter_pyqs(ch)
    t=[]
    for r in pre: t.append(' '.join(r['stem'])+' '+' '.join(r['opts'].values()))
    for m in mn: t.append(m['q']+' '+' '.join(m['kw']))
    return re.sub(r'\s+',' ',' '.join(t))

CSS_PYQ='''<style>
.gdesc.kwkey{font-size:13px}
details.pqgrp{border:1px solid var(--line);border-radius:12px;background:var(--surface);margin:12px 0;padding:0 14px}
details.pqgrp>summary{cursor:pointer;list-style:none;padding:12px 0;display:flex;gap:10px;flex-wrap:wrap;align-items:baseline;justify-content:space-between}
details.pqgrp>summary::-webkit-details-marker{display:none}
details.pqgrp>summary .gt{font:700 16px var(--serif);color:var(--ink);flex:1 1 60%}
details.pqgrp>summary .gc{font:600 12px var(--sans);color:var(--muted);white-space:nowrap}
details.pqgrp[open]>summary{border-bottom:1px solid var(--line);margin-bottom:8px}
.gotonotes{margin:4px 0 8px;font-size:14px}
h4.pqk{font:700 12px var(--sans);letter-spacing:.07em;text-transform:uppercase;color:var(--acc);margin:14px 0 6px}
.pq,.mq{border:1px solid var(--line);border-radius:10px;background:var(--bg);padding:10px 12px;margin:10px 0}
.pqh,.mqh{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:6px}
.yr{font:700 12px var(--sans);background:var(--acc-soft);color:var(--acc);border-radius:99px;padding:2px 9px}
.qno,.mk,.tp{font:600 12px var(--sans);color:var(--muted)}
.tp{background:var(--surface2);border-radius:99px;padding:2px 9px}
.pqs{margin:4px 0}
ol.pqst{margin:4px 0 4px 1.2em;padding:0}
ol.opts{margin:6px 0 6px 1.6em;padding:0}
ol.opts li{margin:2px 0}
details.ans>summary{cursor:pointer;font:700 13px var(--sans);color:var(--saf)}
details.ans[open]>summary{margin-bottom:4px}
details.ans p{margin:2px 0;background:var(--good-soft);border-left:3px solid var(--good);padding:6px 10px;border-radius:0 8px 8px 0}
.mqt{margin:4px 0 8px}
.kw{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.kwl{font:700 11px var(--sans);letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-right:2px}
.kc{font:600 12.5px var(--sans);border-radius:99px;padding:3px 10px;border:1.5px solid var(--acc)}
.kc.n{background:var(--acc);color:var(--acc-ink)}
.kc.q{background:transparent;color:var(--acc)}
a.pyqlink{display:inline-block;font:600 12.5px var(--sans);margin:-4px 0 10px;padding:3px 10px;border-radius:99px;background:var(--saf-soft);color:var(--saf);text-decoration:none}
.pybank-nav{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
</style>'''

def bank_body(chapter_titles, pfx='eco-'):
    pre=[r for r in PYQ['prelims'] if 'bank' in r]
    mn=[m for m in PYQ['mains'] if 'bank' in m]
    h='<main class="page"><div class="chead"><div class="eyebrow">Economy notebook</div><h1>PYQ bank</h1><p class="lede">Questions that belong to topics your 13 chapters do not cover (agriculture, industry, infrastructure, human development, planning) are kept here so nothing is lost. %d Prelims and %d Mains questions. Mains keywords here come from the question wording only, because there is no handout text to check them against.</p></div>'%(len(pre),len(mn))
    h+='<div class="pybank-nav">'+''.join('<a class="btn" href="#bk-%s">%s</a>'%(k,_e(v.split(',')[0].split(' (')[0])) for k,v in BANKS if any(r.get('bank')==k for r in pre) or any(m.get('bank')==k for m in mn))+'</div>'
    for k,name in BANKS:
        p=[r for r in pre if r['bank']==k]; m=[x for x in mn if x['bank']==k]
        if not p and not m: continue
        h+='<section id="bk-%s"><h2>%s<a class="anchor" href="#bk-%s">#</a></h2><p class="gdesc">%d Prelims · %d Mains</p>'%(k,_e(name),k,len(p),len(m))
        if p:
            h+='<details class="pqgrp" open><summary><span class="gt">Prelims</span><span class="gc">%d questions</span></summary>'%len(p)
            h+=''.join(prelim_html(r) for r in sorted(p,key=lambda r:r['year'] or '0',reverse=True))+'</details>'
        if m:
            h+='<details class="pqgrp" open><summary><span class="gt">Mains (GS-III)</span><span class="gc">%d questions</span></summary>'%len(m)
            for x in sorted(m,key=lambda x:x['year'],reverse=True): h+=mains_html(x,None)[0]
            h+='</details>'
        h+='</section>'
    return h+'</main>'

def bank_plain():
    t=[]
    for r in PYQ['prelims']:
        if 'bank' in r: t.append(' '.join(r['stem'])+' '+' '.join(r['opts'].values()))
    for m in PYQ['mains']:
        if 'bank' in m: t.append(m['q']+' '+' '.join(m['kw']))
    return re.sub(r'\s+',' ',' '.join(t))

def master_rows(chs):
    rows=[]
    for c in chs:
        if c.n==0: continue
        p,m=chapter_pyqs(c)
        ys=sorted({r['year'] for r in p if r['year']})
        my=sorted({x['year'] for x in m})
        rows.append((c.n,c.title,len(p),len(m),ys,my))
    return rows

def lens_note(ch):
    pre,mn=chapter_pyqs(ch)
    if not pre and not mn: return ''
    secs=_secs_for(ch); cs=counts_by_section(ch)
    tot=len(pre)+len(mn)
    wt='High' if tot>=15 else ('Medium' if tot>=6 else 'Light')
    ranked=sorted(cs.items(),key=lambda kv:-(kv[1][0]+kv[1][1]))[:3]
    names=[]
    for sec,(a,b) in ranked:
        t=re.sub(r'<[^>]+>','',secs.get(sec,('',str(sec)))[1]); t=re.sub(r'^\d+\s*·\s*','',t)
        names.append('%s (%d Prelims, %d Mains)'%(t,a,b))
    py=sorted({r['year'] for r in pre if r['year']}); my=sorted({x['year'] for x in mn})
    lines=['**PYQ weight from the Saarthi subject-wise sheets: %s.** %d Prelims and %d Mains questions map to this chapter.'%(wt,len(pre),len(mn))]
    lines.append('Most-asked topics: '+'; '.join(names)+'.')
    if py: lines.append('Prelims years: '+', '.join(py)+'. ' + (('Mains years: '+', '.join(my)+'.') if my else 'Mains: none in the sheets.'))
    lines.append('All of them are in [Past-year questions](#pyq), grouped by topic, with Mains keyword chips.')
    return lines
