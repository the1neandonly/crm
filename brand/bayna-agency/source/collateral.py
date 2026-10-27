import os, json, sys
from kit import *
OUT = sys.argv[1]; HT = os.path.abspath('html'); os.makedirs(HT, exist_ok=True)
jobs = []
def emit(name, body, css, w, h, unit='px', outs=()):
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(body, css, f'{w}{unit} {h}{unit}'))
    for kind, out, extra in outs:
        jobs.append(dict(html=p, type=kind, out=out, w=w, h=h, unit=unit, **extra))
    return p

NAME, ROLE = 'Prénom Nom', 'Founder & Creative Director'
PHONE, MAIL, WEB, CITY = '+213 (0) 555 00 00 00', 'hello@bayna.agency', 'bayna.agency', 'Oran, Algérie'
TAG_EN, TAG_FR = 'Proof, by design.', 'La preuve, par le design.'

# ------------------------------------------------------------------ Business card 85x55 + 3mm bleed
bc_css = '''.card{width:91mm;height:61mm;position:relative;overflow:hidden;page-break-after:always}
.front{background:var(--ink)} .back{background:#FBFAFE}
.front .logo{position:absolute;left:50%;top:50%;transform:translate(-50%,-60%)}
.front .glow{position:absolute;width:90mm;height:90mm;right:-48mm;bottom:-56mm;border-radius:50%;background:radial-gradient(circle,rgba(99,55,255,.55),rgba(99,55,255,0) 65%)}
.front .city{position:absolute;left:0;right:0;bottom:8mm;text-align:center;font-size:5.4pt;letter-spacing:.32em;color:rgba(255,255,255,.55);text-transform:uppercase;font-weight:600}
.back .name{position:absolute;left:8mm;top:9.5mm;font-family:Syne;font-weight:700;font-size:11pt;letter-spacing:-.01em}
.back .role{position:absolute;left:8mm;top:15.6mm;font-size:6.4pt;color:var(--violet);font-weight:600;letter-spacing:.02em}
.back .contact{position:absolute;left:8mm;bottom:9mm;font-size:6.4pt;line-height:1.75;font-weight:500}
.back .contact b{display:inline-block;width:4.2mm;color:var(--violet);font-weight:800;font-size:5.6pt}
.back .mk{position:absolute;right:8mm;top:9mm}
.back .bar{position:absolute;left:0;right:0;bottom:0;height:4.4mm;background:var(--grad)}
.back .bar i{position:absolute;right:8mm;top:0;bottom:0;width:4.4mm;background:var(--lime)}'''
def bc_front():
    return f'<div class="card front"><div class="glow"></div><div class="logo">{logo_svg("stacked","color-dark",width="36mm")}</div><div class="city">{CITY}</div></div>'
def bc_back():
    return (f'<div class="card back"><div class="name">{NAME}</div><div class="role">{ROLE}</div>'
            f'<div class="mk">{mark_svg(height="9mm")}</div>'
            f'<div class="contact"><b>T</b>{PHONE}<br><b>E</b>{MAIL}<br><b>W</b>{WEB}<br><b>A</b>{CITY}</div><div class="bar"><i></i></div></div>')
emit('business-card', bc_front() + bc_back(), bc_css, 91, 61, 'mm',
     [('pdf', f'{OUT}/stationery/business-card/Bayna-business-card-print-85x55mm-bleed3mm.pdf', {})])
emit('bc-front', bc_front(), bc_css, 91, 61, 'mm', [('png', f'{OUT}/stationery/business-card/business-card-front.png', {'scale': 4})])
emit('bc-back', bc_back(), bc_css, 91, 61, 'mm', [('png', f'{OUT}/stationery/business-card/business-card-back.png', {'scale': 4})])

# ------------------------------------------------------------------ Letterhead A4
lh_css = '''.a4{width:210mm;height:297mm;position:relative;overflow:hidden;background:#fff}
.hd{position:absolute;left:20mm;top:18mm}
.meta{position:absolute;right:20mm;top:19mm;text-align:right;font-size:7.6pt;line-height:1.7;color:#55555F}
.meta strong{color:var(--ink);font-weight:700}
.rule{position:absolute;left:20mm;right:20mm;top:42mm;height:.3mm;background:var(--line)}
.body{position:absolute;left:20mm;right:20mm;top:56mm;font-size:10pt;line-height:1.65;color:#3a3a44}
.body .date{color:#8a8a96;font-size:8.5pt;margin-bottom:12mm}
.ft{position:absolute;left:20mm;right:20mm;bottom:14mm;display:flex;justify-content:space-between;font-size:7pt;color:#8a8a96;letter-spacing:.04em}
.ft span b{color:var(--violet);font-weight:700}
.corner{position:absolute;right:-1px;bottom:-1px;width:44mm;height:44mm;background:var(--grad);border-top-left-radius:44mm;opacity:1}
.corner i{position:absolute;right:20mm;bottom:20mm;width:14mm;height:14mm;background:var(--lime);border-top-left-radius:14mm}
.ft{right:56mm}'''
lh = (f'<div class="a4"><div class="hd">{logo_svg("horizontal","color",width="54mm")}</div>'
      f'<div class="meta"><strong>Bayna Agency</strong><br>{CITY}<br>{PHONE}<br>{MAIL} · {WEB}</div><div class="rule"></div>'
      f'<div class="body"><div class="date">Oran, le __ / __ / ____</div></div>'
      f'<div class="ft"><span><b>Bayna Agency</b> — Marketing &amp; Communication</span><span>RC 00/00-0000000 · NIF 000000000000000</span></div>'
      f'<div class="corner"><i></i></div></div>')
emit('letterhead', lh, lh_css, 210, 297, 'mm', [('pdf', f'{OUT}/stationery/letterhead/Bayna-letterhead-A4.pdf', {}),
                                                ('png', f'{OUT}/stationery/letterhead/letterhead-A4-preview.png', {'scale': 2})])

# ------------------------------------------------------------------ Email signature 600x180 (@2x)
sig_css = '''.sig{width:600px;height:180px;background:#fff;display:flex;align-items:center;padding:0 28px;gap:24px}
.ic{width:96px;height:96px;border-radius:24px;background:var(--grad);display:flex;align-items:center;justify-content:center;flex:none}
.vl{width:1px;height:96px;background:var(--line)}
.n{font-family:Syne;font-weight:700;font-size:22px;letter-spacing:-.01em}
.r{font-size:12.5px;color:var(--violet);font-weight:700;margin:3px 0 12px}
.c{font-size:12px;line-height:1.7;color:#4a4a55;font-weight:500}.c b{color:var(--ink)}'''
sig = (f'<div class="sig"><div class="ic">{mark_svg(body="#fff", height="54")}</div><div class="vl"></div>'
       f'<div><div class="n">{NAME}</div><div class="r">{ROLE} · Bayna Agency</div>'
       f'<div class="c">{PHONE} &nbsp;·&nbsp; {MAIL}<br><b>{WEB}</b> &nbsp;·&nbsp; {CITY}</div></div></div>')
emit('email-signature', sig, sig_css, 600, 180, 'px', [('png', f'{OUT}/stationery/email-signature/email-signature-600x180@2x.png', {'scale': 2})])

# ------------------------------------------------------------------ Social
soc_css = '''.f{position:relative;overflow:hidden;width:100%;height:100%}
.ink{background:var(--ink);color:#fff}.grad{background:var(--grad);color:#fff}.paper{background:var(--paper)}
.big{font-family:Syne;font-weight:700;letter-spacing:-.025em;line-height:.95}
.hl{color:var(--lime)}
.lbl{font-weight:700;letter-spacing:.3em;text-transform:uppercase}
.abs{position:absolute}
.ghost{position:absolute;opacity:.10}
.pill{display:inline-block;border:2px solid currentColor;border-radius:999px;padding:.5em 1.2em;font-weight:700}'''
def social(name, w, h, body, cls='ink'):
    emit(f'social-{name}', f'<div class="f {cls}" style="width:{w}px;height:{h}px">{body}</div>', soc_css, w, h, 'px',
         [('png', f'{OUT}/social/{name}.png', {'scale': 1}), ('jpg', f'{OUT}/social/{name}.jpg', {'scale': 1})])

big_mark = lambda hgt, st, body='grad', sl=LIME: mark_svg(body=body, slice_c=sl, height=hgt, style=st)

social('linkedin-banner-1584x396', 1584, 396,
    f'{big_mark(620, "position:absolute;right:-60px;top:-40px")}'
    f'<div class="abs" style="left:330px;top:116px"><div class="big" style="font-size:80px">Proof, <span class="hl">by design.</span></div>'
    f'<div style="margin-top:22px;font-size:22px;color:rgba(255,255,255,.66);font-weight:500;letter-spacing:.02em">Marketing &amp; communication agency — {CITY}</div></div>')
social('facebook-cover-1640x624', 1640, 624,
    f'<div class="ghost" style="opacity:.09">{big_mark(1000, "position:absolute;left:1180px;top:-60px", body="#fff", sl="#fff")}</div>'
    f'<div class="abs" style="left:50%;top:50%;transform:translate(-50%,-58%);text-align:center">{logo_svg("horizontal","on-violet",width="620")}'
    f'<div style="margin-top:34px;font-size:26px;font-weight:600;letter-spacing:.04em;color:rgba(255,255,255,.85)">{TAG_EN} &nbsp;<span style="color:var(--lime)">/</span>&nbsp; {TAG_FR}</div></div>', cls='grad')
social('x-header-1500x500', 1500, 500,
    f'{big_mark(700, "position:absolute;right:-40px;top:-60px")}'
    f'<div class="abs" style="left:96px;top:150px"><div class="big" style="font-size:92px">Proof,<br><span class="hl">by design.</span></div></div>')
social('instagram-post-tagline-1080x1350', 1080, 1350,
    f'<div class="abs" style="left:88px;top:88px">{logo_svg("horizontal-compact","color-dark",width="300")}</div>'
    f'{big_mark(900, "position:absolute;right:-330px;bottom:-230px")}'
    f'<div class="abs" style="left:88px;top:420px"><div class="big" style="font-size:140px">Proof,<br><span class="hl">by<br>design.</span></div>'
    f'<div style="margin-top:44px;font-size:32px;color:rgba(255,255,255,.7);font-weight:500">{TAG_FR}</div></div>'
    f'<div class="abs lbl" style="left:88px;bottom:88px;font-size:20px;color:rgba(255,255,255,.55)">{CITY}</div>')
services = ['Stratégie de marque', 'Identité visuelle', 'Social media', 'Publicité digitale', 'Contenu &amp; vidéo', 'Data &amp; performance']
social('instagram-post-services-1080x1350', 1080, 1350,
    f'<div class="abs" style="left:88px;top:88px">{mark_svg(body="#fff", height="96")}</div>'
    f'<div class="abs lbl" style="right:88px;top:120px;font-size:20px;color:var(--lime)">Nos services</div>'
    f'<div class="abs" style="left:88px;right:88px;top:330px">' +
    ''.join(f'<div style="display:flex;align-items:baseline;gap:28px;padding:26px 0;border-top:2px solid rgba(255,255,255,.25)">'
            f'<span class="mono" style="font-size:22px;color:var(--lime)">0{i+1}</span><span class="big" style="font-size:58px;letter-spacing:-.015em">{s}</span></div>' for i, s in enumerate(services)) +
    f'</div><div class="abs" style="left:88px;bottom:88px;font-size:26px;font-weight:700">{WEB}</div>', cls='grad')
social('instagram-story-1080x1920', 1080, 1920,
    f'{big_mark(1200, "position:absolute;left:-180px;top:-120px")}'
    f'<div class="abs" style="left:96px;right:96px;top:1180px"><div class="big" style="font-size:132px">Let’s make<br>it <span class="hl">clear.</span></div>'
    f'<div style="margin-top:40px;font-size:34px;color:rgba(255,255,255,.7);font-weight:500">Parlons de votre marque.</div></div>'
    f'<div class="abs" style="left:96px;bottom:110px;right:96px;display:flex;justify-content:space-between;align-items:center">'
    f'{logo_svg("horizontal-compact","color-dark",width="300")}<span class="pill" style="font-size:28px;color:var(--lime)">{WEB}</span></div>')

json.dump(jobs, open('jobs_html.json', 'w'), indent=0); print(len(jobs), 'jobs')
