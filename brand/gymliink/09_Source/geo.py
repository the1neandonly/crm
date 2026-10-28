"""Shared geometry helpers for Gymliink marks."""
from textpath import text_path
VOLT, INK_ON_VOLT = '#C5F04A', '#12160A'
BG, S1, S2, S3, LINE, TXT, TXT2 = '#0A0A0B', '#141416', '#1D1D20', '#2A2A2F', '#26262B', '#F5F5F6', '#9A9AA3'
LBG = '#F4F4F2'
def rrect(x, y, w, h, r, rev=False):
    r = min(r, w/2, h/2)
    if not rev:
        return (f'M{x+r:.2f},{y:.2f} H{x+w-r:.2f} A{r:.2f},{r:.2f} 0 0,1 {x+w:.2f},{y+r:.2f} V{y+h-r:.2f} A{r:.2f},{r:.2f} 0 0,1 {x+w-r:.2f},{y+h:.2f} '
                f'H{x+r:.2f} A{r:.2f},{r:.2f} 0 0,1 {x:.2f},{y+h-r:.2f} V{y+r:.2f} A{r:.2f},{r:.2f} 0 0,1 {x+r:.2f},{y:.2f} Z')
    return (f'M{x+r:.2f},{y:.2f} A{r:.2f},{r:.2f} 0 0,0 {x:.2f},{y+r:.2f} V{y+h-r:.2f} A{r:.2f},{r:.2f} 0 0,0 {x+r:.2f},{y+h:.2f} H{x+w-r:.2f} '
            f'A{r:.2f},{r:.2f} 0 0,0 {x+w:.2f},{y+h-r:.2f} V{y+r:.2f} A{r:.2f},{r:.2f} 0 0,0 {x+w-r:.2f},{y:.2f} Z')
def ring(x, y, w, h, t, grow=0):
    """Annulus of a capsule/rounded rect: outer grown by `grow`, inner shrunk by `grow`."""
    r = min(w, h)/2
    return rrect(x - grow, y - grow, w + 2*grow, h + 2*grow, r + grow) + ' ' + rrect(x + t + grow, y + t + grow, w - 2*t - 2*grow, h - 2*t - 2*grow, r - t - grow, rev=True)
def circ(cx, cy, r, rev=False):
    s = 0 if rev else 1
    return f'M{cx-r:.2f},{cy:.2f} a{r:.2f},{r:.2f} 0 1,{s} {2*r:.2f},0 a{r:.2f},{r:.2f} 0 1,{s} {-2*r:.2f},0 Z'
_n = [0]
def uid(p='k'):
    _n[0] += 1; return f'{p}{_n[0]}'
def weave(A, B, haloA, haloB, ym, fill, box=(-50, -50, 300, 300), fillB=None):
    """Two interlocked rings: A passes over B above y=ym, B over A below. Gaps are masks, so there are no seams."""
    fillB = fillB or fill
    x0, y0, x1, y1 = box
    mA, mB, ct, cb = uid('ma'), uid('mb'), uid('ct'), uid('cb')
    defs = (f'<clipPath id="{ct}"><rect x="{x0}" y="{y0}" width="{x1-x0}" height="{ym-y0}"/></clipPath>'
            f'<clipPath id="{cb}"><rect x="{x0}" y="{ym}" width="{x1-x0}" height="{y1-ym}"/></clipPath>'
            f'<mask id="{mB}" maskUnits="userSpaceOnUse" x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}"><rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="#fff"/>'
            f'<path fill-rule="evenodd" fill="#000" clip-path="url(#{ct})" d="{haloA}"/></mask>'
            f'<mask id="{mA}" maskUnits="userSpaceOnUse" x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}"><rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="#fff"/>'
            f'<path fill-rule="evenodd" fill="#000" clip-path="url(#{cb})" d="{haloB}"/></mask>')
    return (f'<defs>{defs}</defs><path fill-rule="evenodd" fill="{fill}" mask="url(#{mA})" d="{A}"/>'
            f'<path fill-rule="evenodd" fill="{fillB}" mask="url(#{mB})" d="{B}"/>')
