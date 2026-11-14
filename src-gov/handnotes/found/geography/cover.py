# -*- coding: utf-8 -*-
"""Point-level coverage: which handout blocks (headings, bullets, paragraphs, tables) are not carried by the revision map of their topic."""
import re, html as H
from bs4 import BeautifulSoup, NavigableString
STOP = set('that this with from have been were their there which these those also than then they them into over such when what where while about after before between within without under other more most some only very each both many much will would could should being because during among upon through against still often called known given used using made make like same however whereas whose'.split())
def toks(t):
    t = H.unescape(t).lower()
    return [w[:5] for w in re.findall(r"[a-z]{4,}|\d[\d,\.]*\d|\d", t) if w not in STOP]
def stems(text): return set(toks(re.sub(r'<[^>]+>', ' ', text)))
def blocks(frag):
    """flat list of (kind, depth, text, html) in handout order. kinds: h(level in depth), li, p, tbl, fig"""
    frag = re.sub(r'<details class="qr".*?</details>', '', frag, flags=re.S)
    frag = re.sub(r'<a class="anchor"[^>]*>.*?</a>', '', frag, flags=re.S)
    soup = BeautifulSoup('<div id="root">%s</div>' % frag, 'lxml'); root = soup.find(id='root'); out = []
    def lis(ul, d):
        for c in ul.children:
            if isinstance(c, NavigableString): continue
            if c.name == 'li':
                sub = [x for x in c.children if getattr(x, 'name', None) in ('ul', 'ol')]
                own = ''.join(str(x) for x in c.children if getattr(x, 'name', None) not in ('ul', 'ol'))
                t = BeautifulSoup(own, 'lxml').get_text(' ', strip=True)
                out.append(('li', d, t, own))
                for x in sub: lis(x, d + 1)
            elif c.name in ('ul', 'ol'): lis(c, d + 1)
    def walk(el):
        for c in el.children:
            if isinstance(c, NavigableString): continue
            n = c.name
            if n in ('h2', 'h3', 'h4'): out.append(('h', int(n[1]), c.get_text(' ', strip=True), c.decode_contents()))
            elif n in ('ul', 'ol'): lis(c, 0)
            elif n == 'p': out.append(('p', 0, c.get_text(' ', strip=True), c.decode_contents()))
            elif n == 'figure': out.append(('fig', 0, '', str(c)))
            elif n == 'table': out.append(('tbl', 0, c.get_text(' ', strip=True), str(c)))
            elif n in ('div', 'section', 'blockquote'):
                if c.find(['h2', 'h3', 'h4', 'ul', 'p', 'figure', 'table']) and 'callout' not in (c.get('class') or []): walk(c)
                elif c.find('figure'): walk(c)
                else:
                    t = c.get_text(' ', strip=True)
                    if t: out.append(('p', 0, t, c.decode_contents()))
    walk(root); return out
def covered(text, have):
    s = toks(text)
    if not s: return True
    hit = sum(1 for w in s if w in have)
    nums = [w for w in s if w[0].isdigit()]
    if len(s) <= 2: return hit == len(s)
    if nums and sum(1 for w in nums if w in have) < len(nums) * 0.5 and hit / len(s) < 0.85: return False
    return hit / len(s) >= 0.6
