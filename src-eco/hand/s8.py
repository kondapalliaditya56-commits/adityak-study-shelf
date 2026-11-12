import sys, importlib
sys.path.insert(0,'/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad'); sys.path.insert(0,'/tmp/claude-0/-home-claude/72cbe3e5-542c-596f-8ef0-06a8d705bf8d/scratchpad/hand')
import hand_eco as HE, layer8, ncert8
layer8.NCX = ncert8.NC; layer8.NCSRC = ncert8.SRC
sys.modules['layer8'] = layer8
HE.COVER = ('<div class="cov"><div class="s">UPSC CSE 2027 · GS Foundation</div><h1>ECONOMY</h1><div class="s">Handout + NCERT, integrated</div>'
 '<div><span class="bx">SAMPLE · Chapter 8 · Money and Monetary Policy</span></div><div class="t">Handout layout and order kept. NCERT Class XII Macroeconomics Ch 3 added inside the matching sections as peach boxes.<br>'
 'Only NCERT points the handout lacks, plus “NCERT differs” flags where they disagree.<br>Right column and left binding margin kept blank.<br><br>Personal study edition · for printing</div></div>')
HE.HOWTO = HE.HOWTO.replace('<tr><td><b>📊 Graphs and drawings</b></td><td>Curves, bars, loops and ladders you can redraw from memory on a blank page.</td></tr>',
 '<tr><td><b>📘 From NCERT (peach)</b></td><td>NCERT points not in the handout, placed after the handout section they belong to. Red “NCERT differs” line = conflict; handout/teacher wins in class.</td></tr>'
 '<tr><td><b>Graphs</b></td><td>Only the handout’s own figures. Nothing is redrawn or invented.</td></tr>')
HE.build([8], sys.argv[1])
