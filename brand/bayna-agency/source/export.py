import json, os, sys
from logo import *
OUT = sys.argv[1]
jobs = []
def w(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(txt)

PAD = 16
SCHEMES_OUT = ['color', 'color-dark', 'on-violet', 'black', 'white']
JPG_BG = {'color': WHITE, 'black': WHITE, 'color-dark': INK, 'white': INK, 'on-violet': VIOLET, 'on-lime': LIME}
PNG_WIDTHS = {'horizontal': [800, 2000, 4000], 'horizontal-compact': [400, 800, 2000], 'stacked': [800, 2000, 4000], 'wordmark': [800, 2000, 4000], 'icon': [256, 1024, 2048]}
for lockup in ['horizontal', 'horizontal-compact', 'stacked', 'icon', 'wordmark']:
    schemes = SCHEMES_OUT + (['on-lime'] if lockup == 'icon' else [])
    for sch in schemes:
        if lockup == 'wordmark' and sch == 'on-lime': continue
        name = f'bayna-{lockup}-{sch}'
        svg, (bw, bh) = build(lockup, sch)
        # tight + small safety pad
        svg = svg_wrap(bw, bh, LOCKUPS[lockup](sch)[2], pad=PAD, title=f'Bayna Agency — {lockup} ({sch})')
        vw, vh = bw + 2*PAD, bh + 2*PAD
        p = f'{OUT}/logo/svg/{name}.svg'; w(p, svg)
        for px in PNG_WIDTHS[lockup]:
            jobs.append({'type': 'png', 'svg': p, 'out': f'{OUT}/logo/png/{lockup}/{name}-{px}px.png', 'w': px, 'h': round(px*vh/vw)})
        jobs.append({'type': 'pdf', 'svg': p, 'out': f'{OUT}/logo/pdf/{name}.pdf', 'w': round(vw*2), 'h': round(vh*2)})
        # JPG: logo on its background with generous clear space (= one bowl radius)
        m = R * 1.6
        bgsvg = svg_wrap(bw, bh, LOCKUPS[lockup](sch)[2], bg=JPG_BG[sch], pad=m)
        jp = f'{OUT}/logo/_tmp/{name}-bg.svg'; w(jp, bgsvg)
        jw = 3000 if lockup != 'icon' else 2000
        jobs.append({'type': 'png', 'svg': jp, 'out': f'{OUT}/logo/_tmp/{name}-bg.png', 'w': jw, 'h': round(jw*(bh+2*m)/(bw+2*m)), 'jpg': f'{OUT}/logo/jpg/{name}.jpg'})

# ---- App icons / favicons / avatars: mark on brand backgrounds, square
def square_icon(bg_kind, size_ratio=0.56, radius=0.0, slice_c=LIME, body=WHITE):
    S_ = 1000
    mh = S_ * size_ratio; sc = mh / H; mw = W * sc
    ox, oy = (S_ - mw) / 2 + mw*0.02, (S_ - mh) / 2
    if bg_kind == 'gradient':
        bgel = f'<rect width="{S_}" height="{S_}" rx="{radius*S_}" fill="url(#bgsq)"/>'
    else:
        bgel = f'<rect width="{S_}" height="{S_}" rx="{radius*S_}" fill="{bg_kind}"/>'
    defs = grad_def('bg') + grad_def('bgsq')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S_} {S_}" width="{S_}" height="{S_}"><defs>{defs}</defs>'
            f'{bgel}{mark_paths(body, slice_c, ox, oy, sc)}</svg>')
icons = {
    'app-icon-gradient': square_icon('gradient'),
    'app-icon-ink': square_icon(INK, size_ratio=0.5, body='url(#bg)'),
    'app-icon-violet': square_icon(VIOLET),
    'app-icon-lime': square_icon(LIME, body=INK, slice_c=VIOLET),
    'favicon-master': square_icon('gradient', size_ratio=0.66, radius=0.22),
    'avatar-gradient': square_icon('gradient', size_ratio=0.44),
    'avatar-ink': square_icon(INK, size_ratio=0.44, body='url(#bg)'),
}
for n, s in icons.items():
    p = f'{OUT}/icons/svg/{n}.svg'; w(p, s)
    sizes = {'favicon-master': [16, 32, 48, 64, 180, 192, 512], 'avatar-gradient': [400, 1080], 'avatar-ink': [400, 1080]}.get(n, [1024])
    for px in sizes:
        jobs.append({'type': 'png', 'svg': p, 'out': f'{OUT}/icons/png/{n}-{px}.png', 'w': px, 'h': px})
json.dump(jobs, open('jobs.json', 'w'), indent=0)
print(len(jobs), 'jobs')
