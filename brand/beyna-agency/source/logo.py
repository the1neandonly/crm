"""Beyna Agency logo system v3 — "L'Œil": the b whose counter is an eye. All geometry generated from one construction."""
from textpath import text_path

# ---- Brand colours
VIOLET = '#6337FF'; LIME = '#D2FF5A'; INK = '#1B1046'; WHITE = '#FFFFFF'
G0, G1, G2 = '#9A7CFF', '#6337FF', '#2B1BB5'   # Beyna gradient: lavender -> violet -> deep indigo

# ---- Mark construction (units) — "L'Œil": a lowercase b whose counter is an eye
S = 38          # stem width (Syne Bold stem)
R = 72          # bowl radius — the bowl matches Syne's x-height, the stem its ascender
H = 192         # total mark height (stem top -> bowl bottom)
W = 2 * R       # total mark width (the stem's left edge is tangent to the bowl)
CX, CY = R, H - R
YJ = CY - (R*R - (S - CX)**2) ** 0.5   # where the stem's right edge meets the bowl
CUT = 9                  # calligraphic cut on the stem top (qalam angle), left side lower
EX, EY = CX + 4, CY      # centre of the almond (the counter), nudged toward the name
EW, EH = 110, 34         # almond width, half-height (lid sagitta)
IR, IOFF = 31, 10        # iris radius (touches both lids), offset toward the name
PR, POFF = 13.5, 6.8     # pupil radius, offset from the iris centre
GR = 5                   # catch-light radius
LID = (47, 22, 27.5, 23.5)   # eyelid crease: half-chord, end drop, outer / inner sagitta
IRIS_RING = '#A9D63C'    # limbal ring and iris fibres (deeper lime)
GAP, SR = IOFF, IR       # legacy names

WORD_FONT = 'Syne-700.ttf'
SUB_FONT = 'Manrope-700.ttf'

def grad_def(gid, x1=0, y1=0, x2=1, y2=1):
    return (f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{G0}"/><stop offset="0.55" stop-color="{G1}"/>'
            f'<stop offset="1" stop-color="{G2}"/></linearGradient>')

def _circ(cx, cy, r, rev=False):
    s = 0 if rev else 1
    return f'M{cx - r:.3f},{cy:.3f} a{r:.3f},{r:.3f} 0 1,{s} {2*r:.3f},0 a{r:.3f},{r:.3f} 0 1,{s} {-2*r:.3f},0 Z'

def _P(ox, oy, scale):
    return lambda x, y: f'{ox + x*scale:.3f},{oy + y*scale:.3f}'

def body_d(ox=0, oy=0, scale=1.0):
    """Stem with a calligraphic (qalam) cut on top + full bowl, as one closed outline."""
    p = _P(ox, oy, scale); r = R*scale
    return f'M{p(0, CUT)} L{p(S, 0)} L{p(S, YJ)} A{r:.3f},{r:.3f} 0 1,1 {p(0, CY)} Z'

def almond_d(ox=0, oy=0, scale=1.0, rev=False):
    """The counter: two circular arcs meeting in sharp corners — the eye."""
    p = _P(ox, oy, scale)
    r = ((EW/2)**2 + EH**2) / (2*EH) * scale
    a, b = (EX - EW/2, EX + EW/2) if not rev else (EX + EW/2, EX - EW/2)
    sw = 0 if rev else 1
    return f'M{p(a, EY)} A{r:.3f},{r:.3f} 0 0,{sw} {p(b, EY)} A{r:.3f},{r:.3f} 0 0,{sw} {p(a, EY)} Z'

def lid_d(ox=0, oy=0, scale=1.0, rev=False):
    """The eyelid crease: a fine crescent above the eye, sharp at both ends."""
    p = _P(ox, oy, scale); c, drop, so, si = LID
    ro = (c*c + so*so) / (2*so) * scale; ri = (c*c + si*si) / (2*si) * scale
    a, b, y = (EX - c, EX + c, EY - drop)
    if rev: return f'M{p(b, y)} A{ro:.3f},{ro:.3f} 0 0,0 {p(a, y)} A{ri:.3f},{ri:.3f} 0 0,1 {p(b, y)} Z'
    return f'M{p(a, y)} A{ro:.3f},{ro:.3f} 0 0,1 {p(b, y)} A{ri:.3f},{ri:.3f} 0 0,0 {p(a, y)} Z'

def lid_shadow_d(ox=0, oy=0, scale=1.0):
    """Soft shadow under the upper lid, on the white of the eye."""
    p = _P(ox, oy, scale)
    r = ((EW/2)**2 + EH**2) / (2*EH) * scale; h2 = EH - 7; r2 = ((EW/2)**2 + h2**2) / (2*h2) * scale
    return f'M{p(EX - EW/2, EY)} A{r:.3f},{r:.3f} 0 0,1 {p(EX + EW/2, EY)} A{r2:.3f},{r2:.3f} 0 0,0 {p(EX - EW/2, EY)} Z'

def _white(c): return str(c).lower() in ('#fff', '#ffffff', 'white')

def eye_centres(ox=0, oy=0, scale=1.0, look=1):
    t = lambda x, y: (ox + x*scale, oy + y*scale)
    ix = EX + look*IOFF; px = ix + look*POFF
    return t(ix, EY), t(px, EY), t(px + look*PR*0.55, EY - PR*0.58)

def iris_svg(ix, iy, px, py, gx, gy, s, iris_fill, pupil, look=1, detail=True):
    """Iris with limbal ring and fibres, pupil, two catch-lights."""
    out = f'<circle cx="{ix:.3f}" cy="{iy:.3f}" r="{IR*s:.3f}" fill="{iris_fill}"/>'
    if detail and iris_fill in (LIME, '#D2FF5A'):
        import math
        fib = ''.join(f'M{px + 15.5*s*math.cos(a):.2f},{py + 15.5*s*math.sin(a):.2f}L{ix + 27.5*s*math.cos(a):.2f},{iy + 27.5*s*math.sin(a):.2f}'
                      for a in [k*math.pi/9 for k in range(18)])
        out += (f'<path d="{fib}" stroke="{IRIS_RING}" stroke-width="{1.15*s:.2f}" stroke-linecap="round" fill="none" opacity=".85"/>'
                f'<circle cx="{ix:.3f}" cy="{iy:.3f}" r="{(IR - 1.4)*s:.3f}" fill="none" stroke="{IRIS_RING}" stroke-width="{2.8*s:.2f}"/>')
    hx, hy = px - look*PR*0.62*s, py + PR*0.5*s
    return out + (f'<circle cx="{px:.3f}" cy="{py:.3f}" r="{PR*s:.3f}" fill="{pupil}"/>'
                  f'<circle cx="{gx:.3f}" cy="{gy:.3f}" r="{GR*s:.3f}" fill="#FFFFFF"/>'
                  f'<circle cx="{hx:.3f}" cy="{hy:.3f}" r="{1.9*s:.3f}" fill="#FFFFFF" opacity=".9"/>')

def mark_paths(body_fill, iris_fill, ox=0, oy=0, scale=1.0, look=1, pupil=None):
    """The symbol. Colour: white of the eye, lime iris with fibres, ink pupil, catch-lights.
    Mono (body == iris): a single colour, the white of the eye and the crease knocked out."""
    s = scale
    (ix, iy), (px, py), (gx, gy) = eye_centres(ox, oy, s, look)
    holes = f'{almond_d(ox, oy, s, rev=True)} {lid_d(ox, oy, s, rev=True)}'
    if body_fill == iris_fill:
        return (f'<path fill-rule="evenodd" fill="{body_fill}" d="{body_d(ox, oy, s)} {holes}"/>'
                f'<path fill-rule="evenodd" fill="{body_fill}" d="{_circ(ix, iy, IR*s)} {_circ(gx, gy, GR*1.3*s, True)}"/>')
    knock = _white(body_fill) or _white(iris_fill) or 'rgba' in str(body_fill)
    if knock: out = f'<path fill-rule="evenodd" fill="{body_fill}" d="{body_d(ox, oy, s)} {holes}"/>'
    else: out = (f'<path fill-rule="evenodd" fill="{body_fill}" d="{body_d(ox, oy, s)} {lid_d(ox, oy, s, rev=True)}"/><path fill="{LIME}" d="{lid_d(ox, oy, s)}"/>'
                 f'<path fill="#FFFFFF" d="{almond_d(ox, oy, s)}"/><path fill="#E6E2F5" d="{lid_shadow_d(ox, oy, s)}"/>')
    return out + iris_svg(ix, iy, px, py, gx, gy, s, iris_fill, pupil or INK, look, detail=not knock or iris_fill == LIME)

# Colourways: (body, slice, word, sub)
SCHEMES = {
    'color':       ('url(#bg)', LIME, VIOLET, INK),      # on white / light
    'color-dark':  ('url(#bg)', LIME, WHITE, LIME),      # on ink
    'on-violet':   (WHITE, LIME, WHITE, LIME),           # on violet / gradient
    'on-lime':     (INK, VIOLET, INK, INK),              # on lime
    'black':       (INK, INK, INK, INK),                 # mono
    'white':       (WHITE, WHITE, WHITE, WHITE),         # mono reversed
}
# accessible slice for mono: gap keeps it readable

def svg_wrap(w, h, inner, bg=None, pad=0, title='Beyna Agency'):
    W_, H_ = w + 2*pad, h + 2*pad
    bgr = f'<rect width="{W_}" height="{H_}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_:.2f} {H_:.2f}" '
            f'width="{W_:.2f}" height="{H_:.2f}"><title>{title}</title><defs>{grad_def("bg")}</defs>{bgr}'
            f'<g transform="translate({pad},{pad})">{inner}</g></svg>')

# ---- Lockups
def icon(scheme):
    b, s, _, _ = SCHEMES[scheme]
    return W, H, mark_paths(b, s)

def wordmark_paths(fill, size, x, baseline):
    d, w = text_path('beyna', WORD_FONT, size, x, baseline, tracking=-0.015)
    return f'<path d="{d}" fill="{fill}"/>', w

def sub_paths(text, fill, size, x, baseline, anchor='start', tracking=0.42):
    d, w = text_path(text, SUB_FONT, size, x, baseline, tracking=tracking, anchor=anchor)
    return f'<path d="{d}" fill="{fill}"/>', w

LOGO_SIZE = H / 0.697            # Syne size whose 'b' ascender equals the symbol height
def ayna(fill, x=0):
    """'eyna' set so that the symbol reads as the first letter of beyna."""
    d, w = text_path('eyna', WORD_FONT, LOGO_SIZE, x + W + 0.045*LOGO_SIZE, H, tracking=-0.015)
    return f'<path d="{d}" fill="{fill}"/>', W + 0.045*LOGO_SIZE + w

def horizontal(scheme, tagline=True):
    """Primary logo: the eye-b followed by 'eyna' — the symbol is the first letter of the name."""
    b, s, wc, sc = SCHEMES[scheme]
    word, tw = ayna(wc)
    inner = mark_paths(b, s) + word
    if tagline:                     # descriptor tucked into the ascender zone above "yna"
        sub, _ = sub_paths('AGENCY', sc, 36, tw, H - 0.697*LOGO_SIZE + 0.72*36, anchor='end', tracking=0.5)
        inner += sub
    return tw, H + 0.2*LOGO_SIZE, inner

def stacked(scheme, tagline=True):
    b, s, wc, sc = SCHEMES[scheme]
    size = 200
    _, ww = text_path('beyna', WORD_FONT, size, 0, 0, tracking=-0.015)
    tot_w = ww
    mx = (tot_w - W) / 2
    inner = mark_paths(b, s, ox=mx)
    base = H + 56 + 0.697*size
    word, _ = wordmark_paths(wc, size, 0, base)
    inner += word
    h = base + 4
    if tagline:
        sub, _ = sub_paths('AGENCY', sc, 34, tot_w/2, base + 78, anchor='middle', tracking=0.9)
        inner += sub; h = base + 78
    return tot_w, h, inner

def wordmark(scheme, tagline=True):
    _, _, wc, sc = SCHEMES[scheme]
    size = 236
    word, ww = wordmark_paths(wc, size, -0.08*size, 0.697*size)   # cancel the 'b' side-bearing
    ww -= 0.08*size
    h = 0.697*size + 0.2*size   # descender of y
    inner = word
    if tagline:
        sub, _ = sub_paths('AGENCY', sc, 34, ww, 0.697*size + 64, anchor='end', tracking=0.62)
        inner += sub
        h = 0.697*size + 0.21*size
    return ww, h, inner

AR_FONT = 'ReadexPro-700.ttf'

def arabic(scheme, size=170):
    """Arabic lockup — باينة (Darija: clear, obvious). Reads right-to-left, so the symbol leads on the right."""
    b, s, wc, sc = SCHEMES[scheme]
    d, w = text_path('باينة', AR_FONT, size, 0, H - 1)
    return w + 48 + W, H + 0.45*size, f'<path d="{d}" fill="{wc}"/>' + mark_paths(b, s, ox=w + 48, look=-1)

def bilingual(scheme):
    _, _, _, sc = SCHEMES[scheme]
    tw, th, inner = horizontal(scheme)
    d, _ = text_path('باينة', AR_FONT, 104, tw, H + 150, anchor='end')
    return tw, H + 180, inner + f'<path d="{d}" fill="{sc}"/>'

def bilingual_stacked(scheme):
    b, s, wc, sc = SCHEMES[scheme]
    size, asize, gap = 150, 140, 60
    _, w1 = text_path('beyna', WORD_FONT, size, 0, 0)
    _, w2 = text_path('باينة', AR_FONT, asize, 0, 0)
    tot = w1 + gap + w2; base = H + 50 + 0.697*size
    l, _ = text_path('beyna', WORD_FONT, size, 0, base)
    a, _ = text_path('باينة', AR_FONT, asize, w1 + gap, base)
    return tot, base + 60, (mark_paths(b, s, ox=(tot - W)/2) + f'<path d="{l}" fill="{wc}"/>'
            f'<rect x="{w1 + gap/2 - 1.5}" y="{base - 100}" width="3" height="110" fill="{sc}"/><path d="{a}" fill="{wc}"/>')

def wordmark_plain(scheme):
    """The lettering alone — 'beyna' without the AGENCY descriptor."""
    return wordmark(scheme, tagline=False)

def arabic_wordmark(scheme, size=170):
    """The Arabic lettering alone — باينة without the symbol."""
    _, _, wc, _ = SCHEMES[scheme]
    d, w = text_path('باينة', AR_FONT, size, 0, 0.62*size)
    return w, 0.62*size + 0.42*size, f'<path d="{d}" fill="{wc}"/>'

LOCKUPS = {'horizontal': horizontal, 'horizontal-compact': lambda sch: horizontal(sch, tagline=False), 'stacked': stacked, 'symbol': icon, 'wordmark-plain': wordmark_plain, 'arabic-wordmark': arabic_wordmark, 'arabic': arabic, 'bilingual': bilingual, 'bilingual-stacked': bilingual_stacked, 'wordmark': wordmark}

def build(lockup, scheme, pad_ratio=0.0, bg=None):
    fn = LOCKUPS[lockup]
    w, h, inner = fn(scheme)
    pad = pad_ratio * min(w, h) if pad_ratio else 0
    return svg_wrap(w, h, inner, bg=bg, pad=pad), (w, h)
