from lib import Ch

c = Ch(0, 'Start Here: How to Use This Notebook',
       'Economy · GS Foundation · Start here',
       [('hb', 'Handout only'), ('', '13 chapters written from 14 files')],
       'How the Economy notebook is built, what the box colours mean, which handout in your merged PDF feeds which chapter, and how the figures that disagree between handouts are flagged.')

c.sec('1 · What this notebook is')
c.p('This is your Economy notebook, built the same way as Modern Indian History. Each chapter keeps the handout facts, rewritten clearly, and adds an **exam lens,** tables, redrawn flows, a timeline, traps, a recall sheet, a quiz, mains skeletons and flashcards. Everything comes **only from your merged Economy PDF** (Sarrthi IAS, GS Foundation, material by Aditya Kalia).')
c.call('alert', 'Important: almost no teacher ink in this source', [
    'Your merged PDF (415 pages, 14 files) holds **handouts and two class slide decks.** I looked at every slide image. The **External Sector slides (Chapter 10)** carry one piece of ink: **pink ovals and a star around 2020-21 Q1 and Q2** on the BoP chart (the reason is not written). The **Budget slides (Chapter 12)** are typed with **no handwriting.** The handouts carry no teacher ink. The GST handout (Chapter 11) has the teacher\'s **handwritten worked examples** inside the handout.',
    'So the orange "Teacher\'s board" boxes in most chapters quote the **handout\'s own emphasis** (asterisks, repeated points, "Crucial Trap" boxes), and the PYQ table says "none quoted in the material" wherever the file has none. Nothing is guessed from outside.'])

c.sec('2 · The box colours')
c.call('teacher', 'Orange: stress', 'In Modern India this is the teacher\'s handwriting. Here it marks a point the handout itself stresses (asterisks, "important note", formulas).')
c.call('alert', 'Red: handout alert', 'A conflict, a trap or a garbled place in the source, with a rule for the exam hall. Examples: $4.20 versus $3.65 for the lower-middle-income line.')
c.call('note', 'Blue: note', 'A definition or a pointer the handout gives.')
c.call('example', 'Green: example', 'A worked example from the handout (PPP factor, MPI).')
c.call('key', 'Teal: remember', 'What to prepare for Prelims and Mains.')

c.sec('3 · How to study a chapter')
c.ol([
    'Read the **Exam lens** first (two minutes). It tells you what the handout stresses and what to prepare.',
    'Skim the **Chapter map,** then read the sections. Tap **Mark read** or just scroll; the shelf tracks progress.',
    'Read the **red alerts** twice. They are where marks are lost.',
    'Do the **Quick quiz,** then the **mains skeletons** on a blank page, then **flashcards** on your phone.',
    'Revise with the **recall sheet** at +1, +3, +7, +21 and +45 days.'])

c.sec('4 · Your merged PDF: which file feeds which chapter')
c.table('The 14 files in Merged_Economy_14_PDFs.pdf (page numbers are PDF pages)', ['#', 'File', 'PDF pages', 'Type', 'PYQs in the file', 'Status'], [
    ['1', 'Poverty & Inequality (Ch 1 Poverty, Ch 2 Inequality)', '1-36', 'Handout', 'None', '**Written: Chapters 1 and 2**'],
    ['2', 'Unemployment', '37-71', 'Handout', '**Yes: 10 Prelims PYQs** (years quoted 2011, 2012, 2013, 2017, 2018, 2020, 2021, 2022)', '**Written: Chapter 3**'],
    ['3', 'Basic Concepts of Economics', '73-92', 'Handout', '1 Prelims PYQ (2021)', '**Written: Chapter 4**'],
    ['4', 'National Income Accounting', '93-129', 'Handout', '3 Prelims PYQs (2018, 2015, 2015)', '**Written: Chapter 5**'],
    ['5', 'Inflation', '131-146', 'Handout', 'None quoted', '**Written: Chapter 6**'],
    ['6', 'Banking and NBFCs', '148-180', 'Handout', 'None quoted', '**Written: Chapter 7**'],
    ['7', 'Money and Monetary Policy', '182-212', 'Handout', 'None quoted', '**Written: Chapter 8**'],
    ['8', 'Capital Markets', '214-231', 'Handout', 'None quoted', '**Written: Chapter 9**'],
    ['9', 'External Sector: Balance of Payments', '232-250', 'Class slides', 'None quoted', '**Written: Chapter 10** (with file 11)'],
    ['10', 'GST', '251-265', 'Handout', 'None quoted', '**Written: Chapter 11**'],
    ['11', 'External Sector', '267-313', 'Handout', 'None quoted', '**Written: Chapter 10** (with file 9)'],
    ['12', 'Government Budgeting and Fiscal Policy', '314-342', 'Class slides', 'None quoted', '**Written: Chapter 12** (with file 13)'],
    ['13', 'Government Budgeting and Fiscal Policy', '343-400', 'Handout', 'None quoted', '**Written: Chapter 12** (with file 12)'],
    ['14', 'NABARD, NBFCs, climate finance (Economics class handout)', '402-413', 'Handout', 'None quoted', '**Written: Chapter 13**'],
], rowhead=False)
c.call('note', 'How "PYQs in the file" was found', 'By reading each chapter\'s text and slides for PYQ sections. "None quoted" means no PYQ appears in the material; it does not prove the exam never asked about the topic. The count of years is "years quoted", not distinct questions. Pages 72, 130, 147, 181, 213, 234, 250, 266, 317-323, 325-327, 330, 335, 342, 401 are blank or image-only in the text search (mostly slide images).')
c.call('alert', 'Possible gaps to check', [
    'The merged PDF also ends with pages 414-415 from **other subjects** (a History Optional title page, "Aditya Kalia"). They are not economy and were left out.',
    'The same rule applies to the slides: ink on the External Sector slides is only the pink marks on slide 13; the Budget slides have none.'])

c.sec('5 · Priority map for all 13 chapters')
c.table('Master table (generated from the chapters; PYQ years are "years quoted" in the material)', ['Chapter', 'Marking in the source', 'Prelims years quoted', 'Mains years quoted', 'Where to spend time'], [
    ['1 · Poverty', 'Handout asterisk: Tendulkar stays official PL; heavy space on World Bank lines and National MPI', 'none quoted in the material', 'none quoted in the material', '**High:** committees table, WB lines, MPI formula, NFHS numbers'],
    ['2 · Inequality', 'Kuznets is theory, Gini shortcomings, rule of law, four conditions of trickle-down', 'none quoted in the material', 'none quoted in the material', '**Medium-high:** Lorenz and Gini mechanics; trickle-down versus inclusive'],
    ['3 · Unemployment', 'Handout: “Crucial Prelims Fact” on gratuity; ten PYQs at the end', '**2011, 2012, 2013 (x2), 2017, 2018 (x2), 2020, 2021, 2022**', 'none quoted in the material', '**Highest:** PLFS definitions, types (disguised, marginal product), schemes, Labour Codes'],
    ['4 · Basic Concepts', 'Opportunity cost stressed; types of goods; investment and depreciation', '**2021**', 'none quoted in the material', '**Medium:** types of goods, GCF, depreciation versus CFC versus CCA'],
    ['5 · National Income', 'Longest formula chapter: GDP, GNP, GVA, MP/BP/FC, new base 2022-23', '**2015 (x2), 2018**', 'none quoted in the material', '**High:** formulas, real versus nominal, tax-to-GDP, alternatives to GDP'],
    ['6 · Inflation', 'Handout emphasis only (types, measures, AD-AS)', 'none quoted in the material', 'none quoted in the material', '**High:** CPI/WPI, causes, AD-AS, Phillips-type trade-offs'],
    ['7 · Banking and NBFCs', 'Handout emphasis; many source conflicts flagged', 'none quoted in the material', 'none quoted in the material', '**High:** NPA, IBC, Basel, bank types, SARFAESI, scale-based NBFC regulation'],
    ['8 · Money and Monetary Policy', 'Handout emphasis; EBLR = MCLR alert', 'none quoted in the material', 'none quoted in the material', '**High:** M-measures, money multiplier, repo and the rate corridor, transmission'],
    ['9 · Capital Markets', 'Handout emphasis on numbers (T-bills, Sensex, Nifty)', 'none quoted in the material', 'none quoted in the material', '**Medium-high:** IPO process, intermediaries, derivatives, funds, P-Notes'],
    ['10 · External Sector', 'Slides: pink ovals and star on 2020-21 Q1 and Q2 (reason not written)', 'none quoted in the material', 'none quoted in the material', '**High:** BoP structure, FDI versus FPI, exchange rates, CAD, IMF and World Bank'],
    ['11 · GST', 'Handout emphasis: three properties, Council voting, compensation, RNR', 'none quoted in the material', 'none quoted in the material', '**High:** definition, Articles, Council, outside GST, compensation'],
    ['12 · Budget and Fiscal Policy', 'Handout “Ultimate Prelims Trap” (PMFBY) and “Crucial Trap” (external debt); slides typed', 'none quoted in the material', 'none quoted in the material', '**Highest by volume:** deficits, FRBM, debt, Finance Commission, tax types, buoyancy'],
    ['13 · NABARD, NBFCs, chit funds', 'Handout emphasis on dates, thresholds and regulators', 'none quoted in the material', 'none quoted in the material', '**Medium:** NABARD facts, NBFC types, who regulates what'],
], rowhead=True)
c.call('note', 'Reading the table', 'Inside your 14 handouts, only Chapters 3, 4 and 5 quote any PYQ. For the other ten chapters, priority came from the handout’s own emphasis, not from exam history. The rating in the last column is my reading of how much of each handout is numbers, definitions and flagged traps; it is a guide, not an exam forecast.')
c.call('alert', 'Conflicts between handouts (read before the exam)', [
    '**NBFC size:** Chapter 13 says systemically important = ₹500 crore (older RBI FAQ); Chapter 7 uses the 2022 scale-based layers (Base Layer below ₹1,000 crore).',
    '**GST rates and RNR:** Chapter 11 lists the five slabs (0, 5, 12, 18, 28) and a 30% pre-GST illustration; Chapter 12 says GST 2.0 (August-September 2025) rationalised rates and uses 33% in its illustration. The new slabs are not in the material.',
    '**Composition scheme limit:** ₹100 lakh versus ₹75 lakh inside Chapter 11.'])

c.sec('6 · PYQ map from the Saarthi subject-wise sheets')
from pyqlib import PYQ, BANKS
_T = {1:'Poverty',2:'Inequality',3:'Unemployment',4:'Basic Concepts',5:'National Income',6:'Inflation',7:'Banking and NBFCs',8:'Money and Monetary Policy',9:'Capital Markets',10:'External Sector',11:'GST',12:'Budget and Fiscal Policy',13:'NABARD, NBFCs, chit funds'}
_rows = []
for _n in range(1, 14):
    _p = [r for r in PYQ['prelims'] if r.get('ch') == _n]; _m = [x for x in PYQ['mains'] if x.get('ch') == _n]
    _py = sorted({r['year'] for r in _p if r['year']}); _my = sorted({x['year'] for x in _m})
    _tot = len(_p) + len(_m)
    _wt = 'High' if _tot >= 15 else ('Medium' if _tot >= 6 else 'Light')
    _rows.append(['%d · %s' % (_n, _T[_n]), '%d' % len(_p), ', '.join(_py) if _py else 'none', '%d' % len(_m), ', '.join(_my) if _my else 'none', '**%s**' % _wt])
_bp = len([r for r in PYQ['prelims'] if 'bank' in r]); _bm = len([x for x in PYQ['mains'] if 'bank' in x])
c.p('You gave me two PYQ sheets from Saarthi IAS: the **Economy subject-wise Prelims sheet** (288 questions with keys, 2004 to 2024) and the **GS-III Mains sheet** (economy and agriculture slots, 2013 to 2025). Every question is placed under the chapter and topic it tests. Chapters 1 to 13 each have a **Past-year questions** section; Mains questions carry keyword chips.')
c.table('How many PYQs each chapter carries (counts of questions in the sheets, not of distinct concepts)', ['Chapter', 'Prelims', 'Prelims years', 'Mains', 'Mains years', 'PYQ weight'], _rows, rowhead=True)
c.p('**%d Prelims and %d Mains questions** test topics that none of your 13 chapters cover (agriculture, industry and trade policy, infrastructure and energy, human development, planning). They are kept in the [PYQ bank](eco-pyq.html) so nothing is lost.' % (_bp, _bm))
c.call('alert', 'Read this about the PYQ source', [
    '**These are coaching compilations, not the raw UPSC papers.** upsc.gov.in could not be opened from my workspace, so I could not check each question against the official paper. Questions, years and answer keys are exactly as printed in your sheets.',
    '**Rule for the exam hall:** if a key here disagrees with your own reasoning or with the official key, trust the official key and tell me, and I will correct the note.',
    'Five Prelims questions have no year printed in the sheet; they show "year not stated". A few questions in the Prelims sheet are really Polity, History or Geography (for example Money Bill and chronology items). They sit in the PYQ bank under the last group.',
    'Mains keyword chips: a **solid** chip appears in that chapter\u2019s notes; an **outline** chip is taken from the question wording. In the PYQ bank only question-wording chips are shown, because there is no handout text to check against.'])

c.sec('7 · Tools inside the notebook')
c.ul(['**Aa:** text size, width, sepia or dark theme, focus mode, keep-screen-on.', '**Search** and **Timeline** in the top bar.', '**Done** box per chapter; read marks per section; a resume prompt when you return.', 'Offline reading: an Artifact cannot be installed for offline use. Ask for the PDF edition if you need offline or A4 print.'])

c.timeline = []
