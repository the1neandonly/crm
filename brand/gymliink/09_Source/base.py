"""Shared building blocks for the Gymliink brand book and applications."""
import os, re, segno
from logo import *
HERE = os.path.dirname(os.path.abspath(__file__)); FONTS = os.path.join(HERE, '..', 'fonts', 'ttf'); PH = os.path.join(HERE, '..', 'ph', 'package', 'assets', 'light')
OK, WARN, BAD, INFO = '#4CD98F', '#F6B94F', '#FF6B5E', '#7AA7FF'
def font_css():
    f = 'file://' + os.path.abspath(FONTS)
    out = ''.join(f"@font-face{{font-family:Geist;src:url({f}/Geist-{n}.ttf);font-weight:{w}}}" for n, w in [('Light', 300), ('Regular', 400), ('Medium', 500), ('SemiBold', 600), ('Bold', 700)])
    out += ''.join(f"@font-face{{font-family:'Geist Mono';src:url({f}/GeistMono-{n}.ttf);font-weight:{w}}}" for n, w in [('Regular', 400), ('Medium', 500), ('SemiBold', 600)])
    out += ''.join(f"@font-face{{font-family:'Plex Arabic';src:url({f}/IBMPlexSansArabic-{w}.ttf);font-weight:{w}}}" for w in (300, 400, 500, 600, 700))
    return out
CSS = font_css() + f'''
:root{{--volt:{VOLT};--vink:{INK_ON_VOLT};--vdeep:{VOLT_DEEP};--bg:{BG};--s1:{S1};--s2:{S2};--s3:{S3};--line:{LINE};--tx:{TXT};--tx2:{TXT2};--lbg:{LBG};--ok:{OK};--warn:{WARN};--bad:{BAD};--info:{INFO}}}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{background:var(--bg)}}
body{{font-family:Geist,'Plex Arabic',sans-serif;color:var(--tx);-webkit-font-smoothing:antialiased;font-feature-settings:"ss01"}}
.mono{{font-family:'Geist Mono',monospace;font-feature-settings:"tnum","zero"}} .ar{{font-family:'Plex Arabic',Geist,sans-serif;direction:rtl;text-align:right}}
.v{{color:var(--volt)}} .t2{{color:var(--tx2)}}
'''
_icons = {}
def ic(name, size=24, color='currentColor', style=''):
    if name not in _icons:
        s = open(os.path.join(PH, f'{name}-light.svg')).read()
        _icons[name] = re.sub(r'^<svg[^>]*>|</svg>$', '', s.strip())
    return f'<svg viewBox="0 0 256 256" width="{size}" height="{size}" fill="{color}" style="display:block;{style}">{_icons[name]}</svg>'
def qr_svg(data, size, fg=BG, bg='#FFFFFF', quiet=2, radius=True):
    """QR code with rounded finder patterns and softly rounded modules."""
    q = segno.make(data, error='m'); m = [list(r) for r in q.matrix]; n = len(m); N = n + 2*quiet; u = size / N
    fin = [(0, 0), (0, n - 7), (n - 7, 0)]
    def in_f(r, c): return any(fr <= r < fr + 7 and fc <= c < fc + 7 for fr, fc in fin)
    out = [f'<rect width="{size}" height="{size}" rx="{u*1.6 if radius else 0:.2f}" fill="{bg}"/>']
    rr = u*0.32 if radius else 0
    for r in range(n):
        for c in range(n):
            if m[r][c] and not in_f(r, c):
                out.append(f'<rect x="{(c+quiet)*u + u*0.06:.2f}" y="{(r+quiet)*u + u*0.06:.2f}" width="{u*0.88:.2f}" height="{u*0.88:.2f}" rx="{rr:.2f}" fill="{fg}"/>')
    for fr, fc in fin:
        x, y = (fc + quiet)*u, (fr + quiet)*u
        out.append(f'<path fill-rule="evenodd" fill="{fg}" d="{rrect(x, y, 7*u, 7*u, 2.2*u)} {rrect(x + u, y + u, 5*u, 5*u, 1.4*u, rev=True)}"/>')
        out.append(f'<rect x="{x + 2*u:.2f}" y="{y + 2*u:.2f}" width="{3*u:.2f}" height="{3*u:.2f}" rx="{0.9*u:.2f}" fill="{fg}"/>')
    return f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" style="display:block">{"".join(out)}</svg>'
def logo(lk='horizontal', sc='color-dark', width=None, height=None, style=''):
    w, h, inner = LOCKUPS[lk](sc)
    size = f'width="{width}"' if width else f'height="{height}"'
    return f'<svg viewBox="0 0 {w:.2f} {h:.2f}" {size} style="display:block;overflow:visible;{style}">{inner}</svg>'
def hex2rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [c/255 for c in hex2rgb(h)]; k = 1 - max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    return tuple(round(100*v) for v in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))
def lum(h):
    def ch(c):
        c /= 255; return c/12.92 if c <= 0.03928 else ((c + 0.055)/1.055)**2.4
    r, g, b = hex2rgb(h); return 0.2126*ch(r) + 0.7152*ch(g) + 0.0722*ch(b)
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la + 0.05)/(lb + 0.05)
def pill(label, kind, ar=False, size=15):
    col = {'active': OK, 'expiring': WARN, 'expired': BAD, 'paused': TXT2, 'info': INFO}[kind]
    return (f'<span style="display:inline-flex;align-items:center;gap:8px;padding:6px 12px 6px 10px;border-radius:999px;background:{col}1F;color:{col};'
            f'font:500 {size}px {"'Plex Arabic',Geist" if ar else "Geist"};{"direction:rtl" if ar else ""}"><i style="width:7px;height:7px;border-radius:50%;background:{col};display:block"></i>{label}</span>')
def doc(body, css='', size='1920px 1080px'):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}@page{{size:{size};margin:0}}{css}</style></head><body>{body}</body></html>'
