# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 10 (External Sector). Facts come only from the handout text."""
TOP = {
 'sixty': [('BoP', 'double-entry ledger of residents versus non-residents; autonomous items + Δ reserves + E&O = 0'),
           ('Accounts', 'current (goods, services, incomes, transfers) and capital/financial (debt, investments, others, reserves)'),
           ('FDI versus FPI', '10% or more equity = FDI (control, marriage); below 10% = FPI (hot money); unlisted = always FDI'),
           ('Exchange rate', 'price of a currency where demand for dollars meets supply; India = managed float since 1993'),
           ('REER trap', 'RBI quotes indirect, base 2015-16 = 100: rising index = stronger rupee = less competitive'),
           ('CAD and J-curve', 'CAD = VI − VE; devaluation first worsens it (VI up 1.5×, VE down to 0.75×); currency wars follow'),
           ('IMF', '191 members; quota fixes votes (85% rule, US over 16%); SDR is not a currency; lends after SDR and RTP'),
           ('World Bank Group', 'IBRD, IDA, IFC, MIGA, ICSID; India graduated from IDA in 2014 and is not in ICSID')],
 'words': [('Balance of payments', 'the ledger of all money flowing between a country’s residents and the rest of the world'),
           ('Current account', 'settled everyday flows: goods, services, incomes, transfers'),
           ('Capital account', 'flows that change who owns what: loans, investments, reserves'),
           ('Forex reserves', 'the dollars and gold the RBI keeps to settle gaps and calm the rupee'),
           ('Depreciation', 'the rupee buys fewer dollars: $1 costs more rupees (market-driven)'),
           ('Devaluation', 'the same fall of the rupee, but by official decision under a fixed system'),
           ('REER', 'the rupee’s value against a basket of trading partners, adjusted for inflation'),
           ('SDR', 'an IMF reserve asset, a potential claim on usable currencies; not money you can spend')],
}
SEC = {
 '1': dict(
   plain='Picture a Delhi vendor who buys phone covers from China. The vendor has rupees; the Chinese seller wants yuan. Banks bridge the gap through the dollar, the universal go-between. Every such conversion is reported to the RBI with its purpose, and the RBI adds them all up. That total, kept in double-entry style where every entry has a matching opposite, is the balance of payments. It is a record of flows over a period; the stock of what the country owns and owes sits in the IIP.',
   eg='The handout’s example: 10 lakh covers at 20 Yuan = 2 Crore Yuan, paid as about ₹20 Cr; SBI buys 20 lakh US dollars (assumed ₹100 per dollar) and the Chinese bank sells them at 10 yuan per dollar.',
   hook='BoP = flows, IIP = stocks. Credit = money in, debit = money out. Nostro ours, Vostro yours, Loro theirs. FEMA 1999, FETERS.'),
 '2': dict(
   plain='Split the ledger in two. Above the line are choices made for self-interest: trade, tourism, investment, loans. Below the line are the leftovers: the RBI buying or selling dollars to absorb any gap, plus errors and omissions where the books do not quite match. So the “balance” in the balance of payments is struck by the central bank. If the autonomous items leave a surplus the RBI stores the dollars in reserves; if a deficit, it sells from reserves.',
   eg='The handout’s numbers: CAD $10 B but capital surplus $25 B means net surplus $15 B, absorbed into reserves. Reserves $500 B, inflows $100 B and outflows $80 B means reserves should rise by $20 B to $520 B; observed $20.4 B gives E&O = +$0.4 B.',
   hook='Autonomous (above) + Δ reserves and E&O (below) = 0. Old classification: reserves in capital account. Impossible trinity.'),
 '3': dict(
   plain='This section is a data tour with no new ideas: the slides show charts and tables of India’s BoP from 2019-20 to 2021-22. Read them with the structure of section 2 in mind: trade balance, invisibles, capital account, FDI, FPI, reserves. The only mark the teacher made is the pink oval and star on 2020-21 Q1 and Q2, when the current account was in surplus.',
   eg='The handout gives India’s top 5 trading partners: USA 11.3%, China 10.9%, UAE 7.3%, Saudi Arabia 4.1%, Hong Kong 3.7%.',
   hook='Teacher’s star = 2020-21 Q1 and Q2 current-account surplus. FPI stayed volatile.'),
 '4': dict(
   plain='Foreign money comes in two temperaments. FDI is a marriage: the investor wants a say, builds the factory and stays through bad times. FPI is a date: money that buys shares and bonds, leaves when profits are made or losses start, and can shake the exchange rate. India stopped judging by intent and now uses an objective test: 10% or more of the equity means control, so FDI. Unlisted companies are always FDI. Almost every sector is open except nine prohibited ones, and over 90% of FDI comes by the automatic route.',
   eg='The handout’s cases: 5% equity plus 20% of debt = FPI; an FPI crossing 10% in a listed firm is reclassified as FDI; Budget 2021 raised insurance FDI to 74% from 49%; Kia (greenfield) versus Walmart acquiring Flipkart (brownfield).',
   hook='10% or more = FDI = marriage. Below 10% = FPI = hot money. 9 prohibited sectors; automatic route 90%+; CCEA above ₹5,000 Cr.'),
 '5': dict(
   plain='The exchange rate is simply the price of a dollar in rupees, set where those who want dollars meet those who bring dollars. Importers, tourists, students and FPIs selling stocks want dollars. Exporters, investors, borrowers and remitters bring them. An oil price jump means more demand for dollars and a costlier dollar. Countries then choose a system: let the market decide (floating), fix it by decree (fixed), tie it to a big neighbour’s currency (pegged), or float with the central bank smoothing wild swings (managed float, India).',
   eg='The handout: $1 = ₹90 direct, ₹1 = $(1/90) ≈ $0.011 indirect. A cheap fixed dollar at ₹40 against a market ₹90 would explode demand and breed black markets (Hawala). Bhutan’s ngultrum is pegged 1:1 to the rupee.',
   hook='D$ meets S$. Direct quote = rupees per dollar. India: Par value 1947-1971 → pound 1971-1975 → basket 1975-1992 → LERMS → VERS 1993. Current account convertible; capital account partial.'),
 '6': dict(
   plain='It is the movement of the rate, not its level, that decides who wins trade. The nominal rate is what you see on the screen. The real rate corrects it for inflation: if your prices rise faster than your partner’s, your goods get dearer even with a fixed nominal rate. The effective rate averages the rupee against a whole basket of trading partners. Beware the trap: the dollar falling from ₹90 to ₹80 is a rupee APPRECIATION.',
   eg='The handout’s numbers: NER ₹80, PF = 105, PD = 110, so RER = 80 × 105 ÷ 110 ≈ ₹76. If NER depreciates to ₹85 the handout says about ₹80 (arithmetic gives about ₹81).',
   hook='RER = NER × PF ÷ PD. RBI’s NEER and REER: indirect quotes, index 2015-16 = 100, rising = stronger rupee. Baskets: 6 and 40.'),
 '7': dict(
   plain='A current account deficit means we buy more from the world than we sell. It is not evil in itself; a growing country needs machines. The test is whether it is financed by steady money (FDI) or flighty money (FPI, costly ECB), and whether reserves cover 6 to 8 months of imports. The causes fall in four groups, and each cure has a price: cutting demand costs growth, tariffs invite retaliation, supply reforms take long, and devaluation brings the J-curve.',
   eg='The handout’s groups: 1 demand side (crude, APIs, gold sinkhole), 2 policy side (tariffs, Inverted Duty Structure), 3 supply side (infrastructure, EODB, PLI), 4 strong exchange rate.',
   hook='CAD = VI − VE. Four reasons, four cures, four trade-offs. FDI-financed CAD is sustainable. Reserves: 6 to 8 months of imports.',
   mn=[dict(kind='sentence', title='Four groups of CAD reasons, in the handout’s order', sentence='Deficits Prompt Strong Exports',
            letters=[('D', 'Demand side (incomes, crude, gold)'), ('P', 'Policy side (tariffs, IDS)'), ('S', 'Supply side (infrastructure, EODB)'), ('E', 'Exchange rate too strong')],
            note='Own memory aid (not from the handout): the four groups are the handout’s own table, in its order.')]),
 '8': dict(
   plain='Devaluation is meant to fix the deficit by making imports dear and exports cheap. But if people cannot cut imports quickly (crude, pulses) and foreign buyers do not rush to buy more, the import bill actually grows while export revenue shrinks. So the deficit first gets worse and only later, hopefully, improves: the J. Meanwhile rivals may devalue too, and everyone ends up poorer, a currency war. A floating rate adjusts on its own and nobody cries foul.',
   eg='The handout’s numbers: PI doubles and QI falls to 0.75 QI, so VI′ = 2 × 0.75 = 1.5 VI. PE halves and QE rises to 1.5 QE, so VE′ = 0.5 × 1.5 = 0.75 VE. Import bill up, export revenue down.',
   hook='VI up 1.5×, VE down to 0.75× = CAD worsens first (J-curve). Currency war = beggar thy neighbour. Floating = automatic stabiliser.'),
 '9': dict(
   plain='Countries compete for their own good, and unchecked this ends in tariff wars, devaluations and worse. Game theory says each player grabbing the most can leave all worse off, so rules that everyone accepts are needed. In 1944, 44 countries met at Bretton Woods and built three pillars: the IMF to manage BoP crises, a trade body for rules (the ITO failed and became the WTO in 1995), and the World Bank to rebuild and finance development.',
   eg='The handout’s story: the East India Company took Bengal through the Nawabs’ defaults and the Diwani; British goods paid zero duty in India while Indian goods faced around 200% in Britain. Keynes wanted Bancor; White’s US-dollar anchor prevailed.',
   hook='1944, 44 countries. IMF = crisis manager, WTO = rule-maker (ITO failed, WTO 1995), World Bank = builder. The Bretton Woods twins.'),
 '10': dict(
   plain='“World Bank” strictly means IBRD plus IDA, but the group has five arms. IBRD lends to middle-income countries on near-commercial terms. IDA gives near-free credit to the poorest. IFC lends to private firms and guarantees their credit. MIGA insures foreign investors against political risk. ICSID settles investor-state disputes, and India is not a member. Votes follow shares, the USA is the largest shareholder, and the President is always an American.',
   eg='The handout: IDA credits are repaid over 30 to 40 years; India graduated from IDA in 2014; an Indian corporate may pay 7% instead of 4% because of the sovereign ceiling, which the IFC guarantee eases.',
   hook='IBRD builds, IDA gives, IFC lends to firms, MIGA insures, ICSID arbitrates (India outside). 25 Executive Directors; US President; European IMF head.'),
 '11': dict(
   plain='The IMF is a fund with 191 owners. Each pays a subscription equal to its quota, three quarters in its own currency and a quarter in usable foreign money or gold. That quarter can be withdrawn unconditionally: the reserve tranche. In a crisis a country first uses its SDRs, selling them to a surplus country for hard currency, and only after SDRs and RTP are exhausted does the IMF lend directly through ECF, RCF, SBA or EFF, usually with conditions that critics call an infringement on sovereignty.',
   eg='The handout’s story: Sri Lanka sells SDR holdings to Germany and gets currency; Sri Lanka then pays net interest, Germany earns it. India’s quota of 4 out of 100 would give 4% of quota-based votes; the Indian Executive Director represents India, Bhutan, Bangladesh and Sri Lanka with about 3.5% votes.',
   hook='Quota = subscription = votes = borrowing limit. 85% for big decisions, US over 16%. SDR is not a currency. Reserves = gold + FCA + SDR + RTP.'),
}
NUMBERS = [('44 / 1944', 'countries at Bretton Woods and the year'), ('191', 'IMF members'), ('85% / over 16%', 'IMF supermajority and the US share'),
           ('75% / 25%', 'IMF subscription: domestic currency versus usable currency or gold'), ('10%', 'FDI control test (10% or more)'),
           ('9', 'prohibited FDI sectors'), ('over 90%', 'FDI via automatic route'), ('₹5,000 Cr', 'foreign investment above this needs CCEA approval'),
           ('74%', 'insurance FDI (from 49%) and defence automatic limit'), ('1993', 'VERS and managed float; current account convertible'),
           ('1997 / 2006', 'Tarapore Committees'), ('2015-16 = 100', 'NEER and REER base year'), ('6 and 40', 'partner currencies in RBI’s two baskets'),
           ('1.5× and 0.75×', 'VI and VE after devaluation (handout)'), ('6 to 8 months', 'import cover considered adequate'), ('2014', 'India graduates from IDA; SEBI erases the term FII')]
DRAW = ['Redraw the handout’s BoP structure figure (section 2): current account on one side, capital and financial account on the other, reserves below, with the −50 bn and +50 bn side panel.',
        'Redraw the handout’s J-curve (section 8): the line first dips, then rises; write VI × 1.5 and VE × 0.75 beside it.',
        'Write the FDI versus FPI table (10% rule) and the five World Bank Group names with one job each, from memory.']
FM = {
 '1': [('Double entry', 'credits + debits = 0', 'every transaction has two entries of equal value'),
       ('Mobile cover sum', '10 lakh × 20 Yuan = 2 Crore Yuan', 'about ₹20 Cr via 20 lakh US dollars at ₹100 per dollar (handout)')],
 '2': [('The BoP idea', 'autonomous items + Δ reserves + E&amp;O = 0', 'handout alert: remember the idea, old classification'),
       ('Reserve sum', '$500 B + $100 B − $80 B = $520 B', 'inflows $100 B, outflows $80 B on autonomous items'),
       ('E&amp;O', 'E&amp;O = observed Δ reserves − expected Δ reserves', '$20.4 B − $20 B = +$0.4 B')],
 '4': [('FDI test', 'equity ≥ 10% = FDI; equity &lt; 10% = FPI', 'unlisted company: always FDI')],
 '5': [('Direct quote', '$1 = ₹90', 'price of foreign currency in domestic units'),
       ('Indirect quote', '₹1 = $(1 ÷ 90) ≈ $0.011', 'price of domestic currency in foreign units')],
 '6': [('Real exchange rate', 'RER = NER × (PF ÷ PD)', 'PF = foreign price level, PD = domestic price level'),
       ('Handout numbers', '80 × 105 ÷ 110 ≈ ₹76', 'RER below NER: rupee actually stronger'),
       ('After depreciation', '85 × 105 ÷ 110: handout says ~₹80', 'arithmetic gives about ₹81')],
 '7': [('Current account deficit', 'CAD = VI − VE', 'VI = PI·QI, VE = PE·QE'),
       ('Reserve test', 'reserves ≥ 6 to 8 months of import bill', 'handout’s adequacy measure')],
 '8': [('Import bill', 'VI′ = 2 PI × 0.75 QI = 1.5 VI', 'PI doubles, QI falls to 0.75 QI'),
       ('Export revenue', 'VE′ = 0.5 PE × 1.5 QE = 0.75 VE', 'PE halves, QE rises to 1.5 QE')],
 '11': [('IMF subscription', 'subscription = quota, in SDR', '75% domestic currency + 25% usable currency or gold'),
        ('Forex reserves', 'gold + FCA + SDR holdings + RTP', 'RTP = the 25% part, withdrawable unconditionally'),
        ('Quota-based votes', 'votes = country’s share of total quota', 'quota 4 of 100 gives 4% of QBV (handout)')],
}
