# -*- coding: utf-8 -*-
"""Small flowcharts and hub diagrams added to the handwritten notes (display only; the shelf text is unchanged)."""
import re
from dsl import fl, hub, sec
D = {  # chapter id -> [nodes]; each placed at the top of the chapter as 'At a glance'
 # ---- Governance
 13: [fl(['Apply to the PIO (fee Rs 10; BPL free)', 'Reply in 30 days (48 hours if life or liberty)', 'First appeal to the senior officer within 30 days', 'Second appeal to CIC or SIC within 90 days'], 'RTI request: the route', 4)],
 29: [fl(['CAG audits the accounts', 'Report to the President or Governor', 'Laid before Parliament or the Legislature', 'Public Accounts Committee examines it'], 'CAG audit: how it reaches the House', 4)],
 33: [fl(['Complaint, reference or suo motu', 'Director General investigates', 'CCI inquiry and order (penalty up to 10% of turnover)', 'Appeal to NCLAT, then Supreme Court'], 'CCI: how a case moves', 4)],
 # ---- Polity
 40: [hub('Constitutionalism', ['Rule of law', 'Separation of powers', 'Judicial review', 'Fundamental rights', 'Independent institutions', 'Accountable government'], 'Pillars of constitutionalism')],
 41: [fl(['Legislature makes the law', 'Executive carries it out', 'Judiciary interprets it and can strike it down', 'Each checks the other two'], 'Separation of powers and checks', 4)],
 46: [fl(['President refers the Bill to the State legislature for its views', 'Bill introduced in Parliament on President\'s recommendation', 'Passed by simple majority', 'Not a constitutional amendment under Art 368'], 'Art 3: how a new State is formed', 4)],
 49: [hub('The "State" (Art 12)', ['Government and Parliament of India', 'State governments and legislatures', 'Local authorities', 'Other authorities under government control'], 'Who is bound by Fundamental Rights')],
 53: [hub('Art 19(1): six freedoms', ['(a) Speech and expression', '(b) Assemble peacefully', '(c) Form associations', '(d) Move freely in India', '(e) Reside and settle', '(g) Profession, trade, business'], 'The freedoms of Art 19')],
 61: [hub('Art 20: protection in conviction', ['20(1) No retrospective punishment', '20(2) No double jeopardy', '20(3) No self-incrimination'], 'Three shields')],
 62: [hub('Art 21: life and personal liberty', ['Livelihood (Olga Tellis)', 'Health and medical care', 'Privacy (Puttaswamy)', 'Clean environment', 'Speedy trial and legal aid', 'Dignity'], 'Rights read into Art 21 (Maneka Gandhi: procedure must be fair)')],
 70: [fl(['Arrest', 'Told the grounds of arrest', 'Right to a lawyer of choice', 'Produced before a magistrate within 24 hours', 'Held longer only if the magistrate allows'], 'Art 22: rights of an arrested person', 5)],
 76: [hub('DPSP', ['Socialist: equality, livelihood, workers', 'Gandhian: panchayats, cottage industry, prohibition', 'Liberal-intellectual: UCC, separation of judiciary, peace'], 'Three groups of DPSP')],
 82: [fl(['Selection committee of six recommends', 'President appoints', 'Chairperson + 5 full-time + 7 ex-officio Members', 'Removal only by President after a Supreme Court inquiry'], 'NHRC: from appointment to removal', 4)],
 83: [fl(['Governor appoints on a committee led by the Chief Minister', 'Chairperson + 2 Members', 'Term 3 years or age 70', 'Removal only by President after a Supreme Court inquiry'], 'SHRC: appointment to removal', 4)],
 88: [fl(['Electoral college: elected MPs + elected MLAs (incl. Delhi, Puducherry)', 'Proportional representation by single transferable vote', 'Secret ballot', 'Winner must reach the quota'], 'President: how elected', 4)],
 89: [fl(['Parliament is not in session', 'President issues an Ordinance on Cabinet advice (Art 123)', 'Laid before Parliament when it meets', 'Lapses 6 weeks after reassembly, or earlier if disapproved'], 'Ordinance: life cycle', 4)],
 92: [fl(['Prime Minister', 'Cabinet Ministers', 'Ministers of State', 'Deputy Ministers'], 'Council of Ministers: ranks', 4)],
 98: [fl(['Introduced in either House', 'Three readings and committee study', 'Passed by the other House', 'President\'s assent makes it an Act'], 'An ordinary Bill becomes law', 4)],
 100: [hub('Seventh Schedule', ['Union List: only Parliament', 'State List: State legislature (exceptions Arts 249-252)', 'Concurrent List: both, Union law prevails (Art 254)', 'Residuary: Parliament (Art 248)'], 'Who makes laws on what')],
 103: [fl(['Governor\'s report or other information', 'President satisfied; proclamation under Art 356', 'Both Houses approve within 2 months', 'Lasts 6 months, extendable in 6-month steps, max 3 years'], 'President\'s Rule: the steps', 4)],
 104: [fl(['Union taxes form the divisible pool', 'Finance Commission (Art 280) recommends the States\' share', 'States get their share + grants-in-aid', 'Cesses and surcharges stay outside the pool'], 'Fiscal federalism: money flow', 4)],
 105: [hub('GST Council (Art 279A)', ['Chair: Union Finance Minister', 'Union Minister of State for Finance', 'State Finance Ministers', 'Union has 1/3 of votes', 'States together have 2/3', 'Decisions need 3/4 of votes cast'], 'Who sits and how it votes')],
 54: [hub('Contempt of court', ['Civil: wilful disobedience of a court order', 'Criminal: scandalising the court', 'Criminal: prejudicing a trial', 'Criminal: obstructing justice', 'Punishment: up to 6 months and/or fine Rs 2,000 (1971 Act)'], 'Kinds of contempt')],
 71: [hub('Right against exploitation', ['Art 23: no human trafficking or forced labour (begar)', 'Art 24: no child below 14 in factories, mines or hazardous work'], 'Arts 23-24')],
 72: [hub('Freedom of religion', ['Art 25: conscience, profess, practise, propagate', 'Art 26: manage religious affairs', 'Art 27: no tax to promote a religion', 'Art 28: religious instruction in State schools'], 'Arts 25-28 together')],
 74: [hub('Cultural and educational rights', ['Art 29: protects language, script and culture of any section', 'Art 30: minorities may set up and run educational institutions'], 'Arts 29-30')],
 80: [hub('Commissions for weaker sections', ['Art 338: National Commission for SCs', 'Art 338A: National Commission for STs', 'Art 338B: National Commission for Backward Classes (102nd Amendment, 2018)'], 'Constitutional commissions')],
 94: [fl(['Elected by Lok Sabha members', 'Presides; decides disqualification under the Tenth Schedule', 'Casts a vote only to break a tie', 'Removed by resolution of effective majority, 14 days notice'], 'Speaker: from election to removal', 4)],
 99: [hub('Quasi-federal India', ['Federal: written constitution', 'Federal: division of powers', 'Federal: independent judiciary', 'Unitary: strong Centre', 'Unitary: single citizenship', 'Unitary: Governor and Emergency powers'], 'Federal and unitary features')],
 106: [fl(['Dispute between States over river water', 'Centre tries negotiation first', 'Tribunal under the Inter-State River Water Disputes Act, 1956', 'Award is final; courts barred (Art 262)'], 'River water dispute: the route', 4)],
 3: [fl(['Rajya Sabha resolution by 2/3 of members present and voting (Art 312)', 'Parliament passes a law', 'New All India Service is created'], 'How a new All India Service is created', 3)],
 21: [fl(['Gram Panchayat (village)', 'Panchayat Samiti (block)', 'Zila Parishad (district)'], 'Three-tier Panchayati Raj (73rd Amendment)', 3)],
 27: [fl(['10-20 members save small amounts regularly', 'The group lends to its own members', 'Bank loans linked to the group\'s savings', 'Groups join into village and block federations'], 'How an SHG grows', 4)],
}
STEP = re.compile(r'<b>\s*(\d+)\.\s*([^<]{2,60}?)\.?\s*</b>')
LBL = re.compile(r'step|procedure|process|stage|sequence|how a|how the|flow', re.I)
def auto_steps(nodes):
    out = []
    for x in nodes:
        if x[0] == 'tree' and LBL.search(re.sub(r'<[^>]+>', '', x[1])):
            ks = [STEP.match(k.strip()) for k in x[2] if isinstance(k, str)]
            ks = [m for m in ks if m]
            if len(ks) >= 3 and len(ks) == len([k for k in x[2] if isinstance(k, str)]):
                out.append(fl([m.group(2).strip() for m in ks], 'Steps at a glance', 3 if len(ks) in (3, 6) else 4))
        out.append(x)
    return out
def apply(chs):
    n = 0
    for c in chs:
        c['nodes'] = auto_steps(c['nodes'])
        if c['id'] in D:
            c['nodes'] = list(D[c['id']]) + c['nodes']; n += 1
    return n

D_GS3 = {  # ids as in src-gs3
 4: [fl(['CACP recommends the MSP', 'Cabinet Committee approves it', 'FCI and State agencies buy at MSP', 'Stocks feed PDS and buffer'], 'MSP and procurement chain', 4)],
 5: [fl(['National: NDMA (Prime Minister chairs)', 'State: SDMA (Chief Minister chairs)', 'District: DDMA (Collector heads)', 'Response force: NDRF'], 'DM Act 2005: three tiers', 4)],
 25: [fl(['Indian Navy: overall maritime security', 'Coast Guard: territorial waters and EEZ', 'Marine Police: coastal waters up to 12 nautical miles'], 'Coastal security: who guards what', 3)],
 34: [fl(['Offence under UAPA or another scheduled Act', 'Centre can direct NIA to take over', 'NIA investigates; Special Court tries', 'Appeal lies to the High Court'], 'UAPA and NIA: case route', 4)],
 15: [fl(['Register or get prior permission from MHA', 'Receive foreign money only in the designated FCRA account', 'File annual returns', 'Registration can be suspended or cancelled'], 'FCRA: the compliance chain', 4)],
 30: [hub('Cyber security set-up', ['CERT-In: incident response', 'NCIIPC: critical information infrastructure', 'I4C: cybercrime coordination (MHA)', 'National Cyber Security Coordinator (NSCS)', 'Sectoral CERTs'], 'Who does what')],
 31: [hub('DPDP Act 2023', ['Data Principal: the individual', 'Data Fiduciary: the entity that decides purpose', 'Consent and notice', 'Rights: access, correction, erasure, grievance', 'Data Protection Board of India', 'Penalties for breach'], 'Key parts at a glance')],
}
D_IR = {
 1: [hub("India's foreign policy", ['Strategic autonomy', 'Multi-alignment', 'Neighbourhood First', 'Act East', 'Voice of the Global South', 'Energy and economic security'], 'Pillars to remember')],
 2: [hub('India and major powers', ['USA', 'Russia', 'China', 'European Union', 'Japan'], 'The big five relationships')],
 3: [hub('Neighbourhood First', ['Pakistan', 'China', 'Nepal', 'Bhutan', 'Bangladesh', 'Sri Lanka', 'Maldives', 'Myanmar and Afghanistan'], 'Who is in the neighbourhood')],
 5: [hub('Extended neighbourhood', ['Central Asia: Connect Central Asia', 'West Asia: Look West', 'Southeast Asia: Act East', 'Africa partnership', 'Indian Ocean: SAGAR and MAHASAGAR', 'Indo-Pacific'], 'Regions beyond South Asia')],
}
def apply_to(chs, table):
    n = 0
    for c in chs:
        if 'nodes' not in c: continue
        c['nodes'] = auto_steps(c['nodes'])
        if c['id'] in table:
            c['nodes'] = list(table[c['id']]) + c['nodes']; n += 1
    return n
