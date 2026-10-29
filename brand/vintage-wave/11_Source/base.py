"""Shared building blocks: CSS, fonts, garment illustrations, helpers."""
import os
from logo import *
HERE = os.path.dirname(os.path.abspath(__file__)); FONTS = os.path.join(HERE, '..', 'fonts', 'ttf')
def font_css():
    f = 'file://' + os.path.abspath(FONTS)
    return (''.join(f"@font-face{{font-family:Fraunces;src:url({f}/Fraunces-{w}.ttf);font-weight:{w}}}" for w in (400, 600, 700, 900))
            + f"@font-face{{font-family:Fraunces;src:url({f}/Fraunces-600-Italic.ttf);font-weight:600;font-style:italic}}"
            + ''.join(f"@font-face{{font-family:'DM Sans';src:url({f}/DMSans-{w}.ttf);font-weight:{w}}}" for w in (400, 500, 700))
            + ''.join(f"@font-face{{font-family:Caveat;src:url({f}/Caveat-{w}.ttf);font-weight:{w}}}" for w in (500, 700)))
GRAIN = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter><rect width='240' height='240' filter='url(%23n)'/></svg>\")")
CSS = font_css() + f'''
:root{{--es:{ESPRESSO};--cr:{CREAM};--ru:{RUST};--am:{AMBER};--ma:{MAPLE};--de:{DENIM};--sa:{SAGE};--kr:{KRAFT};--ink:{INK}}}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{background:var(--cr)}}
body{{font-family:'DM Sans',sans-serif;color:var(--es);-webkit-font-smoothing:antialiased}}
.fr{{font-family:Fraunces,serif}} .hand{{font-family:Caveat,cursive}} .up{{text-transform:uppercase;letter-spacing:.18em}}
.grain{{position:absolute;inset:0;background-image:{GRAIN};opacity:.18;mix-blend-mode:multiply;pointer-events:none}}
.grain.l{{mix-blend-mode:screen;opacity:.10}}
'''
# Garment illustrations (flat, 100 x 100) — used as product-photo stand-ins and category icons
G = {
 'tee': 'M30 18 L42 12 Q50 18 58 12 L70 18 L88 32 L78 46 L70 40 L70 88 L30 88 L30 40 L22 46 L12 32 Z',
 'jacket': 'M34 12 L46 10 L50 22 L54 10 L66 12 L86 26 L90 80 L76 82 L74 46 L72 90 L28 90 L26 46 L24 82 L10 80 L14 26 Z',
 'jeans': 'M28 10 L72 10 L76 90 L58 90 L51 38 L49 38 L42 90 L24 90 Z',
 'dress': 'M38 10 L44 10 Q50 18 56 10 L62 10 L64 34 L82 90 L18 90 L36 34 Z',
 'sweater': 'M32 16 Q50 26 68 16 L88 30 L92 78 L80 80 L74 44 L74 88 L26 88 L26 44 L20 80 L8 78 L12 30 Z',
 'bag': 'M18 40 L82 40 L76 88 L24 88 Z M36 40 Q36 16 50 16 Q64 16 64 40 L58 40 Q58 22 50 22 Q42 22 42 40 Z',
 'shoe': 'M10 58 L12 34 L30 36 Q40 48 58 50 L84 56 Q92 60 90 70 L90 74 L10 74 Z',
 'hat': 'M26 56 Q26 26 50 26 Q74 26 74 56 Z M8 60 Q50 50 92 60 Q92 68 82 68 L18 68 Q8 68 8 60 Z',
}
def garment(kind, fill, size=100, stroke=None):
    st = f' stroke="{stroke}" stroke-width="3" stroke-linejoin="round"' if stroke else ''
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" style="display:block"><path d="{G[kind]}" fill="{fill}" fill-rule="evenodd"{st}/></svg>'
def photo(kind, w, h, bg=KRAFT, fg=DENIM, label='', radius=0, grain=True):
    """Product-photo stand-in: garment on a backdrop, soft shadow and paper grain."""
    s = min(w, h)*0.66
    return (f'<div style="width:{w}px;height:{h}px;position:relative;overflow:hidden;border-radius:{radius}px;background:radial-gradient(ellipse at 40% 30%,rgba(255,255,255,.22),rgba(0,0,0,0) 60%),{bg}">'
            f'<div style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);filter:drop-shadow(0 {s*0.05:.0f}px {s*0.06:.0f}px rgba(0,0,0,.28))">{garment(kind, fg, s)}</div>'
            + ('<div class="grain"></div>' if grain else '')
            + (f'<div style="position:absolute;left:14px;bottom:10px;font:500 12px DM Sans;letter-spacing:.14em;color:rgba(28,15,11,.55);text-transform:uppercase">{label}</div>' if label else '') + '</div>')
def logo(lk='stacked', sc='espresso', width=None, height=None, style=''):
    w, h, inner = LOCKUPS[lk](sc)
    size = f'width="{width}"' if width else f'height="{height}"'
    return f'<svg viewBox="0 0 {w:.2f} {h:.2f}" {size} style="display:block;overflow:visible;{style}">{inner}</svg>'
COND = [('Mint', 'Never or barely worn. No signs of wear.', SAGE), ('Excellent', 'Gently worn. No flaws worth mentioning.', DENIM), ('Very good', 'Light, honest wear — fading or softening.', AMBER),
        ('Good', 'Visible wear or a small flaw, photographed.', RUST), ('Fair', 'Loved hard. Flaws shown, priced to match.', MAPLE)]
def cond_badge(name, size=16, solid=False):
    c = dict((n, col) for n, _, col in COND)[name]
    dots = ''.join(f'<i style="width:{size*0.42:.0f}px;height:{size*0.42:.0f}px;border-radius:50%;display:block;background:{c if k < 5 - [n for n, _, _ in COND].index(name) else "transparent"};border:1.5px solid {c}"></i>' for k in range(5))
    return (f'<span style="display:inline-flex;align-items:center;gap:{size*0.55:.0f}px;padding:{size*0.38:.0f}px {size*0.8:.0f}px;border-radius:999px;border:1.5px solid {c};'
            f'font:700 {size}px DM Sans;letter-spacing:.06em;color:{c};background:{"rgba(255,255,255,.5)" if not solid else c}"><span style="display:flex;gap:3px">{dots}</span>{name.upper()}</span>')
def badge(text, bg, fg, size=16, rot=0):
    return f'<span style="display:inline-block;padding:{size*0.4:.0f}px {size*0.85:.0f}px;background:{bg};color:{fg};font:700 {size}px DM Sans;letter-spacing:.14em;transform:rotate({rot}deg)">{text}</span>'
def doc(body, css='', size='1920px 1080px'):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}@page{{size:{size};margin:0}}{css}</style></head><body>{body}</body></html>'
