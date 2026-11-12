# my own test wrapper: same as build_eco.py but tolerates 1-item flow steps (shared bug, not edited)
import sys
SC='/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad'
sys.path.insert(0,SC); sys.path.insert(0,SC+'/hand')
import hand_eco as HE
o=HE.viz
def v(x):
    if x.get('type')=='flow': x=dict(x, steps=[(list(s)+[''])[:2] for s in x['steps']])
    return o(x)
HE.viz=v
HE.build([int(c) for c in sys.argv[2].split(',')], sys.argv[1], sample=False)
