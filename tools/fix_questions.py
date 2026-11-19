#!/usr/bin/env python3
"""Question-bank cleanup for Modern India qNN.html pages.
1) Mains text that leaked into the last MCQ option -> separate 'Past UPSC Mains question' box.
2) Match-the-following stems (List I / List II) flattened into a paragraph -> two-column table.
python3 fix_questions.py REPO [--dry]"""
import re, sys, glob, html, os, itertools
REPO = sys.argv[1]; DRY = '--dry' in sys.argv
E = lambda s: html.escape(s, quote=False).replace("'", '&#x27;')

CSS = ('<style id="mtfcss">.mtft{width:100%;border-collapse:collapse;margin:10px 0;font:16px/1.45 var(--sans)}'
       '.mtft th{background:var(--surface2,#efe6d2);color:var(--ink);text-align:left;padding:7px 10px;border:1px solid var(--line)}'
       '.mtft td{padding:7px 10px;border:1px solid var(--line);vertical-align:top}.mtft td b{color:var(--acc)}'
       '.mnote{margin:10px 0;padding:10px 14px;border-left:4px solid var(--acc);background:var(--surface2,#efe6d2);border-radius:8px;font:15px/1.5 var(--sans)}'
       '.mnote b{display:block;margin-bottom:4px}.mnote ul{margin:4px 0 0 18px;padding:0}'
       '@media print{.mtft{font-size:8.6pt}.mtft th,.mtft td{padding:1.2mm 2mm}.mnote{font-size:8.6pt;break-inside:avoid}}</style>')

# ---------- 1. leaked Mains text in options ----------
LEAK = re.compile(r'\s*(?:A\.\d+\s*[—-]\s*Mains PYQs \(Guiding Themes\)|Past UPSC Mains Questions \(themes\))\s*-{3,}(.*)$', re.S)
def split_leak(opt_html):
    txt = opt_html
    m = LEAK.search(html.unescape(re.sub('<[^>]+>', '', txt)))
    if not m: return None
    plain = html.unescape(re.sub('<[^>]+>', '', txt))
    head = plain[:m.start()].strip()
    tail = m.group(1)
    qs = [q.strip(' -●•') for q in re.split(r'●|•', tail)]
    qs = [re.sub(r'\s*-{3,}\s*$', '', q).strip() for q in qs]
    qs = [q for q in qs if q and not re.fullmatch(r'-*', q)]
    return head, qs

# ---------- 2. List I / List II ----------
def _seq(cands, want):
    """pick first in-order run of wanted labels from candidate list [(start,end,label)]"""
    out = []; i = 0
    for c in cands:
        if i < len(want) and c[2].upper() == want[i]:
            out.append(c); i += 1
    return out if len(out) >= 2 else []

SEP = re.compile(r'\s+(?:\u2014|\u2013|\||-)\s+')
MKRE = re.compile(r'(?:(?<=[\s|:)\]\u2014;])|^)\(?([A-Ea-e]|[1-6])[.)]\s*(?=\S)')

def _items(text, kinds):
    """sequential markers of the given kind ('alpha'|'digit') -> [(label,text)]"""
    mk = [(x.start(1), x.end(), x.group(1)) for x in MKRE.finditer(text)]
    want = 'ABCDE' if kinds == 'alpha' else '123456'
    pick = _seq([x for x in mk if (x[2].isalpha() if kinds == 'alpha' else x[2].isdigit())], want)
    return pick

def _texts(text, pick):
    out = []
    for i, (s_, e_, k) in enumerate(pick):
        end = pick[i + 1][0] if i + 1 < len(pick) else len(text)
        seg = re.sub(r'\s*\($', '', text[e_:end])
        seg = re.sub(r'\s+', ' ', seg).strip(' ;|\n')
        if i == len(pick) - 1:
            seg = re.split(r'\s+(?:1|A)\.\s|(?<=[a-z])(?=Select the)|\s+Select the', seg)[0]
        out.append((k.upper(), seg.strip(' ;|\n\u2014-')))
    return out

def _inter(rest):
    letters, digits = _items(rest, 'alpha'), _items(rest, 'digit')
    allm = sorted(letters + digits)
    if len(letters) < 2 or len(digits) < 2: return None
    segs = {}
    for i, (s_, e_, k) in enumerate(allm):
        end = allm[i + 1][0] if i + 1 < len(allm) else len(rest)
        sg = re.sub(r'\s+', ' ', re.sub(r'\s*\($', '', rest[e_:end])).strip(' ;|\n')
        segs[k.upper()] = sg.strip(' ;|\n\u2014-')
    kl = [x[2].upper() for x in letters]; kd = [x[2] for x in digits]
    k1, k2 = (kl, kd) if allm[0][2].isalpha() else (kd, kl)
    return 'List I', 'List II', [(k, segs[k]) for k in k1], [(k, segs[k]) for k in k2], ''


GG_ROWS = [("A", "Governor General of Presidency of Fort William in Bengal (Under Regulating Act, 1773)", "1", "Archibald Percival Wavell, Viscount and Earl Wavell"),
           ("B", "Governor General of India (Under Charter Act, 1833)", "2", "James Andrew Broun-Ramsay, Earl and Marquess of Dalhousie"),
           ("C", "Governor General and Viceroy of India (Under Indian Councils Act, 1858)", "3", "Charles Cornwallis, 2nd Earl and First Marquess of Cornwallis"),
           ("D", "Governor General and Crown Representative (Under Government of India Act, 1935)", "4", "Gilbert John Elliot-Murray-Kynynmond, Earl of Minto"),
           ("", "", "5", "Louis Mountbatten, Earl Mountbatten of Burma")]
def manual_gg(raw):
    """The one stem whose two columns wrap onto each other in the source text (Prelims 1996 GG/Viceroy match)."""
    if 'Governor General of Presidency of Fort' not in raw: return None
    q17 = 'Dalhousie48-56' in raw or 'Cornwallis86-93' in raw
    rows = []
    for ka, ta, kb, tb in GG_ROWS:
        if q17:
            tb = {'2': 'James Andrew Broun-Ramsay (Dalhousie48-56)', '3': 'Charles Cornwallis (Cornwallis86-93)', '4': 'Gilbert John Elliot-Murray-Kynynmond (Minto)'}.get(kb, tb)
            if kb == '1': tb = 'Archibald Percival Wavell'
            if kb == '5': tb = 'Louis Mountbatten'
        rows.append(((ka, ta), (kb, tb)))
    pre = raw.split('List I')[0].strip() or 'Match List I with List II and select the correct answer using the codes given below the lists:'
    pre = re.sub(r'^\(Match List\)\s*', '', pre)
    h1, h2 = ('List I (Office)', 'List II (Personality)') if q17 else ('List I', 'List II')
    return pre, h1, h2, [r[0] for r in rows], [r[1] for r in rows], ''

def parse_mtf(t):
    mg = manual_gg(html.unescape(t))
    if mg: return mg
    t = html.unescape(t).replace('\r', '')
    t = re.sub(r'[ \t]+', ' ', t)
    m = None
    for cand in re.finditer(r'\[?List[\s-]*I\]?(?![I\w])', t):
        nxt = re.search(r'List[\s-]*II', t[cand.end():])
        if not nxt: continue
        between = t[cand.end():cand.end() + nxt.start()]
        if re.search(r'\bwith\b|\band\b select', between, re.I) and len(between) < 80 and not re.search(r'\n', between): continue
        m = cand; break
    if not m:
        m3 = re.search(r'\n\s*List[\s-]*II\b\s*:?', t)
        nl = t.find('\n')
        if not m3 or nl < 0 or nl > m3.start(): return None
        pre = t[:nl].strip(); block1 = t[nl:m3.start()]; block2 = t[m3.end():]
        b1a, b1d = _items(block1, 'alpha'), _items(block1, 'digit')
        b2a, b2d = _items(block2, 'alpha'), _items(block2, 'digit')
        p1 = b1a if len(b1a) >= len(b1d) else b1d; p2 = b2a if len(b2a) >= len(b2d) else b2d
        if len(p1) < 2 or len(p2) < 2: return None
        tail = re.search(r'\n\s*(?:Which|Select|Choose)\b.*$', block2, re.S)
        trailer = re.sub(r'\s+', ' ', tail.group(0)).strip() if tail else ''
        if tail: block2 = block2[:tail.start()]; p2 = [x for x in p2 if x[0] < tail.start()]
        return pre, 'List I', 'List II', _texts(block1, p1), _texts(block2, p2), trailer
    pre = t[:m.start()].strip(' :')
    if len(_items(pre, 'digit')) >= 3 or len(_items(pre, 'alpha')) >= 3:
        nl = t.find('\n')
        if 0 < nl < m.start():
            r0 = _inter(t[nl:m.start()])
            if r0: return (t[:nl].strip(),) + r0
    body = t[m.start():]
    h1 = re.match(r'\[?List[\s-]*I\]?(?![I\w])\s*:?\s*(\((?![a-eA-E1-6]\))[^)]*\))?', body)
    m2 = re.search(r'\[?List[\s-]*II\]?\s*:?\s*(\((?![a-eA-E1-6]\))[^)]*\))?', body[h1.end() - 1:])
    if not m2: return None
    m2s = h1.end() - 1 + m2.start(); m2e = h1.end() - 1 + m2.end()
    hdr1 = ('List I ' + (h1.group(1) or '')).strip(); hdr2 = ('List II ' + (m2.group(1) or '')).strip()
    block1 = body[h1.end():m2s]; block2 = body[m2e:]
    # duplicated copy of the lists later in the stem: keep text up to it
    dup = re.search(r'\[?List[\s-]*I\]?(?![I\w])', block2)
    tail_instr = ''
    if dup:
        block2 = block2[:dup.start()]
    trailer = ''
    mt = re.search(r'(?:(?<=[.?)\w\u201d"])\s+|\n\s*)((?:Select|Choose|Which one|Which of|Use the|Codes?:|The correct|Answer)\b.*)$', block2, re.S)
    if mt: trailer = re.sub(r'\s+', ' ', mt.group(1)).strip(); block2 = block2[:mt.start()]
    # --- block mode: List I items sit between the two headers
    b1a, b1d = _items(block1, 'alpha'), _items(block1, 'digit')
    if len(b1a) >= 2 or len(b1d) >= 2:
        k1 = 'alpha' if len(b1a) >= len(b1d) else 'digit'
        i1 = _texts(block1, b1a if k1 == 'alpha' else b1d)
        # the stray label of block 2 may sit at the end of block1 (e.g. 'D. ... List II: A.')
        b2a, b2d = _items(block2, 'alpha'), _items(block2, 'digit')
        k2 = 'alpha' if len(b2a) >= len(b2d) else 'digit'
        if (b2a if k2 == 'alpha' else b2d):
            i2 = _texts(block2, b2a if k2 == 'alpha' else b2d)
            return pre, hdr1, hdr2, i1, i2, trailer
        return None
    # --- interleaved / inline mode (everything after both headers)
    rest = block1 + ' \n' + block2
    letters, digits = _items(rest, 'alpha'), _items(rest, 'digit')
    allm = sorted(letters + digits)
    if not allm: return None
    if letters and digits:
        first_alpha = allm[0][2].isalpha()
        tl = dict(_texts(rest[:0] + rest, allm)) if False else None
        segs = {}
        for i, (s_, e_, k) in enumerate(allm):
            end = allm[i + 1][0] if i + 1 < len(allm) else len(rest)
            sg = re.sub(r'\s+', ' ', re.sub(r'\s*\($', '', rest[e_:end])).strip(' ;|\n')
            if i == len(allm) - 1:
                sg = re.split(r'\s+(?:1|A)\.\s|(?<=[a-z])(?=Select the)|\s+Select the', sg)[0]
            segs[k.upper()] = sg.strip(' ;|\n\u2014-')
        kl = [x[2].upper() for x in letters]; kd = [x[2] for x in digits]
        k1, k2 = (kl, kd) if first_alpha else (kd, kl)
        return pre, hdr1, hdr2, [(k, segs[k]) for k in k1], [(k, segs[k]) for k in k2], trailer
    one = letters or digits
    a_, b_ = [], []
    for k, tx in _texts(rest, one):
        parts = SEP.split(tx, 1)
        if len(parts) != 2: return None
        a_.append((k, parts[0].strip())); b_.append(('', parts[1].strip()))
    return pre, hdr1, hdr2, a_, b_, trailer

def mtf_html(p):
    pre, h1, h2, a, b, trailer = p
    rows = ''.join('<tr><td>%s%s</td><td>%s%s</td></tr>' % (('<b>%s.</b> ' % ka) if ka else '', E(ta), ('<b>%s.</b> ' % kb) if kb else '', E(tb)) for (ka, ta), (kb, tb) in itertools.zip_longest(a, b, fillvalue=('', '')))
    out = ''
    if pre: out += '<p class="bqq">%s</p>' % E(pre)
    out += '<table class="mtft"><thead><tr><th>%s</th><th>%s</th></tr></thead><tbody>%s</tbody></table>' % (E(h1), E(h2), rows)
    if trailer: out += '<p class="bqq" style="font-size:.92em">%s</p>' % E(trailer)
    return out

stats = {'leak': 0, 'mtf': 0, 'mtf_fail': []}
for f in sorted(glob.glob(os.path.join(REPO, 'q[0-9][0-9].html'))):
    s = open(f, encoding='utf-8').read(); orig = s
    # leaks
    def fix_art(m):
        art = m.group(0)
        def fo(mo):
            inner = mo.group(3)
            r = split_leak(inner)
            if not r: return mo.group(0)
            head, qs = r
            fo.qs = qs
            k = mo.group(2)
            body = re.sub(r'^[A-E]\.\s*', '', head)
            return '<button type="button" class="opt" data-k="%s"><b>%s.</b> %s</button>' % (k, k.upper(), E(body))
        fo.qs = None
        new = re.sub(r'(<button type="button" class="opt" data-k="(\w)">)(.*?)</button>', lambda mo: fo(mo) if True else '', art, flags=re.S)
        # fo uses groups 1..3: group(2)=key, group(3)=inner
        if fo.qs:
            stats['leak'] += 1
            box = '<div class="mnote"><b>Past UPSC Mains question%s on this theme</b><ul>%s</ul></div>' % ('s' if len(fo.qs) > 1 else '', ''.join('<li>%s</li>' % E(q) for q in fo.qs))
            new = new.replace('</div><div class="bwhy"', '</div>' + box + '<div class="bwhy"', 1)
        return new
    s = re.sub(r'<article class="bq".*?</article>', fix_art, s, flags=re.S)
    # match-the-following
    def fq(m):
        raw = re.sub('<[^>]+>', '', re.sub(r'<br\s*/?>', '\n', m.group(1)))
        r = parse_mtf(raw) or parse_mtf(re.sub(r'(?<=[a-z0-9"\u201d\)])([A-E])\.\s', r' \1. ', raw))
        if r is None:
            if re.search(r'List[\s-]*I\b', html.unescape(m.group(1))): stats['mtf_fail'].append((os.path.basename(f), html.unescape(m.group(1))[:90]))
            return m.group(0)
        stats['mtf'] += 1
        return mtf_html(r)
    s = re.sub(r'<p class="bqq">(.*?)</p>', fq, s, flags=re.S)
    if s != orig and 'id="mtfcss"' not in s:
        s = s.replace('</head>', CSS + '</head>', 1)
    if s != orig and not DRY: open(f, 'w', encoding='utf-8').write(s)
print(stats['leak'], 'leaked-Mains options fixed;', stats['mtf'], 'match tables built;', len(stats['mtf_fail']), 'not parsed')
for x in stats['mtf_fail']: print('  FAIL', x)
