"""DevelopTheOne logo system — same API as the Bayna system so every template generator works unchanged."""
from textpath import text_path
from dto_mark import full_mark, icon_mark, MW, MH, IW, IH, BLUE as _B, INK as _I, WHITE as _W, GRAY as _G

# ---- Brand colours (names kept for template compatibility: VIOLET = primary, LIME = highlight)
VIOLET = '#0F66B6'     # DTO Blue — the wordmark blue of the original logo
LIME = '#4AA3F0'       # Sky Blue — highlight on dark surfaces
INK = '#0A0B0D'        # Code Black — the mark
WHITE = '#FFFFFF'
GRAYC = '#A5A8AA'      # Cursor Gray — the T outline of the original
G0, G1, G2 = '#4AA3F0', '#0F66B6', '#0A3D73'   # DTO gradient: sky → blue → navy

W, H = IW, IH          # the icon ({D} + cursor) is the compact symbol used in templates
WORD_FONT = 'Montserrat-700.ttf'; SUB_FONT = 'Montserrat-600.ttf'; AR_FONT = 'Cairo-700.ttf'

def grad_def(gid, x1=0, y1=0, x2=1, y2=1):
    return (f'<linearGradient id="{gid}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{G0}"/><stop offset="0.5" stop-color="{G1}"/><stop offset="1" stop-color="{G2}"/></linearGradient>')

def _g(o, s, inner): return f'<g transform="translate({o[0]:.2f},{o[1]:.2f}) scale({s})">{inner}</g>'

def mark_paths(body_fill, slice_fill, ox=0, oy=0, scale=1.0):
    """Compact symbol {D}+cursor. body = ink (strokes), slice = fill colour of the cursor / light parts."""
    ink = body_fill; fill = slice_fill if slice_fill else WHITE
    gray = GRAYC if (ink in (INK, '#000', '#24242B') or ink.startswith('url')) else ink
    return _g((ox, oy), scale, icon_mark(ink, fill, gray))

# Colourways: (ink, fill, gray, word, sub)
SCHEMES = {
    'color':      (INK, WHITE, GRAYC, VIOLET, INK),          # original: black mark, blue name — on white
    'color-dark': (WHITE, INK, '#6B7177', LIME, WHITE),      # on Code Black
    'on-violet':  (WHITE, VIOLET, '#9CC4EA', WHITE, WHITE),  # on DTO Blue / gradient
    'on-lime':    (INK, WHITE, INK, INK, INK),               # alias kept for template compatibility (on light blue)
    'black':      (INK, WHITE, INK, INK, INK),
    'white':      (WHITE, 'none', WHITE, WHITE, WHITE),
}

def svg_wrap(w, h, inner, bg=None, pad=0, title='DevelopTheOne'):
    W_, H_ = w + 2*pad, h + 2*pad
    bgr = f'<rect width="{W_}" height="{H_}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W_:.2f} {H_:.2f}" width="{W_:.2f}" height="{H_:.2f}"><title>{title}</title><defs>{grad_def("bg")}</defs>{bgr}'
            f'<g transform="translate({pad},{pad})">{inner}</g></svg>')

def wordmark_paths(fill, size, x, baseline, text='DevelopTheOne'):
    d, w = text_path(text, WORD_FONT, size, x, baseline, tracking=-0.01)
    return f'<path d="{d}" fill="{fill}"/>', w
def sub_paths(text, fill, size, x, baseline, anchor='start', tracking=0.42):
    d, w = text_path(text, SUB_FONT, size, x, baseline, tracking=tracking, anchor=anchor)
    return f'<path d="{d}" fill="{fill}"/>', w

def _full(sch, ox=0, oy=0, s=1.0):
    ink, fill, gray, _, _ = SCHEMES[sch]; return _g((ox, oy), s, full_mark(ink, fill, gray))
def _icon(sch, ox=0, oy=0, s=1.0):
    ink, fill, gray, _, _ = SCHEMES[sch]; return _g((ox, oy), s, icon_mark(ink, fill, gray))

SIZE, BASE, GAP = 170, 276, 26          # wordmark proportions measured on the original logo
def horizontal(sch, tagline=False):
    *_, wc, sc = SCHEMES[sch]
    word, ww = wordmark_paths(wc, SIZE, MW + GAP, BASE)
    return MW + GAP + ww, MH, _full(sch) + word
def horizontal_compact(sch):
    *_, wc, sc = SCHEMES[sch]
    word, ww = wordmark_paths(wc, SIZE, IW + GAP, BASE)
    return IW + GAP + ww, IH, _icon(sch) + word
def stacked(sch):
    *_, wc, sc = SCHEMES[sch]
    _, ww = wordmark_paths(wc, 150, 0, 0); tot = max(ww, MW)
    word, _ = wordmark_paths(wc, 150, (tot - ww)/2, MH + 70 + 105)
    sub, _ = sub_paths('MARKETING AGENCY', sc, 40, tot/2, MH + 70 + 105 + 90, anchor='middle', tracking=0.5)
    return tot, MH + 70 + 105 + 100, _full(sch, (tot - MW)/2, 0) + word + sub
def symbol(sch): return MW, MH, _full(sch)
def icon(sch): return IW, IH, _icon(sch)
def wordmark(sch):
    *_, wc, sc = SCHEMES[sch]
    word, ww = wordmark_paths(wc, SIZE, -0.06*SIZE, 0.70*SIZE)
    sub, _ = sub_paths('MARKETING AGENCY', sc, 44, ww - 0.06*SIZE, 0.70*SIZE + 92, anchor='end', tracking=0.5)
    return ww - 0.1*SIZE, 0.70*SIZE + 104, word + sub
def wordmark_plain(sch):
    *_, wc, sc = SCHEMES[sch]
    word, ww = wordmark_paths(wc, SIZE, -0.06*SIZE, 0.70*SIZE)
    return ww - 0.1*SIZE, 0.70*SIZE + 0.24*SIZE, word

LOCKUPS = {'horizontal': horizontal, 'horizontal-compact': horizontal_compact, 'stacked': stacked, 'symbol': symbol, 'icon': icon,
           'wordmark': wordmark, 'wordmark-plain': wordmark_plain}

def build(lockup, scheme, pad_ratio=0.0, bg=None):
    w, h, inner = LOCKUPS[lockup](scheme)
    pad = pad_ratio * min(w, h) if pad_ratio else 0
    return svg_wrap(w, h, inner, bg=bg, pad=pad), (w, h)
