# -*- coding: utf-8 -*-
"""Post-processing for handwritten notes: (1) brief current-affairs boxes in the right-hand column at matching chapters,
(2) glossary box at the bottom of each chapter (abbreviations, schemes, organisations). Never alters existing text."""
import re, os, sys, html as H, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from gloss_data import G, SKIP
STOP = set('the and for with from that this which are was were has have had not but its their into than also under over such more between about being other these those will shall may can per all any one two three first new act india indian government state states union central national article section bill court law power powers committee commission body body member members chapter notes note case cases'.split())
CHAP = re.compile(r'<div class="(?:pg )?chap" id="c([^"]+)">')
TAG = re.compile(r'<[^>]+>')
def text_of(s): return H.unescape(TAG.sub(' ', s))
def toks(s): return set(w for w in re.findall(r'[a-z][a-z0-9\-]{3,}', s.lower()) if w not in STOP)

def split_chaps(html):
    ms = list(CHAP.finditer(html))
    return ms
def ca_items(prefixes, months=('sep26',)):
    import ca_integrate as ci
    out = []
    for m in months:
        try: out += [i for i in ci.load_month(m)['items'] if set(i['nb']) & set(prefixes)]
        except Exception as ex: print('CA load fail', m, ex)
    return out
CSS = ('.camg{float:right;width:37mm;margin:0 -40.5mm 1.5mm 0;border:1.4px solid #0d47a1;border-radius:3px;background:#f3f8ff;color:#0d2a5c;'
       'font-size:7.6pt;line-height:1.12;padding:.8mm 1.4mm;break-inside:avoid;clear:right}'
       '.camg .h{font-family:KB;font-size:7.4pt;color:#fff;background:#0d47a1;border-radius:6px;padding:0 1.6mm;display:inline-block;margin-bottom:.4mm}'
       '.camg .ti{font-weight:bold;color:#b71c1c;display:block}.camg .it{display:block;margin-bottom:.9mm;padding-bottom:.6mm;border-bottom:1px dotted #90a4ae}.camg .it:last-child{border:0;margin:0;padding:0}'
       '.glo{break-inside:avoid;margin:3mm 0 1mm;border:1.6px dashed #6a1b9a;border-radius:4px;background:#faf5ff;padding:1mm 2.2mm 1.4mm;font-size:8.6pt;line-height:1.16;color:#311b92}'
       '.glo .gh{font-family:CB;font-size:12pt;color:#6a1b9a}.glo .gh i{font-family:PH;font-size:7.6pt;color:#7b1fa2;font-style:normal}'
       '.glo .gc{column-count:2;column-gap:4mm}.glo .ge{break-inside:avoid;margin:0 0 .7mm}.glo b{color:#c62828}.glo u{text-decoration:none;color:#00695c}')

def match_ca(html, ms, items, thr=7.0, maxper=3):
    if not items: return {}
    ctext = {}
    for k, m in enumerate(ms):
        end = ms[k+1].start() if k+1 < len(ms) else len(html)
        ctext[m.group(1)] = toks(text_of(html[m.end():end]))
    df = collections.Counter()
    for t in ctext.values():
        for w in t: df[w] += 1
    N = len(ctext)
    res = collections.defaultdict(list)
    for it in items:
        kw = it['kw'] if isinstance(it['kw'], str) else '; '.join(it['kw'])
        itoks = toks(' '.join([it['t'], kw]))
        itoks2 = toks(it['ctx'] + ' ' + ' '.join(it['pts']))
        best = None
        for cid, t in ctext.items():
            sc = sum(math.log(N / df[w]) * (2 if w in itoks else 1) for w in (itoks | itoks2) & t if df[w] < max(4, N * .12))
            if best is None or sc > best[0]: best = (sc, cid)
        if best and best[0] >= thr: res[best[1]].append((best[0], it))
    out = {}
    for cid, lst in res.items():
        lst.sort(key=lambda x: -x[0]); out[cid] = [i for _, i in lst[:maxper]]
    return out
def ca_box(items):
    b = '<div class="camg"><span class="h">📰 Current affairs · verify dates</span>'
    for it in items:
        ctx = it['ctx'].strip()
        if len(ctx) > 170:
            cut = ctx[:170]; cut = cut[:max(cut.rfind('. '), cut.rfind('; '), cut.rfind(', '))] if max(cut.rfind('. '), cut.rfind('; '), cut.rfind(', ')) > 90 else cut.rsplit(' ', 1)[0]
            ctx = cut.rstrip('.,; ') + ' … (full: CA pages at the end)'
        b += '<span class="it"><span class="ti">%s</span>%s</span>' % (H.escape(it['t']), H.escape(ctx))
    return b + '</div>'

HARV = re.compile(r"((?:[A-Z][\w'’\-]*|of|and|for|the|on|in|to)(?: (?:[A-Z][\w'’\-]*|of|and|for|the|on|in|to|\(|&)){1,9}) \(([A-Z][A-Za-z\-]{1,9})\)")
def gloss(chtext):
    found = collections.Counter()
    for m in re.finditer(r'(?<![A-Za-z])(?:[A-Z][A-Za-z]?[A-Z0-9&\-]*[A-Za-z0-9]|[A-Z]{2,}|PM-KISAN|E-NAM|CERT-In|DoPT|BOLD-QIT)(?![A-Za-z])', chtext):
        a = m.group(0)
        if a in G and a not in SKIP: found[a] += 1
        elif a.upper() in G and a.upper() == a and a not in SKIP: found[a] += 1
    harv = {}
    for m in HARV.finditer(chtext):
        harv.setdefault(m.group(2), m.group(1).strip())
    ents = []
    for a, n in found.most_common():
        full, brief = G[a] if a in G else G[a.upper()]
        src = harv.get(a)
        ents.append((a, full, brief, bool(src)))
    # acronyms the notes themselves expand but dictionary lacks
    for a, full in harv.items():
        if a not in found and a not in G and a not in SKIP and len(a) >= 2 and a.isupper():
            if re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(a), chtext): ents.append((a, full, '', True))
    return ents[:16]
def gloss_box(ents):
    if not ents: return ''
    b = '<div class="glo"><div class="gh">🔤 Quick brief: abbreviations, schemes, bodies <i>(expansions from notes where given; briefs are general knowledge, verify)</i></div><div class="gc">'
    for a, full, brief, _ in ents:
        b += '<div class="ge"><b>%s</b> = <u>%s</u>%s</div>' % (H.escape(a), H.escape(full), (' — ' + H.escape(brief)) if brief else '')
    return b + '</div></div>'

def apply(html, prefixes, months=('sep26',), report=None):
    ms = split_chaps(html)
    if not ms: return html
    items = ca_items(prefixes, months)
    cam = match_ca(html, ms, items)
    parts = []; last = 0; stats = [0, 0]
    for k, m in enumerate(ms):
        end = ms[k+1].start() if k+1 < len(ms) else None
        seg_end = end if end is not None else html.rfind('</body>')
        if seg_end < 0: seg_end = len(html)
        seg = html[m.end():seg_end]
        cid = m.group(1)
        ttl_end = re.search(r'</div>', seg)
        pre = ''
        if cid in cam:
            box = ca_box(cam[cid]); stats[0] += len(cam[cid])
            if report is not None: report.append((cid, [i['id'] + ' ' + i['t'] for i in cam[cid]]))
            pre = box
        # glossary at bottom of chapter: before the closing of the chapter div (last </div> of seg)
        g = gloss_box(gloss(text_of(seg)))
        if g: stats[1] += 1
        # insert CA box right after the title div; glossary before last </div>
        if pre and ttl_end: seg = seg[:ttl_end.end()] + pre + seg[ttl_end.end():]
        if g:
            li = seg.rfind('</div>')
            seg = seg[:li] + g + seg[li:] if li >= 0 else seg + g
        parts.append(html[last:m.end()]); parts.append(seg); last = seg_end
    parts.append(html[last:])
    out = ''.join(parts).replace('</style>', CSS + '</style>', 1)
    print('hwextras: CA boxes', stats[0], 'glossary chapters', stats[1], 'of', len(ms))
    return out
