"""Social media template system. Every text block has class "t" so it can be lifted into editable PPTX."""
import os, sys, json
from kit import *
from icons import icon_svg
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/social'); os.makedirs(HT, exist_ok=True)
jobs, templates = [], []
PAT = lambda n: f'file://{OUT}/patterns/svg/beyna-pattern-{n}.svg'
CSS = '''.f{position:relative;overflow:hidden}
.ink{background:var(--ink);color:#fff}.grad{background:var(--grad);color:#fff}.paper{background:var(--paper);color:var(--ink)}
.limebg{background:var(--lime);color:var(--ink)}.violetbg{background:var(--violet);color:#fff}
.a{position:absolute}.t{position:absolute}
.big{font-family:Syne;font-weight:700;letter-spacing:-.03em;line-height:.98}
.sub{font-family:Manrope;font-weight:500;line-height:1.45}
.lbl{font-family:Manrope;font-weight:700;letter-spacing:.26em;text-transform:uppercase}
.ar{font-family:'Readex Pro';font-weight:700;direction:rtl}
.hl{color:var(--lime)}.vi{color:var(--violet)}
.pill{border:3px solid currentColor;border-radius:999px;padding:.55em 1.3em;font-weight:700;font-family:Manrope}
.zone{border:3px dashed rgba(255,255,255,.35);border-radius:40px;display:flex;align-items:center;justify-content:center;font:600 28px Manrope;color:rgba(255,255,255,.5)}'''

def T(text, x, y, style='', cls='', w=None):
    wd = f'width:{w}px;' if w else ''
    return f'<div class="t {cls}" style="left:{x}px;top:{y}px;{wd}{style}">{text}</div>'
def A(inner, style): return f'<div class="a" style="{style}">{inner}</div>'

def tpl(group, name, wd, ht, cls, body, title):
    p = f'{HT}/{group}-{name}.html'
    open(p, 'w').write(page_doc(f'<div class="f {cls}" style="width:{wd}px;height:{ht}px">{body}</div>', CSS, f'{wd}px {ht}px'))
    base = f'{OUT}/social/{group}/{name}'
    jobs.append(dict(html=p, type='png', out=base + '.png', w=wd, h=ht, unit='px'))
    jobs.append(dict(html=p, type='jpg', out=base + '.jpg', w=wd, h=ht, unit='px'))
    templates.append(dict(group=group, name=name, html=p, w=wd, h=ht, title=title))

big_mark = lambda h, st, body='grad', sl=LIME: mark_svg(body=body, slice_c=sl, height=h, style=st)
logo = lambda lk, sch, wd: logo_svg(lk, sch, width=wd)
G = 'instagram-posts'; W1, H1 = 1080, 1350
M = 88  # outer margin

# ---------------- Instagram posts 1080x1350
tpl(G, '01-tagline', W1, H1, 'ink',
    A(logo('horizontal-compact', 'color-dark', 270), f'left:{M}px;top:{M}px') +
    A(big_mark(900, ''), 'right:-330px;bottom:-230px') +
    T('Make it<br><span class="hl">clear.</span>', M, 420, 'font-size:172px', 'big', 800) +
    T(TAG_FR, M, 800, 'font-size:34px;color:rgba(255,255,255,.72)', 'sub', 600) +
    T(CITY, M, 1220, 'font-size:20px;color:rgba(255,255,255,.55)', 'lbl', 500), 'Tagline')

rows = ''.join(
    A(f'<div style="display:flex;align-items:center;gap:30px;height:112px;border-top:2px solid rgba(255,255,255,.22)">{icon_svg(ic, "#fff", LIME, 52)}</div>', f'left:{M}px;right:{M}px;top:{300+i*118}px') +
    T(fr, M + 86, 300 + i*118 + 30, 'font-size:50px;letter-spacing:-.015em', 'big', 820) for i, (ic, en, fr) in enumerate(SERVICES[:6]))
tpl(G, '02-services', W1, H1, 'grad',
    A(mark_svg(body='#fff', height=92), f'left:{M}px;top:{M}px') +
    T('Nos services', 600, 118, 'font-size:22px;text-align:right;color:var(--lime)', 'lbl', 392) + rows +
    T(WEB, M, 1220, 'font-size:28px;font-weight:700', 'sub', 500) + T(INSTA, 600, 1220, 'font-size:28px;font-weight:700;text-align:right', 'sub', 392), 'Services')

tpl(G, '03-announcement', W1, H1, 'paper',
    A(logo('horizontal-compact', 'color', 260), f'left:{M}px;top:{M}px') +
    T('Nouveau · New', M, 360, 'font-size:22px;color:var(--violet)', 'lbl', 600) +
    T('Grande<br>nouvelle.', M, 420, 'font-size:160px', 'big', 900) +
    T('Écrivez ici votre annonce en une ou deux phrases courtes. Clair, direct, évident.', M, 790, 'font-size:34px;color:#4a4a55', 'sub', 700) +
    T('En savoir plus →', M, 1000, 'font-size:30px;color:var(--violet)', 'pill', None) +
    A('', 'right:-1px;bottom:-1px;width:420px;height:420px;background:var(--grad);border-top-left-radius:420px') +
    A('', 'right:120px;bottom:120px;width:130px;height:130px;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%'), 'Announcement')

stars = ''.join(icon_svg('star', LIME, VIOLET, 46).replace('<svg', '<svg style="display:inline-block;margin-right:8px"') for _ in range(5))
tpl(G, '04-testimonial', W1, H1, 'violetbg',
    A(stars, f'left:{M}px;top:{M+10}px') + T('Témoignage', 600, M+20, 'font-size:22px;text-align:right;color:var(--lime)', 'lbl', 392) +
    T('“', M - 10, 220, 'font-size:300px;line-height:1;color:var(--lime)', 'big', 300) +
    T('Le témoignage de votre client s’écrit ici, en deux ou trois lignes maximum.', M, 470, 'font-size:68px;line-height:1.08;letter-spacing:-.02em', 'big', 900) +
    T('Nom du client', M, 1060, 'font-size:34px;font-weight:700', 'sub', 600) +
    T('Fonction · Entreprise', M, 1110, 'font-size:26px;color:rgba(255,255,255,.7)', 'sub', 600) +
    A(mark_svg(body='#fff', height=110), f'right:{M}px;bottom:{M}px'), 'Testimonial')

tpl(G, '05-result', W1, H1, 'ink',
    A(logo('horizontal-compact', 'color-dark', 240), f'left:{M}px;top:{M}px') + T('Case study', 600, M+18, 'font-size:22px;text-align:right;color:var(--lime)', 'lbl', 392) +
    T('×3', M - 8, 300, 'font-size:440px;color:var(--lime);letter-spacing:-.05em', 'big', 900) +
    T('Visibilité de la marque en 6 mois.', M, 800, 'font-size:64px;letter-spacing:-.02em;line-height:1.05', 'big', 800) +
    A('', f'left:{M}px;right:{M}px;top:1090px;height:2px;background:rgba(255,255,255,.2)') +
    T('Client · Secteur', M, 1130, 'font-size:28px;font-weight:700', 'sub', 500) + T('Chiffre exemple', 600, 1136, 'font-size:18px;text-align:right;color:rgba(255,255,255,.45)', 'lbl', 392), 'Result')

# Carousel — 5 slides
CG = 'instagram-carousel'
tpl(CG, '01-cover', W1, H1, 'ink',
    A(big_mark(760, ''), 'right:-180px;top:-120px') +
    T('3', M - 10, 300, 'font-size:520px;color:var(--lime);letter-spacing:-.05em;line-height:.9', 'big', 400) +
    T('erreurs qui rendent votre marque invisible', M, 790, 'font-size:92px;letter-spacing:-.025em;line-height:1', 'big', 900) +
    T('Swipe →', M, 1220, 'font-size:22px;color:rgba(255,255,255,.6)', 'lbl', 400) + A(logo('horizontal-compact', 'color-dark', 200), f'right:{M}px;bottom:{M}px'), 'Carousel cover')
for k, (tt, body) in enumerate([('Un message flou.', 'Si on ne comprend pas ce que vous vendez en 3 secondes, on passe. Une phrase. Une promesse. Claire.'),
                                ('Des visuels incohérents.', 'Couleurs, typos, ton : chaque post doit être reconnaissable sans voir le logo.'),
                                ('Aucune mesure.', 'Sans chiffres, pas de preuve. Fixez un objectif, suivez-le, ajustez chaque mois.')]):
    tpl(CG, f'0{k+2}-slide', W1, H1, 'paper',
        T(f'0{k+1}', M, M, 'font-size:26px;color:var(--violet)', 'lbl', 300) + T(f'{k+1} / 3', 600, M, 'font-size:22px;text-align:right;color:#8a8a96', 'lbl', 392) +
        A('', f'left:{M}px;top:300px;width:150px;height:150px;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%') +
        T(tt, M, 520, 'font-size:112px;letter-spacing:-.03em;line-height:1', 'big', 900) +
        T(body, M, 830, 'font-size:38px;color:#4a4a55', 'sub', 820) + A(mark_svg(height=70), f'right:{M}px;bottom:{M}px'), f'Carousel slide {k+1}')
tpl(CG, '05-cta', W1, H1, 'grad',
    T('Rendez votre marque', M, 330, 'font-size:96px;letter-spacing:-.03em;line-height:1', 'big', 900) +
    T(NAME_AR + '.', M, 560, 'font-size:220px;line-height:1.1;color:var(--lime);text-align:left', 'ar', 900) +
    T('Écrivez-nous : ' + MAIL, M, 900, 'font-size:34px;color:rgba(255,255,255,.85)', 'sub', 900) +
    A(logo('horizontal-compact', 'on-violet', 280), f'left:{M}px;bottom:{M}px') + T('Save · Share', 600, 1240, 'font-size:22px;text-align:right', 'lbl', 392), 'Carousel CTA')

tpl(G, '06-hiring', W1, H1, 'limebg',
    A(logo('horizontal-compact', 'on-lime', 260), f'left:{M}px;top:{M}px') +
    T('On recrute.', M, 340, 'font-size:142px', 'big', 960) +
    T('Social Media Manager', M, 560, 'font-size:60px;letter-spacing:-.02em;color:var(--violet)', 'big', 900) +
    T('· 2 ans d’expérience minimum<br>· Créatif, organisé, curieux<br>· Basé à Oran', M, 700, 'font-size:36px;line-height:1.7', 'sub', 800) +
    T('Postulez : ' + MAIL, M, 1150, 'font-size:32px;color:var(--ink)', 'pill', None) +
    A(icon_svg('team', INK, VIOLET, 170), f'right:{M}px;top:{M-10}px'), 'Hiring')

tpl(G, '07-event', W1, H1, 'ink',
    A('', f'left:0;right:0;top:0;height:470px;background:url({PAT("violet")}) 0 0/720px 720px') +
    A('', f'left:{M}px;top:380px;width:230px;height:190px;border-radius:28px;background:var(--lime)') +
    T('00', M, 400, 'font-size:96px;color:var(--ink);text-align:center', 'big', 230) + T('Mois', M, 500, 'font-size:22px;color:var(--ink);text-align:center', 'lbl', 230) +
    T('Workshop', M, 640, 'font-size:24px;color:var(--lime)', 'lbl', 600) +
    T('Marketing digital : les bases qui font vendre.', M, 690, 'font-size:84px;letter-spacing:-.025em;line-height:1.02', 'big', 900) +
    T('18:00 · Lieu de l’événement, Oran<br>Places limitées — inscription en bio', M, 1030, 'font-size:32px;color:rgba(255,255,255,.75);line-height:1.6', 'sub', 900) +
    A(logo('horizontal-compact', 'color-dark', 220), f'right:{M}px;bottom:{M}px'), 'Event')

tpl(G, '08-darija', W1, H1, 'grad',
    A(mark_svg(body='#fff', height=100), f'right:{M}px;top:{M}px') +
    T(TAG_AR, M, 300, 'font-size:190px;line-height:1.2;text-align:right', 'ar', 904) +
    T('ماركتك تستاهل تكون باينة.', M, 840, 'font-size:56px;font-weight:500;color:var(--lime);text-align:right', 'ar', 904) +
    T('Make your brand obvious.', M, 1010, 'font-size:34px;color:rgba(255,255,255,.8);text-align:right', 'sub', 904) +
    T(INSTA, M, 1230, 'font-size:24px', 'lbl', 500), 'Darija')

tpl(G, '09-greeting', W1, H1, 'ink',
    A(f'<div style="width:100%;height:100%;background:url({PAT("ink")}) 0 0/540px 540px;opacity:.55"></div>', 'inset:0') +
    A('', 'left:140px;right:140px;top:250px;bottom:250px;background:var(--ink);border-radius:48px') +
    T('عيد مبارك', 140, 420, 'font-size:150px;line-height:1.2;text-align:center;color:var(--lime)', 'ar', 800) +
    T('Aïd Moubarek', 140, 680, 'font-size:76px;text-align:center;letter-spacing:-.02em', 'big', 800) +
    T('Toute l’équipe Beyna vous souhaite une belle fête.', 220, 800, 'font-size:30px;text-align:center;color:rgba(255,255,255,.7)', 'sub', 640) +
    A(logo('horizontal-compact', 'color-dark', 220), 'left:430px;top:960px'), 'Greeting')

tpl(G, '10-portfolio', W1, H1, 'ink',
    A(f'<div style="width:100%;height:100%;background:url({PAT("mono")}) 0 0/480px 480px"></div>', f'left:{M}px;right:{M}px;top:{M}px;height:780px;border-radius:36px;overflow:hidden') +
    A('<div style="font:600 26px Manrope;color:rgba(255,255,255,.55);letter-spacing:.2em;text-transform:uppercase">Votre visuel ici · 904 × 780</div>', f'left:{M}px;right:{M}px;top:{M}px;height:780px;display:flex;align-items:center;justify-content:center') +
    T('Nom du projet', M, 940, 'font-size:84px;letter-spacing:-.025em', 'big', 900) +
    T('Identité visuelle · Social media · Vidéo', M, 1050, 'font-size:30px;color:var(--lime);font-weight:700', 'sub', 900) +
    A(logo('horizontal-compact', 'color-dark', 200), f'right:{M}px;bottom:{M}px') + T('Projet 2026', M, 1236, 'font-size:20px;color:rgba(255,255,255,.5)', 'lbl', 400), 'Portfolio')

# ---------------- Stories 1080x1920 (safe area: 250 top / 340 bottom)
SG = 'instagram-stories'; WS, HS = 1080, 1920
tpl(SG, '01-new-post', WS, HS, 'grad',
    A(mark_svg(body='#fff', height=110), f'left:{M}px;top:260px') +
    T('Nouveau<br>post.', M, 640, 'font-size:200px', 'big', 900) +
    T('Le titre de votre publication s’écrit ici.', M, 1110, 'font-size:44px;color:rgba(255,255,255,.85)', 'sub', 800) +
    T('Voir le post ↓', M, 1400, 'font-size:34px;color:var(--lime)', 'pill', None), 'Story new post')
tpl(SG, '02-question', WS, HS, 'ink',
    A(logo('horizontal-compact', 'color-dark', 260), f'left:{M}px;top:260px') +
    T('Une question sur votre <span class="hl">marque</span> ?', M, 520, 'font-size:128px;line-height:1', 'big', 900) +
    A('Sticker question ici', f'left:{M}px;right:{M}px;top:1020px;height:420px').replace('class="a"', 'class="a zone"'), 'Story question')
tpl(SG, '03-offer', WS, HS, 'limebg',
    A(logo('horizontal-compact', 'on-lime', 260), f'left:{M}px;top:260px') +
    T('Offre de lancement', M, 520, 'font-size:28px;color:var(--violet)', 'lbl', 800) +
    T('Audit de marque offert.', M, 590, 'font-size:150px;line-height:.98', 'big', 900) +
    T('Pour les 10 premières entreprises d’Oran.<br>Offre à adapter.', M, 1080, 'font-size:40px;line-height:1.5', 'sub', 860) +
    T('Réservez maintenant', M, 1400, 'font-size:36px;background:var(--ink);color:var(--lime);border-color:var(--ink)', 'pill', None), 'Story offer')
tpl(SG, '04-link', WS, HS, 'ink',
    A(big_mark(1100, ''), 'left:-160px;top:-60px') +
    T('Let’s make<br>it <span class="hl">clear.</span>', M, 1020, 'font-size:132px', 'big', 900) +
    T('Parlons de votre marque.', M, 1330, 'font-size:40px;color:rgba(255,255,255,.72)', 'sub', 800) +
    A('Sticker lien ici', f'left:{M}px;right:{M}px;top:1430px;height:130px').replace('class="a"', 'class="a zone"'), 'Story link')
tpl(SG, '05-testimonial', WS, HS, 'paper',
    A(stars, f'left:{M}px;top:280px') +
    T('“', M - 10, 380, 'font-size:300px;line-height:1;color:var(--violet)', 'big', 300) +
    T('Le témoignage client s’écrit ici en quelques mots forts.', M, 640, 'font-size:92px;line-height:1.05;letter-spacing:-.025em', 'big', 900) +
    T('Nom du client', M, 1250, 'font-size:40px;font-weight:700', 'sub', 800) + T('Fonction · Entreprise', M, 1310, 'font-size:32px;color:#6a6a76', 'sub', 800) +
    A(logo('horizontal-compact', 'color', 240), f'left:{M}px;top:1460px'), 'Story testimonial')
tpl(SG, '06-countdown', WS, HS, 'violetbg',
    T('J-7', M - 10, 300, 'font-size:420px;color:var(--lime);letter-spacing:-.05em', 'big', 900) +
    T('Nom de l’événement', M, 800, 'font-size:110px;letter-spacing:-.03em;line-height:1', 'big', 900) +
    T('00.00.2026 · Oran', M, 1050, 'font-size:40px;color:rgba(255,255,255,.8)', 'sub', 900) +
    A('Sticker compte à rebours', f'left:{M}px;right:{M}px;top:1200px;height:300px').replace('class="a"', 'class="a zone"'), 'Story countdown')
tpl(SG, '07-darija', WS, HS, 'ink',
    T('باينة؟', M, 560, 'font-size:300px;line-height:1.2;text-align:right;color:var(--lime)', 'ar', 904) +
    T('C’est évident.<br>Ça se voit.', M, 1000, 'font-size:110px;text-align:right', 'big', 904) +
    A(logo('arabic', 'color-dark', 330), f'right:{M}px;top:1440px'), 'Story darija')

# ---------------- Reel covers 1080x1920 (keep text in central 1080x1440 for grid crop)
RG = 'reel-covers'
tpl(RG, '01-tips', WS, HS, 'ink',
    A(f'<div style="width:100%;height:100%;background:url({PAT("ink")}) 0 0/540px 540px;opacity:.35"></div>', 'inset:0') +
    T('Tip #01', M, 560, 'font-size:34px;color:var(--lime)', 'lbl', 800) +
    T('Le titre de votre astuce ici.', M, 640, 'font-size:140px', 'big', 900) + A(mark_svg(height=120), f'left:{M}px;top:1200px'), 'Reel tips')
tpl(RG, '02-behind-the-scenes', WS, HS, 'grad',
    T('Coulisses', M, 560, 'font-size:34px;color:var(--lime)', 'lbl', 800) +
    T('Behind the scenes.', M, 640, 'font-size:150px', 'big', 900) + A(mark_svg(body='#fff', height=120), f'left:{M}px;top:1200px'), 'Reel BTS')
tpl(RG, '03-case-study', WS, HS, 'limebg',
    T('Case study', M, 560, 'font-size:34px;color:var(--violet)', 'lbl', 800) +
    T('Nom du client.', M, 640, 'font-size:150px', 'big', 900) + A(mark_svg(body=INK, slice_c=VIOLET, height=120), f'left:{M}px;top:1200px'), 'Reel case study')

# ---------------- LinkedIn 1200x1200 & Facebook 1200x630
LG = 'linkedin-posts'
tpl(LG, '01-insight', 1200, 1200, 'paper',
    A(logo('horizontal-compact', 'color', 280), 'left:96px;top:96px') + T('Insight', 700, 116, 'font-size:22px;text-align:right;color:var(--violet)', 'lbl', 404) +
    T('Une marque claire se vend <span class="vi">deux fois</span> mieux qu’une marque floue.', 96, 340, 'font-size:96px;line-height:1.03;letter-spacing:-.03em', 'big', 1000) +
    T(NAME + ' · ' + ROLE, 96, 1050, 'font-size:28px;font-weight:700', 'sub', 900) +
    A('', 'right:-1px;bottom:-1px;width:300px;height:300px;background:var(--grad);border-top-left-radius:300px'), 'LinkedIn insight')
tpl(LG, '02-announcement', 1200, 1200, 'ink',
    A(big_mark(760, ''), 'right:-250px;bottom:-280px') +
    T('Announcement', 96, 120, 'font-size:24px;color:var(--lime)', 'lbl', 600) +
    T('Beyna Agency ouvre ses portes à Oran.', 96, 200, 'font-size:100px;line-height:1;letter-spacing:-.03em', 'big', 700) +
    A(logo('horizontal-compact', 'color-dark', 280), 'left:96px;bottom:96px'), 'LinkedIn announcement')
tpl('facebook-posts', '01-link-1200x630', 1200, 630, 'grad',
    T('Make it <span class="hl">clear.</span>', 80, 170, 'font-size:116px', 'big', 1040) +
    T(TAG_FR + ' — ' + WEB, 80, 330, 'font-size:32px;color:rgba(255,255,255,.85)', 'sub', 800) +
    A(logo('horizontal-compact', 'on-violet', 260), 'left:80px;bottom:70px') + A(mark_svg(body='rgba(255,255,255,.14)', slice_c='rgba(255,255,255,.14)', height=760), 'right:-120px;top:-60px'), 'Facebook link')

json.dump(jobs, open('jobs_social.json', 'w')); json.dump(templates, open('templates_social.json', 'w'))
print(len(templates), 'templates')
