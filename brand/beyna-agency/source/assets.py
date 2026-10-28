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
        p = f'{OUT}/icons/service-icons/svg/{cw}/beyna-icon-{n}.svg'; w(p, icon_svg(n, c, a, 48))
        svg_jobs.append({'type': 'png', 'svg': p, 'out': f'{OUT}/icons/service-icons/png/{cw}/beyna-icon-{n}-512.png', 'w': 512, 'h': 512})

# ---------- Patterns (seamless: whole cells only)
def pattern_svg(cols, rows, cell, pal, bg, seed, accent_every=11):
    random.seed(seed); out = [f'<rect width="{cols*cell}" height="{rows*cell}" fill="{bg}"/>']
    for j in range(rows):
        for i in range(cols):
            x, y = i*cell, j*cell; k = random.random()
            hi = random.random() < 1/accent_every; c = LIME if hi else random.choice(pal)
            rot = random.choice([0, 90, 180, 270]); cx, cy = x + cell/2, y + cell/2
            m = cell*0.06; s = cell - 2*m
            if hi:        shp = (f'<circle cx="{cx}" cy="{cy}" r="{s/2}" fill="{LIME}"/><circle cx="{cx + s*0.1}" cy="{cy}" r="{s*0.2}" fill="{INK}"/>'
                                 f'<circle cx="{cx + s*0.17}" cy="{cy - s*0.1}" r="{s*0.06}" fill="#fff"/>')   # the iris
            elif k < .55:   shp = f'<path d="M{x+m},{y+m+s} V{y+m} A{s},{s} 0 0,1 {x+m+s},{y+m+s} Z" fill="{c}" transform="rotate({rot} {cx} {cy})"/>'
            elif k < .72: shp = f'<circle cx="{cx}" cy="{cy}" r="{s/2}" fill="{c}"/>'
            elif k < .86: shp = f'<path d="M{x+m},{cy} A{s/2},{s/2} 0 0,1 {x+m+s},{cy} Z" fill="{c}" transform="rotate({rot} {cx} {cy})"/>'
            else: shp = ''
            out.append(shp)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols*cell} {rows*cell}" width="{cols*cell}" height="{rows*cell}">{"".join(out)}</svg>'
PATTERNS = {
    'ink':    ([VIOLET, '#4A2BD9', '#7B5CFF', '#2F2F38', '#2F2F38'], INK, 7),
    'violet': (['#7B5CFF', '#4A2BD9', '#8C70FF', '#5530F0'], VIOLET, 3),
    'paper':  (['#E6E1FA', '#D9D1FF', '#EDEAF7', VIOLET], '#F5F4F9', 5),
    'lime':   (['#C2F040', '#B8E83A', INK, '#DAFF78'], LIME, 9),
    'mono':   (['#2F2F38', '#34343E', '#3A3A45'], INK, 4),
}
for n, (pal, bg, seed) in PATTERNS.items():
    p = f'{OUT}/patterns/svg/beyna-pattern-{n}.svg'; w(p, pattern_svg(8, 8, 120, pal, bg, seed, 999 if n in ('mono', 'lime') else 11))
    svg_jobs.append({'type': 'png', 'svg': p, 'out': f'{OUT}/patterns/png/beyna-pattern-{n}-tile-1920.png', 'w': 1920, 'h': 1920})
PATTERN_URL = lambda n: f'file://{OUT}/patterns/svg/beyna-pattern-{n}.svg'

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
wall('virtual-background-paper-1920x1080', 1920, 1080, f'<div style="position:absolute;inset:0;background:#F5F4F9"></div><div style="position:absolute;right:70px;top:60px">{logo_svg("horizontal-compact","color",width=300)}</div><div style="position:absolute;left:-1px;bottom:-1px;width:420px;height:420px;background:var(--grad);border-top-right-radius:420px"></div>', folder='virtual-backgrounds')

# ---------- Instagram highlight covers (1080x1920, icon in central safe circle)
HL = [('About', 'growth'), ('Services', 'strategy'), ('Work', 'star'), ('Clients', 'team'), ('Process', 'idea'), ('Social', 'social'), ('Video', 'video'), ('Contact', 'contact')]
for lbl, ic in HL:
    for v, (cls, c, a) in {'gradient': ('grad', WHITE, LIME), 'ink': ('ink', VIOLET, LIME)}.items():
        wall(f'highlight-{lbl.lower()}-{v}', 1080, 1920, f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{icon_svg(ic, c, a, 300)}</div>', cls, folder='social/instagram-highlight-covers')

json.dump(svg_jobs, open('jobs_assets_svg.json', 'w')); json.dump(html_jobs, open('jobs_assets_html.json', 'w'))
# icon sheet preview
sheet = ''.join(f'<div style="display:inline-block;margin:14px">{icon_svg(n, VIOLET, LIME, 96)}</div>' for n in ICONS)
open('icon_sheet.html', 'w').write(f'<body style="background:#fff;width:1000px">{sheet}<div style="background:#24242B;padding:10px">' + ''.join(f'<div style="display:inline-block;margin:14px">{icon_svg(n, WHITE, LIME, 96)}</div>' for n in ICONS) + '</div></body>')
print(len(svg_jobs), len(html_jobs))
