"""Photoreal-ish CSS/SVG mockup scenes of every application (2400x1600)."""
import os, sys, json
from kit import *
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/mockups'); os.makedirs(HT, exist_ok=True)
PV = json.load(open('previews_print.json')); jobs = []
pv = lambda k: 'file://' + PV[k]
F = lambda p: 'file://' + os.path.join(OUT, p)
SW, SH = 2400, 1600
CSS = '''.sc{position:relative;overflow:hidden;width:2400px;height:1600px}
.a{position:absolute}.sh{box-shadow:0 70px 120px -30px rgba(18,14,40,.55),0 24px 40px -12px rgba(18,14,40,.35)}
.shs{box-shadow:0 30px 60px -16px rgba(18,14,40,.45),0 8px 16px -6px rgba(18,14,40,.3)}
.trim{overflow:hidden;position:absolute}.trim img{position:absolute;display:block}
.sheen::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.22) 0%,rgba(255,255,255,0) 38%,rgba(255,255,255,0) 70%,rgba(255,255,255,.08) 100%);pointer-events:none;border-radius:inherit}
.lbl{font:700 22px Manrope;letter-spacing:.24em;text-transform:uppercase}
.big{font-family:Syne;font-weight:700;letter-spacing:-.03em}'''
def scene(name, bg, body, caption=None, dark=False):
    cap = (f'<div class="a lbl" style="left:80px;bottom:60px;color:{"rgba(255,255,255,.5)" if dark else "rgba(27,16,70,.45)"}">{caption}</div>'
           f'<div class="a" style="right:80px;bottom:52px;opacity:.6">{logo_svg("horizontal-compact", "white" if dark else "black", width=150)}</div>') if caption else ''
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(f'<div class="sc" style="background:{bg}">{body}{cap}</div>', CSS, f'{SW}px {SH}px'))
    for k in ('png', 'jpg'): jobs.append(dict(html=p, type=k, out=f'{OUT}/mockups/{name}.{k}', w=SW, h=SH, unit='px', scale=1))
def trim(key, wmm, hmm, bmm, wpx, style='', cls='sh', radius=0):
    k = wpx / wmm
    return (f'<div class="trim {cls} sheen" style="width:{wpx}px;height:{hmm*k}px;border-radius:{radius}px;{style}">'
            f'<img src="{pv(key)}" style="width:{(wmm+2*bmm)*k}px;left:{-bmm*k}px;top:{-bmm*k}px"></div>')
PAPER = 'radial-gradient(ellipse at 30% 20%,#F7F6FB 0%,#E4E1EE 70%,#D6D2E3 100%)'
INKBG = 'radial-gradient(ellipse at 30% 20%,#2D2066 0%,#1B1046 60%,#1A1A20 100%)'
STUDIO = 'linear-gradient(180deg,#ECEAF3 0%,#DCD8E8 62%,#CFCADD 62.1%,#C5C0D6 100%)'

# 1 Business cards
scene('01-business-cards', PAPER,
      trim('business-card-85x55-bleed3mm-2', 85, 55, 3, 900, 'left:1180px;top:520px;transform:rotate(-10deg)') +
      trim('business-card-85x55-bleed3mm-1', 85, 55, 3, 900, 'left:330px;top:300px;transform:rotate(6deg)') +
      trim('business-card-gradient-85x55-bleed3mm-1', 85, 55, 3, 640, 'left:420px;top:1000px;transform:rotate(-4deg)') +
      trim('business-card-arabic-85x55-bleed3mm-2', 85, 55, 3, 640, 'left:1500px;top:110px;transform:rotate(12deg)'), 'Business cards · Cartes de visite')
# 2 NFC card + phone
def phone(inner, w=560, style=''):
    h = w*2.06
    return (f'<div class="a sh" style="width:{w}px;height:{h}px;border-radius:{w*0.16}px;background:#0E0E12;padding:{w*0.035}px;{style}">'
            f'<div style="width:100%;height:100%;border-radius:{w*0.13}px;overflow:hidden;position:relative;background:#fff">{inner}'
            f'<div style="position:absolute;left:50%;top:{w*0.03}px;width:{w*0.3}px;height:{w*0.075}px;border-radius:99px;background:#0E0E12;transform:translateX(-50%)"></div></div></div>')
contact = (f'<div style="height:100%;background:var(--grad);padding:180px 50px 0;color:#fff;font-family:Manrope">'
           f'<div style="width:150px;height:150px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center">{mark_svg(height=80)}</div>'
           f'<div class="big" style="font-size:52px;margin-top:40px">{NAME}</div><div style="font-size:24px;font-weight:700;color:var(--lime);margin-top:8px">{ROLE}</div>'
           + ''.join(f'<div style="margin-top:{40 if i==0 else 18}px;background:rgba(255,255,255,.14);border-radius:24px;padding:24px 28px;font-size:24px;font-weight:600">{t}</div>' for i, t in enumerate([PHONE, MAIL, WEB, 'Enregistrer le contact'])) + '</div>')
scene('02-nfc-card', INKBG,
      phone(contact, 560, 'left:1380px;top:180px;transform:rotate(6deg)') +
      trim('nfc-card-CR80-85.6x54-bleed2mm-1', 85.6, 54, 2, 860, 'left:420px;top:560px;transform:rotate(-14deg)', radius=40) +
      trim('nfc-card-CR80-85.6x54-bleed2mm-2', 85.6, 54, 2, 640, 'left:300px;top:180px;transform:rotate(8deg)', radius=30) +
      ''.join(f'<div class="a" style="left:{1200 + i*40}px;top:{720 - i*40}px;width:{120 + i*80}px;height:{120 + i*80}px;border:5px solid rgba(210,255,90,{.6 - i*.15});border-radius:50%;border-left-color:transparent;border-bottom-color:transparent;transform:rotate(45deg)"></div>' for i in range(3)),
      'NFC card · Carte NFC — tap to connect', True)
# 3 Thank-you card set
scene('03-thank-you-card', PAPER,
      trim('envelope-DL-220x110-1', 220, 110, 0, 1300, 'left:820px;top:820px;transform:rotate(-6deg)') +
      trim('thank-you-card-A6-bleed3mm-2', 105, 148, 3, 620, 'left:1360px;top:200px;transform:rotate(9deg)') +
      trim('thank-you-card-A6-bleed3mm-1', 105, 148, 3, 640, 'left:540px;top:150px;transform:rotate(-5deg)') +
      trim('thank-you-tag-50x90mm-bleed3mm-1', 50, 90, 3, 260, 'left:260px;top:900px;transform:rotate(-18deg)', radius=8), 'Thank-you card · Carte de remerciement')
# 4 Packaging box (CSS 3D)
def box3d(x, y, s, ry, rx, extra=''):
    W_, D_, H_ = 600*s, 440*s, 160*s
    face = lambda w, h, tf, inner: f'<div style="position:absolute;left:{(W_-w)/2}px;top:{(H_-h)/2}px;width:{w}px;height:{h}px;transform:{tf};backface-visibility:hidden;overflow:hidden">{inner}</div>'
    img = lambda key, w, h, b=3, wmm=300, hmm=220: f'<img src="{pv(key)}" style="position:absolute;width:{(wmm+2*b)*w/wmm}px;left:{-b*w/wmm}px;top:{-b*h/hmm}px">'
    shade = lambda a: f'<div style="position:absolute;inset:0;background:rgba(10,8,25,{a})"></div>'
    return (f'<div class="a" style="left:{x}px;top:{y}px;width:{W_}px;height:{H_}px;perspective:4000px">'
            f'<div style="position:absolute;inset:0;transform-style:preserve-3d;transform:rotateX({rx}deg) rotateY({ry}deg)">'
            + face(W_, D_, f'rotateX(90deg) translateZ({H_/2}px)', img('mailer-box-lid-300x220mm-1', W_, D_) + extra)
            + face(W_, H_, f'translateZ({D_/2}px)', img('mailer-box-side-300x80mm-1', W_, H_, 3, 300, 80) + shade(.08))
            + face(D_, H_, f'rotateY(90deg) translateZ({W_/2}px)', f'<div style="position:absolute;inset:0;background:var(--violet)"></div>' + shade(.35))
            + face(D_, H_, f'rotateY(-90deg) translateZ({W_/2}px)', f'<div style="position:absolute;inset:0;background:var(--violet)"></div>' + shade(.2))
            + '</div></div>'
            f'<div class="a" style="left:{x - 60*s}px;top:{y + H_ + 40*s}px;width:{W_*1.2}px;height:{140*s}px;border-radius:50%;background:radial-gradient(ellipse,rgba(20,16,40,.4),rgba(20,16,40,0) 70%);filter:blur(10px);z-index:-1"></div>')
tape = f'<div style="position:absolute;left:44%;top:-5%;width:12%;height:110%;overflow:hidden;opacity:.95"><img src="{pv("packing-tape-50mm-repeat-500mm-1")}" style="height:100%;transform:rotate(90deg) translateY(-100%);transform-origin:0 0;width:auto"></div>'
scene('04-packaging-box', STUDIO,
      f'<div class="a" style="left:0;right:0;bottom:0;height:610px;background:linear-gradient(180deg,#CBC6DA,#BDB7D0)"></div>' +
      box3d(1120, 760, 1.25, -32, -24) + box3d(380, 980, 0.95, 28, -24) +
      trim('sticker-symbol-60mm-round-1', 60, 60, 2, 200, 'left:520px;top:600px;transform:rotate(-12deg)', 'shs', 100) +
      trim('paper-bag-front-260x330mm-1', 260, 330, 3, 420, 'left:1880px;top:520px;transform:rotate(3deg)'), 'Packaging · Emballage')
# 5 Stationery flat-lay (ink surface)
pen = '<div class="a shs" style="left:1960px;top:300px;width:28px;height:820px;border-radius:14px;background:linear-gradient(90deg,#3a3a45,#1B1046 40%,#4a4a55);transform:rotate(14deg)"><div style="position:absolute;left:0;right:0;top:0;height:140px;background:var(--violet);border-radius:14px 14px 0 0"></div><div style="position:absolute;left:4px;right:4px;top:150px;height:6px;background:var(--lime)"></div></div>'
scene('05-stationery-flatlay', INKBG,
      trim('letterhead-A4-1', 210, 297, 0, 760, 'left:240px;top:120px;transform:rotate(-4deg)') +
      trim('invoice-facture-A4-1', 210, 297, 0, 700, 'left:640px;top:330px;transform:rotate(5deg)') +
      trim('notebook-A5-cover-bleed3mm-1', 148, 210, 3, 560, 'left:1430px;top:180px;transform:rotate(-8deg)', radius=12) +
      trim('envelope-DL-220x110-1', 220, 110, 0, 900, 'left:1250px;top:1050px;transform:rotate(4deg)') +
      trim('business-card-85x55-bleed3mm-1', 85, 55, 3, 480, 'left:1500px;top:820px;transform:rotate(-14deg)') +
      trim('business-card-85x55-bleed3mm-2', 85, 55, 3, 480, 'left:1820px;top:900px;transform:rotate(9deg)') +
      trim('sticker-darija-80x40mm-1', 80, 40, 2, 300, 'left:300px;top:1250px;transform:rotate(-8deg)', 'shs', 24) + pen, 'Stationery · Papeterie', True)
# 6 Merch: tee, tote, mug, cap-less
tee_path = 'M300,60 L420,20 Q500,90 580,20 L700,60 L880,200 L800,330 L720,280 L720,900 Q500,930 280,900 L280,280 L200,330 L120,200 Z'
tee = (f'<svg class="a" style="left:120px;top:250px;filter:drop-shadow(0 50px 50px rgba(18,14,40,.4))" width="1000" height="1000" viewBox="0 0 1000 950">'
       f'<defs><linearGradient id="ts" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset=".25" stop-color="#000" stop-opacity="0"/><stop offset=".75" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".3"/></linearGradient></defs>'
       f'<path d="{tee_path}" fill="#1B1046"/><path d="{tee_path}" fill="url(#ts)"/><path d="M420,20 Q500,90 580,20 Q500,60 420,20Z" fill="#111"/>'
       f'<g transform="translate(395,230) scale(0.55)">{mark_paths("url(#tg)", LIME)}</g><defs>{grad_def("tg")}</defs>'
       f'<text x="500" y="420" fill="#fff" font-family="Syne" font-weight="700" font-size="44" text-anchor="middle" letter-spacing="-1">beyna</text></svg>')
tote = (f'<div class="a" style="left:1080px;top:380px;width:560px;height:640px">'
        f'<div style="position:absolute;left:120px;top:-200px;width:320px;height:320px;border:22px solid #E8E2CF;border-bottom:none;border-radius:200px 200px 0 0"></div>'
        f'<div class="sh" style="position:absolute;inset:0;background:#EFEADB;border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px">'
        f'{mark_svg(body=INK, slice_c=VIOLET, height=230)}<div class="big" style="font-size:44px;color:var(--ink)">Make it clear.</div></div></div>')
mug = (f'<svg class="a" style="left:1720px;top:600px;filter:drop-shadow(0 40px 40px rgba(18,14,40,.4))" width="560" height="560" viewBox="0 0 560 560">'
       f'<defs><linearGradient id="ms" x1="0" x2="1"><stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset=".3" stop-color="#fff" stop-opacity=".12"/><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".4"/></linearGradient>{grad_def("mg")}</defs>'
       f'<path d="M360,170 h40 a90,90 0 0 1 0,180 h-40" fill="none" stroke="#6337FF" stroke-width="40"/>'
       f'<path d="M60,90 H380 V440 Q380,500 320,500 H120 Q60,500 60,440 Z" fill="url(#mg)"/><path d="M60,90 H380 V440 Q380,500 320,500 H120 Q60,500 60,440 Z" fill="url(#ms)"/>'
       f'<ellipse cx="220" cy="90" rx="160" ry="22" fill="#4a2be0"/><ellipse cx="220" cy="90" rx="146" ry="16" fill="#1B1046"/>'
       f'<g transform="translate(160,190) scale(0.62)">{mark_paths("#fff", LIME)}</g></svg>')
scene('06-merch', STUDIO, f'<div class="a" style="left:0;right:0;bottom:0;height:610px;background:linear-gradient(180deg,#CBC6DA,#BDB7D0)"></div>' + tee + tote + mug, 'Merch · T-shirt, tote bag, mug')
# 7 Badge + lanyard
scene('07-badge-lanyard', PAPER,
      f'<div class="a" style="left:1050px;top:-40px;width:70px;height:640px;overflow:hidden;transform:rotate(-8deg)"><img src="{pv("lanyard-20x450mm-1")}" style="height:70px;transform:rotate(90deg) translateY(-70px);transform-origin:0 0"></div>' +
      f'<div class="a" style="left:1270px;top:-40px;width:70px;height:640px;overflow:hidden;transform:rotate(8deg)"><img src="{pv("lanyard-20x450mm-1")}" style="height:70px;transform:rotate(90deg) translateY(-70px);transform-origin:0 0"></div>' +
      '<div class="a" style="left:1150px;top:560px;width:90px;height:60px;border-radius:12px;background:#9a9aa6"></div>' +
      trim('staff-badge-54x85.6mm-bleed2mm-1', 54, 85.6, 2, 560, 'left:915px;top:600px', radius=30) +
      trim('business-card-gradient-85x55-bleed3mm-2', 85, 55, 3, 560, 'left:220px;top:900px;transform:rotate(-10deg)') +
      trim('sticker-make-it-clear-70mm-round-1', 70, 70, 2, 280, 'left:1700px;top:1040px;transform:rotate(10deg)', 'shs', 140), 'Staff badge · Badge & lanyard')
# 8 Office signage
scene('08-office-signage', 'linear-gradient(180deg,#F1F0F5 0%,#E3E1EA 74%,#B9B4C6 74.1%,#A9A3B9 100%)',
      '<div class="a" style="left:0;right:0;top:0;height:1184px;background:repeating-linear-gradient(90deg,rgba(0,0,0,.015) 0 2px,transparent 2px 240px)"></div>' +
      trim('office-sign-1200x400mm-1', 1200, 400, 0, 1400, 'left:500px;top:300px;box-shadow:0 40px 60px -20px rgba(18,14,40,.5)', '') +
      ''.join(f'<div class="a" style="left:{x}px;top:{y}px;width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,#9a9aa6)"></div>' for x, y in [(530, 330), (1868, 330), (530, 728), (1868, 728)]) +
      '<div class="a" style="left:300px;top:880px;width:180px;height:300px;border-radius:20px 20px 0 0;background:linear-gradient(180deg,#3a3a45,#1B1046)"></div><div class="a" style="left:240px;top:560px;width:300px;height:340px;border-radius:50% 50% 40% 40%;background:radial-gradient(circle at 40% 30%,#6b8f4e,#2f4a26)"></div>',
      'Signage · Signalétique bureau')
# 9 Storefront
scene('09-storefront', 'linear-gradient(180deg,#BFD3EA 0%,#E6EEF7 40%)',
      '<div class="a" style="left:0;right:0;top:260px;bottom:0;background:#E9E4DA"></div>' +
      trim('storefront-fascia-3000x600mm-1', 3000, 600, 0, 2000, 'left:200px;top:340px;box-shadow:0 30px 40px -20px rgba(0,0,0,.4)', '') +
      '<div class="a" style="left:200px;top:740px;width:2000px;height:720px;background:linear-gradient(135deg,rgba(40,44,60,.92),rgba(70,80,100,.85));"></div>' +
      ''.join(f'<div class="a" style="left:{200 + i*500}px;top:740px;width:14px;height:720px;background:#1a1a20"></div>' for i in range(5)) +
      trim('door-vinyl-hours-400x300mm-1', 400, 300, 0, 300, 'left:1310px;top:900px;opacity:.95', '') +
      '<div class="a" style="left:0;right:0;top:1460px;bottom:0;background:#8f8a82"></div>', 'Storefront · Façade')
# 10 Roll-up + billboard
rollup = (f'<div class="a" style="left:300px;top:110px;width:470px;height:1270px;overflow:hidden;box-shadow:0 40px 60px -20px rgba(18,14,40,.5)"><img src="{F("banners/print/rollup-850x2000mm-bleed5mm.png")}" style="width:100%"></div>'
          '<div class="a" style="left:270px;top:1370px;width:530px;height:60px;border-radius:10px;background:linear-gradient(180deg,#c8c8d0,#8a8a96)"></div>')
bill = (f'<div class="a" style="left:1050px;top:160px;width:1200px;height:900px;padding:22px;background:#1a1a20;box-shadow:0 40px 60px -20px rgba(18,14,40,.6)"><img src="{F("banners/print/billboard-4x3m-scale-1-10.png")}" style="width:100%;height:100%;display:block"></div>'
        '<div class="a" style="left:1610px;top:1080px;width:80px;height:520px;background:linear-gradient(90deg,#55555f,#1B1046)"></div>')
scene('10-rollup-billboard', 'linear-gradient(180deg,#C9D9EC 0%,#EEF1F7 70%,#B9B4C6 70.1%,#A9A3B9 100%)', rollup + bill, 'Roll-up & billboard · Kakémono & affichage')
# 11 Phone: Instagram profile + story
posts = sorted(os.listdir(f'{OUT}/social/instagram-posts')); posts = [p for p in posts if p.endswith('.png')][:9]
grid = ''.join(f'<img src="{F("social/instagram-posts/" + p)}" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">' for p in posts)
ig = (f'<div style="padding:110px 30px 0;font-family:Manrope;color:#111"><div style="display:flex;align-items:center;gap:30px">'
      f'<img src="{F("icons/png/avatar-gradient-400.png")}" style="width:150px;height:150px;border-radius:50%">'
      f'<div style="display:flex;gap:30px;text-align:center;font-size:22px"><div><b style="font-size:30px">128</b><br>posts</div><div><b style="font-size:30px">12,4k</b><br>abonnés</div><div><b style="font-size:30px">310</b><br>suivis</div></div></div>'
      f'<div style="margin-top:20px;font-size:24px;font-weight:800">Beyna Agency · باينة</div><div style="font-size:21px;line-height:1.45;color:#333">Marketing &amp; communication · Oran 🇩🇿<br>Make it clear. — {WEB}</div>'
      f'<div style="display:flex;gap:16px;margin:26px 0">' + ''.join(f'<div style="flex:none;width:96px;text-align:center;font-size:16px"><img src="{F(f"social/instagram-highlight-covers/highlight-{n}-gradient.png")}" style="width:96px;height:96px;border-radius:50%;object-fit:cover;border:3px solid #ddd"><br>{n.title()}</div>' for n in ['about', 'services', 'work', 'clients']) +
      f'</div></div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px">{grid}</div>')
story = f'<img src="{F("social/instagram-stories/04-link.png")}" style="width:100%;height:100%;object-fit:cover">'
scene('11-instagram-phone', 'linear-gradient(135deg,#9A7CFF,#6337FF 55%,#2B1BB5)',
      phone(ig, 620, 'left:620px;top:120px;transform:rotate(-4deg)') + phone(story, 560, 'left:1340px;top:220px;transform:rotate(5deg)'), 'Social media · Instagram', True)
# 12 Laptop website
site = f'<img src="{F("banners/web/website-hero-1920x800.png")}" style="width:100%;display:block"><div style="background:#F5F4F9;height:600px;padding:50px 70px;display:grid;grid-template-columns:repeat(4,1fr);gap:30px">' + ''.join(f'<div style="background:#fff;border-radius:24px;padding:30px"><img src="{F(f"icons/service-icons/png/violet/beyna-icon-{ic}-512.png")}" style="width:70px"><div class="big" style="font-size:30px;margin-top:20px;color:#1B1046">{t}</div></div>' for ic, t in [('strategy', 'Stratégie'), ('branding', 'Identité'), ('social', 'Social media'), ('analytics', 'Data')]) + '</div>'
laptop = (f'<div class="a" style="left:400px;top:170px;width:1600px;height:1010px;border-radius:40px 40px 0 0;background:#0E0E12;padding:34px 34px 50px;box-shadow:0 60px 100px -30px rgba(18,14,40,.6)"><div style="width:100%;height:100%;overflow:hidden;border-radius:8px;background:#fff">{site}</div></div>'
          '<div class="a" style="left:250px;top:1180px;width:1900px;height:56px;border-radius:0 0 40px 40px;background:linear-gradient(180deg,#d7d7de,#9c9ca8)"></div>'
          '<div class="a" style="left:1080px;top:1180px;width:240px;height:18px;border-radius:0 0 16px 16px;background:#8a8a96"></div>')
scene('12-website-laptop', STUDIO, laptop, 'Website · Site web')
# 13 Stickers & NFC tag scattered
stk = ''.join(trim(k, w, h, b, px, st, 'shs', r) for k, w, h, b, px, st, r in [
    ('sticker-symbol-60mm-round-1', 60, 60, 2, 420, 'left:300px;top:260px;transform:rotate(-10deg)', 210),
    ('sticker-darija-80x40mm-1', 80, 40, 2, 620, 'left:900px;top:220px;transform:rotate(6deg)', 40),
    ('sticker-logo-90x30mm-1', 90, 30, 2, 700, 'left:1560px;top:380px;transform:rotate(-5deg)', 30),
    ('sticker-make-it-clear-70mm-round-1', 70, 70, 2, 460, 'left:520px;top:860px;transform:rotate(12deg)', 230),
    ('nfc-tag-sticker-30mm-round-1', 30, 30, 3, 300, 'left:1180px;top:820px;transform:rotate(-8deg)', 150),
    ('sticker-symbol-60mm-round-1', 60, 60, 2, 300, 'left:1640px;top:900px;transform:rotate(20deg)', 150)])
scene('13-stickers', 'radial-gradient(ellipse at 30% 20%,#E9FF9E 0%,#D2FF5A 60%,#BDE84A 100%)', stk, 'Stickers & NFC tag')
# 14 Wall mural / reception
scene('14-wall-mural', '#E8E6EE',
      f'<div class="a" style="left:0;right:0;top:0;height:1200px;overflow:hidden"><img src="{pv("wall-mural-3000x2000mm-1")}" style="width:100%"></div>' +
      '<div class="a" style="left:0;right:0;top:1200px;bottom:0;background:linear-gradient(180deg,#8d8799,#77718a)"></div>' +
      '<div class="a" style="left:700px;top:980px;width:1000px;height:300px;border-radius:24px 24px 0 0;background:linear-gradient(180deg,#2A1D63,#1a1a20);box-shadow:0 40px 60px -20px rgba(0,0,0,.5)"></div>' +
      f'<div class="a" style="left:1080px;top:1060px;opacity:.9">{logo_svg("horizontal-compact", "color-dark", width=240)}</div>', 'Reception wall · Accueil', True)
json.dump(jobs, open('jobs_mockups.json', 'w')); print(len(jobs))
