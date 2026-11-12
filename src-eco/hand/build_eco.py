"""Build detailed handwritten Economy notes: python3 hand/build_eco.py OUT.pdf 1,2,3  [full]"""
import sys, importlib
SC = '/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad'
sys.path.insert(0, SC); sys.path.insert(0, SC + '/hand')
import hand_eco as HE
chs = [int(x) for x in sys.argv[2].split(',')]
sample = not (len(sys.argv) > 3 and sys.argv[3] == 'full')
HE.build(chs, sys.argv[1], sample=sample)
