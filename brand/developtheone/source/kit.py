import itertools, os, json
from logo import *
FONTS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fonts'))
_ids = itertools.count()
GRAD_CSS = f'linear-gradient(135deg, {G0} 0%, {G1} 55%, {G2} 100%)'

def font_css():
    faces = [('Montserrat', 400), ('Montserrat', 500), ('Montserrat', 600), ('Montserrat', 700), ('Montserrat', 800), ('Montserrat', 900), ('Inter', 300), ('Inter', 400), ('Inter', 500),
             ('Inter', 600), ('Inter', 700), ('Inter', 800), ('Cairo', 400), ('Cairo', 600), ('Cairo', 700), ('JetBrainsMono', 400), ('JetBrainsMono', 500), ('JetBrainsMono', 700)]
    fam = {'JetBrainsMono': 'JetBrains Mono'}
    return ''.join(f"@font-face{{font-family:'{fam.get(f, f)}';font-weight:{w};src:url('file://{FONTS}/{f}-{w}.ttf')}}" for f, w in faces)

BASE_CSS = f''':root{{--violet:{VIOLET};--lime:{LIME};--ink:{INK};--g0:{G0};--g2:{G2};--grad:{GRAD_CSS};--paper:#F2F6FB;--line:rgba(36,36,43,.12)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Inter',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}}
.syne{{font-family:'Montserrat',sans-serif}} .mono{{font-family:'JetBrains Mono',monospace}}
svg{{display:block}}'''

def logo_svg(lockup, scheme, height=None, width=None, style=''):
    w, h, inner = LOCKUPS[lockup](scheme)
    gid = f'lg{next(_ids)}'
    inner = inner.replace('url(#bg)', f'url(#{gid})')
    size = f'height="{height}"' if height else f'width="{width}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" {size} style="{style}" aria-label="DevelopTheOne">'
            f'<defs>{grad_def(gid)}</defs>{inner}</svg>')

def mark_svg(body='grad', slice_c=None, height=None, width=None, style='', extra=''):
    """DTO compact symbol ({D} + clicking cursor). 'grad' = blue-gradient strokes with a white cursor."""
    gid = f'mg{next(_ids)}'
    if body == 'grad': ink, fill = f'url(#{gid})', (slice_c or '#FFFFFF')
    else: ink, fill = body, (slice_c or LIME)
    if height is not None:   # the {D} icon is wider than tall: scale heights so templates keep the same footprint
        import re as _re
        height = (f'{float(_re.match(r"[\d.]+", height).group()) * 0.62:.2f}' + _re.sub(r'^[\d.]+', '', height)) if isinstance(height, str) else height * 0.62
    size = f'height="{height}"' if height else f'width="{width}"'
    gd = (f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="{H}">'
          f'<stop offset="0" stop-color="{G0}"/><stop offset=".5" stop-color="{G1}"/><stop offset="1" stop-color="{G2}"/></linearGradient>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" {size} style="{style}" overflow="visible">'
            f'<defs>{gd}</defs>{mark_paths(ink, fill)}{extra}</svg>')

def full_mark_svg(scheme='color', height=None, width=None, style=''):
    w, h, inner = LOCKUPS['symbol'](scheme); size = f'height="{height}"' if height else f'width="{width}"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {size} style="{style}">{inner}</svg>'

def page_doc(body, css, size_css):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{font_css()}{BASE_CSS}'
            f'@page{{size:{size_css};margin:0}}{css}</style></head><body>{body}</body></html>')
