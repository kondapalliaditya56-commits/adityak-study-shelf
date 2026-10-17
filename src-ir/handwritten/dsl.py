# -*- coding: utf-8 -*-
"""Chapter DSL: write once -> handwritten print notes (HTML) + textbook notes items."""
import textwrap,re,math
from hwlib import *
import hwlib
# ---- constructors
def t(label,*kids,c=None,w=None): return ('tree',label,list(kids),c,w)
def sec(title,c=''): return ('sec',title,c)
def bx(kind,html): return ('bx',kind,html)       # kind: pk ye gr bl ca qt
def tb(head,*rows): return ('tb',head,[list(r) for r in rows])
def mn(word,html): return ('mn',word,html)
def fl(steps,title=None,cols=4): return ('fl',steps,title,cols)
def hub(center,spokes,title=None): return ('hub',center,spokes,title)
def tl(*items): return ('tl',list(items))        # timeline arrow [(head,body)]
def two(a,b): return ('two',a,b)
def sw(x): return ('sw',x)
# ---- svg helpers
COL=['#fde7ea|#c62828','#fff9c4|#b26a00','#e8f5e9|#2e7d32','#e3f2fd|#1565c0','#f3e5f5|#6a1b9a','#e0f7fa|#00838f']
def wrap(s,n): return textwrap.wrap(s,n) or ['']
def svg_flow(steps,cols=4):
    rows=[steps[i:i+cols] for i in range(0,len(steps),cols)]
    W=320;bw=(W-10-(cols-1)*12)/cols;out=[];y=4;idx=0;pos=[]
    for r in rows:
        mx=max(len(wrap(x,int(bw/4.1))) for x in r);bh=10+mx*10
        for k,x in enumerate(r):
            xx=5+k*(bw+12);bg,fg=COL[idx%6].split('|');idx+=1
            out.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" rx="6" fill="%s" stroke="%s" stroke-width="1.5"/>'%(xx,y,bw,bh,bg,fg))
            for li,l in enumerate(wrap(x,int(bw/4.1))):
                out.append('<text x="%.1f" y="%.1f" fill="#1a237e">%s</text>'%(xx+bw/2,y+11+li*10,l))
            pos.append((xx,y,bw,bh))
        y+=bh+14
    arrows=[]
    for i in range(len(pos)-1):
        a,b=pos[i],pos[i+1]
        if b[1]==a[1]: arrows.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'%(a[0]+a[2],a[1]+a[3]/2,b[0]-1,b[1]+b[3]/2))
        else: arrows.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f"/>'%(a[0]+a[2]/2,a[1]+a[3],a[0]+a[2]/2,a[1]+a[3]+7,b[0]+b[2]/2,a[1]+a[3]+7,b[0]+b[2]/2,b[1]-1))
    return '<svg class="sv" viewBox="0 0 320 %d" width="100%%" style="max-width:150mm"><defs><marker id="fa" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0L6,3L0,6z" fill="#111"/></marker></defs><g font-family="KL" font-size="7.6" text-anchor="middle">%s<g stroke="#111" stroke-width="1.3" fill="none" marker-end="url(#fa)">%s</g></g></svg>'%(y,''.join(out),''.join(arrows))
def svg_hub(center,spokes):
    n=len(spokes);cx,cy=160,85;out=[];lines=[]
    for i,s in enumerate(spokes):
        a=-math.pi/2+2*math.pi*i/n;x=cx+118*math.cos(a);y=cy+62*math.sin(a)
        bg,fg=COL[(i+1)%6].split('|');L=wrap(s,18);w=82;h=8+len(L)*9
        lines.append('<line x1="%d" y1="%d" x2="%.1f" y2="%.1f"/>'%(cx,cy,x,y))
        out.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="6" fill="%s" stroke="%s" stroke-width="1.4"/>'%(x-w/2,y-h/2,w,h,bg,fg))
        for li,l in enumerate(L): out.append('<text x="%.1f" y="%.1f" fill="#1a237e">%s</text>'%(x,y-h/2+9+li*9,l))
    CL=wrap(center,14)
    c='<ellipse cx="%d" cy="%d" rx="42" ry="%d" fill="#fff59d" stroke="#111" stroke-width="1.8"/>'%(cx,cy,12+len(CL)*7)
    for li,l in enumerate(CL): c+='<text x="%d" y="%.1f" font-family="KB" font-size="9" fill="#111">%s</text>'%(cx,cy-len(CL)*4.5+9+li*9,l)
    return '<svg class="sv" viewBox="0 0 320 170" width="100%%" style="max-width:150mm"><g font-family="KL" font-size="7.4" text-anchor="middle"><g stroke="#888" stroke-width="1.2">%s</g>%s%s</g></svg>'%(''.join(lines),''.join(out),c)
# ---- render handwritten
def strip(x): return re.sub(r'<[^>]+>','',x)
def r_hw(n):
    k=n[0]
    if k=='tree':
        kids=[r_hw(x) if isinstance(x,tuple) else x for x in n[2]]
        return B(n[1],kids,n[3],n[4] or 26)
    if k=='sec': return S(n[1],n[2])
    if k=='bx': return box(n[1],n[2])
    if k=='tb': return tbl(n[1],n[2])
    if k=='mn': return box('ye','<span class="mn">%s</span> — %s'%(n[1],n[2]))
    if k=='fl': return (S(n[2],'b') if n[2] else '')+svg_flow(n[1],n[3])
    if k=='hub': return (S(n[3],'g') if n[3] else '')+svg_hub(n[1],n[2])
    if k=='tl': return arrow(n[1])
    if k=='two': return '<div class="row"><div>%s</div><div>%s</div></div>'%(''.join(r_hw(x) for x in n[1]),''.join(r_hw(x) for x in n[2]))
    if k=='sw': return SW(n[1])
def chapter_hw(ch):
    ic=ICON.get(ch.get('icon','bag'),ICON['bag'])
    h='<div class="chap" id="c%s"><div class="ttl">%s&nbsp;%s&nbsp;%s</div>'%(ch['id'],ic,ch['title'],ic)
    if ch.get('pyq'): h+='<div class="pyqline">%s</div>'%P(ch['pyq'])
    if ch.get('simple'): h+=SW(ch['simple'])
    h+=''.join(r_hw(x) for x in ch['nodes'])
    if ch.get('recall'):
        h+=S('Recall drill: cover and answer','r')+'<table>'+''.join('<tr><td style="width:55%%">%s</td><td>%s</td></tr>'%(q,a) for q,a in ch['recall'])+'</table>'
    return h+'</div>'
# ---- render textbook items
def flat(n,depth=0):
    out=[]
    for x in n[2]:
        if isinstance(x,tuple): out.append(('sub',x))
        else: out.append(x)
    return out
def r_book(n):
    k=n[0];it=[]
    if k=='tree':
        it.append({'h':strip(n[1])})
        for x in n[2]:
            if isinstance(x,tuple):
                it.append('<b>%s</b>'%n[1] if False else '<b>%s</b>'%strip(x[1]))
                for y in x[2]: it.append('› '+y if not isinstance(y,tuple) else '› <b>%s</b>'%strip(y[1]))
            else: it.append(x)
    elif k=='sec': it.append({'h':strip(n[1]),'sec':1})
    elif k=='bx':
        if n[1]=='ca': it.append({'ca':n[2]})
        elif n[1]=='qt': it.append({'call':{'kind':'quote','tag':'Quote','body':[n[2]]}})
        elif n[1]=='pk': it.append({'call':{'kind':'teacher','tag':'Value addition','body':[n[2]]}})
        else: it.append({'call':{'kind':'note','tag':'Note','body':[n[2]]}})
    elif k=='tb': it.append({'tbl':{'head':n[1],'rows':n[2]}})
    elif k=='mn': it.append({'call':{'kind':'teacher','tag':'Memory aid · '+n[1],'body':[n[2]]}})
    elif k=='fl': it.append({'h':n[2] or 'Flow'}); it.append(' → '.join('<b>%s</b>'%x for x in n[1]))
    elif k=='hub': it.append({'h':n[3] or n[1]}); it.append('<b>%s</b>: '%n[1]+' · '.join(n[2]))
    elif k=='tl':
        it.append({'h':'Timeline / way forward'})
        for a,b in n[1]: it.append('<b>%s</b>: %s'%(a,b.replace('<br>','; ')))
    elif k=='two':
        for x in n[1]+n[2]: it+=r_book(x)
    return it
def chapter_book(ch,cid,pri='M'):
    notes=[]
    for n in ch['nodes']:
        if n[0]=='sw': continue
        notes+=r_book(n)
    return {'id':cid,'title':ch['title'],'pages':ch.get('pages',''),'priority':ch.get('prio',pri),'pyqs':ch.get('pyq','none quoted in the material'),
      'prelims_pyqs':'none quoted in the material','lens':{'prelims':ch.get('lens_p',[]),'mains':ch.get('lens_m',[]),'close':ch.get('lens_c','')},
      'simple':ch.get('simple_b',[ch.get('simple','')]),'terms':ch.get('terms',[]),'remember':ch.get('remember',''),'notes':notes,'recall':ch.get('recall',[]),'traps':[],'quiz':[],'visuals':[]}
