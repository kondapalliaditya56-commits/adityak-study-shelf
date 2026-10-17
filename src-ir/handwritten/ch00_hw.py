# -*- coding: utf-8 -*-
"""Start Here page for the IR handwritten notes."""
from dsl import *
from hwlib import P, H, R

CHS = [
dict(toc='Start here: how to use these notes', id=0, title='START HERE: HOW TO USE THESE NOTES', part=1, icon='lens',
 simple='Read once with a pen. Fill the right column with your class notes. Before a test, cover the recall drill at the end of each chapter.',
 nodes=[
 two([bx('pk', '<b>How IR is asked (PPT-1, slide 3):</b> 4 questions, <b>50 marks every year</b>. Q9, Q10 = 10 marks / 150 words (~7 min). Q19, Q20 = 15 marks / 250 words (~11 min). Questions are <b>broad and statement-based</b>: test the claim, don\'t endorse it.')],
     [tb(['Box', 'Means'], ['<span class="rd"><b>Pink</b></span>', 'slide line / handout error'], ['<b>Yellow</b>', 'trap or rule for the exam hall'], ['<span class="gn"><b>Green</b></span>', 'ready conclusion line'], ['<b>Blue dashed</b>', 'definition'], ['<b>Navy</b>', 'current affairs (verify dates)'])]),
 sec('APPROACHES SHEET (your teacher\'s): pick one for the BODY', 'b'),
 tb(['No.', 'Approach', 'How to use', 'Best IR fit'],
    ['1', '<b>Stakeholder</b>', 'impact, limits, way forward', '"to what extent", policy questions'],
    ['2', '<b>Supply chain</b>', 'process', 'corridors: Chabahar → INSTC'],
    ['3', '<b>GS Paper-wise</b>', 'PESTEL', '"examine influence / relations"'],
    ['4', '<b>Level analysis</b>', 'personal → national → international', 'diaspora, soft power, global role'],
    ['5', '<b>Component</b>', 'parts the question names', '"diplomatic, economic, strategic"'],
    ['6', '<b>SDGs</b>', '"sustainable" word', 'climate, Africa, island states'],
    ['7', '<b>Syllabus</b>', 'broad question', 'groupings, effect of policies'],
    ['8', '<b>Demand / supply</b>', 'need vs offer', 'minerals, energy, labour'],
    ['9', '<b>P3I</b>', 'people, powers, processes, infra', 'connectivity, regional engagement'],
    ['10', '<b>Life cycle</b>', 'birth → growth → crisis → reset', 'Maldives, Bangladesh'],
    ['11', '<b>Temporal</b>', 'timeline', '"evolution", "post-Cold War"'],
    ['12', '<b>SWOT</b>', 'S, W, O, T', '"importance + challenges", "pros and cons"']),
 bx('ye', '<b>Quick recall (teacher):</b> Stakeholder → Supply Chain → GS Paper Wise → Level → Component → SDG → Syllabus → Demand/Supply → P3I → Life Cycle → Temporal → SWOT. &nbsp;<b>Every answer:</b> Intro (number / slide line / current hook) → Body (one approach) → Way forward → Conclusion (slide\'s closing phrase).'),
 sec('WHICH LECTURE FEEDS WHICH CHAPTER', 'g'),
 tb(['Chapter', 'Class slides', 'Handout', 'Mains PYQs quoted'],
    ['1 World order &amp; foreign policy', 'PPT-1, PPT-2', 'Ch 1 pp. 1-21', '2026 (4), 2025, 2020, 2019'],
    ['2 Major powers', 'PPT-3, PPT-4 (Other Powers)', 'Ch 2 pp. 1-24', '2017-2026 (10)'],
    ['3 Neighbourhood', 'PPT-4 Neighbourhood', 'Ch 3 pp. 1-27', '2024, 2022, 2015 (2)'],
    ['4 Diaspora', 'PPT-6', 'merged pp. 72-77', '2026, 2023, 2020, 2017'],
    ['5 Extended neighbourhood', 'PPT-7.2, PPT-7', 'merged pp. 78-100', '2024, 2021 (2), 2018 (2), 2016, 2015'],
    ['6 International organisations', '<span class="rd">slides pending</span>', 'merged pp. 101-143', 'to come']),
 bx('bl', '<b>Sources:</b> only your Sarrthi IAS handouts and class slides. The decks are typed (no handwriting), so "slide phrase" boxes quote the slides\' own "core idea" and "conclusion" lines. Current-affairs boxes come from your July and August 2026 magazines (web items are marked). Mnemonics marked "own mnemonic" are not from class.'),
 ]),
]
