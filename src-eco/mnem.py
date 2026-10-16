import itertools, sys
from wordfreq import top_n_list
W=[w.upper() for w in top_n_list('en',80000) if w.isalpha() and 4<=len(w)<=8]
def find(opts):
    """opts: list of candidate-letter strings per item. returns words using each item once."""
    n=len(opts);res=[]
    for w in W:
        if len(w)!=n: continue
        # assign letters to items via permutation matching
        def ok(i,used):
            if i==n: return True
            for j,ch in enumerate(opts[i]):
                pass
            return False
        # bipartite: each word letter must map to a distinct item
        from itertools import permutations
        letters=list(w)
        # try matching
        match={}
        def try_item(it,seen):
            for pos,l in enumerate(letters):
                if l in opts[it] and pos not in seen:
                    seen.add(pos)
                    if pos not in match or try_item(match[pos],seen):
                        match[pos]=it;return True
            return False
        if all(try_item(it,set()) for it in range(n)): res.append((w,{match[p]:w[p] for p in match}))
    return res
if __name__=='__main__':
    pass
