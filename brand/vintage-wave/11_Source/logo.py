"""Vintage Wave logo system — vector rebuild of the original wave symbol and hand-cut wordmark."""
import math, os
from textpath import text_path
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(n):
    b, d = open(os.path.join(HERE, n)).read().split('\n')[:2]; return [float(v) for v in b.split()], d
(SX0, SY0, SX1, SY1), SYM = _load('symbol.path')
(WX0, WY0, WX1, WY1), WORD = _load('word.path')
SW, SH = SX1 - SX0, SY1 - SY0          # 549.7 x 291.5
WW, WH = WX1 - WX0, WY1 - WY0          # 419.4 x 61
# ---- Palette (from autumn leaves, faded denim and kraft paper)
ESPRESSO, CREAM, RUST, AMBER, MAPLE, DENIM, SAGE, KRAFT = '#2A1712', '#F3ECE1', '#A63D1E', '#D9962B', '#6E1F17', '#48657A', '#8A8F68', '#C9A57A'
INK = '#1C0F0B'
SCHEMES = {'cream': CREAM, 'espresso': ESPRESSO, 'rust': RUST, 'amber': AMBER, 'black': '#000000', 'white': '#FFFFFF'}
SCHEME_BG = {'cream': ESPRESSO, 'espresso': CREAM, 'rust': CREAM, 'amber': ESPRESSO, 'black': '#FFFFFF', 'white': ESPRESSO}
def symbol(fill, x=0, y=0, h=SH):
    s = h / SH
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({x - SX0*s:.3f},{y - SY0*s:.3f}) scale({s:.5f})" d="{SYM}"/>'
def word(fill, x=0, y=0, w=WW):
    s = w / WW
    return f'<path fill-rule="evenodd" fill="{fill}" transform="translate({x - WX0*s:.3f},{y - WY0*s:.3f}) scale({s:.5f})" d="{WORD}"/>'
def lk_stacked(sc):            # the original lockup
    c = SCHEMES[sc]; ww = SW*0.765; wh = WH*ww/WW; gap = SH*0.17
    return SW, SH + gap + wh, symbol(c, 0, 0) + word(c, (SW - ww)/2, SH + gap, ww)
def lk_horizontal(sc):
    c = SCHEMES[sc]; h = 200; sw = SW*h/SH; ww = 520; wh = WH*ww/WW
    return sw + 46 + ww, h, symbol(c, 0, 0, h) + word(c, sw + 46, (h - wh)/2 + 8, ww)
def lk_symbol(sc): return SW, SH, symbol(SCHEMES[sc])
def lk_wordmark(sc): return WW, WH, word(SCHEMES[sc])
def lk_tagline(sc):            # wordmark + descriptor, for the shop header and labels
    c = SCHEMES[sc]; d, w = text_path('THRIFT · VINTAGE · PRE-LOVED', 'DMSans-700.ttf', 17.5, 0, 0, tracking=0.32)
    s = WW / w
    return WW, WH + 34, word(c) + f'<path fill="{c}" transform="translate(0,{WH + 32}) scale({s:.4f},1)" d="{d}"/>'
def ring_text(text, font, size, cx, cy, r, start=-90, tracking=0.12, fill='#000', inside=False):
    """Set text along a circle, glyph by glyph (outlines, so the SVG stays portable)."""
    from textpath import _load as L
    tt, hbf, upem = L(font); out = []
    widths = []
    for ch in text:
        _, w = text_path(ch, font, size, 0, 0); widths.append(w + tracking*size)
    total = sum(widths); tdeg = math.degrees(total / r)
    ang = start - tdeg/2 if not inside else start + tdeg/2
    for ch, w in zip(text, widths):
        step = math.degrees(w / r)
        mid = ang + step/2 if not inside else ang - step/2
        d, gw = text_path(ch, font, size, -(w - tracking*size)/2, 0 if not inside else size*0.72)
        rot = mid + 90 if not inside else mid - 90
        if ch.strip():
            out.append(f'<path fill="{fill}" d="{d}" transform="translate({cx + r*math.cos(math.radians(mid)):.2f},{cy + r*math.sin(math.radians(mid)):.2f}) rotate({rot:.2f})"/>')
        ang = ang + step if not inside else ang - step
    return ''.join(out)
def lk_badge(sc):
    c = SCHEMES[sc]; R = 300
    ring = (f'<circle cx="{R}" cy="{R}" r="{R - 6}" fill="none" stroke="{c}" stroke-width="6"/><circle cx="{R}" cy="{R}" r="{R - 92}" fill="none" stroke="{c}" stroke-width="2.5"/>'
            + ring_text('VINTAGE WAVE', 'Fraunces-900.ttf', 50, R, R, R - 66, -90, 0.10, c)
            + ring_text('THRIFT · EST. 2026', 'Fraunces-700.ttf', 34, R, R, R - 68, 90, 0.16, c, inside=True)
            + f'<circle cx="{R - 222}" cy="{R}" r="6" fill="{c}"/><circle cx="{R + 222}" cy="{R}" r="6" fill="{c}"/>')
    sh = 170; sw = SW*sh/SH
    return 2*R, 2*R, ring + symbol(c, R - sw/2, R - sh/2 - 4, sh)
LOCKUPS = {'stacked': lk_stacked, 'horizontal': lk_horizontal, 'symbol': lk_symbol, 'wordmark': lk_wordmark, 'tagline': lk_tagline, 'badge': lk_badge}
def svg_doc(w, h, inner, pad=0, bg=None, title='Vintage Wave'):
    W_, H_ = w + 2*pad, h + 2*pad
    b = f'<rect width="{W_:.2f}" height="{H_:.2f}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_:.2f} {H_:.2f}" width="{W_:.2f}" height="{H_:.2f}"><title>{title}</title>{b}'
            f'<g transform="translate({pad:.2f},{pad:.2f})">{inner}</g></svg>')
