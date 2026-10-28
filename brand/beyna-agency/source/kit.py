import itertools, os, json
from logo import *
FONTS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fonts'))
_ids = itertools.count()
GRAD_CSS = f'linear-gradient(135deg, {G0} 0%, {G1} 55%, {G2} 100%)'

def font_css():
    faces = [('Syne', 500), ('Syne', 600), ('Syne', 700), ('Syne', 800), ('Manrope', 300), ('Manrope', 400), ('Manrope', 500),
             ('Manrope', 600), ('Manrope', 700), ('Manrope', 800), ('ReadexPro', 500), ('ReadexPro', 700), ('JetBrainsMono', 500)]
    fam = {'ReadexPro': 'Readex Pro', 'JetBrainsMono': 'JetBrains Mono'}
    return ''.join(f"@font-face{{font-family:'{fam.get(f, f)}';font-weight:{w};src:url('file://{FONTS}/{f}-{w}.ttf')}}" for f, w in faces)

BASE_CSS = f''':root{{--violet:{VIOLET};--lime:{LIME};--ink:{INK};--g0:{G0};--g2:{G2};--grad:{GRAD_CSS};--paper:#F5F4F9;--line:rgba(36,36,43,.12)}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Manrope',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}}
.syne{{font-family:'Syne',sans-serif}} .mono{{font-family:'JetBrains Mono',monospace}}
svg{{display:block}}'''

def logo_svg(lockup, scheme, height=None, width=None, style=''):
    w, h, inner = LOCKUPS[lockup](scheme)
    gid = f'lg{next(_ids)}'
    inner = inner.replace('url(#bg)', f'url(#{gid})')
    size = f'height="{height}"' if height else f'width="{width}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" {size} style="{style}" aria-label="Beyna Agency">'
            f'<defs>{grad_def(gid)}</defs>{inner}</svg>')

def mark_svg(body='grad', slice_c=LIME, height=None, width=None, style='', extra=''):
    gid = f'mg{next(_ids)}'
    b = f'url(#{gid})' if body == 'grad' else body
    size = f'height="{height}"' if height else f'width="{width}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" {size} style="{style}" overflow="visible">'
            f'<defs>{grad_def(gid)}</defs>{mark_paths(b, slice_c)}{extra}</svg>')

def page_doc(body, css, size_css):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{font_css()}{BASE_CSS}'
            f'@page{{size:{size_css};margin:0}}{css}</style></head><body>{body}</body></html>')
