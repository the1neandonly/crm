"""Export the logo system and app icons: SVG + render jobs (PNG / PDF), JPG afterwards."""
import os, sys, json
from logo import *
OUT = sys.argv[1]; jobs = []; jpgs = []
def w(p, t): os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(t)
NAMES = {'horizontal': '01_Horizontal', 'stacked': '02_Vertical_Stacked', 'symbol': '03_Symbole_Symbol', 'symbol-small': '04_Symbole-petite-taille_Symbol-small',
         'wordmark': '05_Logotype_Wordmark', 'arabic': '06_Arabe_Arabic', 'arabic-stacked': '07_Arabe-vertical_Arabic-stacked', 'bilingual': '08_Bilingue_Bilingual'}
for lk, folder in NAMES.items():
    for sc in SCHEMES:
        bw, bh, inner = LOCKUPS[lk](sc); pad = 0.06*max(bw, bh) if lk.startswith('symbol') else 0.04*bh
        base = f'{OUT}/02_Logos/{folder}/gymliink-{lk}-{sc}'
        svg = svg_doc(bw, bh, inner, pad=pad, title=f'Gymliink — {lk} ({sc})'); w(base + '.svg', svg)
        W_, H_ = bw + 2*pad, bh + 2*pad; px = 1024 if lk.startswith('symbol') else 2400
        jobs.append({'type': 'png', 'svg': base + '.svg', 'out': base + '.png', 'w': px, 'h': round(px*H_/W_)})
        jobs.append({'type': 'pdf', 'svg': base + '.svg', 'out': base + '.pdf', 'w': round(W_*3), 'h': round(H_*3)})
        m = 0.35*max(bw, bh) if lk.startswith('symbol') else 0.5*bh
        bg = svg_doc(bw, bh, inner, pad=m, bg=SCHEME_BG[sc]); tp = f'{OUT}/_tmp/{lk}-{sc}.svg'; w(tp, bg)
        Wj, Hj = bw + 2*m, bh + 2*m; pxj = 1600 if lk.startswith('symbol') else 2400
        jobs.append({'type': 'png', 'svg': tp, 'out': tp[:-4] + '.png', 'w': pxj, 'h': round(pxj*Hj/Wj)}); jpgs.append((tp[:-4] + '.png', base + '.jpg'))
# ---- App icons
GLOW = f'<radialGradient id="glow" cx="50%" cy="46%" r="50%"><stop offset="0" stop-color="{VOLT}" stop-opacity=".16"/><stop offset=".6" stop-color="{VOLT}" stop-opacity=".03"/><stop offset="1" stop-color="{VOLT}" stop-opacity="0"/></radialGradient>'
def icon(size, bg=True, glow=True, scheme='color-dark', frac=0.56, small=False, rx=0):
    l, d1, d2, *_ = SCHEMES[scheme]
    sh = size*frac; s = sh/SH; sw = SW*s
    b = (f'<rect width="{size}" height="{size}" rx="{rx}" fill="{BG}"/>' + (f'<rect width="{size}" height="{size}" rx="{rx}" fill="url(#glow)"/>' if glow else '')) if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><defs>{GLOW}</defs>{b}'
            f'{symbol(l, d1, d2, (size - sw)/2, (size - sh)/2 + size*0.01, s, small)}</svg>')
def tinted(size, frac=0.56):
    sh = size*frac; s = sh/SH; sw = SW*s
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><rect width="{size}" height="{size}" fill="#000"/>'
            f'{symbol("#FFFFFF", "#FFFFFF", "#BDBDBD", (size - sw)/2, (size - sh)/2, s)}</svg>')
A = f'{OUT}/03_Icones-app_App-icons'
icons = {
    f'{A}/iOS/gymliink-ios-1024': icon(1024),
    f'{A}/iOS/gymliink-ios-dark-1024': icon(1024, bg=False),
    f'{A}/iOS/gymliink-ios-tinted-1024': tinted(1024),
    f'{A}/Android/gymliink-android-foreground-432': icon(432, bg=False, frac=0.40),
    f'{A}/Android/gymliink-android-background-432': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 432 432" width="432" height="432"><defs>{GLOW}</defs><rect width="432" height="432" fill="{BG}"/><rect width="432" height="432" fill="url(#glow)"/></svg>',
    f'{A}/Android/gymliink-android-monochrome-432': icon(432, bg=False, frac=0.40, scheme='white'),
    f'{A}/Android/gymliink-play-store-512': icon(512),
    f'{A}/Favicon/favicon-16': icon(16, frac=0.78, small=True, glow=False, rx=3),
    f'{A}/Favicon/favicon-32': icon(32, frac=0.74, small=True, glow=False, rx=6),
    f'{A}/Favicon/favicon-48': icon(48, frac=0.72, small=True, glow=False, rx=9),
    f'{A}/Favicon/apple-touch-icon-180': icon(180),
    f'{A}/Favicon/android-chrome-192': icon(192),
    f'{A}/Favicon/android-chrome-512': icon(512),
}
for p, svg in icons.items():
    w(p + '.svg', svg); n = int(p.rsplit('-', 1)[1]); jobs.append({'type': 'png', 'svg': p + '.svg', 'out': p + '.png', 'w': n, 'h': n})
w(f'{A}/Favicon/favicon.svg', icon(64, frac=0.74, small=True, glow=False, rx=12))
# splash screens
def splash(wd, ht, word=True):
    sh = 0.11*wd*1.9; s = sh/SH; sw = SW*s
    l, d1, d2, wc, t1, t2 = SCHEMES['color-dark']
    wsvg, ww = wordmark_svg(wc, t1, t2, 0.075*wd, 0, 0)
    g = f'<radialGradient id="sg" cx="50%" cy="46%" r="38%"><stop offset="0" stop-color="{VOLT}" stop-opacity=".10"/><stop offset="1" stop-color="{VOLT}" stop-opacity="0"/></radialGradient>'
    wm = f'<g transform="translate({(wd - ww)/2:.1f},{ht*0.9:.1f})" opacity=".9">{wordmark_svg(TXT2, TXT2, VOLT, 0.05*wd, 0, 0)[0]}</g>' if word else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {wd} {ht}" width="{wd}" height="{ht}"><defs>{g}</defs><rect width="{wd}" height="{ht}" fill="{BG}"/>'
            f'<rect width="{wd}" height="{ht}" fill="url(#sg)"/>{symbol(l, d1, d2, (wd - sw)/2, ht*0.46 - sh/2, s)}{wm}</svg>')
for nm, wd, ht in [('splash-ios-1290x2796', 1290, 2796), ('splash-android-1080x1920', 1080, 1920), ('splash-tablet-2048x2732', 2048, 2732)]:
    p = f'{A}/Splash/gymliink-{nm}'; svg = splash(wd, ht)
    svg = svg.replace(f'<g transform="translate({(wd - wordmark_svg(TXT, TXT, VOLT, 0.075*wd, 0, 0)[1])/2:.1f}', f'<g transform="translate({(wd - wordmark_svg(TXT2, TXT2, VOLT, 0.05*wd, 0, 0)[1])/2:.1f}')
    w(p + '.svg', svg); jobs.append({'type': 'png', 'svg': p + '.svg', 'out': p + '.png', 'w': wd, 'h': ht})
p = f'{A}/Splash/gymliink-splash-icon-android12-1152'; w(p + '.svg', icon(1152, bg=False, frac=0.30)); jobs.append({'type': 'png', 'svg': p + '.svg', 'out': p + '.png', 'w': 1152, 'h': 1152})
json.dump(jobs, open('jobs_logo.json', 'w')); json.dump(jpgs, open('jpgs_logo.json', 'w')); print(len(jobs))
