"""Idempotent: add the 'Regulator PYQs' section to the Governance Study Shelf chapter 5 (gov-ch05.html) and update priority badge.
Note: if build.py regenerates gov-ch05.html, re-run this script, then tools/ca_integrate.py sep26."""
import re, json
M = '<!--pyq-reg-->'
SEC = M + '''<h2 id="pyq-regulators">Regulator PYQs (added outside the handout)<a class="anchor" href="#pyq-regulators" aria-label="Link to this section">#</a></h2><p class="gdesc">From UPSC PYQ lists and your August 2026 current-affairs magazine. Question gist is paraphrased: check exact wording in your PYQ book.</p><table><thead><tr><th>Year</th><th>Question gist</th><th>Where to answer from</th></tr></thead><tbody>
<tr><td>Mains 2015 (10 marks, 150 words)</td><td>Regulatory institutions must stay independent and autonomous to achieve their objectives; discuss in light of recent experience.</td><td>Section 1 (why regulators rose, courts) and Section 2 (people, parent ministry, accountability). Skeleton: why independence matters → where it falls short → accountability and appeals → reforms.</td></tr>
<tr><td>Mains 2014</td><td>Would a Rail Tariff Authority to regulate fares benefit consumers, Indian Railways or private container operators? Use the power-sector experience.</td><td>Section 1 (power-sector regulators) and Section 2 (conflicts, clear jurisdiction).</td></tr>
<tr><td>Mains 2013 (10 marks, 150 words)</td><td>Justify the merger of SEBI and IRDA given overlapping products of financial institutions and insurers.</td><td>Section 2 (inter-regulator conflicts, clear division of sectoral regulators).</td></tr>
<tr><td>Mains 2023 (10 marks, 150 words)</td><td>Role of the Competition Commission of India in containing abuse of dominant position; refer to recent decisions.</td><td>Section 4 (CCI functions, recent cases).</td></tr>
<tr><td>Prelims 2026 (August 2026 magazine, PYQ Connect)</td><td>NBFC statements: cannot accept demand deposits; all NBFCs must be RBI-registered; can issue cheques on themselves; no DICGC cover for deposit-taking NBFCs.</td><td>Not in this handout; see the August 2026 current-affairs notes. Likely key (own working, verify): (a) 1 and 4.</td></tr></tbody></table><p class="gdesc">Priority for this chapter is now High for Sections 1-2 (three Mains PYQs) and Medium for Section 4 (one PYQ). These PYQs come from outside the handout; verify before relying on them.</p>'''
BADGE = 'High · Mains (PYQs added)'
p = 'gov-ch05.html'; h = open(p, encoding='utf8').read()
if M not in h:
    k = h.index('<h2 id="recall"'); h = h[:k] + SEC + h[k:]
    open(p, 'w', encoding='utf8').write(h)
def fix(secs):
    if not any(s['id'] == 'pyq-regulators' for s in secs):
        j = next(i for i, s in enumerate(secs) if s['id'] == 'recall')
        secs.insert(j, {'id': 'pyq-regulators', 't': 'Regulator PYQs'})
def patch(chs):
    for c in chs:
        if c.get('n') == 5 and 'Regulatory' in c['title']:
            c['badge'] = BADGE; fix(c['secs'])
lib = json.load(open('library.json'))
for n in lib:
    if n['id'] == 'governance': patch(n['chapters'])
json.dump(lib, open('library.json', 'w'), ensure_ascii=False, indent=1)
ix = open('index.html', encoding='utf8').read()
m = re.search(r'(<script type="application/json" id="libdata">)(.*?)(</script>)', ix, re.S)
d = json.loads(m.group(2))
for n in d:
    if n['id'] == 'governance': patch(n['chapters'])
open('index.html', 'w', encoding='utf8').write(ix[:m.start(2)] + json.dumps(d, ensure_ascii=False) + ix[m.end(2):])
cj = 'gov-chapters.json'
try:
    g = json.load(open(cj)); patch(g['chapters']); json.dump(g, open(cj, 'w'), ensure_ascii=False, indent=1)
except FileNotFoundError: pass
print('ok')
