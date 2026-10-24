# -*- coding: utf-8 -*-
"""Turn 'Label: a · b · c' summary boxes into bullet trees (label on the left, one bullet per item).
Applied when chapters are loaded, for both the handwritten build and the shelf export."""
import re
SKIP_LABELS = ('pyq', 'teacher')
SEMI_OK = ('Objectives in detail', 'Problematic SC observations', 'Tenure and pay', 'Digital divide', 'Lobbying', 'SHG', 'Pressure group', 'Need for protective data usage', '2G case', 'Constitutional locus', 'Public-interest override')
LAB = re.compile(r'^<b>([^<]{2,60}?):?</b>:?\s*(.*)$', re.S)
def convert(node, cid):
    if cid == 0 or node[0] != 'bx' or node[1] not in ('pk', 'ye', 'gr', 'bl'): return node
    m = LAB.match(node[2].strip())
    if not m: return node
    label, body = m.group(1).strip(), m.group(2).strip()
    if label.lower().startswith(SKIP_LABELS): return node
    # split on ' · ' that is not inside a tag
    items = [x.strip() for x in re.split(r'\s·\s', body) if x.strip()]
    if len(items) < 3 and label.startswith(SEMI_OK):
        items = [x.strip() for x in re.split(r';\s+(?![^()]*\))', body) if x.strip()]
    if len(items) < 3: return node
    # lead-in sentence stays with first item
    return ('tree', '<b>%s</b>' % label, items, None, None)
def walk(nodes, cid, log=None):
    out = []
    for x in nodes:
        if x[0] == 'two':
            a = walk(x[1] if isinstance(x[1], list) else [x[1]], cid, log); b = walk(x[2] if isinstance(x[2], list) else [x[2]], cid, log)
            out.append(('two', a, b)); continue
        y = convert(x, cid)
        if y is not x and log is not None: log.append((cid, y[1], len(y[2])))
        out.append(y)
    return out
def apply(chs, log=None):
    for c in chs: c['nodes'] = walk(c['nodes'], c['id'], log)
    return chs


# own mnemonics for lists that had none (inserted right after the list they summarise)
def _m(word, html): return ('mn', word, html + ' <i>(own mnemonic)</i>')
ADD_MN = {
 9: [('Way forward', _m('SCI-TEC', 'Reform way forward: <b>S</b>upport (political, cross-party) · <b>C</b>apacity (training, reform units) · <b>I</b>nvolve civil servants · <b>T</b>ailor to states · <b>E</b>ngage (consult, feedback) · <b>C</b>ushion (safety nets).'))],
 20: [('Features', _m('3S-CLMP-R', 'Features of good governance: <b>3 S</b> = Social justice · SMART government · Sustainable development; <b>CLMP</b> = Community space · Local bodies · Market (socially responsible) · Participation; <b>R</b> = Rule of law.')),
      ('WGI six', _m('VP GRRC', 'World Bank WGI six, handout order: <b>V</b>oice and accountability · <b>P</b>olitical stability · <b>G</b>overnment effectiveness · <b>R</b>egulatory quality · <b>R</b>ule of law · <b>C</b>ontrol of corruption.'))],
 22: [('Digital divide', _m('DIVIDE', 'Digital divide: <b>D</b>igital illiteracy · <b>I</b>ncome and telemedicine missed · <b>V</b>ernacular content gap · <b>I</b>nternet users 75% urban · <b>D</b>ependent elderly · <b>E</b>nd (last-mile) connectivity.'))],
 23: [('Way forward', _m('PEACH', 'Cyber way forward: <b>P</b>PP hubs · <b>E</b>nforce DPDPA 2023 · <b>A</b>uthority and capacity (CERT-In, I4C, cyber authority) · <b>C</b>yber education · <b>H</b>ome-grown R&amp;D.'))],
 26: [('Significance', _m('PACT-D', 'Why the 2026 Bill matters: <b>P</b>revents avoidance · <b>A</b>ssets protected · <b>C</b>loses the legal gap · <b>T</b>ransparency and anti-money-laundering · <b>D</b>ecriminalisation.'))],
}
def add_mn(nodes, cid, done=None):
    done = set() if done is None else done; out = []
    for x in nodes:
        if x[0] == 'two':
            out.append(('two', add_mn(x[1] if isinstance(x[1], list) else [x[1]], cid, done), add_mn(x[2] if isinstance(x[2], list) else [x[2]], cid, done))); continue
        out.append(x)
        if x[0] == 'tree':
            lab = re.sub(r'<[^>]+>', '', x[1])
            for k, (pre, node) in enumerate(ADD_MN.get(cid, [])):
                if (cid, k) not in done and lab.startswith(pre):
                    done.add((cid, k)); out.append(node)
    return out
def apply_all(chs, log=None):
    apply(chs, log)
    for c in chs: c['nodes'] = add_mn(c['nodes'], c['id'])
    return chs
