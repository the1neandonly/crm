"""Ready-to-use pack: one folder per usage, every file separate and sized for its destination."""
import os, sys, json, shutil, glob, subprocess
from kit import *
from brand import *
SRC = sys.argv[1]; R = os.path.join(SRC, 'ready-to-use'); HT = os.path.abspath('html/ready'); os.makedirs(HT, exist_ok=True)
svg_jobs, html_jobs = [], []
def cp(g, d, rename=None):
    os.makedirs(os.path.join(R, d), exist_ok=True); fs = sorted(glob.glob(os.path.join(SRC, g))); assert fs, g
    for f in fs: shutil.copy2(f, os.path.join(R, d, rename or os.path.basename(f)))
def svgpng(svg, d, name, w, h=None):
    svg_jobs.append({'type': 'png', 'svg': os.path.join(SRC, svg), 'out': os.path.join(R, d, name), 'w': w, 'h': h or w})
CSS = '.f{position:relative;overflow:hidden}.a{position:absolute}.big{font-family:Montserrat;font-weight:700;letter-spacing:-.03em;line-height:1}.hl{color:var(--lime)}'
def html(d, name, w, h, bg, body, kinds=('png',), unit='px', scale=1):
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(f'<div class="f" style="width:{w}{unit};height:{h}{unit};background:{bg}">{body}</div>', CSS, f'{w}{unit} {h}{unit}'))
    for k in kinds:
        html_jobs.append(dict(html=p, type=k, out=os.path.join(R, d, f'{name}.{k}'), w=w, h=h, unit=unit, scale=scale, alpha=(bg == 'transparent')))
A = lambda i, s: f'<div class="a" style="{s}">{i}</div>'
AV = {'gradient': 'icons/svg/avatar-gradient.svg', 'ink': 'icons/svg/avatar-ink.svg'}
def avatars(d, sizes):
    for v, s in AV.items():
        for px in sizes: svgpng(s, d, f'profile-picture-{v}-{px}x{px}.png', px)

# ---- Social platforms
avatars('01_Instagram/Photo-de-profil_Profile-picture', [320, 1080])
cp('social/instagram-posts/*', '01_Instagram/Posts'); cp('social/instagram-carousel/*', '01_Instagram/Carrousel_Carousel')
cp('social/instagram-stories/*', '01_Instagram/Stories'); cp('social/instagram-highlight-covers/*', '01_Instagram/Highlights'); cp('social/reel-covers/*', '01_Instagram/Reels-covers')
avatars('02_Facebook/Photo-de-profil_Profile-picture', [720])
cp('banners/social-headers/facebook-cover-1640x624.*', '02_Facebook/Couverture_Cover'); cp('banners/social-headers/facebook-event-cover-1920x1005.*', '02_Facebook/Couverture-evenement_Event-cover')
cp('social/facebook-posts/*', '02_Facebook/Posts'); cp('banners/display-ads/ad-1080x1080.*', '02_Facebook/Publicite_Ads'); cp('banners/display-ads/ad-1200x628.*', '02_Facebook/Publicite_Ads')
avatars('03_WhatsApp-Business/Photo-de-profil_Profile-picture', [640]); cp('social/instagram-stories/*.jpg', '03_WhatsApp-Business/Statut_Status')
avatars('04_TikTok/Photo-de-profil_Profile-picture', [720]); cp('social/reel-covers/*', '04_TikTok/Couvertures-video_Video-covers')
avatars('05_YouTube/Photo-de-profil_Profile-picture', [800]); cp('banners/social-headers/youtube-channel-art-2560x1440.*', '05_YouTube/Banniere_Banner')
cp('video/stills/youtube-thumbnail-template-1280x720.*', '05_YouTube/Miniature_Thumbnail'); svgpng('logo/svg/dto-symbol-white.svg', '05_YouTube/Filigrane_Watermark', 'youtube-watermark-150x150.png', 150, 200)
cp('video/logo-intro-16x9-1920x1080.mp4', '05_YouTube/Intro-Outro'); cp('video/end-card-16x9-1920x1080.mp4', '05_YouTube/Intro-Outro')
avatars('06_LinkedIn/Logo-page', [400]); cp('banners/social-headers/linkedin-company-1128x191.*', '06_LinkedIn/Couverture-page_Company-cover')
cp('banners/social-headers/linkedin-personal-1584x396.*', '06_LinkedIn/Couverture-profil_Personal-cover'); cp('social/linkedin-posts/*', '06_LinkedIn/Posts')
avatars('07_X-Twitter/Photo-de-profil_Profile-picture', [400]); cp('banners/social-headers/x-twitter-header-1500x500.*', '07_X-Twitter/Banniere_Header')
avatars('08_Google-Business-Maps/Logo', [720])
html('08_Google-Business-Maps/Couverture_Cover', 'google-business-cover-1080x608', 1080, 608, 'var(--ink)',
     A(mark_svg(height=800), 'right:-120px;top:-90px') + A(logo_svg('horizontal', 'color-dark', width=520), 'left:70px;top:70px') +
     A('<div class="big" style="font-size:64px;color:#fff">Become <span class="hl">the one.</span></div>', 'left:70px;bottom:80px'), ('png', 'jpg'))
avatars('09_Telegram-Snapchat-Autres_Others', [512, 1024])

# ---- Website
W_ = '10_Site-web_Website'
for f in ['dto-horizontal-compact-color.svg', 'dto-horizontal-compact-white.svg', 'dto-horizontal-color.svg', 'dto-horizontal-white.svg', 'dto-symbol-color.svg']:
    cp(f'logo/svg/{f}', f'{W_}/Logo-header')
svgpng('logo/svg/dto-horizontal-compact-color.svg', f'{W_}/Logo-header', 'logo-header-color-600w.png', 600, 180)
svgpng('logo/svg/dto-horizontal-compact-white.svg', f'{W_}/Logo-header', 'logo-header-white-600w.png', 600, 180)
cp('icons/favicon.ico', f'{W_}/Favicon'); cp('icons/png/favicon-*.png', f'{W_}/Favicon'); cp('icons/png/apple-touch-icon-180.png', f'{W_}/Favicon'); cp('icons/png/android-chrome-*.png', f'{W_}/Favicon')
cp('social/facebook-posts/01-link-1200x630.png', f'{W_}/Image-partage_Share-image', 'og-image-1200x630.png')
cp('banners/web/website-hero-1920x800.*', f'{W_}/Banniere-accueil_Hero'); cp('banners/web/blog-cover-1600x900.*', f'{W_}/Blog')
cp('icons/service-icons/svg/violet/*.svg', f'{W_}/Icones_Icons'); cp('colors/DTO-palette.css', f'{W_}/Code')
os.makedirs(os.path.join(R, W_, 'Code'), exist_ok=True)
open(os.path.join(R, W_, 'Favicon', 'site.webmanifest'), 'w').write(json.dumps({'name': 'DevelopTheOne', 'short_name': 'DevelopTheOne', 'icons': [{'src': '/android-chrome-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '/android-chrome-512.png', 'sizes': '512x512', 'type': 'image/png'}], 'theme_color': VIOLET, 'background_color': INK, 'display': 'standalone'}, indent=2))
open(os.path.join(R, W_, 'Code', 'head-snippet.html'), 'w').write(f'''<!-- Paste inside <head> -->
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="{VIOLET}">
<meta property="og:title" content="DevelopTheOne — Become the one.">
<meta property="og:description" content="{TAG_FR} Agence de marketing digital.">
<meta property="og:image" content="https://{WEB}/og-image-1200x630.png">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Inter:wght@400;500;700&family=Readex+Pro:wght@400;700&display=swap" rel="stylesheet">
''')
# ---- Email
cp('email-signature/*', '11_Email/Signature'); cp('banners/web/email-header-1200x400.*', '11_Email/Newsletter'); cp('banners/web/newsletter-footer-1200x300.*', '11_Email/Newsletter')
# ---- Office
cp('print/letterhead/DTO-letterhead-A4-EDITABLE.docx', '12_Bureau_Office/Word'); cp('presentation/*.pptx', '12_Bureau_Office/PowerPoint')
cp('print/letterhead/invoice-facture-A4.pdf', '12_Bureau_Office/Facture-Devis_Invoice-Quote'); cp('print/letterhead/quote-devis-A4.pdf', '12_Bureau_Office/Facture-Devis_Invoice-Quote')
cp('print/letterhead/letterhead-A4.pdf', '12_Bureau_Office/Papier-en-tete_Letterhead')
cp('virtual-backgrounds/*', '12_Bureau_Office/Fonds-visio_Video-call-backgrounds'); cp('wallpapers/desktop-*', '12_Bureau_Office/Fonds-ecran_Wallpapers'); cp('wallpapers/phone-*', '12_Bureau_Office/Fonds-ecran_Wallpapers')

# ---- Merch print files (transparent PNG @300 dpi + vector PDF)
M = '14_Goodies-Merch'
def merch(name, wpx, hpx, body, bg='transparent'):
    html(M, name, wpx, hpx, bg, body, ('png', 'pdf'))
merch('tshirt-front-chest-white-ink-for-dark-tees-3000x3000', 3000, 3000, A(logo_svg('stacked', 'white', width=2400), 'left:300px;top:640px'))
merch('tshirt-front-chest-ink-for-light-tees-3000x3000', 3000, 3000, A(logo_svg('stacked', 'black', width=2400), 'left:300px;top:640px'))
merch('tshirt-back-symbol-color-4500x5400', 4500, 5400, A(mark_svg(height=3600), 'left:900px;top:500px') + A('<div class="big" style="font-size:420px;color:#fff;text-align:center">Become <span class="hl">the one.</span></div>', 'left:0;right:0;top:4400px'))
merch('tote-bag-print-ink-3000x3000', 3000, 3000, A(mark_svg(body=INK, slice_c=INK, height=1500), 'left:960px;top:400px') + A('<div class="big" style="font-size:250px;color:#0A0B0D;text-align:center">Become the one.</div>', 'left:0;right:0;top:2250px'))
merch('mug-wrap-sublimation-2475x1155', 2475, 1155, A(mark_svg(height=760), 'left:250px;top:200px') + A(logo_svg('horizontal-compact', 'color', width=1000), 'left:1250px;top:360px') + A('<div class="big" style="font-size:110px;color:#0A0B0D">Make it <span style="color:#0F66B6">clear.</span></div>', 'left:1250px;top:700px'), '#fff')
merch('cap-embroidery-symbol-1-colour-1200x1200', 1200, 1200, A(mark_svg(body='#fff', slice_c='#fff', height=1000), 'left:225px;top:100px'))
for f in ['dto-symbol-white.svg', 'dto-symbol-black.svg', 'dto-horizontal-compact-white.svg', 'dto-horizontal-compact-black.svg', 'dto-stacked-white.svg', 'dto-stacked-black.svg']:
    cp(f'logo/svg/{f}', f'{M}/Broderie-gravure-1-couleur_Embroidery-engraving-1-colour')

# ---- Company stamp (cachet / tampon) — one colour, vector
def stamp(col):
    ring = (f'<svg viewBox="0 0 400 400" width="100%" height="100%"><defs><path id="c" d="M200,200 m-150,0 a150,150 0 1,1 300,0 a150,150 0 1,1 -300,0"/></defs>'
            f'<circle cx="200" cy="200" r="194" fill="none" stroke="{col}" stroke-width="8"/><circle cx="200" cy="200" r="122" fill="none" stroke="{col}" stroke-width="3"/>'
            f'<text font-family="Montserrat" font-weight="700" font-size="27" fill="{col}"><textPath href="#c" startOffset="0" textLength="925" lengthAdjust="spacing">DEVELOPTHEONE · DIGITAL MARKETING AGENCY ·</textPath></text>'
            f'<g transform="translate(141,108) scale(0.21)">{__import__("logo").mark_paths(col, col)}</g>'
            f'<text x="200" y="255" text-anchor="middle" font-family="Cairo" font-weight="700" font-size="30" fill="{col}">DTO</text>'
            f'<text x="200" y="290" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" letter-spacing="4" fill="{col}">ALGÉRIE</text></svg>')
    return ring
for cname, col in [('dto-blue', '#0F66B6'), ('black', '#111111'), ('navy', '#0A3D73')]:
    html('15_Cachet-Tampon_Company-stamp', f'stamp-round-40mm-{cname}', 40, 40, 'transparent', A(stamp(col), 'inset:0'), ('pdf', 'png'), 'mm', 12)
    html('15_Cachet-Tampon_Company-stamp', f'stamp-rectangle-60x30mm-{cname}', 60, 30, 'transparent',
         A(f'<div style="width:100%;height:100%;border:.8mm solid {col};border-radius:2mm;display:flex;align-items:center;gap:3mm;padding:0 3.5mm;color:{col}">'
           f'{mark_svg(body=col, slice_c=col, height="17mm")}<div><div class="big" style="font-size:13pt">DevelopTheOne</div><div style="font:700 6.2pt Inter;margin-top:1mm">Marketing &amp; Communication</div>'
           f'<div style="font:700 9pt \'Cairo\';margin-top:.5mm;direction:rtl;text-align:left">ديفلوب ذا وان</div><div style="font:600 5.5pt Inter;margin-top:.6mm">RC 00/00-0000000 · Algérie</div></div></div>', 'inset:0'), ('pdf', 'png'), 'mm', 12)

# ---- Vehicle & window decals (vector PDF + PNG)
V = '16_Vehicule-Vitrine_Vehicle-Window'
html(V, 'car-door-decal-600x250mm-white', 600, 250, 'transparent', A(logo_svg('horizontal', 'white', width='540mm'), 'left:30mm;top:40mm') + A(f'<div style="font:700 26mm Inter;color:#fff">{PHONE}</div>', 'left:30mm;top:190mm'), ('pdf', 'png'), 'mm', 2)
html(V, 'car-door-decal-600x250mm-color', 600, 250, 'transparent', A(logo_svg('horizontal', 'color', width='540mm'), 'left:30mm;top:40mm') + A(f'<div style="font:700 26mm Inter;color:#0A0B0D">{PHONE}</div>', 'left:30mm;top:190mm'), ('pdf', 'png'), 'mm', 2)
html(V, 'rear-window-decal-800x200mm-white', 800, 200, 'transparent', A(f'<div class="big" style="font-size:70mm;color:#fff;white-space:nowrap">{WEB}</div>', 'left:20mm;top:40mm'), ('pdf', 'png'), 'mm', 2)
html(V, 'window-vinyl-symbol-600x600mm-white', 600, 600, 'transparent', A(mark_svg(body='#fff', slice_c=LIME, height='500mm'), 'left:112mm;top:50mm'), ('pdf', 'png'), 'mm', 1.5)

# ---- Photo watermark
cp('video/stills/watermark-*.png', '17_Filigrane-photo_Photo-watermark')

json.dump(svg_jobs, open('jobs_ready_svg.json', 'w')); json.dump(html_jobs, open('jobs_ready_html.json', 'w')); print(len(svg_jobs), len(html_jobs))
