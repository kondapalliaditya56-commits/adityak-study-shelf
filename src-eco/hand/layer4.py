# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 4 (Basic concepts: PPF, goods and capital). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('Problem', 'limited resources, unlimited wants: someone must choose'),
           ('PPF', 'the best output you can sustain for each mix; a target, not a fact'),
           ('Two costs', 'MC = what you spend; OC = what you give up'),
           ('Two systems', 'free market (prices, invisible hand) vs command (planner, rent-seeking)'),
           ('Goods', 'private or public; final or intermediate; consumer or capital'),
           ('Capital', 'investment is a flow that adds to the capital stock: Net I = Gross I − Depreciation')],
 'words': [('Budget constraint', 'the resource that actually limits output (for a farmer it may be water, not seeds)'),
           ('Technology', 'the current way of using resources: stone tools, iron tools, tractors'),
           ('Opportunity cost', 'the next best thing you give up when you choose'),
           ('Final good', 'a good whose economic identity is kept: nobody makes a new product for sale out of it'),
           ('Intermediate good', 'a good used as an input; it is merged into a new good that is sold'),
           ('Capital good', 'a machine or tool that helps production and lasts many cycles'),
           ('Stock and flow', 'a stock is how much you have now; a flow is how much moves in a period'),
           ('Depreciation', 'the loss in value of capital goods from wear and tear (not a real payment)')],
}
SEC = {
 '1': dict(
   plain='Picture a farmer with a fixed amount of water and a fixed tool kit. The economist cannot give him more water or fewer wishes. The economist only asks which things really limit him and which tools he has, and then lists the best he can sustain for every mix of crops. That list of best mixes is the PPF. Points on it are the target; points below waste something, and points beyond cannot be kept up.',
   eg='The handout’s own table: 8 hours of daylight. 10 deer and 0 berries at one end, 0 deer and 700 berries at the other. Each 2 fewer deer buys 200, then 180, 150, 100 and 70 more berries: each sacrifice buys less than the one before.',
   hook='PPF = the best you can SUSTAIN for each mix. Below: wasteful. Beyond: impossible. Better technology pushes it out.'),
 '2': dict(
   plain='Two different bills. Marginal cost is the bill you actually pay for one more unit: cement, steel, labour. Opportunity cost is the bill you never see: the hospital or school the same cement and steel could have built. The first stops you from over-reaching, because the best resources go first and each extra unit gets dearer. The second makes you look past the visible result to what was sacrificed.',
   eg='The handout’s stadium: MC = the cement, steel and labour bought. OC = the rural hospital or school the same resources could have built. Economics “has no morals”: it only shows the trade-off.',
   hook='MC = what you pay. OC = what you give up. Every choice is also a refusal.'),
 '3': dict(
   plain='Two ways to run a country’s resources. In a free market millions of people follow prices, and self-interest ends up serving others (the invisible hand), but people with more capital and luck pull ahead. In a command system an authority decides, hoping to be fair, but no planner can know millions of wants, so being connected starts to matter more than serving customers (rent-seeking). Both end in inequality, of different kinds.',
   eg='The handout quotes Milton Friedman: “A society that puts equality before freedom will get neither. A society that puts freedom before equality will get a high degree of both.” It adds that none of the systems is perfect.',
   hook='Market: prices + invisible hand, inequality of luck. Command: planner + licences, inequality of connections.'),
 '4': dict(
   plain='Goods are sorted by how buyers react. Change the price: necessary goods barely move (a steep curve), luxuries swing (a flat curve). Change income: normal goods rise, inferior goods fall. Change another good’s price: substitutes move with it, complements move against it. Sort by effect on society: merit goods are under-consumed, demerit goods over-consumed. Veblen and Giffen goods are the odd cases where a higher price brings more demand.',
   eg='The handout’s own cases: a basic motorcycle is normal in a low-income nation but inferior in a high-income one. Giffen: a worker spends 90% of income on coarse grain and 10% on meat; grain gets dearer, meat becomes unaffordable, so he buys more grain. The 2021 Prelims question is answered (a) 1 and 4 only.',
   hook='Four sorting keys: price, income, other price, effect on society. Giffen = inferior + huge share + no cheaper substitute.',
   mn=[dict(kind='word', title='Four ways to sort goods (order is free)', word='EPIC',
            letters=[('E', 'Effect on society (merit vs demerit)'), ('P', 'Price elasticity (necessary vs luxury)'),
                     ('I', 'Income elasticity (normal vs inferior)'), ('C', 'Cross-price (substitute vs complement)')],
            note='Own memory aid (not from the handout): an EPIC list of how goods are sorted.')]),
 '5': dict(
   plain='Ask two questions. Can I stop you using it if you do not pay? Does your use leave less for me? Food: yes and yes, so the market works. A streetlight or national defence: no and no, so nobody pays and everybody waits for someone else (the free-rider problem). That permanent gap is a market failure, and it is why society creates a government with the authority to collect taxes and the duty to provide.',
   eg='The handout’s examples: private goods are food, clothing, cars, electronics; public goods are law and order, defence, administration, streetlights and lighthouses. Government can afford only the most vital ones, prioritised by necessity.',
   hook='Public = non-excludable + non-rival → free rider → market failure → government and taxes.'),
 '6': dict(
   plain='A packet of salt is not final or intermediate by itself; what the buyer does with it decides. Cooked at home, the meal is not sold, so the salt is a final good. Bought by a hotel and sold inside a meal, its identity merges into a new product for sale, so it is intermediate. Only economic change counts, not physical change.',
   eg='The handout’s table: salt for a household is final; salt for a hotel is intermediate; a phone, screen guard and cover used together are all final; a phone sold second-hand after 3 years is still final (only ownership moves).',
   hook='Final = economic identity kept. Intermediate = identity merged into something sold. Used-goods resale creates nothing new.'),
 '7': dict(
   plain='Final goods split two ways. Consumer goods end with households. Capital goods are machines and tools bought by producers; they are not used up in one cycle but serve many. Capital comes in two types: fixed capital (the rigid infrastructure kept over a year) and working capital (the blood that is used up day to day). Money, shares and bonds are not capital in this economic sense.',
   eg='The handout’s examples: fixed capital = plants, machinery, equipment, buildings; working capital = raw-material inventory, work-in-progress, cash for wages and utilities. SNA capital goods are used “for more than one year”.',
   hook='Consumer goods feed people; capital goods feed production. Fixed = infrastructure, working = blood. Financial capital is NOT capital.'),
 '8': dict(
   plain='In daily speech investment means mutual funds or gold. In macroeconomics that is just a transfer of paper ownership. Investment is firms spending on new capital goods during a year. Picture a water tank: the tap running in is the flow (investment); the water standing in the tank is the stock (capital).',
   eg='The handout: capital = total value of the machines a firm owns now (stock); investment = money spent buying new capital goods over a period (flow). GCF = gross fixed capital formation + changes in inventories + acquisitions less disposals of valuables. New dwellings added in a year count as investment.',
   hook='Capital = stock. Investment = flow. GCF = GFCF + inventories + valuables. Shares and gold are not investment.'),
 '9': dict(
   plain='Machines wear out, so part of a year’s capital spending only replaces the broken ones. Net investment is what is left after that replacement. Three people measure the wear differently: the accountant uses what the machine originally cost, the national statistician uses what it would cost to replace today, and the tax department uses a rate fixed by law. Oiling a machine does not stop it ageing; a newer machine can make it obsolete.',
   eg='The handout’s machine bought for ₹10 lakh in 2015, life 10 years: depreciation ₹1 lakh a year even if a new one now costs ₹25 lakh; replacing 10% of capacity costs ₹2.5 lakh today, so CFC = ₹2.5 lakh; CCA lets a solar plant write off 40% in year one.',
   hook='Net I = Gross I − Dep. Accountant: historical cost. Statistician: replacement cost (CFC). Tax: legal rate (CCA).'),
}
NUMBERS = [('8 hours', 'daylight in the hunter-gatherer PPF'), ('10 deer / 700 berries', 'the two ends of the handout PPF'),
           ('200-180-150-100-70', 'berries bought by each 2 fewer deer'), ('90% / 10%', 'Giffen worker: coarse grain / meat'),
           ('4 pairs', 'necessary-luxury, normal-inferior, substitute-complement, merit-demerit'),
           ('more than 1 year', 'life of an SNA capital good'), ('₹10 lakh, 10 years', 'machine: ₹1 lakh depreciation a year'),
           ('₹25 lakh', 'cost of a new machine today'), ('₹2.5 lakh', 'CFC for replacing 10% of capacity'),
           ('40%', 'CCA write-off in year one (solar plant)'), ('2021', 'Prelims PYQ: answer (a) 1 and 4 only'),
           ('8 + 2', 'Prelims and Mains PYQs mapped to this chapter')]
DRAW = ['Redraw the handout’s goods matrix (excludable yes/no × rivalrous yes/no) and write one example in each of the four boxes (section 5).',
        'Redraw the handout’s production boundary figure: salt at home (final) versus salt in a hotel meal (intermediate) (section 6).',
        'Write from memory the three net-investment cases (above, equal to, below zero) and the three-row table: depreciation, CFC, CCA with owner and basis (section 9).']
FM = {
 '1': [('PPF trade-off', 'each 2 fewer deer buys 200, 180, 150, 100, 70 more berries', 'handout table: every sacrifice buys less than the one before', 'wide')],
 '2': [('Opportunity cost', 'OC = value of the next best alternative given up', 'conceptual, not necessarily financial'),
       ('Marginal cost', 'MC = cost of one more unit at the current output', 'a high MC is justified only if the marginal benefit is equally high')],
 '4': [('Substitutes', 'price of B ↑ ⇒ demand for A ↑', 'positive cross-price effect (coffee, tea)'),
       ('Complements', 'price of B ↑ ⇒ demand for A ↓', 'negative cross-price effect (cars, petrol)'),
       ('Normal / inferior', 'income ↑ ⇒ demand ↑ / demand ↓', 'curve shifts right / left'),
       ('Necessary / luxury', 'steep (inelastic) / flat (elastic)', 'price elasticity'),
       ('Giffen', 'inferior good, huge share of income, no cheaper substitute', 'negative income effect overpowers substitution effect', 'wide')],
 '5': [('Public good', 'non-excludable and non-rival', 'free-rider problem ⇒ market failure ⇒ government and taxes')],
 '6': [('Final or intermediate?', 'economically modified for sale ⇒ intermediate; identity kept ⇒ final', 'physical change does not matter')],
 '7': [('Capital good test', 'used repeatedly in production for more than one year', 'still a final good'),
       ('Fixed vs working', 'fixed: over a year, infrastructure; working: used up in a cycle, blood', 'financial capital is not economic capital')],
 '8': [('Capital vs investment', 'capital = stock; investment = flow', 'tank and tap'),
       ('GCF', 'GCF = GFCF + changes in inventories + acquisitions less disposals of valuables', 'IMF, OECD and India’s NAS term for investment', 'wide')],
 '9': [('Net investment', 'Net Investment = Gross Investment − Depreciation', 'handout formula'),
       ('Three cases', '> 0 capacity expands; = 0 stagnant; < 0 capacity shrinks', 'PPF shifts outward only in the first'),
       ('Three bases', 'Depreciation: historical cost · CFC: replacement cost · CCA: statutory rate', 'accountant · statistician and RBI · Income Tax Department', 'wide')],
}
