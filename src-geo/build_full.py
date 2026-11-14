import sys, os, json, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_book as G
src = open(os.path.join(os.path.dirname(__file__), 'build_sample.py')).read()
ns = {}
chs = {n: G.build_chapter(n, importlib.import_module('chap.ch%d' % n)) for n in (1, 2, 3, 4, 5, 6)}
parts = [{'label': 'Part 1', 'title': 'Physical geography', 'sub': 'Geomorphology, climatology, oceanography', 'chapters': [chs[1], chs[2], chs[3]]},
 {'label': 'Part 2', 'title': 'Indian geography', 'sub': 'Physiography, drainage, climate, soils, resources', 'chapters': [chs[4]]},
 {'label': 'Part 3', 'title': 'Human and economic geography', 'sub': 'People, settlements, resources and industry', 'chapters': [chs[5], chs[6]]}]
meta = G.__dict__.get('META')
import re
m = re.search(r"meta = (\{.*?\})\nout =", src, re.S); meta = eval(m.group(1))
json.dump({'meta': meta, 'parts': parts}, open(os.path.join(sys.argv[1], 'bookdata.json'), 'w'), ensure_ascii=False)
