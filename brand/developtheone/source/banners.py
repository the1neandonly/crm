import os, sys, json
from kit import *
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/banners'); os.makedirs(HT, exist_ok=True)
jobs = []
CSS = '''.f{position:relative;overflow:hidden}.ink{background:var(--ink);color:#fff}.grad{background:var(--grad);color:#fff}.paper{background:var(--paper);color:var(--ink)}
.a{position:absolute}.big{font-family:Montserrat;font-weight:700;letter-spacing:-.03em;line-height:1}.hl{color:var(--lime)}
.lbl{font-weight:700;letter-spacing:.24em;text-transform:uppercase}.sub{font-weight:500}
.cta{background:var(--lime);color:var(--ink);border-radius:999px;font-weight:800;white-space:nowrap;display:inline-flex;align-items:center;justify-content:center}'''
def emit(folder, name, w, h, cls, body, unit='px', kinds=('png', 'jpg'), scale=1):
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(f'<div class="f {cls}" style="width:{w}{unit};height:{h}{unit}">{body}</div>', CSS, f'{w}{unit} {h}{unit}'))
    for k in kinds:
        ext = {'png': 'png', 'jpg': 'jpg', 'pdf': 'pdf'}[k]
        jobs.append(dict(html=p, type=k, out=f'{OUT}/banners/{folder}/{name}.{ext}', w=w, h=h, unit=unit, scale=scale))
A = lambda inner, st: f'<div class="a" style="{st}">{inner}</div>'
bm = lambda h, st, body='grad': mark_svg(body=body, height=h, style=st)

# ---------- Social headers (key content inside the centre safe zones)
emit('social-headers', 'linkedin-personal-1584x396', 1584, 396, 'ink',
     bm(620, 'position:absolute;right:-60px;top:-40px') +
     A(f'<div class="big" style="font-size:84px">Become <span class="hl">the one.</span></div><div class="sub" style="margin-top:20px;font-size:24px;color:rgba(255,255,255,.66)">Digital marketing agency — {CITY}</div>', 'left:420px;top:110px'))
emit('social-headers', 'linkedin-company-1128x191', 1128, 191, 'ink',
     bm(300, 'position:absolute;right:-20px;top:-30px') +
     A(f'<div class="big" style="font-size:46px">Become <span class="hl">the one.</span></div><div class="sub" style="margin-top:8px;font-size:16px;color:rgba(255,255,255,.6)">{TAG_FR} · {CITY}</div>', 'left:330px;top:52px'))
emit('social-headers', 'facebook-cover-1640x624', 1640, 624, 'grad',
     A(mark_svg(body='rgba(255,255,255,.10)', slice_c='rgba(255,255,255,.10)', height=1000), 'left:1180px;top:-60px') +
     A(f'<div style="text-align:center">{logo_svg("stacked","on-violet",width=520)}<div class="sub" style="margin-top:34px;font-size:28px;font-weight:600;color:rgba(255,255,255,.9)">{TAG_EN} &nbsp;<span class="hl">/</span>&nbsp; {TAG_FR}</div></div>', 'left:50%;top:50%;transform:translate(-50%,-50%)'))
emit('social-headers', 'x-twitter-header-1500x500', 1500, 500, 'ink',
     bm(700, 'position:absolute;right:-40px;top:-60px') +
     A('<div class="big" style="font-size:96px">Become<br><span class="hl">the one.</span></div>', 'left:96px;top:140px'))
emit('social-headers', 'youtube-channel-art-2560x1440', 2560, 1440, 'ink',
     A(f'<div style="width:100%;height:100%;background:url(file://{OUT}/patterns/svg/dto-pattern-ink.svg) 0 0/960px 960px;opacity:.5"></div>', 'inset:0') +
     A('', 'left:507px;top:509px;width:1546px;height:423px;background:var(--ink);border-radius:30px') +
     A(f'<div style="display:flex;align-items:center;gap:70px">{logo_svg("horizontal","color-dark",width=720)}<div style="width:2px;height:150px;background:rgba(255,255,255,.2)"></div><div class="big" style="font-size:72px">Become<br><span class="hl">the one.</span></div></div>', 'left:50%;top:50%;transform:translate(-50%,-50%)'))
emit('social-headers', 'facebook-event-cover-1920x1005', 1920, 1005, 'grad',
     A('<div class="lbl hl" style="font-size:26px">Événement · Event</div><div class="big" style="font-size:120px;margin-top:24px">Nom de<br>l’événement</div><div class="sub" style="font-size:36px;margin-top:30px;color:rgba(255,255,255,.85)">00.00.2026 · Algérie</div>', 'left:140px;top:250px') +
     A(mark_svg(body='#fff', height=520), 'right:200px;top:240px'))

# ---------- Web
emit('web', 'website-hero-1920x800', 1920, 800, 'ink',
     bm(1100, 'position:absolute;right:-120px;top:-170px') +
     A(logo_svg('horizontal-compact', 'color-dark', width=240), 'left:140px;top:60px') +
     A(f'<div class="big" style="font-size:130px">Become<br><span class="hl">the one.</span></div><div class="sub" style="font-size:30px;margin-top:34px;color:rgba(255,255,255,.72);width:700px">Stratégie, identité, social media et publicité — pour les marques qui veulent être vues.</div><div class="cta" style="margin-top:46px;font-size:24px;padding:22px 44px">Parlons de votre projet →</div>', 'left:140px;top:200px'))
emit('web', 'email-header-1200x400', 1200, 400, 'grad',
     A(logo_svg('horizontal', 'on-violet', width=420), 'left:80px;top:80px') +
     A(f'<div class="sub" style="font-size:26px;color:rgba(255,255,255,.85)">{TAG_FR}</div>', 'left:80px;top:290px') +
     A(mark_svg(body='rgba(255,255,255,.12)', slice_c=LIME, height=520), 'right:-60px;top:-40px'))
emit('web', 'newsletter-footer-1200x300', 1200, 300, 'ink',
     A(logo_svg('horizontal-compact', 'color-dark', width=260), 'left:80px;top:80px') +
     A(f'<div class="sub" style="font-size:20px;line-height:1.8;color:rgba(255,255,255,.7)">{WEB} · {MAIL}<br>{INSTA} · {CITY}</div>', 'left:80px;top:170px') +
     A('<div class="big" style="font-size:52px;text-align:right">Become<br><span class="hl">the one.</span></div>', 'right:80px;top:80px'))
emit('web', 'blog-cover-1600x900', 1600, 900, 'paper',
     A('<div class="lbl" style="font-size:22px;color:var(--violet)">Blog · Article</div><div class="big" style="font-size:96px;margin-top:26px;width:1000px">Le titre de votre article sur deux lignes.</div>', 'left:120px;top:250px') +
     A('', 'right:-1px;bottom:-1px;width:520px;height:520px;background:var(--grad);border-top-left-radius:520px') +
     A('', 'right:180px;bottom:180px;width:160px;height:160px;background:var(--lime);border-top-left-radius:160px') +
     A(logo_svg('horizontal-compact', 'color', width=220), 'left:120px;bottom:90px'))

# ---------- Display ads (IAB sizes) — one responsive layout
HEAD, CTA = 'Votre marque mérite d’être vue.', 'Parlons-en'
for w, h in [(300, 250), (336, 280), (728, 90), (970, 250), (160, 600), (300, 600), (320, 50), (320, 100), (1200, 628), (1080, 1080)]:
    r = w / h; u = min(w, h)
    if r >= 3:        # leaderboard — size the headline to the space left between symbol and button
        cta_fs = min(h*0.19 if h < 120 else h*0.11, w*0.034)
        cta_w = len(CTA)*cta_fs*0.62 + 2*cta_fs*0.9
        left = h*0.22 + h*0.56*0.75 + h*0.25
        avail = w - left - cta_w - h*0.22 - h*0.3
        fs = min(h*0.34, avail/(len(HEAD)*0.6)); head = HEAD
        if fs < h*0.18:   # short banner: break the headline over two lines
            head = 'Votre marque mérite<br>d’être <span class="hl">vue.</span>'; fs = min(h*0.24, avail/(19*0.6))
        body = (A(mark_svg(height=h*0.56), f'left:{h*0.22}px;top:{h*0.22}px') +
                A(f'<div class="big" style="font-size:{fs}px;white-space:nowrap;line-height:1.05">{head}</div>', f'left:{left}px;top:50%;transform:translateY(-50%)') +
                A(f'<div class="cta" style="font-size:{cta_fs}px;padding:{cta_fs*0.6}px {cta_fs*0.9}px">{CTA}</div>', f'right:{h*0.22}px;top:50%;transform:translateY(-50%)'))
    elif r <= 0.6:    # skyscraper
        body = (A(logo_svg('horizontal-compact', 'color-dark', width=w*0.62), f'left:{w*0.12}px;top:{w*0.14}px') +
                A(f'<div class="big" style="font-size:{w*0.15}px">Votre marque mérite d’être <span class="hl">vue.</span></div>', f'left:{w*0.12}px;right:{w*0.1}px;top:{h*0.18}px') +
                A(bm(h*0.42, ''), f'right:{-w*0.25}px;bottom:{h*0.1}px') +
                A(f'<div class="cta" style="font-size:{w*0.085}px;padding:{w*0.06}px {w*0.1}px">{CTA}</div>', f'left:{w*0.12}px;bottom:{w*0.12}px'))
    else:             # rectangle / square / landscape
        body = (A(bm(h*0.9, ''), f'right:{-h*0.18}px;bottom:{-h*0.18}px') +
                A(logo_svg('horizontal-compact', 'color-dark', width=u*0.42), f'left:{u*0.08}px;top:{u*0.08}px') +
                A(f'<div class="big" style="font-size:{u*0.105}px">Votre marque<br>mérite d’être <span class="hl">vue.</span></div>', f'left:{u*0.08}px;top:{h*0.34}px') +
                A(f'<div class="cta" style="font-size:{u*0.05}px;padding:{u*0.035}px {u*0.07}px">{CTA}</div>', f'left:{u*0.08}px;bottom:{u*0.08}px'))
    emit('display-ads', f'ad-{w}x{h}', w, h, 'ink', body, scale=2 if u < 400 else 1)

# ---------- Large format print (vector PDF)
rb = (A(logo_svg('horizontal', 'color-dark', width='620mm'), 'left:115mm;top:160mm') +
      A('<div class="big" style="font-size:185mm;line-height:.95">Become<br><span class="hl">the one.</span></div>', 'left:110mm;top:500mm') +
      A(f'<div class="sub" style="font-size:44mm;color:rgba(255,255,255,.75);width:640mm">{TAG_FR}</div>', 'left:115mm;top:930mm') +
      A(mark_svg(height='900mm'), 'right:-260mm;top:1080mm') +
      A(f'<div class="sub" style="font-size:34mm;font-weight:700;line-height:1.6">{WEB}<br>{INSTA}</div>', 'left:115mm;top:1760mm'))
emit('print', 'rollup-850x2000mm-bleed5mm', 860, 2010, 'ink', rb, 'mm', ('pdf', 'png'), scale=0.4)
bb = (A(mark_svg(height='340mm'), 'right:-70mm;top:-10mm') +
      A('<div class="big" style="font-size:56mm;line-height:.95">Become<br><span class="hl">the one.</span></div>', 'left:28mm;top:45mm') +
      A(f'<div class="sub" style="font-size:11mm;color:rgba(255,255,255,.75)">{TAG_FR}</div>', 'left:30mm;top:170mm') +
      A(logo_svg('horizontal-compact', 'color-dark', width='120mm'), 'left:30mm;top:245mm'))
emit('print', 'billboard-4x3m-scale-1-10', 400, 300, 'ink', bb, 'mm', ('pdf', 'png'), scale=1.4)
emit('print', 'poster-A3-297x420mm-bleed3mm', 303, 426, 'grad',
     A(logo_svg('stacked', 'on-violet', width='150mm'), 'left:50%;top:70mm;transform:translateX(-50%)') +
     A('<div class="big" style="font-size:40mm;text-align:center">Become <span class="hl">the one.</span></div>', 'left:0;right:0;top:250mm') +
     A(f'<div class="sub" style="font-size:9mm;text-align:center;color:rgba(255,255,255,.85)">{TAG_FR} · {WEB}</div>', 'left:0;right:0;top:300mm'), 'mm', ('pdf', 'png'))
json.dump(jobs, open('jobs_banners.json', 'w')); print(len(jobs))
