"""gymliink logo system — "Le lien ii": the two i's of the name drawn as two interlocked links."""
from geo import *
from textpath import text_path
VOLT_DEEP = '#7FA61A'          # Volt for light backgrounds (proposed addition)
# ---- Symbol construction (units)
T, GAPW = 10, 4                       # link stroke, weave gap
LA, LB = (25, 36, 50, 82), (45, 36, 50, 82)   # the two links: x, y, w, h (offset = 2 strokes)
DOTS = ((50, 16), (70, 16)); DR = 7.5         # tittles: member (left), gym (right, Volt)
SX0, SY0, SW, SH = 25, 8.5, 70, 109.5         # symbol bounds
WEAVE_Y = 77                                  # links cross over above, under below
# Colourways: (link, dot1, dot2, word, tittle1, tittle2)
SCHEMES = {
    'color-dark':  (TXT, TXT, VOLT, TXT, TXT, VOLT),
    'color-light': (BG, BG, VOLT_DEEP, BG, BG, VOLT_DEEP),
    'volt':        (VOLT, VOLT, VOLT, VOLT, VOLT, VOLT),
    'black':       ('#000000',) * 6,
    'white':       ('#FFFFFF',) * 6,
    'on-volt':     (INK_ON_VOLT,) * 6,
}
SCHEME_BG = {'color-dark': BG, 'color-light': LBG, 'volt': BG, 'black': '#FFFFFF', 'white': BG, 'on-volt': VOLT}

def symbol(link, d1, d2, ox=0, oy=0, s=1.0, small=False):
    """The symbol, placed so its bounds start at (ox, oy). small=True: optical version for ≤ 24 px (heavier, no weave gap)."""
    tr = f'translate({ox - SX0*s:.3f},{oy - SY0*s:.3f}) scale({s})'
    if small:
        t = 12
        body = f'<path fill-rule="nonzero" fill="{link}" d="{ring(*LA, t)}"/><path fill-rule="evenodd" fill="{link}" d="{ring(*LB, t)}"/>'
        body = f'<path fill-rule="evenodd" fill="{link}" d="{ring(*LA, t)}"/><path fill-rule="evenodd" fill="{link}" d="{ring(*LB, t)}"/>'
        dots = f'<circle cx="{DOTS[0][0]}" cy="{DOTS[0][1]}" r="{DR+1}" fill="{d1}"/><circle cx="{DOTS[1][0]}" cy="{DOTS[1][1]}" r="{DR+1}" fill="{d2}"/>'
        return f'<g transform="{tr}">{body}{dots}</g>'
    body = weave(ring(*LA, T), ring(*LB, T), ring(*LA, T, GAPW), ring(*LB, T, GAPW), WEAVE_Y, link)
    dots = f'<circle cx="{DOTS[0][0]}" cy="{DOTS[0][1]}" r="{DR}" fill="{d1}"/><circle cx="{DOTS[1][0]}" cy="{DOTS[1][1]}" r="{DR}" fill="{d2}"/>'
    return f'<g transform="{tr}">{body}{dots}</g>'

def wordmark_svg(c, t1, t2, size, x, y):
    """gymliink — Geist SemiBold, custom-kerned; dotless i's with round tittles, the second one in Volt."""
    d1, w1 = text_path('gyml', 'Geist-SemiBold.ttf', size, x, y, tracking=-0.025)
    xi = x + w1 - 0.012*size
    d2, w2 = text_path('ıı', 'Geist-SemiBold.ttf', size, xi, y, tracking=-0.01)
    d3, w3 = text_path('nk', 'Geist-SemiBold.ttf', size, xi + w2 - 0.018*size, y, tracking=-0.025)
    r = 0.0665*size; i1 = xi + 0.1345*size; i2 = i1 + 0.259*size; cy = y - 0.655*size
    return (f'<path d="{d1} {d2} {d3}" fill="{c}"/><circle cx="{i1:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{t1}"/>'
            f'<circle cx="{i2:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{t2}"/>'), (xi + w2 - 0.018*size + w3) - x

AR_NAME = 'جيم لينك'
AR_FONT = 'IBMPlexSansArabic-600.ttf'
WS = 100                                # wordmark size in lockups (units)
def lk_symbol(sc, small=False):
    l, d1, d2, *_ = SCHEMES[sc]; return SW, SH, symbol(l, d1, d2, 0, 0, 1, small)
def lk_wordmark(sc):
    _, _, _, w, t1, t2 = SCHEMES[sc]
    svg, ww = wordmark_svg(w, t1, t2, WS, 0, 0.719*WS)
    return ww, 0.719*WS + 0.165*WS, svg
def lk_horizontal(sc):
    l, d1, d2, w, t1, t2 = SCHEMES[sc]
    s = 1.08*WS / SH                       # symbol rises above the ascenders, links sit on the baseline
    sh = SH*s; base = sh                  # links sit on the baseline
    word, ww = wordmark_svg(w, t1, t2, WS, SW*s + 0.26*WS, base)
    return SW*s + 0.26*WS + ww, base + 0.165*WS, symbol(l, d1, d2, 0, 0, s) + word
def lk_stacked(sc):
    l, d1, d2, w, t1, t2 = SCHEMES[sc]
    _, ww = wordmark_svg(w, t1, t2, WS, 0, 0)
    s = 1.35; sw, sh = SW*s, SH*s
    word, _ = wordmark_svg(w, t1, t2, WS, 0, sh + 0.42*WS + 0.719*WS)
    return ww, sh + 0.42*WS + 0.719*WS + 0.165*WS, symbol(l, d1, d2, (ww - sw)/2, 0, s) + word
def ar_text(fill, size, x, y, anchor='start'):
    d, w = text_path(AR_NAME, AR_FONT, size, x, y, anchor=anchor); return f'<path d="{d}" fill="{fill}"/>', w
def lk_arabic(sc):
    """Arabic lockup, right-to-left: the symbol leads on the right."""
    l, d1, d2, w, *_ = SCHEMES[sc]
    s = 1.08*WS / SH; sw, sh = SW*s, SH*s
    asize = 0.84*WS                        # Plex Arabic sized to match the colour of the Latin wordmark
    a, aw = ar_text(w, asize, 0, sh - 0.04*WS)
    return aw + 0.34*WS + sw, sh + 0.30*WS, a + symbol(l, d1, d2, aw + 0.34*WS, 0, s)
def lk_arabic_stacked(sc):
    l, d1, d2, w, *_ = SCHEMES[sc]
    _, aw = ar_text(w, 0.95*WS, 0, 0)
    s = 1.35; sw, sh = SW*s, SH*s
    a, _ = ar_text(w, 0.95*WS, 0, sh + 0.40*WS + 0.66*WS)
    return aw, sh + 0.40*WS + 0.72*WS + 0.35*WS, symbol(l, d1, d2, (aw - sw)/2, 0, s) + a
def lk_bilingual(sc):
    l, d1, d2, w, t1, t2 = SCHEMES[sc]
    W1, H1, inner = lk_horizontal(sc)
    a, aw = ar_text(w if sc not in ('color-dark', 'color-light') else (TXT2 if sc == 'color-dark' else '#5C5C66'), 0.62*WS, W1, H1 + 0.62*WS, anchor='end')
    return W1, H1 + 0.62*WS + 0.2*WS, inner + a
LOCKUPS = {'horizontal': lk_horizontal, 'stacked': lk_stacked, 'symbol': lk_symbol, 'symbol-small': lambda sc: lk_symbol(sc, True),
           'wordmark': lk_wordmark, 'arabic': lk_arabic, 'arabic-stacked': lk_arabic_stacked, 'bilingual': lk_bilingual}
def svg_doc(w, h, inner, pad=0, bg=None, title='Gymliink'):
    W_, H_ = w + 2*pad, h + 2*pad
    b = f'<rect width="{W_:.2f}" height="{H_:.2f}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_:.2f} {H_:.2f}" width="{W_:.2f}" height="{H_:.2f}"><title>{title}</title>{b}'
            f'<g transform="translate({pad},{pad})">{inner}</g></svg>')
