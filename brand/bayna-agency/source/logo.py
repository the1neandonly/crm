"""Bayna Agency logo system — all geometry generated from a single construction grid."""
from textpath import text_path

# ---- Brand colours
VIOLET = '#6337FF'; LIME = '#D2FF5A'; INK = '#24242B'; WHITE = '#FFFFFF'
G0, G1, G2 = '#9A7CFF', '#6337FF', '#2B1BB5'   # Bayna gradient: lavender -> violet -> deep indigo

# ---- Mark construction (units)
S = 36          # stem width  (= R/2)
R = 72          # bowl radius
GAP = 8         # slice offset (= R/9)
H = 192         # total mark height
W = 2 * R       # total mark width
CX, CY = R, H - R
SR = R - S - GAP  # lime slice radius

WORD_FONT = 'Syne-700.ttf'
SUB_FONT = 'Manrope-700.ttf'

def grad_def(gid, x1=0, y1=0, x2=1, y2=1):
    return (f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{G0}"/><stop offset="0.55" stop-color="{G1}"/>'
            f'<stop offset="1" stop-color="{G2}"/></linearGradient>')

def mark_paths(body_fill, slice_fill, ox=0, oy=0, scale=1.0):
    def p(x, y): return f'{ox + x*scale:.3f},{oy + y*scale:.3f}'
    r = R*scale; sr = SR*scale
    body = (f'M{p(0,0)} L{p(S,0)} L{p(S,CY)} L{p(CX,CY)} L{p(CX,CY-R)} '
            f'A{r:.3f},{r:.3f} 0 1,1 {p(0,CY)} Z')
    sx, sy = CX - GAP, CY - GAP
    slc = f'M{p(sx,sy)} L{p(sx-SR,sy)} A{sr:.3f},{sr:.3f} 0 0,1 {p(sx,sy-SR)} Z'
    return f'<path d="{body}" fill="{body_fill}"/><path d="{slc}" fill="{slice_fill}"/>'

# Colourways: (body, slice, word, sub)
SCHEMES = {
    'color':       ('url(#bg)', LIME, INK, VIOLET),      # on white / light
    'color-dark':  ('url(#bg)', LIME, WHITE, LIME),      # on ink
    'on-violet':   (WHITE, LIME, WHITE, LIME),           # on violet / gradient
    'on-lime':     (INK, VIOLET, INK, INK),              # on lime
    'black':       (INK, INK, INK, INK),                 # mono
    'white':       (WHITE, WHITE, WHITE, WHITE),         # mono reversed
}
# accessible slice for mono: gap keeps it readable

def svg_wrap(w, h, inner, bg=None, pad=0, title='Bayna Agency'):
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
    d, w = text_path('bayna', WORD_FONT, size, x, baseline, tracking=-0.015)
    return f'<path d="{d}" fill="{fill}"/>', w

def sub_paths(text, fill, size, x, baseline, anchor='start', tracking=0.42):
    d, w = text_path(text, SUB_FONT, size, x, baseline, tracking=tracking, anchor=anchor)
    return f'<path d="{d}" fill="{fill}"/>', w

def horizontal(scheme, tagline=True):
    b, s, wc, sc = SCHEMES[scheme]
    size = 196                      # 'b' ascender ~ 137u, x-height 98u
    gapx = 48
    base = H - 1                    # wordmark baseline sits on the bowl (optical overshoot 1u)
    word, ww = wordmark_paths(wc, size, W + gapx, base)
    inner = mark_paths(b, s) + word
    total_w = W + gapx + ww
    if tagline:                     # descriptor tucked into the ascender zone above "yna"
        sub, _ = sub_paths('AGENCY', sc, 29, total_w, base - 0.697*size + 0.72*29, anchor='end', tracking=0.46)
        inner += sub
    return total_w, H + 0.2*size, inner

def stacked(scheme, tagline=True):
    b, s, wc, sc = SCHEMES[scheme]
    size = 200
    _, ww = text_path('bayna', WORD_FONT, size, 0, 0, tracking=-0.015)
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

LOCKUPS = {'horizontal': horizontal, 'horizontal-compact': lambda sch: horizontal(sch, tagline=False), 'stacked': stacked, 'icon': icon, 'wordmark': wordmark}

def build(lockup, scheme, pad_ratio=0.0, bg=None):
    fn = LOCKUPS[lockup]
    w, h, inner = fn(scheme)
    pad = pad_ratio * min(w, h) if pad_ratio else 0
    return svg_wrap(w, h, inner, bg=bg, pad=pad), (w, h)
