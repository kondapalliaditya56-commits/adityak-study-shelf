# -*- coding: utf-8 -*-
"""Hand-drawn style SVG graphs for the Economy handwritten notes (curves, bars, loops, ladders).
Every function returns an <svg> string that WeasyPrint can place inline. Fonts KL/KB come from hwlib CSS."""
import html as _h

INK = '#1a237e'; RED = '#c62828'; GRN = '#2e7d32'; ORG = '#e65100'; BLU = '#1565c0'; PUR = '#6a1b9a'


def esc(t): return _h.escape(t, quote=False)


def qb(p0, p1, p2, t):
    return ((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0], (1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1])


def cross(a, b, n=400):
    best = None
    for i in range(n+1):
        pa = qb(*a, i/n)
        for j in range(0, n+1, 2):
            pb = qb(*b, j/n); d = (pa[0]-pb[0])**2+(pa[1]-pb[1])**2
            if best is None or d < best[0]: best = (d, pa)
    return best[1]


class Cv:
    def __init__(self, w=320, h=190, title=None):
        self.w, self.h, self.o = w, h, []
        self.title = title

    def add(self, s): self.o.append(s); return self

    def text(self, x, y, t, size=8, fill=INK, anchor='middle', bold=False, rot=None):
        tr = ' transform="rotate(%s %.1f %.1f)"' % (rot, x, y) if rot else ''
        return self.add('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s%s>%s</text>' % (
            x, y, size, fill, anchor, ' font-family="KB"' if bold else '', tr, esc(t)))

    def line(self, x1, y1, x2, y2, c=INK, w=1.2, dash=None, arrow=False):
        return self.add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s%s/>' % (
            x1, y1, x2, y2, c, w, ' stroke-dasharray="%s"' % dash if dash else '', ' marker-end="url(#ar)"' if arrow else ''))

    def path(self, d, c=INK, w=1.8, dash=None, arrow=False, fill='none'):
        return self.add('<path d="%s" stroke="%s" stroke-width="%s" fill="%s"%s%s stroke-linecap="round"/>' % (
            d, c, w, fill, ' stroke-dasharray="%s"' % dash if dash else '', ' marker-end="url(#ar)"' if arrow else ''))

    def dot(self, x, y, c=RED, r=2.6): return self.add('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, r, c))

    def rect(self, x, y, w, h, fill='#fff', stroke=INK, sw=1.3, rx=3):
        return self.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, rx, fill, stroke, sw))

    def axes(self, x0, y0, x1, y1, xl='', yl=''):
        """origin (x0,y0) bottom-left; x1 right end; y1 top end (smaller y)."""
        self.line(x0, y0, x1, y0, INK, 1.6, arrow=True)
        self.line(x0, y0, x0, y1, INK, 1.6, arrow=True)
        if xl: self.text((x0 + x1) / 2, y0 + 24, xl, 8, INK, bold=True)
        if yl: self.text(x0 - 14, (y0 + y1) / 2, yl, 8, INK, bold=True, rot=-90)
        return self

    def svg(self, maxw=150):
        s = ('<svg class="sv" viewBox="0 0 %d %d" width="100%%" style="max-width:%dmm"><defs><marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">'
             '<path d="M0,0L7,3.5L0,7z" fill="#111"/></marker></defs><g font-family="KL" font-size="8" text-anchor="middle">%s</g></svg>') % (self.w, self.h, maxw, ''.join(self.o))
        if self.title: s = '<div class="gtitle">%s</div>' % esc(self.title) + s
        return s


def two_panels(left, right, maxw=165):
    """Two graphs side by side (each a Cv with w=160)."""
    return '<div class="gp2"><div>%s</div><div>%s</div></div>' % (left.svg(80), right.svg(80))


# ---------- ready-made economy graphs ----------
def adas_equilibrium(title='AD meets AS: the price level is where they cross'):
    c = Cv(320, 200, title)
    c.axes(40, 160, 235, 20, 'Real GDP (output, Y)', 'Price level (P)')
    ad = ((62, 38), (120, 92), (215, 142)); as_ = ((62, 142), (130, 120), (215, 42))
    c.path('M%d %d Q%d %d %d %d' % (ad[0]+ad[1]+ad[2]), BLU, 2.4); c.text(224, 150, 'AD', 9, BLU, bold=True)
    c.path('M%d %d Q%d %d %d %d' % (as_[0]+as_[1]+as_[2]), RED, 2.4); c.text(224, 40, 'AS', 9, RED, bold=True)
    x, y = cross(ad, as_)
    c.line(x, y, x, 160, '#777', 1, '3 3'); c.line(40, y, x, y, '#777', 1, '3 3')
    c.dot(x, y); c.text(x + 9, y - 6, 'E', 9, RED, bold=True)
    c.text(x, 171, 'Y0', 8, INK, bold=True); c.text(30, y + 3, 'P0', 8, INK, bold=True)
    for i, t in enumerate(['AD slopes DOWN:', 'dearer goods, less', 'demanded', '', 'AS slopes UP:', 'higher price, producers', 'make more']):
        c.text(244, 60 + i * 10, t, 7, BLU if i < 3 else RED, 'start', i in (0, 4))
    return c


def demand_cost_panels():
    """Both panels are computed: curves are drawn first, the equilibria are their true intersections."""
    def P(c): return 'M%.1f %.1f Q%.1f %.1f %.1f %.1f' % (c[0]+c[1]+c[2])
    def sh(c, dx): return tuple((x+dx, y) for x, y in c)
    AD = ((40, 36), (75, 95), (135, 130)); AS = ((36, 128), (85, 110), (138, 40))
    # demand-pull: AD0 -> AD1 (right)
    AD1 = sh(AD, 16)
    e0 = cross(AD, AS); e1 = cross(AD1, AS)
    assert e1[0] > e0[0] and e1[1] < e0[1], 'demand-pull must raise price and output'
    a = Cv(160, 185, 'DEMAND-PULL: AD shifts RIGHT')
    a.axes(28, 140, 150, 20, 'Output Y', 'Price P')
    a.path(P(AD), BLU, 2, '4 3'); a.path(P(AD1), BLU, 2.2); a.path(P(AS), RED, 2.2)
    a.text(AD[2][0]+4, AD[2][1]+4, 'AD0', 7, BLU, 'start', True); a.text(AD1[2][0]+2, AD1[2][1]-3, 'AD1', 7, BLU, 'start', True); a.text(AS[2][0]+3, AS[2][1]-2, 'AS', 8, RED, 'start', True)
    for (x, y), c, lx, ly in ((e0, '#777', 'Y0', 'P0'), (e1, RED, 'Y1', 'P1')):
        a.dot(x, y, c, 2.6); a.line(x, y, x, 140, c, .9, '3 3'); a.line(28, y, x, y, c, .9, '3 3')
        a.text(x, 150, lx, 7, INK if c == '#777' else RED, bold=True); a.text(18, y+3, ly, 7, INK if c == '#777' else RED, bold=True)
    a.text(80, 181, 'price UP, output UP', 8, GRN, bold=True)
    # cost-push: AS0 -> AS1 (left)
    AS1 = sh(AS, -26)
    f0 = cross(AD, AS); f1 = cross(AD, AS1)
    assert f1[0] < f0[0] and f1[1] < f0[1], 'cost-push must raise price and cut output'
    b = Cv(160, 185, 'COST-PUSH: AS shifts LEFT')
    b.axes(28, 140, 150, 20, 'Output Y', 'Price P')
    b.path(P(AD), BLU, 2.2); b.path(P(AS), RED, 2, '4 3'); b.path(P(AS1), RED, 2.2)
    b.text(AD[2][0]+4, AD[2][1]+4, 'AD', 8, BLU, 'start', True); b.text(AS[2][0]+3, AS[2][1]-2, 'AS0', 7, RED, 'start', True); b.text(AS1[2][0]+3, AS1[2][1]-2, 'AS1', 7, RED, 'start', True)
    for (x, y), c, lx, ly in ((f0, '#777', 'Y0', 'P0'), (f1, RED, 'Y1', 'P1')):
        b.dot(x, y, c, 2.6); b.line(x, y, x, 140, c, .9, '3 3'); b.line(28, y, x, y, c, .9, '3 3')
        b.text(x, 150, lx, 7, INK if c == '#777' else RED, bold=True); b.text(18, y+3, ly, 7, INK if c == '#777' else RED, bold=True)
    b.text(80, 181, 'price UP, output DOWN', 8, RED, bold=True)
    return two_panels(a, b)


def index_bars():
    c = Cv(320, 205, 'The handout’s index example (base year March 2015 = 100)')
    c.axes(40, 160, 300, 30, 'Month of the year', 'Basket price (₹)')
    data = [('Mar 2015', 10000, 100, '#bbdefb'), ('Mar 2025', 15000, 150, '#ffe082'), ('Mar 2026', 16500, 165, '#ffccbc')]
    for i, (lab, v, ix, col) in enumerate(data):
        x = 62 + i * 70; h = v / 16500 * 105
        c.rect(x, 160 - h, 46, h, col, INK, 1.3, 2)
        c.text(x + 23, 160 - h - 14, '₹{:,}'.format(v), 8, INK, bold=True)
        c.text(x + 23, 160 - h - 4, 'index %d' % ix, 8, RED, bold=True)
        c.text(x + 23, 172, lab, 7.5, INK)
    c.text(190, 24, '+10% in the last year (150 → 165)', 8, GRN, bold=True)
    c.text(282, 80, '165 =', 8, RED, bold=True); c.text(282, 91, '+65% over', 8, RED); c.text(282, 102, '2015 base', 8, RED)
    return c


def weights_bars():
    c = Cv(320, 150, 'CPI weights: old 2012 series vs new 2024 series (handout)')
    rows = [('Food and Beverages', 45.86, 36.75), ('“Miscellaneous” bucket', 28.32, None)]
    c.text(160, 22, 'Bar length = weight in the basket (%)', 7.5, '#555')
    y = 38
    for lab, a, b in rows:
        c.text(12, y + 9, lab, 8, INK, 'start', True)
        c.rect(12, y + 14, a * 5.2, 14, '#ffe082', INK, 1.1, 2); c.text(12 + a * 5.2 + 4, y + 25, '%.2f  (2012)' % a, 7.5, INK, 'start')
        if b is not None:
            c.rect(12, y + 31, b * 5.2, 14, '#c8e6c9', INK, 1.1, 2); c.text(12 + b * 5.2 + 4, y + 42, '%.2f  (2024)' % b, 7.5, GRN, 'start', True)
        else:
            c.text(12, y + 42, '2024: broken into 12 divisions (Transport, Health, Education… separate)', 7.5, GRN, 'start', True)
        y += 58
    return c


def phillips():
    c = Cv(320, 205, 'Phillips Curve (UK 1861-1957): inflation vs unemployment')
    c.axes(40, 165, 300, 20, 'Unemployment (UE)', 'Inflation (wage growth)')
    c.path('M62 38 Q80 130 270 152', PUR, 2.6)
    c.text(185, 98, 'Phillips Curve', 9, PUR, bold=True); c.text(185, 108, '(inverse: one up, other down)', 7, PUR)
    c.dot(70, 66, GRN); c.text(78, 58, 'high inflation, low UE', 7, GRN, 'start')
    c.dot(268, 152, GRN); c.text(222, 124, 'low inflation, high UE', 7, GRN, 'middle')
    c.dot(268, 46, RED, 3.2); c.text(262, 36, 'STAGFLATION: both high', 8, RED, 'end', True)
    c.text(248, 62, '(off the curve: outlier)', 7, RED, 'end')
    c.path('M262 126 Q272 90 270 56', RED, 1.4, '3 3', arrow=True)
    return c


def real_rate_bar():
    c = Cv(320, 120, 'Real interest rate: what the lender really earns')
    c.rect(20, 40, 210, 26, '#bbdefb', INK, 1.4, 3); c.text(125, 57, 'Nominal rate NIR = 10%', 9, INK, bold=True)
    c.rect(20, 72, 147, 26, '#ffccbc', INK, 1.4, 3); c.text(93, 89, 'Inflation = 7%', 9, RED, bold=True)
    c.rect(167, 72, 63, 26, '#c8e6c9', GRN, 1.8, 3); c.text(198, 89, 'RIR = 3%', 9, GRN, bold=True)
    c.text(160, 18, 'RIR = NIR − Inflation  →  10 − 7 = 3', 10, RED, bold=True)
    c.text(240, 54, 'what the bank charges', 7, INK, 'start')
    c.text(240, 88, 'real gain left', 7, GRN, 'start')
    c.text(125, 113, 'inflation eats its share first; the rest is the real return', 7.5, '#555')
    return c


def engel_curve():
    c = Cv(320, 205, 'Engel’s Law: richer family, smaller share of income on food')
    c.axes(40, 150, 300, 20, 'Household income  →', '% of income spent on food')
    c.path('M60 36 Q100 110 285 134', ORG, 2.6)
    c.dot(75, 62, RED); c.text(90, 50, 'POOR household: most income goes on food', 7.5, RED, 'start', True)
    c.text(90, 59, 'price rise on food hits it hardest', 7, RED, 'start')
    c.dot(255, 132, GRN); c.text(262, 108, 'RICH: small share on food', 7.5, GRN, 'end', True)
    c.text(160, 198, 'absolute food spending may rise; the SHARE falls', 7.5, '#444')
    return c


def measure_ladder():
    c = Cv(320, 185, 'Inflation measures: what is left in after each subtraction')
    steps = [('HEADLINE = CPI-C (all items)', '#bbdefb', 310), ('CORE = headline − food − fuel & light', '#c8e6c9', 290),
             ('SUPER CORE = core − petrol − diesel − precious metals', '#ffe082', 310)]
    y = 12
    for lab, col, w in steps:
        c.rect(5, y, w, 28, col, INK, 1.4, 4); c.text(12, y + 18, lab, 7.6, INK, 'start', True)
        y += 36
    c.text(8, 134, 'Trap: petrol and diesel sit in Transport (inside core),', 8, RED, 'start', True)
    c.text(8, 146, 'NOT in “Fuel and Light”. They leave only at SUPER CORE.', 8, RED, 'start', True)
    c.text(8, 166, 'Skewflation: one or two items spike (onion, pulses) while the rest stay calm.', 7.2, '#444', 'start')
    return c


def price_paths():
    c = Cv(320, 206, 'Inflation vs disinflation vs deflation (price LEVEL over time)')
    c.axes(40, 160, 230, 20, 'Time  →', 'Price level')
    c.path('M50 138 L110 112 L170 78 L222 40', RED, 2.4); c.text(232, 40, 'inflation:', 7.5, RED, 'start', True); c.text(232, 49, 'rising fast', 7.5, RED, 'start')
    c.path('M50 148 L110 138 L170 124 L222 108', ORG, 2.4); c.text(232, 104, 'disinflation:', 7.5, ORG, 'start', True); c.text(232, 113, 'still rising, slower', 7.5, ORG, 'start')
    c.path('M50 100 L110 112 L170 126 L222 142', BLU, 2.4); c.text(232, 140, 'deflation:', 7.5, BLU, 'start', True); c.text(232, 149, 'price level falling', 7.5, BLU, 'start')
    c.text(160, 202, 'disinflation = the RATE falls (prices still rise).  deflation = the LEVEL falls.', 7.5, '#444')
    return c


def spiral_loop():
    c = Cv(340, 170, 'Price-wage spiral: a loop that feeds itself')
    pts = [(170, 22, 'Prices rise'), (278, 84, 'Workers demand higher wages'), (170, 146, 'Firms pass cost on to buyers'), (62, 84, 'Prices rise again')]
    for (x, y, t) in pts:
        w = 124; c.rect(x - w / 2, y - 14, w, 28, '#fff9c4', '#f9a825', 1.5, 6); c.text(x, y + 3, t, 7.4, INK, bold=True)
    c.path('M232 28 Q276 36 278 68', INK, 1.5, arrow=True)
    c.path('M270 100 Q262 138 232 144', INK, 1.5, arrow=True)
    c.path('M108 146 Q64 138 62 100', INK, 1.5, arrow=True)
    c.path('M62 68 Q66 30 108 24', INK, 1.5, arrow=True)
    c.text(170, 88, 'repeat', 10, RED, bold=True)
    return c


def fiscal_drag_bars():
    c = Cv(320, 200, 'Fiscal drag: income +20%, but tax +28.2% (handout hypothetical)')
    c.axes(40, 150, 300, 18, '', '₹ lakh')
    data = [('Income', 9, 10.8, '#bbdefb', '#90caf9'), ('Tax paid', 1.1, 1.41, '#ffccbc', '#ef9a9a'), ('Take-home', 7.9, 9.39, '#c8e6c9', '#a5d6a5')]
    for i, (lab, a, b, ca, cb) in enumerate(data):
        x = 62 + i * 80; sc = 120 / 11
        c.rect(x, 150 - a * sc, 26, a * sc, ca, INK, 1.2, 2); c.text(x + 13, 150 - a * sc - 3, '%g' % a, 7.5, INK, bold=True)
        c.rect(x + 28, 150 - b * sc, 26, b * sc, cb, INK, 1.2, 2); c.text(x + 41, 150 - b * sc - 3, '%g' % b, 7.5, RED, bold=True)
        c.text(x + 27, 162, lab, 8, INK, bold=True)
    c.text(160, 178, 'left bar = before, right bar = after the 20% raise', 7, '#555')
    c.text(160, 191, 'income +20%  ·  tax +28.2%  ·  take-home +18.8% (less than 20%)', 8, RED, bold=True)
    return c


def gain_lose():
    c = Cv(320, 150, 'Who gains and who loses when prices rise')
    c.rect(10, 24, 145, 100, '#e8f5e9', GRN, 1.6, 6); c.text(82, 40, 'GAIN', 11, GRN, bold=True)
    for i, t in enumerate(['Borrowers (debt shrinks)', 'Producers (margins grow)']):
        c.text(18, 60 + i * 20, '• ' + t, 7.2, INK, 'start')
    c.rect(165, 24, 145, 100, '#ffebee', RED, 1.6, 6); c.text(237, 40, 'LOSE', 11, RED, bold=True)
    for i, t in enumerate(['Lenders / banks (unless protected)', 'Depositors (real return negative)', 'Consumers (money buys less)']):
        c.text(173, 60 + i * 20, '• ' + t, 7.2, INK, 'start')
    c.text(160, 142, 'Remember: “LDC lose; BP gain”', 9, PUR, bold=True)
    return c


def stag_boxes():
    c = Cv(320, 120, 'Stagflation = stagnation + inflation (both at once)')
    c.rect(10, 28, 120, 50, '#e3f2fd', BLU, 1.6, 6); c.text(70, 46, 'STAGNATION', 9, BLU, bold=True); c.text(70, 60, 'low growth + high', 7.5, INK); c.text(70, 70, 'unemployment', 7.5, INK)
    c.text(145, 58, '+', 18, INK, bold=True)
    c.rect(160, 28, 120, 50, '#ffebee', RED, 1.6, 6); c.text(220, 46, 'INFLATION', 9, RED, bold=True); c.text(220, 60, 'prices rising fast', 7.5, INK)
    c.path('M70 78 Q145 108 220 78', GRN, 1.6)
    c.text(145, 112, '= STAGFLATION: fixing either worsens the other', 8, GRN, bold=True)
    return c
