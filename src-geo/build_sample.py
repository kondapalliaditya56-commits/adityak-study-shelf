import sys, os, json, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_book as G
ch3 = G.build_chapter(3, importlib.import_module('chap.ch3'))
def stub(i, t, pr='M'): return dict(id=i, title=t, pages='', priority=pr, pyqs='', lens={'prelims': [], 'mains': [], 'close': ''}, simple=[], terms=[], remember='', notes=[], recall=[], traps=[], quiz=[], visuals=[])
parts = [
 {'label': 'Part 1', 'title': 'Physical geography', 'sub': 'Geomorphology, climatology, oceanography', 'chapters': [stub(1, 'Geomorphology', 'H'), stub(2, 'Climatology'), ch3]},
 {'label': 'Part 2', 'title': 'Indian geography', 'sub': 'Physiography, drainage, climate, soils, resources', 'chapters': [stub(4, 'Indian Geography', 'H')]},
 {'label': 'Part 3', 'title': 'Human and economic geography', 'sub': 'People, settlements, resources and industry', 'chapters': [stub(5, 'Human Geography'), stub(6, 'Economic Geography')]}]
meta = {'title': 'Geography', 'subtitle': 'Geomorphology, Climatology, Oceanography, Indian, Human and Economic Geography', 'cover_top': 'UPSC CSE 2027 · GS FOUNDATION · GEOGRAPHY', 'cover_mid': 'A study companion built from the Sarrthi IAS Geography handouts and mind maps, with every Prelims and Mains PYQ the handouts print.', 'cover_foot': 'UPSC CIVIL SERVICES EXAMINATION 2027 · PERSONAL STUDY EDITION', 'running_head': 'Geography · Personal Study Edition',
 'imprint': ['<b>Personal Study Edition, 2026</b>', 'Prepared for the UPSC Civil Services Examination 2027 and APPSC Group 1, General Studies.', 'Source: Sarrthi IAS Geography handouts and mind maps. The facts printed here are the source documents’ own; no outside facts or value-addition data. Copyright belongs to the source institute; keep this private.', 'The wide ruled panel on the right of every page is blank for your own current affairs, data and value additions.']}
out = sys.argv[1]
json.dump({'meta': meta, 'parts': parts}, open(os.path.join(out, 'bookdata.json'), 'w'), ensure_ascii=False)
