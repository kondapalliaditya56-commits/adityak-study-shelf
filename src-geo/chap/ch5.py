# -*- coding: utf-8 -*-
import sys, os, re, html
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src-gov', 'handnotes', 'found', 'geography'))
import detail_data as DD
UND = DD.UND[5]
TITLE = 'Human Geography'; PAGES = 'Handout, 13 pages'; PRIORITY = 'M'; PYQS = 'none quoted'; PRELIMS = '2013, 2014, 2 undated'
SKIP_H = {'1 · DEMOGRAPHY', 'Population Pyramids', 'Population Theory of Malthus', 'Demographic Transition Theory', 'MAJOR TRIBES OF INDIA', '2 · SETTLEMENTS', 'PYQ'}
def _H(bl, text, start=0):
    for i in range(start, len(bl)):
        if bl[i][0] == 'h' and re.sub(r'\s+', ' ', bl[i][2]).strip() == text: return i
    raise KeyError(text)
def _marks(bl):
    M = {}
    for k, t in (('dem', '1 · DEMOGRAPHY'), ('pyr', 'Population Pyramids'), ('mal', 'Population Theory of Malthus'), ('dtt', 'Demographic Transition Theory'), ('tri', 'MAJOR TRIBES OF INDIA'), ('pq', 'PYQ'), ('set', '2 · SETTLEMENTS')):
        M[k] = _H(bl, t, M.get('dem', 0))
    M['rec'] = _H(bl, 'Recall sheet', M['set'])
    return M
_KEEP = ('The Niyamgiri hill range', 'Niyamgiri is an area', 'The Changpa or Champa', 'Most of the regions', 'As of 1989')
def drop(bl):
    """PYQ block (questions, options, answers, the five missed Indian-Geography questions) goes to the PYQ block; the explanatory tribe bullets stay in the notes."""
    M = _marks(bl); d = set()
    for i in range(M['pq'], M['set']):
        if bl[i][0] == 'li' and re.sub(r'\s+', ' ', bl[i][2]).startswith(_KEEP): continue
        if bl[i][0] in ('p', 'h', 'li'): d.add(i)
    return d
def sections(bl):
    M = _marks(bl)
    return [
     ('Demography', [(M['dem'], M['pyr'])], UND[0], '<b>TFR is per woman, not per 1,000 people</b>: average live births over her child-bearing years; replacement 2.1 (India 2.0 NFHS-5, 1.9 SRS). Working age 15-64; dividend 56% (2022-23) → 68.9% in 2030.'),
     ('Population pyramids', [(M['pyr'], M['mal'])], UND[1], 'The base tells the future: <b>Nigeria Nests many children (wide), Japan is Narrow at the foot (constricted), the US is Neat and straight (stationary)</b>. India: expansive, base stabilising.'),
     ('Malthus’s population theory', [(M['mal'], M['dtt'])], UND[2], 'People multiply (2, 4, 8, 16), food only adds (1, 2, 3, 4). <b>Preventive = Planned</b> (we cut births: restraint, contraception); <b>Positive = Painful</b> (famine, disease, war raise deaths).'),
     ('Demographic transition theory', [(M['dtt'], M['tri'])], UND[3], '<b>Doctors come before Decisions</b>: in Stage 2 deaths fall first (healthcare, sanitation) while births stay high, so the population booms; births fall later (Stage 3). India: late expanding.'),
     ('Major tribes of India', [(M['tri'], M['set'])], UND[4], 'Tribe = State pair. <b>Limbu–Sikkim and Dongria–Odisha are right; Karbi–Himachal and Bonda–Tamil Nadu are wrong.</b> Changpa = Changtang in Ladakh (not Uttarakhand), rearing pashmina animals.'),
     ('Rural and urban settlements', [(M['set'], M['rec'])], UND[5], 'Rural (recall-sheet order): <b>compact → semi-compact → hamleted → dispersed</b>. Urban ladder: <b>town, city, metropolis, megacity (&gt;10 million), conurbation, megalopolis</b>.')]
SEC_PYQ = {0: '2 undated', 4: '2013, 2014'}
EXTRA = {
 1: [{'tbl': {'cap': 'Three pyramid shapes at a glance (handout)', 'head': ['Pyramid', 'Base', 'Middle and top', 'Growth', 'Example'], 'rows': [
      ['Expansive', 'Broad: many young', 'Narrow top: few old', 'Rapid', 'Nigeria; India (expansive, base stabilising)'],
      ['Constricted', 'Narrow: low birth rate', 'Bulging middle: large working-age group', 'Slowing down', 'Japan'],
      ['Stationary', 'Roughly equal across all age groups', 'Except the very old', 'Stable or very slow', 'USA']]}}],
 3: [{'tbl': {'cap': 'Five stages of the demographic transition (handout)', 'head': ['Stage', 'Birth rate', 'Death rate', 'Growth', 'Example'], 'rows': [
      ['1 High stationary', 'High', 'High', 'Slow, fluctuating', 'Societies before the 18th century; primitive tribal societies'],
      ['2 Early expanding', 'High', 'Declining', 'Rapid', 'Many developing countries in Africa'],
      ['3 Late expanding', 'Declining', 'Low', 'Slowing', 'India, Brazil'],
      ['4 Low stationary', 'Low', 'Low', 'Stable or declining', 'United States, much of Europe'],
      ['5 Decline (proposed)', 'Very low', 'Low', 'Declining', 'Japan, South Korea, Germany, Italy (some demographers)']]}}],
 5: [{'tbl': {'cap': 'Four types of rural settlement (handout)', 'head': ['Type', 'Relief and climate', 'Where (handout)'], 'rows': [
      ['Compact / nucleated', 'Favourable relief + favourable climate; houses closely packed', 'North Indian Plains, wet points in Rajasthan, Bundelkhand, Nagaland'],
      ['Semi-compact', 'Favourable relief + less favourable climate; transitional', 'Indus Basin, Gujarat Plains, parts of Rajasthan Plains'],
      ['Hamleted', 'Fragmented into separate units (panna, para, palli, nagla, dhani)', 'Ganga plains, lower Himalayan valleys, Chhattisgarh Plains, parts of South India'],
      ['Dispersed', 'Bad climate and relief; houses spread over a large area', 'Himalayan region (Uttarakhand, Himachal Pradesh, Ladakh), Meghalaya']]}},
     {'call': {'kind': 'note', 'tag': 'Connects to', 'body': [
      '<b>Indian Geography</b>: Changpa and Ladakh, Dongria and Niyamgiri, Thar and Himalaya settlements. <b>Economic Geography</b>: labour, agriculture, urban industry.',
      'Mains hooks named in the handout: demographic dividend, ageing, urbanisation, gentrification, climate-driven settlement shifts.']}}],
}
LENS = {
 'prelims': ['definitions: TFR, sex ratio, dependency ratio (TFR asked)', 'where-is-which tribe: tribe–State pairs (2013, 2014)', 'the five DTT stages as a birth-rate / death-rate table', 'Malthus: geometric versus arithmetic; preventive versus positive checks', 'countries known for low birth rate and ageing (undated PYQ)'],
 'mains': ['demographic dividend: 56% in 2022-23, peak 68.9% in 2030', 'ageing, low fertility and the second demographic dividend', 'urbanisation, urban sprawl, slums and gentrification', 'climate-driven shift of settlements (coastal villages moved inland)'],
 'close': 'A short, concept-heavy chapter. Prelims asks exact definitions (TFR is per woman), tribe–State pairs and the stage logic of the transition theory. Learn the ratios and the stage table; use the Mains hooks for dividend, ageing and urbanisation.'}
SIMPLE = [
 '**Demography** counts people and how fast the count changes; the key terms (TFR, IMR, sex ratio, dependency ratio) are simple ratios.',
 'A **population pyramid** is a bar chart of age and sex: a wide base means growth, a narrow base means ageing.',
 '**Malthus** said people multiply faster than food; shortage comes unless **preventive** or **positive** checks act.',
 'The **demographic transition** runs from high births and deaths, to deaths falling first, to both low; India is in the late expanding stage.',
 '**Rural settlements** are classed by closeness of houses and by pattern; **urban** ones by size and function (town to megalopolis).']
TERMS = [('Total Fertility Rate', 'Average live births a woman has over her child-bearing years; replacement is 2.1.'), ('IMR', 'Deaths of infants under one year per 1,000 live births.'), ('Sex ratio', 'Females per 1,000 males in India (2011: 943).'), ('Child sex ratio', 'Sex ratio in the 0-6 age group (2011: 914).'), ('Dependency ratio', 'Dependants (0-14 and above 65) to the working-age group.'), ('Demographic dividend', 'Working-age group much larger than the dependants.'), ('Second demographic dividend', 'Fewer children and longer life bring savings that can be invested.'), ('Expansive pyramid', 'Broad base, narrow top: rapid growth.'), ('Preventive checks', 'Moral restraint and contraception: fewer births, under our control.'), ('Positive checks', 'Famine, disease, war: more deaths, not under our control.'), ('Conurbation', 'Several towns or cities and suburbs merged into one urban area.'), ('Gentrification', 'Redevelopment that raises property values and displaces poorer residents.')]
REMEMBER = 'Per woman, deaths fall first, tribe by State.'
VISUALS = [
 {'type': 'mindmap', 'pos': 'top', 'title': 'Human Geography at a glance', 'center': 'People and places', 'branches': [
   {'t': 'Demography', 'c': ['Growth factors', 'Distribution', 'TFR, IMR, sex ratio', 'Dependency, dividend']},
   {'t': 'Pyramids', 'c': ['Expansive: Nigeria, India', 'Constricted: Japan', 'Stationary: USA']},
   {'t': 'Theories', 'c': ['Malthus: checks', 'DTT: five stages', 'India: late expanding']},
   {'t': 'Tribes', 'c': ['State-wise table', 'Limbu, Dongria', 'Changpa: Ladakh']},
   {'t': 'Settlements', 'c': ['Rural: factors, types, patterns', 'Urban: town to megalopolis', 'Sprawl, slum, gentrification']}]},
 {'type': 'mnemonic', 'after': 'Factors Affecting Settlements', 'title': 'Factors behind rural settlements (order is free)', 'label': 'Memory aid', 'word': 'PEEPS',
  'hook': 'Village “peeps” (people) settle where physical, economic, environmental, political and social conditions suit them.',
  'letters': [['P', 'Physical (topography, climate, water, soil, resources)'], ['E', 'Economic (productivity, jobs, transport)'], ['E', 'Environmental (natural disasters, climate change)'], ['P', 'Political (policies, security)'], ['S', 'Social and cultural (kinship, practices, land ownership)']],
  'note': 'Rearranged initials of an unordered list. Own memory aid, not from the handout.'},
 {'type': 'mnemonic', 'after': 'Terminologies associated', 'title': 'Urban ladder, smallest to largest', 'label': 'Memory aid', 'sentence': 'Tiny Cafes Make Many Cozy Moments',
  'letters': [['T', 'Town'], ['C', 'City'], ['M', 'Metropolis'], ['M', 'Megacity (>10 million)'], ['C', 'Conurbation'], ['M', 'Megalopolis']],
  'note': 'Order follows the handout’s recall sheet (the body lists megacity before metropolis). Own memory aid, not from the handout.'},
 {'type': 'mnemonic', 'after': 'Demographic Transition in India', 'title': 'Order of the five DTT stages', 'label': 'Memory aid', 'sentence': 'Hungry Eaters Learn Lighter Diets',
  'letters': [['H', 'High stationary'], ['E', 'Early expanding'], ['L', 'Late expanding'], ['L', 'Low stationary'], ['D', 'Decline (proposed)']],
  'note': 'Order kept: it is the order of the stages. Own memory aid, not from the handout.'},
]
RECALL = [[html.unescape(q), html.unescape(a)] for q, a in [
 ('Replacement TFR; India now?', '2.1; 2.0 (NFHS-5), 1.9 (SRS)'), ('Only states with TFR above 2.1?', 'Bihar, Meghalaya, UP, Jharkhand, Manipur'), ('India’s TFR projected for 2050?', '1.29'),
 ('Sex ratio 2011 and child sex ratio 2011?', '943; 914 (NFHS-5: 1020; 920)'), ('Working-age group; dependants?', '15-64; 0-14 and above 65'), ('Demographic dividend in India?', '56% (2022-23); peak 68.9% in 2030'),
 ('Global population peak (UN)?', '10.3 billion, mid-2080s'), ('India’s population peak (UN)?', '1.7 billion, early 2060s'), ('Pyramid examples?', 'Expansive: Nigeria, India; constricted: Japan; stationary: USA'),
 ('Malthus: growth of people and food?', 'Geometric (2, 4, 8, 16); arithmetic (1, 2, 3, 4)'), ('Which DTT stage has deaths falling, births high?', 'Stage 2, early expanding'), ('India in the DTT?', 'Stage 3, late expanding (since 1981)'),
 ('Megacity size?', 'More than 10 million'), ('Rural settlement order (recall sheet)?', 'Compact, semi-compact, hamleted, dispersed')]]
TRAPS = [
 {'k': 'Trap', 't': 'TFR is not the birth rate', 'd': 'The wrong options give “children per 1,000 people” or “birth rate minus death rate”. TFR is average live births per woman over her child-bearing years.', 'r': 'Exam-hall rule: TFR means per woman, over a lifetime.'},
 {'k': 'Trap', 't': 'Sex ratio direction', 'd': 'Sex ratio in India is females per 1,000 males; the world often counts the other way round.', 'r': 'Exam-hall rule: for India write females per 1,000 males (943 in 2011).'},
 {'k': 'Trap', 't': 'Who falls first in DTT', 'd': 'The wording “former before latter” (fertility before mortality) is misleading: the death rate falls first.', 'r': 'Exam-hall rule: Stage 2 means deaths down, births still high.'},
 {'k': 'Trap', 't': 'Changpa, Karbi, Bonda', 'd': 'Changpa live mainly in Ladakh (Changtang), not Uttarakhand. Karbi is not Himachal; Bonda is not Tamil Nadu.', 'r': 'Exam-hall rule: Limbu–Sikkim and Dongria–Odisha are the safe pairs.'},
 {'k': 'Trap', 't': 'Low-birth-rate countries', 'd': 'The undated PYQ answer is Italy, Japan and South Korea; Nigeria and South Africa are not in it.', 'r': 'Exam-hall rule: ageing and shrinking = Italy, Japan, South Korea.'},
 {'k': 'Handout conflict', 't': 'Constricted pyramid', 'd': 'The points say “narrow top, fewer elderly”, but the Japan example says the top is wider than the base, an ageing population.', 'r': 'Exam-hall rule: remember it as narrow base, bulging middle, slowing growth; Japan is the example.'},
 {'k': 'Handout conflict', 't': 'Changpa wording and the state-border PYQ', 'd': 'The Changpa statement says pashmina goats while the handout’s note says pashmina sheep (answer B stands). The state-border question prints answer (a), but its explanation marks statements 2 and 3 as wrong, which would be (c).', 'r': 'Exam-hall rule: use the printed answers (B, a) and verify the border question in the Indian chapter.'},
 {'k': 'Handout conflict', 't': 'Tribe table and urban ladder', 'd': 'The State-wise tribe table does not show Limbu, Karbi, Dongria or Bonda by those names. The urban terms list megacity before metropolis, but the recall sheet puts metropolis first.', 'r': 'Exam-hall rule: learn the PYQ pairs from the PYQ page; keep the recall-sheet ladder.'}]
QUIZ = [
 {'q': 'The total fertility rate is best defined as:', 'o': ['Births per 1,000 people in a year', 'Average live births a woman has by the end of her child-bearing age', 'Birth rate minus death rate', 'Children born to a couple in a lifetime'], 'a': 1},
 {'q': 'In the demographic transition, which stage has a high birth rate and a declining death rate?', 'o': ['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4'], 'a': 1},
 {'q': 'Malthus’s positive checks:', 'o': ['reduce births by moral restraint', 'reduce births by contraception', 'raise the death rate through famine, disease and war', 'raise food supply by technology'], 'a': 2},
 {'q': 'Which country is the handout’s example of a constricted pyramid?', 'o': ['Nigeria', 'Japan', 'USA', 'India'], 'a': 1},
 {'q': 'The Changpa community lives mainly in:', 'o': ['Uttarakhand', 'Sikkim', 'Ladakh (Changtang)', 'Odisha'], 'a': 2},
 {'q': 'A megacity is an urban area with a population of more than:', 'o': ['1 million', '5 million', '10 million', '50 million'], 'a': 2}]
PYQBLOCK = {'intro': '4 Prelims PYQs on this chapter and 5 undated Indian-Geography Prelims PYQs the handout reprints at its end, with the handout’s own answers; no Mains PYQ is quoted', 'groups': [
 {'title': 'Tribes and States', 'count': '2 Prelims', 'prelims': [
   {'year': '2013', 'blocks': [('q', 'Consider the following pairs:'), ('s', 'Limboo (Limbu): Sikkim'), ('s', 'Karbi: Himachal Pradesh'), ('s', 'Dongaria: Odisha'), ('s', 'Bonda: Tamil Nadu'), ('q', 'Which of the above pairs are correctly matched?')], 'opts': ['1 and 3 only', '1 and 2 only', '2 and 3 only', '1, 2, 3 and 4'], 'ans': 'a', 'anstext': 'The Limbu are the Kirati people of the Limbuwan region, including Northern Sikkim; the Dongria Kondh live in the Niyamgiri hills of Odisha.'},
   {'year': '2014', 'blocks': [('q', 'With reference to the “Changpa” community of India, consider the following statements:'), ('s', 'They live mainly in the State of Uttarakhand.'), ('s', 'They rear the Pashmina goats that yield fine wool.'), ('s', 'They are kept in the category of Scheduled Tribes.'), ('q', 'Which of the statements given above is/are correct?')], 'opts': ['1 only', '2 and 3 only', '3 only', '1, 2 and 3'], 'ans': 'b', 'anstext': 'The Changpa are a semi-nomadic Tibetan people of the Changtang in Ladakh, so statement 1 is wrong.'}]},
 {'title': 'Fertility and ageing', 'count': '2 Prelims', 'prelims': [
   {'year': 'undated', 'blocks': [('q', 'The total fertility rate in an economy is defined as:')], 'opts': ['The number of children born per 1000 people in the population in a year.', 'The number of children born to a couple in their lifetime in a given population.', 'The birth rate minus death rate.', 'The average number of live births a woman would have by the end of her child-bearing age.'], 'ans': 'd', 'anstext': 'TFR is per woman across her child-bearing years (the handout’s own answer).'},
   {'year': 'undated', 'blocks': [('q', 'Consider the following countries:'), ('s', 'Italy'), ('s', 'Japan'), ('s', 'Nigeria'), ('s', 'South Korea'), ('s', 'South Africa'), ('q', 'Which of the above countries are frequently mentioned in the media for their low birth rates, or ageing population or declining population?')], 'opts': ['1, 2 and 4', '1, 3 and 5', '2 and 4 only', '3 and 5 only'], 'ans': 'a', 'anstext': 'Italy, Japan and South Korea; Nigeria and South Africa are not in it (handout’s trap note).'}]},
 {'title': 'Missed Indian-Geography questions', 'count': '5 Prelims', 'prelims': [
   {'year': 'undated', 'blocks': [('q', 'With reference to the climate of Andaman and Nicobar Islands, which of the following statements is/are correct?'), ('s', 'The climate can be defined as a humid, tropical coastal climate.'), ('s', 'It receives rainfall from both South-west monsoon and North-east monsoon.'), ('s', 'Maximum precipitation is between December and May.')], 'opts': ['1 only', '1 and 2', '2 and 3', '3 only'], 'ans': 'b', 'anstext': 'Humid tropical maritime climate; both monsoon winds are onshore; maximum rainfall is in the South-West Monsoon months, May to September.'},
   {'year': 'undated', 'blocks': [('q', 'Which of the following geographical features or phenomena is/are associated with the Peninsular Block of India?'), ('s', 'Submergence of parts of the western coast due to tectonic activity'), ('s', 'Presence of residual mountain ranges such as the Veliconda Hills and Mahendragiri Hills'), ('s', 'Deep, V-shaped river valleys formed by fast-flowing rivers')], 'opts': ['1 only', '1 and 2', '2 and 3', '3 only'], 'ans': 'b', 'anstext': 'Ancient stable landmass with parts of the western coast submerged; Eastern Ghats are denuded; most peninsular rivers are mature, over old hard rocks.'},
   {'year': 'undated', 'blocks': [('q', 'Which of the following best explain(s) the rationale for protecting mangrove ecosystems in the context of coastal regions?'), ('s', 'Mangroves reduce tidal energy and store freshwater, making them ideal sites for paddy cultivation in saline zones.'), ('s', 'Their salt-sensitive roots filter seawater, making mangroves key to converting coastal land into freshwater zones.'), ('s', 'By withstanding tidal surges and offering biomass resources, mangroves function both as natural bio-shields and as sources of livelihood.')], 'opts': ['1 only', '1 and 2', '2 and 3', '3 only'], 'ans': 'd', 'anstext': 'Mangroves do not store salt water, and their roots are salt tolerant, not salt sensitive (a play on words).'},
   {'year': 'undated', 'blocks': [('q', 'Identify the river of the Indian sub-continent on the basis of the following information:'), ('s', 'It has an antecedent drainage system.'), ('s', 'It flows through three countries.'), ('s', 'It originates in the Tibetan Plateau and is an important river for irrigation.'), ('s', 'It does not form distributaries.')], 'opts': ['Brahmaputra', 'Indus', 'Sutlej', 'Teesta'], 'ans': 'c', 'anstext': 'By elimination: Brahmaputra and Indus have distributaries; the Teesta originates in Sikkim.'},
   {'year': 'undated', 'blocks': [('q', 'Which of the following with reference to Indian States is/are not correct?'), ('s', 'Uttar Pradesh shares its boundary with the highest number of other Indian States.'), ('s', 'Rajasthan shares the longest international border among all Indian States.'), ('s', 'Sikkim is the only State that shares its boundary with just one other Indian State.')], 'opts': ['1 only', '1 and 2', '2 and 3', '3 only'], 'ans': 'a', 'anstext': 'Printed answer (a). Handout conflict: its explanation (West Bengal has the longest international border; Meghalaya also touches only one State) marks 2 and 3 as wrong, which would be (c).'}]}]}
NUMBERS = [('2.1', 'replacement TFR'), ('2.0 / 1.9', 'India TFR: NFHS-5 / SRS'), ('1.29', 'India TFR projected for 2050'), ('943 / 914', 'sex ratio / child sex ratio, 2011'), ('15-64', 'working-age group (years)'), ('56% → 68.9%', 'dividend: 2022-23 → 2030'), ('10.3 bn · mid-2080s', 'world population peak (UN)'), ('1.7 bn · early 2060s', 'India population peak (UN)'), ('> 10 million', 'megacity'), ('62.18%', 'Asia’s share of world population, 2025')]
