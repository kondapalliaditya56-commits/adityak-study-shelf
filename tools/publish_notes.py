#!/usr/bin/env python3
"""Publish a new version of a subject's handwritten-notes PDF to the Study Shelf viewer.
Usage: python3 tools/publish_notes.py SUBJECT_ID PDF "what changed" [--title "Title"]
Adds notes/<SUBJECT_ID>/vN.pdf, puts it at the top of manifest.json (the viewer always opens the newest), keeps all older versions.
Skips if the PDF is identical to the latest version."""
import sys, os, json, hashlib, shutil, subprocess, datetime
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sid, pdf, note = sys.argv[1], sys.argv[2], sys.argv[3]
title = sys.argv[sys.argv.index('--title') + 1] if '--title' in sys.argv else None
d = os.path.join(root, 'notes', sid); os.makedirs(d, exist_ok=True)
mp = os.path.join(d, 'manifest.json')
m = json.load(open(mp)) if os.path.exists(mp) else {'subject': sid, 'title': title or sid + ' handwritten notes', 'versions': []}
if title: m['title'] = title
b = open(pdf, 'rb').read(); sha = hashlib.sha256(b).hexdigest()[:16]
if m['versions'] and m['versions'][0]['sha'] == sha: print('unchanged: same as latest v%d' % m['versions'][0]['v']); sys.exit(0)
v = (m['versions'][0]['v'] + 1) if m['versions'] else 1
shutil.copy(pdf, os.path.join(d, 'v%d.pdf' % v))
pg = int([l for l in subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout.split('\n') if l.startswith('Pages')][0].split()[1])
m['versions'].insert(0, {'v': v, 'file': 'v%d.pdf' % v, 'date': datetime.date.today().isoformat(), 'pages': pg, 'sha': sha, 'note': note})
json.dump(m, open(mp, 'w'), indent=1, ensure_ascii=False)
print('published %s v%d (%d pages)' % (sid, v, pg))
