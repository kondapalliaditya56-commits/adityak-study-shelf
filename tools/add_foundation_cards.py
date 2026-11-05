#!/usr/bin/env python3
"""Insert the 'Handwritten revision notes (PDF)' card on the Polity, Economy, Geography and Modern India contents pages (idempotent, marker <!--fh-card-->)."""
import os, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOMES = {'pol-home.html': 'polity', 'eco-home.html': 'economy', 'geo-home.html': 'geography', 'home.html': 'modern-india'}
CARD = ('<!--fh-card--><a class="hwcard" href="pdfview.html?s=%s" style="display:flex;align-items:center;gap:12px;margin:14px 0 4px;padding:14px 16px;border:1px solid var(--line);border-radius:14px;background:var(--surface);text-decoration:none;color:inherit;font-family:var(--sans)">'
        '<span style="font-size:26px" aria-hidden="true">&#9998;</span><span style="flex:1"><b style="display:block;font-size:16px">Handwritten revision notes (PDF)</b>'
        '<small id="fhmeta" style="color:var(--muted)">Opens the latest version in the PDF viewer</small></span><span style="font-weight:700;color:var(--accent)">Open &rsaquo;</span></a>'
        '<script>fetch("notes/%s/manifest.json",{cache:"no-store"}).then(function(r){return r.json()}).then(function(m){var v=m.versions[0],e=document.getElementById("fhmeta");if(e)e.textContent="Latest: version "+v.v+" \\u00b7 "+v.pages+" pages \\u00b7 "+v.date}).catch(function(){})</script>')
for f, sid in HOMES.items():
    p = os.path.join(root, f)
    if not os.path.exists(p) or not os.path.exists(os.path.join(root, 'notes', sid, 'manifest.json')): continue
    h = open(p, encoding='utf8').read()
    if '<!--fh-card-->' in h: print('has card', f); continue
    m = re.search(r'<p class="lede">.*?</p>', h, re.S)
    if not m: print('no anchor', f); continue
    open(p, 'w', encoding='utf8').write(h[:m.end()] + CARD % (sid, sid) + h[m.end():]); print('added', f)
