import sys,json,copy
sys.path.insert(0,'/home/claude/is/hw')
import os; os.chdir('hw')
import buildhw
from dsl import chapter_book
import ch_k
old=json.load(open('../bookdata.json'))
oldch={c['id']:c for p in old['parts'] for c in p['chapters']}
chs=[c for c in buildhw.load()]+ch_k.BK
ORDER=[1,47,48,2,3,4,49,50,51,52, 5,6,7, 8,9,33,32,36,20,37, 10,39,11,12,13,35,38, 18,19,55,21,22,23,24,25,40, 26,41,42,54,34, 27,28,53,29, 14,15,16,17, 30,43,44,31,45,46]
by={c['id']:c for c in chs}
parts=copy.deepcopy(old['parts'])
for p in parts: p['chapters']=[]
for cid in ORDER:
    c=by[cid]
    if cid==10:
        ch=oldch[10]
        for it in ch['notes']:
            if isinstance(it,dict) and 'h' in it and ("class='pq'" in it['h'] or it['h'].startswith(('Case study','Women in','PYQ skeletons'))): it['sec']=1
    else:
        ch=chapter_book(c,cid)
        o=oldch.get(cid,{})
        ch['pyqs']=c.get('pyq',o.get('pyqs',''))
    parts[c['part']]['chapters'].append(ch)
n=0
for p in parts:
    for ch in p['chapters']:
        n+=1; ch['id']=n
old['parts']=parts
old['meta']['imprint']=[x for x in old['meta']['imprint'] if not x.startswith('Sample edition')]
json.dump(old,open('../bookdata_full.json','w'),ensure_ascii=False,indent=1)
print(sum(len(p['chapters']) for p in parts),'chapters')
