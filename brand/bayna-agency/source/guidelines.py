import sys, os, math
from kit import *
OUT = sys.argv[1]; HT = os.path.abspath('html')
A = lambda p: 'file://' + os.path.join(OUT, p)

def hex2rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [c/255 for c in hex2rgb(h)]; k = 1 - max(r, g, b)
    if k == 1: return (0, 0, 0, 100)
    return tuple(round(100*x) for x in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))
def lum(h):
    def ch(c): c /= 255; return c/12.92 if c <= .03928 else ((c+.055)/1.055)**2.4
    r, g, b = [ch(c) for c in hex2rgb(h)]; return .2126*r + .7152*g + .0722*b
def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True); return (la+.05)/(lb+.05)
def grade(c): return 'AAA' if c >= 7 else 'AA' if c >= 4.5 else 'AA large' if c >= 3 else 'Fail'

TOTAL = 17
def chrome(n, section, dark):
    c = 'rgba(255,255,255,.5)' if dark else 'rgba(36,36,43,.5)'
    return (f'<div class="chrome" style="color:{c}"><span>Bayna Agency — Brand Guidelines</span><span>{section}</span></div>'
            f'<div class="folio" style="color:{c}"><span>{n:02d} / {TOTAL}</span><span>Charte graphique · v1.0</span></div>')
def page(n, section, body, cls='light', chrome_on=True):
    dark = cls in ('dark', 'gradp')
    return f'<section class="page {cls}">{chrome(n, section, dark) if chrome_on else ""}{body}</section>'
def head(num, en, fr, dark=False):
    return (f'<div class="eyebrow">{num} — {fr}</div><h2>{en}</h2>')

css = '''
.page{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;padding:150px 120px 120px}
.light{background:var(--paper)}.white{background:#fff}.dark{background:var(--ink);color:#fff}.gradp{background:var(--grad);color:#fff}
.chrome{position:absolute;left:120px;right:120px;top:56px;display:flex;justify-content:space-between;font-size:15px;font-weight:600;letter-spacing:.08em;text-transform:uppercase}
.folio{position:absolute;left:120px;right:120px;bottom:52px;display:flex;justify-content:space-between;font-size:15px;font-weight:600;letter-spacing:.08em}
.eyebrow{font-size:17px;font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:var(--violet);margin-bottom:22px}
.dark .eyebrow,.gradp .eyebrow{color:var(--lime)}
h2{font-family:Syne;font-weight:700;font-size:84px;letter-spacing:-.03em;line-height:1}
h3{font-family:Syne;font-weight:700;font-size:30px;letter-spacing:-.01em;margin-bottom:10px}
p{font-size:21px;line-height:1.6;color:#4a4a55}.dark p,.gradp p{color:rgba(255,255,255,.72)}
.lbl{font-size:14px;font-weight:700;letter-spacing:.2em;text-transform:uppercase}
.muted{color:#8a8a96}.dark .muted{color:rgba(255,255,255,.5)}
.card{background:#fff;border-radius:28px;position:relative;overflow:hidden}
.row{display:flex;gap:28px}.col{display:flex;flex-direction:column;gap:28px}
.cap{position:absolute;left:28px;bottom:22px;font-size:14px;font-weight:700;letter-spacing:.16em;text-transform:uppercase}
.mono{font-family:'JetBrains Mono',monospace}
.x{position:absolute;right:20px;top:20px;width:40px;height:40px;border-radius:50%;background:#FF4F5E;color:#fff;font:800 26px/40px Manrope;text-align:center}
.ok{position:absolute;right:20px;top:20px;width:40px;height:40px;border-radius:50%;background:var(--lime);color:var(--ink);font:800 22px/40px Manrope;text-align:center}
.hl{color:var(--lime)}
.spec td{padding:9px 0;font-size:18px;border-top:1px solid rgba(255,255,255,.14)}
.spec td:first-child{width:120px;font-weight:700;letter-spacing:.14em;font-size:13px;text-transform:uppercase;opacity:.6}
'''
P = []

# 1 — Cover
P.append(page(1, '', f'''
{mark_svg(height=1500, style="position:absolute;right:-260px;top:-150px")}
<div style="position:absolute;left:120px;top:110px">{logo_svg("horizontal","color-dark",width=420)}</div>
<div style="position:absolute;left:120px;bottom:130px">
  <div class="syne" style="font-weight:700;font-size:168px;letter-spacing:-.04em;line-height:.9">Brand<br>Guidelines</div>
  <div class="syne hl" style="font-weight:600;font-size:44px;margin-top:30px;letter-spacing:-.01em">Charte graphique</div>
  <div style="margin-top:46px;font-size:18px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.55)">Version 1.0 &nbsp;·&nbsp; Octobre 2026 &nbsp;·&nbsp; Oran, Algérie</div>
</div>''', 'dark', chrome_on=False))

# 2 — Contents
toc = [('Brand essence', "L'essence de la marque", 3), ('The symbol', 'Le symbole', 4), ('Construction', 'Construction', 5),
       ('Logo suite', 'Déclinaisons', 6), ('Clear space & sizes', 'Zone de protection', 7), ('Colour versions', 'Versions couleur', 8),
       ('Misuse', 'Usages interdits', 9), ('Colour palette', 'Palette', 10), ('Gradient', 'Dégradé', 11),
       ('Typography', 'Typographie', 12), ('Graphic elements', 'Éléments graphiques', 13), ('Data & charts', 'Graphiques', 14),
       ('Applications', 'Applications', 15)]
items = ''.join(f'<div style="display:flex;align-items:baseline;gap:26px;padding:17px 0;border-top:1px solid var(--line)">'
                f'<span class="mono" style="color:var(--violet);font-size:17px;width:40px">{i+1:02d}</span>'
                f'<span class="syne" style="font-size:31px;font-weight:700;letter-spacing:-.01em;flex:1">{en}</span>'
                f'<span class="muted" style="font-size:18px;width:260px">{fr}</span><span class="mono muted" style="font-size:17px">p.{pg:02d}</span></div>'
                for i, (en, fr, pg) in enumerate(toc))
half = 7
P.append(page(2, 'Contents', f'''{head("00", "Contents", "Sommaire")}
<div class="row" style="gap:90px;margin-top:70px">
<div style="flex:1">{items.split('</div><div style="display:flex')[0]}</div></div>''', 'light'))
# (rebuild contents in two clean columns)
rows = [r for r in items.split('<div style="display:flex') if r]
rows = ['<div style="display:flex' + r for r in rows]
P[-1] = page(2, 'Contents', f'''{head("00", "Contents", "Sommaire")}
<div class="row" style="gap:90px;margin-top:70px"><div style="flex:1">{"".join(rows[:half])}</div><div style="flex:1">{"".join(rows[half:])}</div></div>''', 'light')

# 3 — Brand essence
values = [('Clarity', 'Clarté', 'We make complex things simple and visible.'),
          ('Proof', 'Preuve', 'Every idea is measured. Results speak.'),
          ('Boldness', 'Audace', 'Bright ideas, confident execution.'),
          ('Craft', 'Exigence', 'High-end detail in everything we ship.')]
vals = ''.join(f'<div style="flex:1;border-top:2px solid var(--lime);padding-top:22px"><h3 style="font-size:28px">{en}</h3>'
               f'<div class="lbl muted" style="margin-bottom:12px">{fr}</div><p style="font-size:18px">{d}</p></div>' for en, fr, d in values)
P.append(page(3, '01 Brand essence', f'''{head("01", "Brand essence", "L'essence de la marque")}
<div class="row" style="margin-top:64px;gap:110px">
 <div style="width:640px">
  <div style="font-family:'Readex Pro';font-weight:700;font-size:250px;line-height:1.05;background:var(--grad);-webkit-background-clip:text;color:transparent;direction:rtl;text-align:left;filter:brightness(1.25)">بيّنة</div>
  <div class="syne" style="font-size:34px;font-weight:600;margin-top:10px">bayyina <span class="muted" style="font-family:Manrope;font-weight:500;font-size:22px">— arabic, noun</span></div>
  <p style="margin-top:16px">Clear proof; evidence that makes the truth plain to see. Also an echo of <span style="font-family:'Readex Pro'">بين</span> <i>(bayn — between)</i>: the agency stands between a brand and its audience.</p>
 </div>
 <div style="flex:1">
  <div class="syne" style="font-size:58px;font-weight:700;letter-spacing:-.025em;line-height:1.08">Bayna turns brands into <span class="hl">evidence</span>: strategy you can read, creative you can feel, results you can measure.</div>
  <div class="row" style="margin-top:52px;align-items:center;gap:22px"><span class="lbl hl">Tagline</span><span class="syne" style="font-size:30px;font-weight:700">Proof, by design.</span><span class="muted" style="font-size:22px">/ La preuve, par le design.</span></div>
 </div>
</div>
<div class="row" style="position:absolute;left:120px;right:120px;bottom:120px;gap:40px">{vals}</div>''', 'dark'))

# 4 — The symbol
u = 0.9
def piece(kind):
    gid = f'pc{kind}'
    g = grad_def(gid); f = f'url(#{gid})'
    if kind == 'bar': d = f'<path d="M0,0 H{S} V{CY} H0Z" fill="{f}"/>'
    elif kind == 'pie': d = f'<path d="M0,{CY} L{CX},{CY} L{CX},{CY-R} A{R},{R} 0 1,1 0,{CY} Z" fill="{f}"/>'
    elif kind == 'slice':
        sx, sy = CX-GAP, CY-GAP; d = f'<path d="M{sx},{sy} L{sx-SR},{sy} A{SR},{SR} 0 0,1 {sx},{sy-SR} Z" fill="{LIME}"/>'
    else: d = mark_paths(f, LIME)
    ghost = '' if kind == 'all' else f'<g opacity=".09">{mark_paths("#24242B", "#24242B")}</g>'
    return f'<svg viewBox="-10 -10 {W+20} {H+20}" height="300"><defs>{g}</defs>{ghost}{d}</svg>'
parts = [('bar', 'The bar', 'Growth', 'A rising bar — the one result every client wants to see.'),
         ('pie', 'The pie', 'Audience', 'The market, the data, the whole picture we study first.'),
         ('slice', 'The slice', 'Insight', 'The share we win for you — highlighted in lime.'),
         ('all', 'The b', 'Bayna', 'Together they draw a letter built from data.')]
sym = ''
for i, (k, t, kw, d) in enumerate(parts):
    sym += (f'<div style="flex:1;text-align:left"><div class="card" style="height:400px;display:flex;align-items:center;justify-content:center;'
            f'{"background:var(--ink)" if k=="all" else ""}">{piece(k)}</div>'
            f'<div class="row" style="margin-top:26px;align-items:baseline;gap:14px"><h3>{t}</h3><span class="lbl" style="color:var(--violet)">{kw}</span></div><p style="font-size:18px">{d}</p></div>')
    if i < 3: sym += f'<div class="syne" style="font-size:64px;font-weight:600;color:var(--violet);padding-top:160px">{"+" if i<2 else "="}</div>'
P.append(page(4, '02 The symbol', f'''{head("02", "The symbol", "Le symbole")}
<p style="max-width:1100px;margin-top:24px">The Bayna mark is a lowercase <b>b</b> assembled from the three shapes of a marketing report — a bar, a pie chart and its highlighted slice. It says what we do before a single word is read.</p>
<div class="row" style="margin-top:58px;gap:30px;align-items:flex-start">{sym}</div>''', 'light'))

# 5 — Construction
cell = 12; scale = 4.2
gl = ''.join(f'<line x1="{x*cell}" y1="0" x2="{x*cell}" y2="{H}" />' for x in range(0, 13)) + ''.join(f'<line x1="0" y1="{y*cell}" x2="{W}" y2="{y*cell}" />' for y in range(0, 17))
ann_c = 'rgba(210,255,90,.95)'
def dim_h(x1, x2, y, label):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{ann_c}" stroke-width=".5"/><line x1="{x1}" y1="{y-3}" x2="{x1}" y2="{y+3}" stroke="{ann_c}" stroke-width=".5"/>'
            f'<line x1="{x2}" y1="{y-3}" x2="{x2}" y2="{y+3}" stroke="{ann_c}" stroke-width=".5"/><text x="{(x1+x2)/2}" y="{y-4}" fill="{ann_c}" font-size="5.5" text-anchor="middle" font-family="JetBrains Mono">{label}</text>')
def dim_v(y1, y2, x, label):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{ann_c}" stroke-width=".5"/><line x1="{x-3}" y1="{y1}" x2="{x+3}" y2="{y1}" stroke="{ann_c}" stroke-width=".5"/>'
            f'<line x1="{x-3}" y1="{y2}" x2="{x+3}" y2="{y2}" stroke="{ann_c}" stroke-width=".5"/><text x="{x-5}" y="{(y1+y2)/2}" fill="{ann_c}" font-size="5.5" text-anchor="end" dominant-baseline="middle" font-family="JetBrains Mono">{label}</text>')
cons = (f'<svg viewBox="-60 -24 {W+90} {H+40}" height="800"><defs>{grad_def("cg")}</defs>'
        f'<g stroke="rgba(255,255,255,.10)" stroke-width=".4">{gl}</g>'
        f'<g opacity=".92">{mark_paths("url(#cg)", LIME)}</g>'
        f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#fff" stroke-width=".5" stroke-dasharray="2 2"/>'
        f'<circle cx="{CX-GAP}" cy="{CY-GAP}" r="{SR}" fill="none" stroke="#fff" stroke-width=".4" stroke-dasharray="1.5 1.5" opacity=".7"/>'
        f'<circle cx="{CX}" cy="{CY}" r="1.6" fill="#fff"/>'
        f'{dim_h(0, S, -8, "3")}{dim_h(0, W, H+14, "12 — W")}{dim_v(0, H, -16, "16 — H")}{dim_v(CY, H, -40, "6 — R")}'
        f'{dim_h(CX-GAP, CX, CY+8, "⅔")}</svg>')
specs = [('Grid', '12 × 16 modules (3 : 4)'), ('Stem', '3 modules wide'), ('Bowl', 'Radius 6 — half the width'), ('Notch', 'One quadrant removed'),
         ('Slice', 'Offset ⅔ module, radius 2⅓'), ('Wordmark', 'Syne Bold, −1.5 % tracking'), ('Baseline', 'Sits on the bowl')]
P.append(page(5, '03 Construction', f'''
<div style="position:absolute;right:170px;top:150px">{cons}</div>
{head("03", "Construction", "Construction")}
<p style="max-width:640px;margin-top:26px">Every curve and edge sits on a 12 × 16 modular grid. Always reproduce the logo from the master files — never redraw it.</p>
<table class="spec" style="margin-top:46px;width:640px;border-collapse:collapse">{"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in specs)}</table>''', 'dark'))

# 6 — Logo suite
def lc(inner, cap, h, bg='#fff', capc='var(--ink)', extra=''):
    return f'<div class="card" style="flex:1;height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center;{extra}">{inner}<div class="cap" style="color:{capc}">{cap}</div></div>'
P.append(page(6, '04 Logo suite', f'''{head("04", "Logo suite", "Déclinaisons du logo")}
<div class="row" style="margin-top:50px">{lc(logo_svg("horizontal","color",width=900), "Primary · Horizontal", 430)}
<div class="col" style="width:520px">{lc(logo_svg("stacked","color",width=250), "Stacked", 430)}</div></div>
<div class="row" style="margin-top:28px">{lc(mark_svg(height=150), "Symbol", 250)}{lc(logo_svg("horizontal-compact","color",width=440), "Compact", 250)}{lc(logo_svg("wordmark","color",width=420), "Wordmark", 250)}</div>''', 'light'))

# 7 — Clear space & minimum size
hw, hh, _ = horizontal('color'); sc7 = 820/hw; Rp = R*sc7
cs = (f'<div style="position:relative;padding:{Rp}px;border:2px dashed rgba(99,55,255,.5);display:inline-block">'
      f'{logo_svg("horizontal","color",width=820)}' +
      ''.join(f'<div style="position:absolute;{pos};width:{Rp}px;height:{Rp}px;background:rgba(99,55,255,.12);display:flex;align-items:center;justify-content:center;font:700 22px Syne;color:var(--violet)">R</div>'
              for pos in ['left:0;top:0', 'right:0;top:0', 'left:0;bottom:0', 'right:0;bottom:0']) + '</div>')
mins = [('horizontal', 'Horizontal + AGENCY', '320 px', '55 mm', 320), ('horizontal-compact', 'Compact', '120 px', '25 mm', 120),
        ('stacked', 'Stacked', '120 px', '30 mm', 120), ('icon', 'Symbol', '24 px', '6 mm', 24)]
mn = ''.join(f'<div style="display:flex;align-items:center;gap:30px;padding:24px 0;border-top:1px solid var(--line)"><div style="width:340px;height:110px;display:flex;align-items:center">'
             f'{mark_svg(height=wpx*H/W) if k=="icon" else logo_svg(k,"color",width=wpx)}</div><div style="flex:1"><div style="font-weight:700;font-size:20px">{name}</div>'
             f'<div class="mono muted" style="font-size:16px;margin-top:4px">min. {px} · {mm}</div></div></div>' for k, name, px, mm, wpx in mins)
P.append(page(7, '05 Clear space & sizes', f'''{head("05", "Clear space & sizes", "Zone de protection & tailles minimales")}
<div class="row" style="margin-top:56px;gap:90px;align-items:flex-start">
<div><div class="card" style="padding:60px">{cs}</div>
<p style="margin-top:28px;max-width:1000px;font-size:19px">Keep a clear zone equal to <b>R</b> — the radius of the bowl — on every side. No text, image or edge may enter it.</p></div>
<div style="flex:1"><div class="lbl" style="color:var(--violet);margin-bottom:12px">Minimum sizes · digital / print</div>{mn}</div></div>''', 'light'))

# 8 — Colour versions
tiles = [('horizontal', 'color', '#fff', 'Full colour · light', 'var(--ink)'), ('horizontal', 'color-dark', INK, 'Full colour · ink', '#fff'),
         ('horizontal', 'on-violet', VIOLET, 'Reversed · violet', '#fff'), ('horizontal', 'on-violet', 'var(--grad)', 'Reversed · gradient', '#fff'),
         ('horizontal', 'on-lime', LIME, 'On lime', 'var(--ink)'), ('horizontal', 'black', '#fff', 'Mono · black', 'var(--ink)'),
         ('horizontal', 'white', INK, 'Mono · white', '#fff'), ('horizontal', 'white', '#6B6B78', 'Mono · on images', '#fff')]
tl = ''.join(f'<div class="card" style="height:330px;background:{bg};display:flex;align-items:center;justify-content:center">{logo_svg(l,s,width=330)}<div class="cap" style="color:{cc};opacity:.7">{c}</div></div>' for l, s, bg, c, cc in tiles)
P.append(page(8, '06 Colour versions', f'''{head("06", "Colour versions", "Versions couleur")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:50px">{tl}</div>''', 'light'))

# 9 — Misuse
hz = lambda st='', s='color', w=330: logo_svg('horizontal', s, width=w, style=st)
bad_order = f'<div style="display:flex;align-items:center;gap:18px">{logo_svg("wordmark","color",width=230)}{mark_svg(height=70)}</div>'
bad_font = f'<div style="display:flex;align-items:center;gap:16px">{mark_svg(height=74)}<span style="font:italic 700 66px Georgia,DejaVu Serif,serif">Bayna</span></div>'
mis = [(hz('transform:scaleX(1.3) scaleY(.8)', w=250), 'Don’t stretch or distort', '#fff'), (hz('transform:rotate(-12deg)'), 'Don’t rotate', '#fff'),
       (hz('filter:hue-rotate(150deg) saturate(1.4)'), 'Don’t change the colours', '#fff'), (hz('filter:drop-shadow(6px 10px 6px rgba(0,0,0,.45))'), 'Don’t add shadows or effects', '#fff'),
       (bad_order, 'Don’t rearrange the elements', '#fff'), (bad_font, 'Don’t change the typeface', '#fff'),
       (hz(), 'Don’t use low-contrast backgrounds', VIOLET), (logo_svg('horizontal', 'color-dark', width=330), 'Don’t use the dark version on light', '#fff')]
ml = ''.join(f'<div class="card" style="height:330px;background:{bg};display:flex;align-items:center;justify-content:center">{i}<div class="x">×</div>'
             f'<div class="cap" style="color:{"#fff" if bg!="#fff" else "var(--ink)"};letter-spacing:.06em;text-transform:none;font-size:17px">{c}</div></div>' for i, c, bg in mis)
P.append(page(9, '07 Misuse', f'''{head("07", "Misuse", "Usages interdits")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:50px">{ml}</div>''', 'light'))

# 10 — Palette
cols = [('Bayna Violet', VIOLET, 'Primary. Headlines, buttons, brand moments.', '≈ 2725 C*'),
        ('Electric Lime', LIME, 'Highlight. Calls-to-action, accents — use sparingly.', '≈ 380 C*'),
        ('Ink', INK, 'Base. Dark surfaces and all body text.', '≈ 419 C*'),
        ('White', '#FFFFFF', 'Space. Light surfaces and reversed text.', '—')]
sw = ''
for n, h, use, pms in cols:
    tc = '#fff' if lum(h) < .4 else INK; r, g, b = hex2rgb(h); c, m, y, k = cmyk(h)
    border = 'box-shadow:inset 0 0 0 1px rgba(255,255,255,.18);' if h == INK else ''
    sw += (f'<div style="flex:1;display:flex;flex-direction:column"><div style="height:310px;border-radius:28px;background:{h};{border}padding:30px;color:{tc};position:relative">'
           f'<div class="syne" style="font-size:34px;font-weight:700">{n}</div><div class="mono" style="position:absolute;left:30px;bottom:26px;font-size:30px">{h.upper()}</div></div>'
           f'<table class="spec" style="margin-top:20px;border-collapse:collapse;width:100%"><tr><td>RGB</td><td class="mono">{r} {g} {b}</td></tr>'
           f'<tr><td>CMYK</td><td class="mono">{c} {m} {y} {k}</td></tr><tr><td>Pantone</td><td class="mono">{pms}</td></tr></table>'
           f'<p style="font-size:16px;margin-top:14px">{use}</p></div>')
ratio = [(INK, 45, 'Ink 45%'), ('#FFFFFF', 28, 'White 28%'), (VIOLET, 20, 'Violet & gradient 20%'), (LIME, 7, 'Lime 7%')]
rb = ''.join(f'<div style="flex:{p};background:{h};height:100%;display:flex;align-items:center;padding-left:16px;font-size:13px;font-weight:700;color:{"#fff" if lum(h)<.4 else INK};white-space:nowrap;overflow:hidden">{l}</div>' for h, p, l in ratio)
P.append(page(10, '08 Colour palette', f'''{head("08", "Colour palette", "Palette de couleurs")}
<div class="row" style="margin-top:46px;gap:30px">{sw}</div>
<div style="position:absolute;left:120px;right:120px;bottom:110px"><div class="row" style="justify-content:space-between;align-items:baseline;margin-bottom:12px">
<span class="lbl hl">Colour balance</span><span class="muted" style="font-size:14px">* Nearest Pantone — confirm on a physical swatch book before printing. CMYK values are a starting point; ask for a press proof.</span></div>
<div style="display:flex;height:46px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1px rgba(255,255,255,.14)">{rb}</div></div>''', 'dark'))

# 11 — Gradient + contrast
pairs = [(LIME, INK), ('#FFFFFF', INK), ('#FFFFFF', VIOLET), (LIME, VIOLET), (INK, LIME), (VIOLET, '#FFFFFF'), (INK, '#FFFFFF'), (LIME, '#FFFFFF')]
pc = ''.join(f'<div style="background:{bg};border-radius:18px;padding:18px 20px;height:120px;position:relative;{"box-shadow:inset 0 0 0 1px rgba(36,36,43,.1);" if bg=="#FFFFFF" else ""}">'
             f'<div class="syne" style="color:{fg};font-size:40px;font-weight:700;line-height:1">Aa</div>'
             f'<div style="position:absolute;right:18px;bottom:14px;font-size:14px;font-weight:800;color:{fg}">{contrast(fg,bg):.1f}:1 · {grade(contrast(fg,bg))}</div></div>'
             for fg, bg in pairs)
P.append(page(11, '09 Gradient', f'''{head("09", "Gradient & contrast", "Dégradé & contrastes")}
<div class="row" style="margin-top:46px;gap:60px">
<div style="width:900px"><div style="height:520px;border-radius:28px;background:var(--grad);position:relative;overflow:hidden">
{mark_svg(body="rgba(255,255,255,.95)", height=300, style="position:absolute;left:60px;bottom:60px")}
<div class="mono" style="position:absolute;right:30px;top:28px;color:#fff;font-size:18px">135°</div></div>
<div class="row" style="margin-top:26px;gap:16px">{"".join(f'<div style="flex:1;display:flex;gap:14px;align-items:center"><div style="width:46px;height:46px;border-radius:12px;background:{h}"></div><div><div style="font-weight:700;font-size:16px">{n}</div><div class="mono muted" style="font-size:14px">{h} · {o}</div></div></div>' for n,h,o in [("Lavender",G0,"0%"),("Bayna Violet",G1,"55%"),("Deep Indigo",G2,"100%")])}</div>
<div class="mono" style="margin-top:22px;background:#fff;border-radius:14px;padding:16px 20px;font-size:15px;color:#4a4a55">background: linear-gradient(135deg, {G0} 0%, {G1} 55%, {G2} 100%);</div></div>
<div style="flex:1"><div class="lbl" style="color:var(--violet);margin-bottom:16px">Contrast pairs · WCAG</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{pc}</div>
<p style="font-size:16px;margin-top:20px">Never set lime text on white. Use lime on Ink or Violet, and Ink on lime.</p></div></div>''', 'light'))

# 12 — Typography
P.append(page(12, '10 Typography', f'''{head("10", "Typography", "Typographie")}
<div class="row" style="margin-top:46px;gap:30px">
<div class="card" style="flex:1.15;height:560px;padding:44px"><div class="lbl" style="color:var(--violet)">Display · Titres</div>
<div class="syne" style="font-size:210px;font-weight:700;letter-spacing:-.04em;line-height:1.05;margin-top:10px">Aa</div>
<div class="syne" style="font-size:44px;font-weight:700;margin-top:6px">Syne</div><div class="muted" style="font-size:18px;margin:4px 0 22px">SemiBold 600 · Bold 700 — Google Fonts (OFL)</div>
<div class="syne" style="font-size:24px;font-weight:600;letter-spacing:.02em;line-height:1.5;color:#4a4a55">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div></div>
<div class="card" style="flex:1;height:560px;padding:44px"><div class="lbl" style="color:var(--violet)">Text · Texte courant</div>
<div style="font-size:210px;font-weight:600;letter-spacing:-.04em;line-height:1.05;margin-top:10px">Aa</div>
<div style="font-size:44px;font-weight:700;margin-top:6px">Manrope</div><div class="muted" style="font-size:18px;margin:4px 0 22px">Regular 400 → ExtraBold 800 — Google Fonts (OFL)</div>
<div style="font-size:24px;font-weight:500;line-height:1.5;color:#4a4a55">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div></div>
<div class="card" style="width:520px;height:560px;padding:44px;background:var(--ink);color:#fff"><div class="lbl hl">Hierarchy</div>
<div class="syne" style="font-size:58px;font-weight:700;letter-spacing:-.03em;line-height:1;margin-top:26px">Headline</div><div class="mono" style="font-size:13px;opacity:.5;margin:8px 0 24px">Syne 700 · −3 % · 1.0</div>
<div class="syne" style="font-size:32px;font-weight:600;letter-spacing:-.01em">Sub-headline</div><div class="mono" style="font-size:13px;opacity:.5;margin:8px 0 24px">Syne 600 · −1 %</div>
<div style="font-size:18px;line-height:1.6;color:rgba(255,255,255,.75)">Body copy is set in Manrope Regular with generous line spacing for comfortable reading.</div><div class="mono" style="font-size:13px;opacity:.5;margin:8px 0 24px">Manrope 400 · 1.6</div>
<div class="lbl hl">Label · Étiquette</div><div class="mono" style="font-size:13px;opacity:.5;margin-top:8px">Manrope 700 · caps · +20 %</div>
<div style="font-family:'Readex Pro';font-size:30px;font-weight:500;margin-top:24px;direction:rtl;text-align:left">النص العربي — Readex Pro</div></div>
</div>''', 'light'))

# 13 — Graphic elements: slice pattern
def qtile(rot, c, sl=None):
    s = f'<div style="width:100%;height:100%;background:{c};border-top-left-radius:100%;transform:rotate({rot}deg)"></div>'
    return s
import random
random.seed(7)
pal = [VIOLET, VIOLET, '#4A2BD9', '#7B5CFF', '#2F2F38', '#2F2F38', LIME]
cells = ''
for i in range(6*4):
    c = pal[random.randrange(len(pal))] if i not in (9,) else LIME
    rot = random.choice([0, 90, 180, 270]); shape = random.choice(['q', 'q', 'q', 'c', 'h'])
    if shape == 'c': inner = f'<div style="width:100%;height:100%;border-radius:50%;background:{c}"></div>'
    elif shape == 'h': inner = f'<div style="width:100%;height:50%;margin-top:50%;background:{c};border-radius:999px 999px 0 0;transform:rotate({rot}deg)"></div>'
    else: inner = qtile(rot, c)
    cells += f'<div style="aspect-ratio:1">{inner}</div>'
rules = [('The slice', 'A lime quarter-circle marks the single most important thing on a layout: a number, a CTA, a word.'),
         ('The pattern', 'Quarter circles, half circles and dots on a square grid build backgrounds and covers.'),
         ('The crop', 'Scale the symbol up and let it bleed off the edge — never shrink it into a corner as decoration.')]
P.append(page(13, '11 Graphic elements', f'''{head("11", "Graphic elements", "Éléments graphiques")}
<div style="position:absolute;right:120px;top:150px;width:820px;display:grid;grid-template-columns:repeat(6,1fr);gap:14px">{cells}</div>
<div style="width:760px;margin-top:56px">{"".join(f'<div style="display:flex;gap:26px;padding:26px 0;border-top:1px solid rgba(255,255,255,.14)"><div style="width:44px;height:44px;flex:none;background:var(--lime);border-top-left-radius:44px;margin-top:4px"></div><div><h3>{t}</h3><p style="font-size:19px">{d}</p></div></div>' for t,d in rules)}</div>''', 'dark'))

# 14 — Data & charts (dark surface: lime passes contrast here)
months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin']; vals_b = [32, 41, 38, 52, 61, 78]
bw_, gap_, ch = 86, 34, 360; mx = 90
bars = ''
for i, v in enumerate(vals_b):
    h = v/mx*ch; x = i*(bw_+gap_); c = LIME if i == 5 else '#7B5CFF'
    bars += (f'<path d="M{x},{ch} V{ch-h+4} Q{x},{ch-h} {x+4},{ch-h} H{x+bw_-4} Q{x+bw_},{ch-h} {x+bw_},{ch-h+4} V{ch} Z" fill="{c}"/>'
             f'<text x="{x+bw_/2}" y="{ch+30}" fill="rgba(255,255,255,.55)" font-size="16" text-anchor="middle" font-family="Manrope" font-weight="600">{months[i]}</text>')
bars += f'<text x="{5*(bw_+gap_)+bw_/2}" y="{ch-78/mx*ch-14}" fill="#fff" font-size="22" font-weight="800" text-anchor="middle" font-family="Manrope">78</text>'
grid = ''.join(f'<line x1="0" x2="{6*(bw_+gap_)-gap_}" y1="{ch-v/mx*ch}" y2="{ch-v/mx*ch}" stroke="rgba(255,255,255,.08)"/>' for v in (30, 60, 90))
bar_svg = f'<svg viewBox="0 -10 {6*(bw_+gap_)-gap_} {ch+50}" width="560">{grid}<line x1="0" x2="{6*(bw_+gap_)-gap_}" y1="{ch}" y2="{ch}" stroke="rgba(255,255,255,.3)"/>{bars}</svg>'
# donut: 3/4 + lime slice mirrors the mark
segs = [(0.46, '#7B5CFF', 'Social'), (0.29, '#B9A6FF', 'Search'), (0.25, LIME, 'Referral')]
cx = cy = 170; ro, ri = 160, 104; a0 = -90; dn = ''
for f, c, n in segs:
    a1 = a0 + f*360 - 1.2
    def pt(a, r): return cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a))
    large = 1 if (a1 - a0) > 180 else 0
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = pt(a0, ro), pt(a1, ro), pt(a1, ri), pt(a0, ri)
    dn += f'<path d="M{x0:.2f},{y0:.2f} A{ro},{ro} 0 {large},1 {x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f} A{ri},{ri} 0 {large},0 {x3:.2f},{y3:.2f} Z" fill="{c}"/>'
    a0 = a1 + 1.2
dn_svg = f'<svg viewBox="0 0 340 340" width="250">{dn}<text x="170" y="168" fill="#fff" font-size="44" font-weight="800" text-anchor="middle" font-family="Syne">25%</text><text x="170" y="198" fill="rgba(255,255,255,.55)" font-size="15" font-weight="600" text-anchor="middle" font-family="Manrope">referral</text></svg>'
legend = ''.join(f'<div style="display:flex;align-items:center;gap:12px;font-size:17px;font-weight:600;margin-top:12px"><span style="width:14px;height:14px;border-radius:4px;background:{c}"></span>{n}<span class="muted" style="margin-left:auto">{round(f*100)}%</span></div>' for f, c, n in segs)
kpis = [('Reach', '1.2M', '+18%'), ('Leads', '3 480', '+42%'), ('CPA', '640 DA', '−21%')]
kp = ''.join(f'<div style="flex:1;background:#2E2E37;border-radius:22px;padding:20px 28px"><div class="lbl muted">{n}</div><div class="syne" style="font-size:40px;font-weight:700;margin-top:6px">{v}</div><div style="font-weight:800;color:var(--lime);margin-top:4px">{d} <span class="muted" style="font-weight:600">vs last month</span></div></div>' for n, v, d in kpis)
P.append(page(14, '12 Data & charts', f'''{head("12", "Data & charts", "Graphiques & data")}
<p style="max-width:1200px;margin-top:22px">Our reports are part of the brand. Charts sit on Ink, data is Violet, and <span class="hl">lime is reserved for the one number that matters</span>. Every series is labelled — colour is never the only key.</p>
<div class="row" style="margin-top:36px;gap:28px">
<div style="background:#2E2E37;border-radius:28px;padding:28px 38px;width:760px"><div class="lbl muted">Monthly leads · sample data</div><div style="margin-top:26px">{bar_svg}</div></div>
<div style="background:#2E2E37;border-radius:28px;padding:34px 38px;flex:1;display:flex;gap:40px;align-items:center"><div>{dn_svg}</div><div style="flex:1"><div class="lbl muted">Traffic by source · sample</div>{legend}
<p style="font-size:15px;margin-top:22px">The donut echoes the symbol: three quarters in violet, the highlighted slice in lime.</p></div></div></div>
<div class="row" style="margin-top:24px;gap:28px">{kp}</div>''', 'dark'))

# 15 — Applications: stationery
P.append(page(15, '13 Applications', f'''{head("13", "Stationery", "Applications · Papeterie")}
<div style="position:absolute;left:120px;top:400px;width:1000px;height:560px;border-radius:28px;background:#E9E7F1;overflow:hidden">
 <img src="{A('stationery/business-card/business-card-back.png')}" style="position:absolute;width:520px;left:420px;top:150px;transform:rotate(-8deg);box-shadow:0 30px 60px rgba(36,36,43,.25);border-radius:6px">
 <img src="{A('stationery/business-card/business-card-front.png')}" style="position:absolute;width:520px;left:70px;top:70px;transform:rotate(4deg);box-shadow:0 30px 60px rgba(36,36,43,.35);border-radius:6px">
</div>
<div style="position:absolute;left:1150px;top:150px;width:650px;height:810px;border-radius:28px;background:#D9D6E5;overflow:hidden">
 <img src="{A('stationery/letterhead/letterhead-A4-preview.png')}" style="position:absolute;width:470px;left:90px;top:60px;box-shadow:0 30px 60px rgba(36,36,43,.25)">
</div>
<p style="position:absolute;left:120px;top:300px;width:960px;font-size:19px">Business card 85 × 55 mm · Letterhead A4 · Email signature. Print files with 3 mm bleed are in <span class="mono">/stationery</span>.</p>''', 'light'))

# 16 — Applications: social
P.append(page(16, '13 Applications', f'''{head("13", "Social media", "Applications · Réseaux sociaux")}
<div class="row" style="margin-top:50px;gap:26px;align-items:flex-start">
<img src="{A('social/instagram-post-tagline-1080x1350.png')}" style="height:560px;border-radius:20px">
<img src="{A('social/instagram-post-services-1080x1350.png')}" style="height:560px;border-radius:20px">
<img src="{A('social/instagram-story-1080x1920.png')}" style="height:560px;border-radius:20px">
<div class="col" style="gap:26px;flex:1"><img src="{A('social/linkedin-banner-1584x396.png')}" style="width:100%;border-radius:16px">
<img src="{A('social/facebook-cover-1640x624.png')}" style="width:100%;border-radius:16px">
<img src="{A('icons/png/avatar-gradient-400.png')}" style="width:150px;border-radius:50%"></div></div>''', 'light'))

# 17 — Back cover
P.append(page(17, '', f'''
<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-62%);text-align:center">
{logo_svg("stacked","on-violet",width=520)}
<div class="syne" style="font-size:46px;font-weight:700;margin-top:70px;letter-spacing:-.02em">Proof, by design.</div>
<div style="font-size:22px;margin-top:12px;color:rgba(255,255,255,.75)">La preuve, par le design.</div></div>
<div style="position:absolute;left:120px;right:120px;bottom:70px;display:flex;justify-content:space-between;font-size:17px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.75)">
<span>Bayna Agency</span><span>Oran, Algérie</span><span>bayna.agency</span></div>''', 'gradp', chrome_on=False))

html = page_doc(''.join(P), css, '1920px 1080px')
open(f'{HT}/guidelines.html', 'w').write(html)
print('pages', len(P))
