# -*- coding: utf-8 -*-
import sys, os, re, html
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src-gov', 'handnotes', 'found', 'geography'))
import detail_data as DD
UND = DD.UND[3]
TITLE = 'Oceanography'; PAGES = 'Handout pp. 1-29'; PRIORITY = 'H'; PYQS = '2017'; PRELIMS = '2013 ×2, 2015 ×2, 2021 ×2'
SKIP_H = {'1 · OCEANS AND THEIR RELIEF', '3 · OCEAN MOVEMENTS: OCEAN CURRENTS', '2 · PYQ', '4 · PYQ', 'PYQ', 'CRYOSPHERE', 'CORAL REEFS', 'OCEANIC DEPOSITS', 'DEAD ZONES', 'OCEAN RESOURCES:', 'LAW OF SEA', 'Ocean Movements: Tides'}
def _H(bl, text, start=0):
    for i in range(start, len(bl)):
        if bl[i][0] == 'h' and re.sub(r'\s+', ' ', bl[i][2]).strip() == text: return i
    raise KeyError(text)
def _Q(bl, a, b): return [i for i in range(a, b) if bl[i][0] == 'p' and re.match(r'Q\.\d', bl[i][2])]
def _marks(bl):
    M = {}
    for k, t in (('oc', '1 · OCEANS AND THEIR RELIEF'), ('tsd', 'Properties Of The Oceanic Water: Temperature'), ('fw', '2 · PYQ'), ('cur', '3 · OCEAN MOVEMENTS: OCEAN CURRENTS'), ('tide', 'Ocean Movements: Tides'), ('cry', 'CRYOSPHERE'), ('pq4', '4 · PYQ'), ('coral', 'CORAL REEFS'), ('dep', 'OCEANIC DEPOSITS'), ('dz', 'DEAD ZONES'), ('res', 'OCEAN RESOURCES:'), ('law', 'LAW OF SEA'), ('pq', 'PYQ'), ('rec', 'Recall sheet')):
        M[k] = _H(bl, t, M.get('oc', 0))
    # the heading 'PYQ' also matches inside earlier text only once after LAW OF SEA
    M['pq'] = _H(bl, 'PYQ', M['law']); M['rec'] = _H(bl, 'Recall sheet', M['pq'])
    return M
def drop(bl):
    M = _marks(bl); d = set()
    for a, b in ((M['fw'], M['cur']), (M['pq4'], M['coral']), (M['pq'], M['rec'])):
        for i in range(a, b):
            if bl[i][0] in ('p', 'h'): d.add(i)
    return d
def sections(bl):
    M = _marks(bl); q4 = _Q(bl, M['pq4'], M['coral']) + [M['coral']]
    return [
     ('Oceans and their relief', [(M['oc'], M['tsd'])], UND[0], 'Coast to deep: <b>Shelf → Slope → Rise → Abyssal plain → Trench</b>. Shelf 1-2°, slope 3-6°, trenches deeper than 6,000 m (Mariana); average ocean depth 3,800 m.'),
     ('Temperature, salinity, density', [(M['tsd'], M['fw'])], UND[1], '<b>Sun + No Rain = Salty</b>: subtropics are saltiest. Cold, salty water is heavier; temperature drives density more than salinity. Mean temperature: 26.7 °C at the equator, 12.7 °C at 45°.'),
     ('Freshwater', [(M['fw'], M['cur'])], UND[2], 'Order of the fresh water: <b>ice caps and glaciers &gt; groundwater &gt; rivers and lakes</b>. The handout prints surface water as 0.3% once and about 1% once.'),
     ('Ocean currents', [(M['cur'], M['tide']), (q4[0], q4[1]), (q4[2], q4[3])], UND[3], '<b>West = Warm &amp; Wild</b> (narrow, fast); <b>East = cold &amp; Easygoing</b> (broad, slow, upwelling). The counter-current flows east because the two equatorial currents pile water up.'),
     ('Tides and waves', [(M['tide'], M['cry']), (q4[1], q4[2])], UND[4], 'Tides = <b>Moon + Sun + Earth’s centrifugal force</b>; spring tide when the three are in one line (new and full moon). In a wave the energy travels, the water only circles.'),
     ('Cryosphere', [(M['cry'], M['pq4'])], UND[5], 'Ice does three jobs: <b>store</b> of fresh water, <b>mirror</b> (albedo), <b>lid</b> over trapped gases. Melting breaks all three.'),
     ('Coral reefs', [(M['coral'], M['dep'])], UND[6], 'Reef needs <b>20-29 °C · clear · shallow (&lt;50 m) · salinity 32-40 ppt · low nutrients · moderate waves</b>. Fringing = Friend, Barrier = Bodyguard, Atoll = Wedding ring.'),
     ('Oceanic deposits', [(M['dep'], M['dz'])], UND[7], '<b>Land, Life, Liquid, Cosmos</b>: terrigenous, biogenous, hydrogenous, cosmogenous.'),
     ('Dead zones', [(M['dz'], M['res'])], UND[8], 'Run-off nutrients → algal bloom → algae die and sink → bacteria use up the oxygen → <b>hypoxic dead zone</b>.'),
     ('Ocean resources and fishing grounds', [(M['res'], M['law']), (M['pq'], M['rec'])], UND[9], 'Best fishing grounds: where a <b>warm and a cold current meet</b>, so plankton are mixed up (Newfoundland banks, Sea of Japan).'),
     ('Law of the sea: UNCLOS 1982', [(M['law'], M['pq'])], UND[10], '<b>12 · 24 · 200</b>: territorial sea 12 nm, contiguous zone 24 nm, EEZ 200 nm; beyond that, the high seas.')]
SEC_PYQ = {1: '2017', 2: '2013, 2021', 3: '2015, 2021', 4: '2015', 8: '2013', 9: '2013'}
EXTRA = {
 1: [{'call': {'kind': 'note', 'tag': 'Mains skeleton · 2017 (15 marks): variations in oceanic salinity and its effects', 'body': [
      '<b>Intro:</b> sea water is a solution of dissolved salts; average about 35 ppt, deep water about 34.7.',
      '<b>Body (variation):</b> latitude (subtropical high), evaporation versus rain, river water, sea ice, currents, inland seas (Great Salt Lake 220, Dead Sea 240, Lake Van 330).',
      '<b>Body (effects):</b> density → thermohaline circulation; stratification (halocline); nutrients, habitats and productivity.',
      '<b>Close:</b> melting-ice fresh water is now altering salinity and circulation.']}}],
 8: [{'h': 'How a dead zone forms (memory aid)'}],
 10: [{'h': 'UNCLOS belts (memory aid)'}],
 9: [{'call': {'kind': 'note', 'tag': 'Connects to', 'body': [
      'Trenches, guyots, hotspots → <b>Geomorphology</b>. Coriolis, trade winds, westerlies, cyclones, El Niño → <b>Climatology</b> and Indian climate.',
      'Resources, ports, fisheries → <b>Economic Geography</b>. Palk Strait, Chilika, Gulf of Kutch, Cape Comorin → <b>Indian Geography</b>.']}}],
}
LENS = {
 'prelims': ['why the equatorial counter-current flows east (convergence, not rotation)', 'what causes tides: Sun, Moon and centrifugal force together', 'freshwater order: ice, then groundwater, then rivers and lakes', 'west warmer in the tropics, east warmer in the temperate zone', 'where fishing grounds sit: warm and cold currents meeting', 'UNCLOS belts: 12, 24 and 200 nm'],
 'mains': ['variations in oceanic salinity and their multi-dimensional effects (2017, 15 marks)', 'AMOC weakening and what it does to climate', 'coral bleaching, dead zones, marine heatwaves: causes, effects, remedies', 'cryosphere melt and its effect on oceans and cities'],
 'close': 'The exam asks why, not what: why the counter-current flows east, why tides occur, why fishing grounds sit where warm and cold currents meet. Learn the cause chain in each topic and the current-affairs themes (AMOC, corals, dead zones) for Mains.'}
SIMPLE = [
 'The sea floor steps down from the **shelf** to the **slope**, the **rise**, the **abyssal plain** and the **trench**.',
 'Three properties of sea water, **temperature, salinity and density**, decide where water sinks and where it flows.',
 'Almost all water is salty. Of the fresh water, most is **ice**, then **groundwater**; rivers and lakes hold very little.',
 '**Currents** are one-way rivers in the sea (wind + Coriolis + continents); **tides** come from Moon, Sun and centrifugal force; **waves** carry energy, not water.',
 '**Corals**, **dead zones** and the melting **cryosphere** show how warming and pollution hurt the ocean; **UNCLOS** sets who may use which belt of sea.']
TERMS = [('Continental shelf', 'The gently sloping sea floor next to land (1-2°).'), ('Abyssal plain', 'The wide, flat deep-ocean floor.'), ('Salinity', 'Dissolved salt in sea water, about 35 ppt on average.'), ('Thermohaline circulation', 'Slow deep circulation driven by temperature and salt differences.'), ('Gyre', 'A big loop of ocean current.'), ('Upwelling', 'Cold, nutrient-rich water rising to the surface.'), ('Spring tide', 'Highest high tide, when Sun, Moon and Earth are in one line.'), ('Neap tide', 'Weak tide when Sun and Moon pull at right angles.'), ('Bleaching', 'A stressed coral expels its alga and turns white.'), ('Hypoxia', 'Oxygen so low that most life cannot survive (a dead zone).'), ('EEZ', 'Exclusive Economic Zone: coastal State’s resource rights up to 200 nm.'), ('AMOC', 'Atlantic Meridional Overturning Circulation, a deep-water conveyor.')]
REMEMBER = 'Coast to deep, warm meets cold, 12-24-200.'
VISUALS = [
 {'type': 'mindmap', 'pos': 'top', 'title': 'Oceanography at a glance', 'center': 'Oceans', 'branches': [
   {'t': 'Relief', 'c': ['Shelf, slope, rise', 'Abyssal plain', 'Trench']},
   {'t': 'Water properties', 'c': ['Temperature', 'Salinity', 'Density', 'Acidification']},
   {'t': 'Movements', 'c': ['Currents, gyres, AMOC', 'Tides', 'Waves, rogue waves, seiches']},
   {'t': 'Life and ice', 'c': ['Coral reefs', 'Dead zones', 'Cryosphere']},
   {'t': 'Resources and law', 'c': ['Deposits', 'Fishing grounds', 'UNCLOS 12 · 24 · 200']}]},
 {'type': 'mnemonic', 'after': 'Oceanic Relief Features', 'title': 'Order of the ocean floor', 'sentence': 'Sailors Seldom Rest Above Trenches', 'label': 'Memory aid',
  'letters': [['S', 'Shelf'], ['S', 'Slope'], ['R', 'Rise'], ['A', 'Abyssal plain'], ['T', 'Trench']], 'note': 'Order kept: it is the order you meet them going from coast to deep. Own memory aid, not from the handout.'},
 {'type': 'fork', 'after': 'Types of currents', 'title': 'Two sides of an ocean', 'root': {'t': 'Ocean basin currents', 'c': ['Wind + Coriolis + continents']}, 'branches': [
   {'t': 'West = Warm & Wild', 'c': ['Gulf Stream, Kuroshio, Brazil, East Australian, Agulhas', 'warm, narrow, fast, strong'], 'verdict': 'Western boundary currents'},
   {'t': 'East = cold & Easygoing', 'c': ['Canary, Benguela, California, Peru, West Australian', 'cold, broad, slow, upwelling'], 'verdict': 'Eastern boundary currents'}]},
 {'type': 'flow', 'after': 'How a dead zone forms (memory aid)', 'title': 'How a dead zone forms', 'per_row': 3, 'steps': [['Nutrient run-off', 'nitrogen and phosphorus'], ['Algal bloom', 'rapid algae growth'], ['Algae die and sink', 'decompose on the bottom'], ['Bacteria use oxygen', 'oxygen falls'], ['Dead zone', 'hypoxic water']]},
 {'type': 'flow', 'after': 'UNCLOS belts (memory aid)', 'title': 'UNCLOS belts, coast outward', 'per_row': 4, 'steps': [['Territorial sea', '12 nm (22.2 km)'], ['Contiguous zone', '24 nm (44.4 km): customs, fiscal, immigration, sanitary laws'], ['EEZ', '200 nm (370.4 km): sovereign rights over resources'], ['High seas', 'beyond: navigation, overflight, fishing, research']]},
]
RECALL = [[html.unescape(q), html.unescape(a)] for q, a in [
 ('Average ocean depth; shelf and slope gradient?', '3,800 m; 1-2° / 3-6°'), ('Trench depth; example?', '&gt; 6,000 m; Mariana'), ('Mean temperature equator vs 45°?', '26.7 °C / 12.7 °C'),
 ('Saltiest listed water bodies?', 'Lake Van 330 &gt; Dead Sea 240 &gt; Great Salt Lake 220'), ('Ocean pH now?', '8.04 (2024); pre-industrial 8.2'),
 ('Why does the counter-current flow east?', 'Convergence/pile-up of the two equatorial currents'), ('Only sea with no coastline?', 'Sargasso Sea (N Atlantic gyre)'),
 ('Tide repeats after; spring tide when?', '12 h 26 min; new and full moon (syzygy)'), ('Tidal bore in India; world’s biggest?', 'Hooghly; Qiantang (China)'),
 ('Tsunami speed in deep ocean?', '500-1,000 km/h, under 1 m high'), ('Coral temperature / depth / salinity?', '20-29 °C / &lt;50 m / 32-40 ppt'), ('UNCLOS zones?', '12 · 24 · 200 nm')]]
TRAPS = [
 {'k': 'Trap', 't': 'Counter-current and Earth’s rotation', 'd': 'The equatorial counter-current is not caused by the Earth’s rotation directly.', 'r': 'Exam-hall rule: pick “convergence (pile-up) of the two equatorial currents”.'},
 {'k': 'Trap', 't': 'Salinity at the equator', 'd': 'Salinity is not highest at the equator: the subtropics are saltiest; equator and poles are diluted.', 'r': 'Exam-hall rule: high salinity = hot, dry, low-rain belts.'},
 {'k': 'Trap', 't': 'What drives density', 'd': 'Density is driven more by temperature than by salinity.', 'r': 'Exam-hall rule: temperature first, salinity second.'},
 {'k': 'Trap', 't': 'Freshwater after ice', 'd': 'Rivers and lakes do not hold most fresh water after ice; groundwater does.', 'r': 'Exam-hall rule: ice, groundwater, then surface water.'},
 {'k': 'Trap', 't': 'Spring tide and atolls', 'd': 'Spring tide is not a tide in spring (it is Sun-Moon-Earth in line); atolls form on sinking volcanic islands, not on continents.', 'r': 'Exam-hall rule: read the word by its cause, not its name.'},
 {'k': 'Handout conflict', 't': 'Surface water share', 'd': 'Surface water is printed as 0.3% in one note and about 1% in another; the 4th mass bleaching event starts in January 2023 once and February 2023 once.', 'r': 'Exam-hall rule: the ranking (ice, groundwater, surface) decides the answer, not the exact percentage.'}]
QUIZ = [
 {'q': 'Which belt gives the coastal State sovereign rights over resources up to 200 nautical miles?', 'o': ['Territorial sea', 'Contiguous zone', 'Exclusive Economic Zone', 'High seas'], 'a': 2},
 {'q': 'Western boundary currents of oceans are generally:', 'o': ['cold, broad and slow', 'warm, narrow and fast', 'cold, narrow and fast', 'warm, broad and slow'], 'a': 1},
 {'q': 'Spring tides occur when:', 'o': ['Sun, Moon and Earth are in one line', 'the Moon is at right angles to the Sun', 'it is the spring season', 'the Earth is farthest from the Sun'], 'a': 0},
 {'q': 'A dead zone is a region of:', 'o': ['very high salinity', 'oxygen depletion after an algal bloom', 'extreme cold', 'coral growth'], 'a': 1},
 {'q': 'Which is a cold eastern boundary current?', 'o': ['Gulf Stream', 'Kuroshio', 'Canary', 'Agulhas'], 'a': 2}]
PYQBLOCK = {'intro': '6 Prelims PYQs and 1 Mains PYQ printed in the handout, with the handout’s own answers', 'groups': [
 {'title': 'Freshwater and ice', 'count': '2 Prelims', 'prelims': [
   {'year': '2013', 'blocks': [('q', 'On the planet earth, most of the freshwater exists as ice caps and glaciers. Out of the remaining freshwater, the largest proportion')], 'opts': ['is found in the atmosphere as moisture and clouds', 'is found in freshwater lakes and rivers', 'exists as groundwater', 'exists as soil moisture'], 'ans': 'c', 'anstext': 'Over 68 percent of fresh water is in ice caps and glaciers and just over 30 percent is groundwater.'},
   {'year': '2021', 'blocks': [('q', 'With reference to the water on the planet Earth, consider the following statements:'), ('s', 'The amount of water in the rivers and lakes is more than the amount of groundwater.'), ('s', 'The amount of water in polar ice caps and glaciers is more than the amount of groundwater.'), ('q', 'Which of the statements given above is/are correct?')], 'opts': ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 'ans': 'b', 'anstext': 'Polar ice caps and glaciers hold more water than groundwater; rivers and lakes hold far less.'}]},
 {'title': 'Currents and heat', 'count': '2 Prelims', 'prelims': [
   {'year': '2015', 'blocks': [('q', 'What explains the eastward flow of the equatorial counter-current?')], 'opts': ['The Earth’s rotation on its axis', 'Convergence of the two equatorial currents', 'Difference in salinity of the water', 'Occurrence of the belt of calm near the equator'], 'ans': 'b', 'anstext': 'Water piles up in the west where the two equatorial currents meet and flows back east.'},
   {'year': '2021', 'blocks': [('q', 'Consider the following statements:'), ('s', 'In the tropical zone, the western sections of the oceans are warmer than the eastern sections owing to the influence of trade winds.'), ('s', 'In the temperate zone, westerlies make the eastern sections of oceans warmer than the western sections.'), ('q', 'Which of the statements given above is/are correct?')], 'opts': ['1 only', '2 only', 'Both 1 and 2', 'Neither 1 nor 2'], 'ans': 'c', 'anstext': 'Both are correct, as the handout explains with trade winds and westerlies.'}]},
 {'title': 'Tides', 'count': '1 Prelims', 'prelims': [
   {'year': '2015', 'blocks': [('q', 'Tides occur in oceans and seas due to which among the following?'), ('s', 'Gravitational force of the Sun'), ('s', 'Gravitational force of the Moon'), ('s', 'Centrifugal force of the Earth'), ('q', 'Select the correct answer using the code given below')], 'opts': ['1 only', '2 and 3 only', '1 and 3 only', '1, 2 and 3'], 'ans': 'd', 'anstext': 'Combined gravity of Moon and Sun, with Earth’s rotation (centrifugal force).'}]},
 {'title': 'Fishing grounds', 'count': '1 Prelims', 'prelims': [
   {'year': '2013', 'blocks': [('q', 'The most important fishing grounds of the world are found in the regions where:')], 'opts': ['Warm and cold atmospheric currents meet', 'Rivers drain out large amounts of fresh water into the sea', 'Warm and cold oceanic currents meet', 'Continental shelf is undulating'], 'ans': 'c', 'anstext': 'Mixing of cold and warm currents encourages plankton growth (Newfoundland banks, Sea of Japan).'}]},
 {'title': 'Salinity (Mains)', 'count': '1 Mains', 'mains': [
   {'year': '2017', 'marks': '15', 'topic': 'Oceanic salinity', 'q': 'Account for variations in oceanic salinity and discuss its multi-dimensional effects.', 'chips': [['q', 'variations'], ['q', 'multi-dimensional effects'], ['n', 'salinity'], ['n', 'density'], ['n', 'temperature']]}]}]}
NUMBERS = [('3,800 m', 'average ocean depth'), ('1-2° / 3-6°', 'shelf / slope gradient'), ('> 6,000 m', 'trench (Mariana)'), ('35 ppt', 'average salinity'), ('26.7 °C / 12.7 °C', 'mean temperature, equator / 45°'), ('8.04', 'ocean pH (2024); 8.2 pre-industrial'), ('12 h 26 min', 'tide repeats after'), ('20-29 °C · <50 m · 32-40 ppt', 'coral reef limits'), ('12 · 24 · 200 nm', 'UNCLOS belts')]
