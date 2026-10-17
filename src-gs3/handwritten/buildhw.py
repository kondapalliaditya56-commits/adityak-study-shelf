# -*- coding: utf-8 -*-
import sys,glob,importlib,json,os
from weasyprint import HTML
import hwlib
from hwlib import *
from dsl import *
import ml_pages
PARTS=[('Part I','Agriculture and Food','#fff3e0'),('Part II','Disaster Management','#e0f2f1'),('Part III','Internal Security','#e8eaf6')]
def load():
    chs=[]
    for f in sorted(glob.glob('ch_*.py')):
        m=importlib.import_module(f[:-3]); chs+=m.CHS
    return chs
def raw(cid,title,part,pages,pg0=None): return dict(id=cid,title=title,part=part,raw=pages)
def all_chapters():
    chs=load()
    mp=ml_pages.pages
    chs.append(dict(id=14,title='Money Laundering and Black Money',part=2,raw=mp[0:9]+[mp[10]]))
    chs.append(dict(id=17,title='Terror Financing and Black Money',part=2,raw=[mp[9]]))
    ORDER=[1,47,48,2,3,4,49,50,51,52, 5,6,7, 8,9,33,32,36,20,37, 10,39,11,12,13,35,38, 18,19,55,21,22,23,24,25,40, 26,41,42,54,34, 27,28,53,29, 14,15,16,17, 30,43,44,31,45,46]
    assert sorted(ORDER)==sorted(c['id'] for c in chs),(set(c['id'] for c in chs)^set(ORDER))
    chs=sorted(chs,key=lambda c:ORDER.index(c['id']))
    for n,c in enumerate(chs,1): c['no']=n
    return chs
def build(out):
    chs=all_chapters()
    body=['<div class="cov"><div class="s">UPSC CSE Mains 2027 · GS Paper III</div><h1>INTERNAL SECURITY</h1><div class="s">Agriculture · Disaster Management · Security</div>'
      '<div><span class="bx">Handwritten-style notes</span></div><div class="t">Built from the Sarrthi IAS MMP+ handouts, class slides and PYQ sets.<br>Bracket trees · diagrams · mnemonics · keywords · current affairs<br>Right column and left binding margin are kept blank for your own use.<br><br>Personal study edition · for printing</div></div>']
    toc='<div class="partpg" style="padding:0;break-before:page"><div class="toc"><h2>INDEX</h2>'
    cur=-1
    for c in chs:
        if c['part']!=cur:
            cur=c['part'];l,t_,bg=PARTS[cur];toc+='<div class="pt" style="background:%s">%s · %s</div>'%(bg,l,t_)
        toc+='<a href="#c%s">%s &nbsp;%s</a>'%(c['id'],c['no'],c['title'])
    toc+='</div></div>'
    body.append(toc)
    cur=-1
    for c in chs:
        if c['part']!=cur:
            cur=c['part'];l,t_,bg=PARTS[cur]
            body.append('<div class="partpg" style="background:%s"><h1>%s</h1><div class="s">%s</div></div>'%(bg,t_,l))
        if 'raw' in c:
            r=list(c['raw']);r[0]=r[0].replace('<div class="pg">','<div class="pg chap" id="c%s">'%c['id'],1);body+=r
        else: body.append(chapter_hw(c))
    html='<html><head><style>%s</style></head><body>%s</body></html>'%(hwlib.CSS,''.join(body))
    d=HTML(string=html,base_url='.').render();print('pages',len(d.pages));d.write_pdf(out)
if __name__=='__main__': build(sys.argv[1] if len(sys.argv)>1 else 'GS3_Handwritten_Notes.pdf')
