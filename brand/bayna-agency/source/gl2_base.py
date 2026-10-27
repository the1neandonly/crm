import os, sys, math, json, random
from kit import *
from icons import ICONS, icon_svg
from brand import *
from logo import horizontal, S, R, CX, CY, GAP, SR
OUT = sys.argv[1]; HT = os.path.abspath('html')
F = lambda p: 'file://' + os.path.join(OUT, p)
PV = json.load(open('previews_print.json'))
def hex2rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [c/255 for c in hex2rgb(h)]; k = 1 - max(r, g, b)
    return (0, 0, 0, 100) if k == 1 else tuple(round(100*x) for x in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))
def lum(h):
    def ch(c): c /= 255; return c/12.92 if c <= .03928 else ((c+.055)/1.055)**2.4
    r, g, b = [ch(c) for c in hex2rgb(h)]; return .2126*r + .7152*g + .0722*b
def contrast(a, b): la, lb = sorted((lum(a), lum(b)), reverse=True); return (la+.05)/(lb+.05)
def grade(c): return 'AAA' if c >= 7 else 'AA' if c >= 4.5 else 'AA large' if c >= 3 else 'Fail'

PAGES = []   # (section, cls, body, chrome)
def add(section, body, cls='light', chrome=True): PAGES.append((section, cls, body, chrome))
def head(num, en, fr): return f'<div class="eyebrow">{num} — {fr}</div><h2>{en}</h2>'
def img(path, style=''): return f'<img src="{F(path)}" style="display:block;{style}">'
CSS = '''
.page{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;padding:150px 120px 120px}
.light{background:var(--paper)}.white{background:#fff}.dark{background:var(--ink);color:#fff}.gradp{background:var(--grad);color:#fff}.limep{background:var(--lime)}
.chrome{position:absolute;left:120px;right:120px;top:56px;display:flex;justify-content:space-between;font-size:15px;font-weight:600;letter-spacing:.08em;text-transform:uppercase}
.folio{position:absolute;left:120px;right:120px;bottom:52px;display:flex;justify-content:space-between;font-size:15px;font-weight:600;letter-spacing:.08em}
.eyebrow{font-size:17px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--violet);margin-bottom:22px}
.dark .eyebrow,.gradp .eyebrow{color:var(--lime)}
h2{font-family:Syne;font-weight:700;font-size:84px;letter-spacing:-.03em;line-height:1}
h3{font-family:Syne;font-weight:700;font-size:30px;letter-spacing:-.01em;margin-bottom:10px}
p{font-size:21px;line-height:1.6;color:#4a4a55}.dark p,.gradp p{color:rgba(255,255,255,.74)}
.lbl{font-size:14px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}
.muted{color:#8a8a96}.dark .muted{color:rgba(255,255,255,.5)}
.card{background:#fff;border-radius:28px;position:relative;overflow:hidden}.dark .card{background:#2E2E37}
.row{display:flex;gap:28px}.col{display:flex;flex-direction:column;gap:28px}
.cap{position:absolute;left:28px;bottom:22px;font-size:14px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}
.mono{font-family:'JetBrains Mono',monospace}.ar{font-family:'Readex Pro';direction:rtl}
.x{position:absolute;right:20px;top:20px;width:40px;height:40px;border-radius:50%;background:#FF4F5E;color:#fff;font:800 26px/40px Manrope;text-align:center}
.ok{display:inline-block;width:34px;height:34px;border-radius:50%;background:var(--lime);color:var(--ink);font:800 20px/34px Manrope;text-align:center}
.no{display:inline-block;width:34px;height:34px;border-radius:50%;background:#FF4F5E;color:#fff;font:800 22px/34px Manrope;text-align:center}
.hl{color:var(--lime)}.vi{color:var(--violet)}
.spec td{padding:9px 0;font-size:18px;border-top:1px solid rgba(255,255,255,.14)}
.light .spec td{border-top:1px solid var(--line)}
.spec td:first-child{width:120px;font-weight:700;letter-spacing:.14em;font-size:13px;text-transform:uppercase;opacity:.6}
.shot{border-radius:20px;box-shadow:0 30px 60px -20px rgba(18,14,40,.35)}
.big{font-family:Syne;font-weight:700;letter-spacing:-.03em;line-height:1}
.num{font-family:'JetBrains Mono';font-size:17px;color:var(--violet)}.dark .num{color:var(--lime)}
'''
def render(path_html):
    total = len(PAGES); out = []
    for i, (sec, cls, body, ch) in enumerate(PAGES):
        dark = cls in ('dark', 'gradp'); c = 'rgba(255,255,255,.5)' if dark else 'rgba(36,36,43,.5)'
        chrome = (f'<div class="chrome" style="color:{c}"><span>Bayna Agency — Brand Guidelines</span><span>{sec}</span></div>'
                  f'<div class="folio" style="color:{c}"><span>{i+1:02d} / {total}</span><span>Charte graphique · v2.0 · باينة</span></div>') if ch else ''
        out.append(f'<section class="page {cls}">{chrome}{body}</section>')
    open(path_html, 'w').write(page_doc(''.join(out), CSS, '1920px 1080px')); return total
