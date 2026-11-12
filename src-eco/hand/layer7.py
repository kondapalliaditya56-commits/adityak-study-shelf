# -*- coding: utf-8 -*-
"""Concept-first layer for Economy Ch 7 (Banking and NBFCs). Facts come only from the handout text.
plain = idea in everyday words (memory aid); eg = the handout's own example; hook = one-line handle."""
TOP = {
 'sixty': [('Bank', 'decision-making intermediary: it keeps the reward, so it must carry the risk'),
           ('Regulator', 'RBI for banks and NBFCs (BR Act 1949); SEBI for brokers and exchanges'),
           ('Capital', 'CRAR = Capital ÷ RWA ≥ 9%; CCB 2.5%; provisioning per loan'),
           ('Bad loans', 'SMA-0/1/2, then NPA at 90+ days: sub-standard, doubtful, loss'),
           ('Clean-up', '4R: Recognise (AQR), Recover (IBC), Recapitalise (₹2.11 L Cr), Reform'),
           ('Reach', 'inclusion 1955 to PMJDY 2014; PSL 40% / 75%; differentiated banks and NBFC layers')],
 'words': [('Intermediary', 'a middleman that collects information, builds trust and arranges the contract between the money supplier and the money user'),
           ('Capital (of a bank)', 'the bank’s OWN money (equity, retained profit), not deposits'),
           ('Risk Weighted Assets', 'each loan counted at loan value × its risk %, so riskier loans use more capital'),
           ('Provisioning', 'setting aside a % of a loan’s value from capital against likely default'),
           ('NPA', 'a loan whose principal or interest is overdue more than 90 days'),
           ('Haircut', 'cutting the book value of a bad loan, an accounting step, not a waiver'),
           ('Creditor-in-control', 'under the IBC the lenders, not the old owner, take charge of the defaulting firm'),
           ('Financial inclusion', 'bringing everyone into the formal financial system, starting with a bank account')],
}
SEC = {
 '1': dict(
   plain='Money moves from people who have it to people who need it in return for a promise. A debt promise says “I will pay you back with interest”; an equity promise says “you now own a slice and share my decisions”. Going directly is hard, so middlemen help for a fee. Some middlemen (banks, NBFCs) decide what to do with your money. Others (brokers, exchanges) only arrange the meeting and you decide. The first kind must carry the risk; the second kind must only be honest.',
   eg='The handout’s contrast: banks and NBFCs are decision-making (RBI regulates); brokers and stock exchanges are decision-facilitating (SEBI regulates). Debt examples: bank loans, bonds. Equity example: shares.',
   hook='Who decides, bears the risk. Banks decide (RBI); brokers only facilitate (SEBI).'),
 '2': dict(
   plain='A bank’s business looks like “heads I win, tails you lose”: the bank keeps the interest, but the depositor’s money is the one at risk. That is unfair, so rules force the bank to have its own money at stake (skin in the game). CRR and SLR guard the deposit side. Rules are also needed on the lending side, and since a bank will not honestly admit its own risk, the central bank has to do it.',
   eg='The handout’s key law is the Banking Regulation (BR) Act 1949, which makes RBI the regulator. Section 5 defines “banking” (deposits from the public for lending or investment, withdrawable by cheque or draft) and only licensed entities may use the word “bank”.',
   hook='Heads I win, tails you lose ⇒ bank needs skin in the game. BR Act 1949 = RBI is the regulator.'),
 '3': dict(
   plain='Think of the bank’s own money as a cushion. Every loan can go bad, and risky loans can go bad sooner. RBI makes the bank (a) set aside a slice of each loan, called provisioning, and (b) hold a minimum cushion for the whole balance sheet, the CRAR. Riskier loans count for more, so they use up the cushion faster. When the cushion is full, the bank cannot lend more, however many deposits it holds. RBI never bans risky loans; it only makes the bank pay for them with its own money.',
   eg='The handout’s farmer example: ₹10 L agriculture loan, risk 20%, provisioning 3%. Provisioning 3% × ₹10 L = ₹30,000; RWA 20% × ₹10 L = ₹2 L; minimum capital 9% × ₹2 L = ₹18,000; total ₹48,000 of own capital to put ₹10 L of depositors’ money at risk. In the bank table, the ₹12 L credit-card loan (risk 90%) eats ₹3,97,200 of capital while P6 + P7 (₹42 L) need only ₹2.03 L.',
   hook='Capital ≥ 9% of (risk × loan) + provisioning. Risky loans burn capital fast. Basel III exists because Basel I and II missed market and operational risk.'),
 '4': dict(
   plain='A loan is like a bill with a due date. The longer it is overdue, the sicker it is. First a yellow warning (SMA: overdue 1 to 90 days, still not a bad loan). Past 90 days it is officially bad (NPA), and the class gets worse with time: sub-standard, doubtful, loss. A worse class means a bigger provision. Before 2014 there was no yellow stage, so banks played games by paying one small EMI on day 89.',
   eg='The handout’s trick: default for 88 days, pay one EMI on day 89, and the clock resets. SMA-0 is 1 to 30 days; SMA-1 more than 30 up to 60; SMA-2 more than 60 up to 90. NPA classes: sub-standard (up to 12 months, provision ~15%), doubtful (more than 12 months, 25% to 100%), loss (100%).',
   hook='Yellow (SMA, 1-90 days) → red at 90+ days (NPA). Worse class = bigger provision. Haircut and write-off are not waivers.',
   mn=[dict(kind='sentence', title='The ladder of bad loans, mildest to worst (an order)', sentence='Some Slip, Some Sink, Debts Linger',
            letters=[('S', 'SMA-0: 1 to 30 days, a red flag'), ('S', 'SMA-1: more than 30 up to 60 days'), ('S', 'SMA-2: more than 60 up to 90 days'),
                     ('S', 'Sub-standard NPA: up to 12 months, provision ~15%'), ('D', 'Doubtful NPA: more than 12 months, 25% to 100%'), ('L', 'Loss asset: 100% provision')],
            note='Own memory aid (not from the handout): the sentence is about slips that sink into debts, which is the whole ladder.')]),
 '5': dict(
   plain='Loans go bad for three kinds of reasons. Some borrowers can pay but do not (wilful default). Some are hit by things nobody controls (slowdown, war, floods, policy change). And some are simply badly judged by the bank. Economic reasons hit every bank alike, so a bank with far more bad loans than others has a risk-assessment problem. Bad loans then double-hurt the bank: assets earn nothing while deposits must still be paid.',
   eg='The handout’s test: economic reasons hit all banks equally, so similar NPAs are expected. If PSBs (historically) show much higher NPAs than private banks, the reason is poor risk assessment. Twin Balance Sheet Problem: the borrower’s stress hurts the bank, and the bank’s stress then hurts the borrower.',
   hook='Wilful, Economic, Poor assessment. DFR = bank’s own squeeze; TBP = borrower and bank drag each other down.'),
 '6': dict(
   plain='India treated a banking crisis in four steps. First admit how bad it is (Recognise: the AQR stopped hiding bad loans as restructured ones). Then get the money back (Recover: tribunals, SARFAESI, and finally IBC). Then refill the banks’ cushion (Recapitalise). Last, fix the reason it happened (Reform the governance of PSBs). Money alone is a bandage; the cure is distance between the owner and the bank.',
   eg='Handout numbers: March 2015 official GNPA 4.6% but stressed assets 11.1% (PSBs 13.2%); PSB GNPA peak 14.58% (March 2018); March 2021 7.3%; March 2024 2.8%; September 2024 2.6% with Net NPA 0.6%. IBC: 30 + 180 + 90 = 300 days (330 now), 2/3 of creditors by value. Recap: ₹2.11 Lakh Crore, October 2017.',
   hook='4R = Recognise, Recover, Recapitalise, Reform. IBC = creditor-in-control, CoC votes 2/3. Recap is a bandage; reform is the cure.'),
 '7': dict(
   plain='Strict licences built trust but also made banking an elite club, so many people stayed outside. Inclusion means bringing them in. India tried five phases: first the state forced branches into villages; then special institutions (co-operatives, RRBs, DFIs); then liberalisation with new private banks; then differently licensed banks; and finally Jan Dhan, which went looking for each unbanked person. The four pillars are: be in the system, have products, afford them, and know how to use them.',
   eg='The handout’s own “Quick reference”: 1955 SBI; 1969 Lead Bank Scheme and 14 banks; 1975 RRB; 1980 six more banks; 1992 SHG-Bank Linkage; 2005 No-Frills Accounts; 2006 Business Correspondents; 2011 Swabhimaan; Aug 2014 PMJDY; 2015 SFB and payments-bank licences. RRB ownership: Centre 50%, State 15%, sponsor bank 35%.',
   hook='Area-focused (open branches, hope) → person-focused (find each person): Jan Dhan, Aug 2014.',
   mn=[dict(kind='sentence', title='The five phases, in order', sentence='Seeds Sprout, Liberalisation Spreads, People',
            letters=[('S', 'State intervention: 1955, 1969, 1980'), ('S', 'Specialised architecture: co-operatives, RRBs, DFIs'), ('L', 'Liberalisation of the 1990s: private banks, BC model'),
                     ('S', 'Structural innovation 2013-14: SFBs, payments banks'), ('P', 'PM Jan Dhan Yojana, Aug 2014: person-focused')],
            note='Own memory aid (not from the handout): seeds are planted by the state and spread by liberalisation until people are reached. Order matters.')]),
 '8': dict(
   plain='RBI says: out of every rupee of bank credit, a fixed share must go to sectors the nation treats as priority, like farming, small business, education, housing, renewable energy and start-ups. Bigger commercial banks owe 40%; smaller, local-type banks owe 75%. Only the quantity is fixed, not the price; loans still cost market rates, and cheaper farm loans come through a separate interest subsidy. A bank that falls short can park the gap in a rural infrastructure fund or buy certificates from a bank that overshoots.',
   eg='The handout’s targets: 40% of ANBC for scheduled commercial banks and sizeable foreign private banks; 75% of ANBC for RRBs, co-operative banks and Small Finance Banks. Start-ups got PSL status in 2020. Shortfall: invest in RIDF at a low return or buy PSLCs.',
   hook='PSL fixes the allocation, not the price. 40% (commercial) and 75% (RRB, co-operative, SFB) of ANBC.'),
 '9': dict(
   plain='India has many kinds of banks because each does a different job. Commercial banks are for profit and regulated only by RBI. Co-operative banks serve members and answer to both a State and RBI. Scheduled banks are in the RBI Act’s Second Schedule, so they can borrow from RBI. RRBs mix local feel with professional skill. DFIs give long-term money to others, not to the public. SFBs and payments banks were created for inclusion, and NBFCs lend but cannot take demand deposits or issue cheques. NBFCs are then sorted into four layers by size and risk.',
   eg='The handout’s differences: payments bank holds 75% of deposits in Government Securities and cannot lend (deposits up to ₹2 Lakh per customer); SFB gives 75% of loans to PSL and at least 50% of its portfolio in loans under ₹25 Lakh. NBFC layers from 2022: Base below ₹1,000 Crore, Middle, Upper, Top (ideally empty).',
   hook='Trap: ₹100 Cr is the SARFAESI NBFC threshold; ₹1,000 Cr is the SBR base-layer limit. Payments bank: no loans.',
   mn=[dict(kind='sentence', title='NBFC scale-based layers, lightest to heaviest (an order)', sentence='Bigger Means Upper Tier',
            letters=[('B', 'Base layer: non-deposit-taking, below ₹1,000 Crore'), ('M', 'Middle layer: all deposit-taking NBFCs and larger non-deposit-taking'), ('U', 'Upper layer: systemically critical, bank-like scrutiny'), ('T', 'Top layer: ideally empty')],
            note='Own memory aid (not from the handout): a bigger NBFC moves to a higher layer and a tighter watch.')]),
}
FM = {
 '1': [('Debt', 'money given is repaid, generally with interest, in a promised period', 'bank loans, bonds'),
       ('Equity', 'money is not paid back; supplier gets rights and part-ownership', 'shares')],
 '3': [('CRAR', 'CRAR = Capital ÷ Risk Weighted Assets ≥ 9%', 'RBI asks 9%; Basel requires 8%'),
       ('Risk weighted assets', 'RWA = Risk × loan value', 'so Capital ≥ 9% of RWA, or RWA ≤ Capital ÷ 9%'),
       ('Capital CCB', 'Capital Conservation Buffer = 2.5% of RWA', 'protects the 9% line in stress'),
       ('Capital needed for a loan', 'Provisioning + 9% × (risk × loan)', 'handout method', 'wide'),
       ('Farmer example', '3% × ₹10 L = ₹30,000 · 20% × ₹10 L = ₹2 L · 9% × ₹2 L = ₹18,000 · total ₹48,000', 'handout: ₹10 L agriculture loan', 'wide')],
 '4': [('Overdue ladder', 'SMA-0: 1-30 · SMA-1: 31-60 · SMA-2: 61-90 · NPA: more than 90 days', 'days overdue'),
       ('GNPA', 'GNPA = total loans classified NPA (as % of total loans)', ''),
       ('Net NPA', 'Net NPA = GNPA − provisioning', ''),
       ('PCR', 'PCR (Provisioning Coverage Ratio) = capital as a proportion of GNPAs', 'handout’s wording'),
       ('Stressed assets', 'Stressed assets = GNPAs + restructured assets', '')],
 '6': [('IBC clock', '30 + 180 + 90 = 300 days (revised to 330 days now)', 'CoC within 30 days; plan within 180; extension up to 90'),
       ('IBC plan vote', 'plan needs 2/3 of creditors by credit value', 'only financial creditors vote'),
       ('SARFAESI limits', 'not agricultural loans · not dues under ₹1 lakh · not if 80% or more of principal repaid', 'only secured loans', 'wide'),
       ('Recapitalisation loop', 'government issues bonds ⇒ banks lend to it ⇒ government returns the money as equity', '₹2.11 Lakh Crore, Oct 2017'),
       ('Bhushan Steel', '₹35,200 Cr of ₹56,000 Cr claims (63%)', 'acquired by Tata Steel, 2018')],
 '7': [('RRB ownership', 'Centre 50% : State 15% : sponsor bank 35%', 'RRBs, 1975'),
       ('Area approach', 'one branch per defined area, e.g. 5,000 people (2,000 adults in hilly areas)', 'branch licensing policy since 2005', 'wide')],
 '8': [('PSL target', 'Scheduled commercial and foreign private banks: 40% of ANBC · RRBs, co-operative banks, SFBs: 75% of ANBC', 'ANBC = Adjusted Net Bank Credit', 'wide'),
       ('Shortfall', 'invest in RIDF at a low return or buy PSLCs', 'PSL fixes allocation, not price')],
 '9': [('SFB', '75% of loans to PSL · at least 50% of portfolio in loans under ₹25 Lakh', 'cannot set up insurance or pension subsidiaries'),
       ('Payments bank', 'deposits up to ₹2 Lakh per customer · 75% of deposits in Government Securities · no loans', ''),
       ('NBFC layers', 'Base below ₹1,000 Cr · Middle · Upper · Top', 'SBR effective 2022')],
}
NUMBERS = [('9% / 8%', 'CRAR: RBI / Basel'), ('2.5%', 'Capital Conservation Buffer'), ('₹48,000', 'capital for a ₹10 L farm loan'), ('90 days', 'overdue = NPA'),
           ('~15%, 25-100%, 100%', 'provision: sub-standard, doubtful, loss'), ('14.58%', 'PSB GNPA peak, March 2018'), ('2.6% / 0.6%', 'GNPA / Net NPA, Sept 2024'),
           ('₹2.11 Lakh Cr', 'recap package, Oct 2017'), ('2/3 · 180 + 90', 'IBC plan vote; days (330 now)'), ('2016', 'IBC enacted'),
           ('40% / 75%', 'PSL of ANBC'), ('₹1,000 Cr / ₹100 Cr', 'SBR base layer / SARFAESI NBFC size'), ('50 : 15 : 35', 'RRB ownership'),
           ('Aug 2014', 'PMJDY'), ('₹25 L · ₹2 L', 'SFB loan ticket · payments-bank deposit cap')]
DRAW = ['Redraw the handout’s IBC / CIRP chart: Default, NCLT admission, IRP takeover, CoC within 30 days, then Resolution or Liquidation.',
        'Write the ladder of bad loans (SMA-0 to Loss) with days and provisions, and the sentence “Some Slip, Some Sink, Debts Linger”.',
        'Write the financial-inclusion “Quick reference” years 1955 to 2015 from memory, then the five phases with “Seeds Sprout, Liberalisation Spreads, People”.']
