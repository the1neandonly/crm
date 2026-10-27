import os, sys, json, random
from kit import *
from icons import ICONS, icon_svg
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html'); os.makedirs(HT, exist_ok=True)
svg_jobs, html_jobs = [], []
def w(p, t): os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(t)

# ---------- Icon set
COLS = {'violet': (VIOLET, LIME), 'white': (WHITE, LIME), 'ink': (INK, VIOLET), 'mono-ink': (INK, INK), 'mono-white': (WHITE, WHITE)}
for n in ICONS:
    for cw, (c, a) in COLS.items():
        p = f'{OUT}/icons/service-icons/svg/{cw}/dto-icon-{n}.svg'; w(p, icon_svg(n, c, a, 48))
        svg_jobs.append({'type': 'png', 'svg': p, 'out': f'{OUT}/icons/service-icons/png/{cw}/dto-icon-{n}-512.png', 'w': 512, 'h': 512})

# ---------- Patterns (seamless: whole cells only) — DTO code glyphs: braces, </>, cursors, nodes, waves
from textpath import text_path
from dto_mark import BRACE
def pattern_svg(cols, rows, cell, pal, bg, seed, accent_every=11):
    random.seed(seed); out = [f'<rect width="{cols*cell}" height="{rows*cell}" fill="{bg}"/>']
    for j in range(rows):
        for i in range(cols):
            x, y = i*cell, j*cell; k = random.random(); cx, cy = x + cell/2, y + cell/2
            c = LIME if random.random() < 1/accent_every else random.choice(pal)
            if k < .22:   # braces pair
                sc = cell*0.62/438
                out.append(f'<g transform="translate({cx - cell*0.36},{cy - cell*0.31}) scale({sc})"><path d="{BRACE}" fill="{c}"/></g>'
                           f'<g transform="translate({cx + cell*0.36},{cy - cell*0.31}) scale({-sc},{sc})"><path d="{BRACE}" fill="{c}"/></g>')
            elif k < .40: # </>
                d, w = text_path('</>', 'JetBrainsMono-700.ttf', cell*0.42, 0, 0)
                out.append(f'<path d="{d}" fill="{c}" transform="translate({cx - w/2},{cy + cell*0.14})"/>')
            elif k < .56: # cursor
                out.append(f'<g transform="translate({cx - cell*0.18},{cy - cell*0.32}) rotate(-14) scale({cell*0.0034})"><polygon points="0,0 0,150 36,116 62,176 86,166 60,108 112,106" fill="{c}"/></g>')
            elif k < .74: # node (ring + dot)
                out.append(f'<circle cx="{cx}" cy="{cy}" r="{cell*0.26}" fill="none" stroke="{c}" stroke-width="{cell*0.08}"/><circle cx="{cx + cell*0.18}" cy="{cy - cell*0.18}" r="{cell*0.08}" fill="{c}"/>')
            elif k < .88: # wave
                m = cell*0.14
                out.append(f'<path d="M{x+m},{cy} C{x+cell*0.35},{cy-cell*0.3} {x+cell*0.65},{cy+cell*0.3} {x+cell-m},{cy}" fill="none" stroke="{c}" stroke-width="{cell*0.09}" stroke-linecap="round"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols*cell} {rows*cell}" width="{cols*cell}" height="{rows*cell}">{"".join(out)}</svg>'
PATTERNS = {
    'ink':    (['#1A3B5E', '#14324F', '#0F66B6', '#2A2D33', '#2A2D33'], INK, 7),
    'violet': (['#3E86CF', '#0B559A', '#5596D6', '#2F78C2'], VIOLET, 3),
    'paper':  (['#D6E5F5', '#C4DBF2', '#E3EDF8', VIOLET], '#F2F6FB', 5),
    'sky':    (['#7FBDF5', '#3693E6', INK, '#9ACCF7'], LIME, 9),
    'mono':   (['#1C1E22', '#202328', '#25282E'], INK, 4),
}
for n, (pal, bg, seed) in PATTERNS.items():
    p = f'{OUT}/patterns/svg/dto-pattern-{n}.svg'; w(p, pattern_svg(8, 8, 120, pal, bg, seed, 999 if n in ('mono', 'sky') else 11))
    svg_jobs.append({'type': 'png', 'svg': p, 'out': f'{OUT}/patterns/png/dto-pattern-{n}-tile-1920.png', 'w': 1920, 'h': 1920})
PATTERN_URL = lambda n: f'file://{OUT}/patterns/svg/dto-pattern-{n}.svg'

# ---------- Wallpapers / virtual backgrounds
wcss = '.f{position:relative;overflow:hidden}.ink{background:var(--ink)}.grad{background:var(--grad)}'
def wall(name, wd, ht, body, cls='ink', folder='wallpapers'):
    p = f'{HT}/wall-{name}.html'
    open(p, 'w').write(page_doc(f'<div class="f {cls}" style="width:{wd}px;height:{ht}px">{body}</div>', wcss, f'{wd}px {ht}px'))
    html_jobs.append(dict(html=p, type='png', out=f'{OUT}/{folder}/{name}.png', w=wd, h=ht, unit='px'))
wall('desktop-ink-2560x1440', 2560, 1440, mark_svg(height=1800, style='position:absolute;right:-300px;top:-200px'))
wall('desktop-gradient-2560x1440', 2560, 1440, f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{mark_svg(body="#fff", height=420)}</div>', 'grad')
wall('desktop-pattern-2560x1440', 2560, 1440, f'<div style="position:absolute;inset:0;background:url({PATTERN_URL("ink")}) 0 0/960px 960px"></div>')
wall('phone-ink-1290x2796', 1290, 2796, mark_svg(height=2100, style='position:absolute;left:-500px;bottom:-200px'))
wall('phone-gradient-1290x2796', 1290, 2796, f'<div style="position:absolute;left:0;right:0;top:1500px;display:flex;justify-content:center">{mark_svg(body="#fff", height=360)}</div>', 'grad')
wall('phone-pattern-1290x2796', 1290, 2796, f'<div style="position:absolute;inset:0;background:url({PATTERN_URL("violet")}) 0 0/860px 860px"></div>')
# Zoom / Teams / Meet backgrounds — logo top-right, subject area kept calm
wall('virtual-background-ink-1920x1080', 1920, 1080, f'{mark_svg(height=1300, style="position:absolute;right:-420px;bottom:-380px;opacity:.9")}<div style="position:absolute;right:70px;top:60px">{logo_svg("horizontal-compact","color-dark",width=300)}</div>', folder='virtual-backgrounds')
wall('virtual-background-gradient-1920x1080', 1920, 1080, f'<div style="position:absolute;right:70px;top:60px">{logo_svg("horizontal-compact","on-violet",width=300)}</div>', 'grad', folder='virtual-backgrounds')
wall('virtual-background-paper-1920x1080', 1920, 1080, f'<div style="position:absolute;inset:0;background:#F2F6FB"></div><div style="position:absolute;right:70px;top:60px">{logo_svg("horizontal-compact","color",width=300)}</div><div style="position:absolute;left:-1px;bottom:-1px;width:420px;height:420px;background:var(--grad);border-top-right-radius:420px"></div>', folder='virtual-backgrounds')

# ---------- Instagram highlight covers (1080x1920, icon in central safe circle)
HL = [('About', 'growth'), ('Services', 'strategy'), ('Work', 'star'), ('Clients', 'team'), ('Process', 'idea'), ('Social', 'social'), ('Video', 'video'), ('Contact', 'contact')]
for lbl, ic in HL:
    for v, (cls, c, a) in {'gradient': ('grad', WHITE, LIME), 'ink': ('ink', VIOLET, LIME)}.items():
        wall(f'highlight-{lbl.lower()}-{v}', 1080, 1920, f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{icon_svg(ic, c, a, 300)}</div>', cls, folder='social/instagram-highlight-covers')

json.dump(svg_jobs, open('jobs_assets_svg.json', 'w')); json.dump(html_jobs, open('jobs_assets_html.json', 'w'))
# icon sheet preview
sheet = ''.join(f'<div style="display:inline-block;margin:14px">{icon_svg(n, VIOLET, LIME, 96)}</div>' for n in ICONS)
open('icon_sheet.html', 'w').write(f'<body style="background:#fff;width:1000px">{sheet}<div style="background:#0A0B0D;padding:10px">' + ''.join(f'<div style="display:inline-block;margin:14px">{icon_svg(n, WHITE, LIME, 96)}</div>' for n in ICONS) + '</div></body>')
print(len(svg_jobs), len(html_jobs))
