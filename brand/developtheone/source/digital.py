import os, sys, json
from kit import *
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/digital'); os.makedirs(HT, exist_ok=True)
jobs = []
CSS = '''.f{position:relative;overflow:hidden}.ink{background:var(--ink);color:#fff}.grad{background:var(--grad);color:#fff}.white{background:#fff}.clear{background:transparent}
.a{position:absolute}.big{font-family:Montserrat;font-weight:700;letter-spacing:-.03em;line-height:1}.hl{color:var(--lime)}'''
def emit(folder, name, w, h, cls, body, kinds=('png',), scale=1):
    p = f'{HT}/{name}.html'; open(p, 'w').write(page_doc(f'<div class="f {cls}" style="width:{w}px;height:{h}px">{body}</div>', CSS, f'{w}px {h}px'))
    for k in kinds: jobs.append(dict(html=p, type=k, out=f'{OUT}/{folder}/{name}.{k}', w=w, h=h, unit='px', scale=scale, alpha=(cls == 'clear')))
A = lambda i, s: f'<div class="a" style="{s}">{i}</div>'
emit('video/stills', 'youtube-thumbnail-template-1280x720', 1280, 720, 'ink',
     A('<div style="font:700 30px Inter;letter-spacing:.24em;text-transform:uppercase;color:var(--lime)">Épisode 01</div><div class="big" style="font-size:118px;margin-top:20px">Titre<br>de la <span class="hl">vidéo.</span></div>', 'left:70px;top:150px') +
     A('<div style="width:500px;height:560px;border-radius:40px;border:4px dashed rgba(255,255,255,.3);display:flex;align-items:center;justify-content:center;font:600 24px Inter;color:rgba(255,255,255,.45)">PHOTO / VISAGE</div>', 'right:70px;top:80px') +
     A(logo_svg('horizontal-compact', 'color-dark', width=200), 'left:70px;bottom:60px'), ('png', 'jpg'))
emit('video/stills', 'watermark-logo-white-600', 600, 200, 'clear', A(logo_svg('horizontal-compact', 'white', width=560), 'left:20px;top:30px;opacity:.6'))
emit('video/stills', 'watermark-symbol-white-200', 200, 200, 'clear', A(mark_svg(body='#fff', slice_c='#fff', height=160), 'left:40px;top:20px;opacity:.6'))
emit('video/stills', 'story-frame-overlay-1080x1920', 1080, 1920, 'clear',
     A('', 'inset:28px;border:6px solid var(--lime);border-radius:48px') + A(logo_svg('horizontal-compact', 'color-dark', width=230), 'left:80px;top:260px') +
     A(f'<div style="background:var(--ink);color:#fff;font:700 28px Inter;padding:16px 30px;border-radius:999px">{INSTA}</div>', 'left:80px;bottom:330px'))
for lang in ('fr', 'ar'):
    rtl = lang == 'ar'
    nm, rl = ('الاسم واللقب', 'المؤسس والمدير الإبداعي') if rtl else (NAME, ROLE)
    emit('email-signature', f'email-signature-{lang}-600x180', 600, 180, 'white',
         f'<div style="display:flex;align-items:center;gap:24px;height:180px;padding:0 28px;{"flex-direction:row-reverse;text-align:right" if rtl else ""}">'
         f'<div style="width:96px;height:96px;border-radius:24px;background:var(--grad);display:flex;align-items:center;justify-content:center;flex:none">{mark_svg(body="#fff", height=54)}</div>'
         f'<div style="width:1px;height:96px;background:rgba(36,36,43,.12)"></div><div><div class="big" style="font-size:22px;color:var(--ink);{"font-family:Cairo" if rtl else ""}">{nm}</div>'
         f'<div style="font:700 12.5px {"Cairo" if rtl else "Inter"};color:var(--violet);margin:4px 0 12px">{rl} · DevelopTheOne</div>'
         f'<div style="font:500 12px/1.7 Inter;color:#4a4a55;direction:ltr">{PHONE} · {MAIL}<br><b style="color:var(--ink)">{WEB}</b> · {CITY}</div></div></div>', scale=2)
emit('presentation', 'presentation-cover-1920x1080', 1920, 1080, 'ink',
     A(mark_svg(height=1400), 'right:-300px;top:-160px') + A(logo_svg('horizontal-compact', 'color-dark', width=300), 'left:120px;top:100px') +
     A('<div style="font:700 22px Inter;letter-spacing:.24em;text-transform:uppercase;color:var(--lime)">Proposition commerciale</div><div class="big" style="font-size:120px;margin-top:26px">Titre de la<br>présentation.</div><div style="font:500 28px Inter;color:rgba(255,255,255,.7);margin-top:30px">Nom du client · Mois 2026</div>', 'left:120px;top:380px'), ('png', 'jpg'))
emit('presentation', 'presentation-section-1920x1080', 1920, 1080, 'grad',
     A('<div style="font:500 40px JetBrains Mono;color:var(--lime)">01</div><div class="big" style="font-size:150px;margin-top:20px">Titre de<br>section.</div>', 'left:120px;top:330px') + A(mark_svg(body='#fff', height=120), 'right:120px;bottom:100px'), ('png', 'jpg'))
emit('presentation', 'presentation-content-1920x1080', 1920, 1080, 'white',
     A(logo_svg('horizontal-compact', 'color', width=200), 'right:120px;top:80px') +
     A('<div style="font:700 20px Inter;letter-spacing:.24em;text-transform:uppercase;color:var(--violet)">Sous-titre</div><div class="big" style="font-size:80px;margin-top:20px;color:var(--ink)">Titre de la diapositive.</div><div style="font:400 28px/1.6 Inter;color:#4a4a55;margin-top:40px;width:900px">Zone de texte. Une idée par diapositive, des phrases courtes, un chiffre clé en lime sur fond sombre si nécessaire.</div>', 'left:120px;top:220px') +
     A('', 'right:-1px;bottom:-1px;width:360px;height:360px;background:var(--grad);border-top-left-radius:360px') + A('', 'right:120px;bottom:120px;width:110px;height:110px;background:var(--lime);border-top-left-radius:110px'), ('png', 'jpg'))
json.dump(jobs, open('jobs_digital.json', 'w')); print(len(jobs))
