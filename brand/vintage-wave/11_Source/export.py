import os, sys, json
from logo import *
OUT = sys.argv[1]; jobs = []; jpgs = []
def w(p, t): os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(t)
NAMES = {'stacked': '01_Logo-principal_Primary-stacked', 'horizontal': '02_Horizontal', 'symbol': '03_Symbole_Symbol', 'wordmark': '04_Logotype_Wordmark',
         'tagline': '05_Logotype-signature_Wordmark-tagline', 'badge': '06_Badge-tampon_Badge'}
for lk, folder in NAMES.items():
    for sc in SCHEMES:
        bw, bh, inner = LOCKUPS[lk](sc); pad = 0.05*max(bw, bh)
        base = f'{OUT}/02_Logos/{folder}/vintage-wave-{lk}-{sc}'
        w(base + '.svg', svg_doc(bw, bh, inner, pad=pad, title=f'Vintage Wave — {lk} ({sc})'))
        W_, H_ = bw + 2*pad, bh + 2*pad; px = 2400 if lk in ('horizontal', 'tagline', 'wordmark') else 2000
        jobs += [{'type': 'png', 'svg': base + '.svg', 'out': base + '.png', 'w': px, 'h': round(px*H_/W_)}, {'type': 'pdf', 'svg': base + '.svg', 'out': base + '.pdf', 'w': round(W_*2), 'h': round(H_*2)}]
        m = 0.3*max(bw, bh); tp = f'{OUT}/_tmp/{lk}-{sc}.svg'; w(tp, svg_doc(bw, bh, inner, pad=m, bg=SCHEME_BG[sc]))
        Wj, Hj = bw + 2*m, bh + 2*m
        jobs.append({'type': 'png', 'svg': tp, 'out': tp[:-4] + '.png', 'w': 2000, 'h': round(2000*Hj/Wj)}); jpgs.append((tp[:-4] + '.png', base + '.jpg'))
# web icons
def sq(size, bg=ESPRESSO, fg=CREAM, frac=0.72, rx=0):
    sw = size*frac; sh = SH*sw/SW
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}"><rect width="{size}" height="{size}" rx="{rx}" fill="{bg}"/>{symbol(fg, (size - sw)/2, (size - sh)/2, sh)}</svg>'
I = f'{OUT}/03_Web-icones_Web-icons'
for n, s in [('favicon-16', sq(16, frac=0.92, rx=3)), ('favicon-32', sq(32, frac=0.88, rx=6)), ('favicon-48', sq(48, frac=0.86, rx=8)), ('apple-touch-icon-180', sq(180)), ('android-chrome-192', sq(192)),
             ('android-chrome-512', sq(512)), ('app-icon-1024', sq(1024)), ('profile-picture-1080-espresso', sq(1080, frac=0.66)), ('profile-picture-1080-rust', sq(1080, RUST, CREAM, 0.66)), ('profile-picture-1080-cream', sq(1080, CREAM, ESPRESSO, 0.66))]:
    p = f'{I}/vintage-wave-{n}'; w(p + '.svg', s); px = int(n.split('-')[-1]) if n.split('-')[-1].isdigit() else int(n.split('-')[-2])
    jobs.append({'type': 'png', 'svg': p + '.svg', 'out': p + '.png', 'w': px, 'h': px})
w(f'{I}/favicon.svg', sq(64, frac=0.88, rx=12))
json.dump(jobs, open('jobs_logo.json', 'w')); json.dump(jpgs, open('jpgs_logo.json', 'w')); print(len(jobs))
