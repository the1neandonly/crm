"""Complete kit: every item delivered as PNG + JPG + SVG + PDF in one folder tree (sources: all generator job lists)."""
import os, sys, json, glob, shutil, re
SRC = '/home/user/crm/brand/developtheone'; G = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
L = lambda f: json.load(open(os.path.join(G, f)))
items = []      # html items: dict(html,w,h,unit,alpha,dest,name,png,jpg)
svgitems = []   # svg items: dict(svg,dest,name,png,w,h,jpg,pdf,eps)
copies = []     # (src, dest_rel)
def H(j, dest, name, png=None, jpg=None):
    items.append(dict(html=j['html'], w=j['w'], h=j['h'], unit=j.get('unit', 'px'), alpha=bool(j.get('alpha')), dest=dest, name=name, png=png, jpg=jpg))
def pngjpg(jobs):
    by = {}
    for j in jobs:
        b = by.setdefault(j['html'], {'j': j})
        b[j['type']] = j['out']
    return by.values()

# ---------- Social
SOC = {'instagram-posts': '06_Reseaux-sociaux/01_Instagram-posts', 'instagram-carousel': '06_Reseaux-sociaux/02_Instagram-carrousel', 'instagram-stories': '06_Reseaux-sociaux/03_Instagram-stories',
       'reel-covers': '06_Reseaux-sociaux/04_Couvertures-reels_TikTok', 'linkedin-posts': '06_Reseaux-sociaux/06_LinkedIn-posts', 'facebook-posts': '06_Reseaux-sociaux/07_Facebook-posts'}
for b in pngjpg(L('jobs_social.json')):
    grp = b['png'].split('/social/')[1].split('/')[0]
    H(b['j'], SOC[grp], os.path.basename(b['png'])[:-4], b.get('png'), b.get('jpg'))
# ---------- Banners
BAN = {'social-headers': '06_Reseaux-sociaux/08_Couvertures-reseaux_Covers', 'web': '05_Web-et-applications/04_Bannieres-web', 'display-ads': '05_Web-et-applications/05_Publicites-web_Ads', 'print': '07_Impression/12_Grand-format_Kakemono-panneau-affiche'}
for b in pngjpg(L('jobs_banners.json')):
    any_out = b.get('png') or b.get('pdf'); sub = any_out.split('/banners/')[1].split('/')[0]
    H(b['j'], BAN[sub], os.path.basename(any_out).rsplit('.', 1)[0], b.get('png'), b.get('jpg'))
# ---------- Print (one item per printed side)
PR = {'business-cards': '01_Cartes-de-visite', 'nfc-card': '02_Carte-NFC', 'thank-you-card': '03_Carte-de-remerciement', 'envelope': '04_Enveloppe', 'letterhead': '05_En-tete-facture-devis',
      'folder': '06_Chemise', 'notebook': '07_Carnet', 'stickers': '08_Stickers', 'packaging': '09_Emballage-boite', 'badge': '10_Badge', 'signage': '11_Signaletique'}
pj = [j for j in L('jobs_print.json') if j['type'] == 'png']
pages = {}
for j in pj:
    m = re.match(r'(.+)-(\d+)\.png$', os.path.basename(j['out'])); pages.setdefault(m.group(1), []).append((int(m.group(2)), j))
for base, lst in pages.items():
    for i, j in sorted(lst):
        side = ('-recto' if i == 1 else '-verso') if len(lst) == 2 else (f'-page{i}' if len(lst) > 2 else '')
        folder = j['out'].split('/print/')[1].split('/')[0]
        H(j, f'07_Impression/{PR[folder]}', base + side, j['out'])
copies.append((f'{SRC}/print/letterhead/DTO-letterhead-A4-EDITABLE.docx', '07_Impression/05_En-tete-facture-devis'))
copies.append((f'{SRC}/print/letterhead/DTO-letterhead-A4-EDITABLE.docx', '08_Bureau_Office'))
# ---------- Digital extras
for b in pngjpg(L('jobs_digital.json')):
    o = b.get('png'); nm = os.path.basename(o)[:-4]
    if '/presentation/' in o: continue
    dest = '05_Web-et-applications/09_Signature-email' if 'email-signature' in o else ('06_Reseaux-sociaux/10_YouTube' if 'youtube' in o else '09_Videos/Images-video_Watermarks-overlays')
    H(b['j'], dest, nm, o, b.get('jpg'))
# ---------- Presentation slides
for b in pngjpg(L('jobs_pres.json')):
    H(b['j'], '08_Bureau_Office/Presentation-slides', 'presentation-' + os.path.basename(b['png'])[:-4], f"{SRC}/presentation/preview/{os.path.basename(b['png'])}")
copies.append((f'{SRC}/presentation/DTO-Presentation-16x9-EDITABLE.pptx', '08_Bureau_Office'))
for f in glob.glob(f'{SRC}/social/editable-pptx/*.pptx'): copies.append((f, '06_Reseaux-sociaux/09_MODIFIABLES_PowerPoint-Canva'))
# ---------- Wallpapers, virtual backgrounds, highlight covers
for j in L('jobs_assets_html.json'):
    o = j['out']; nm = os.path.basename(o)[:-4]
    dest = '06_Reseaux-sociaux/05_Instagram-a-la-une_Highlights' if 'highlight' in o else '05_Web-et-applications/08_Fonds-ecran-et-visio'
    H(j, dest, nm, o)
# ---------- Colour swatches
for j in L('jobs_colors.json'): H(j, '04_Couleurs_Colors', os.path.basename(j['out'])[:-4], j['out'])
for f in glob.glob(f'{SRC}/colors/DTO-palette.*'): copies.append((f, '04_Couleurs_Colors/Fichiers-palette'))
# ---------- Ready-made extras (Google cover, merch, stamps, decals)
by = {}
for j in L('jobs_ready_html.json'): by.setdefault(j['html'], {})[j['type']] = j
for d in by.values():
    j = d.get('png') or d.get('pdf'); o = j['out']; nm = os.path.basename(o).rsplit('.', 1)[0]
    dest = ('06_Reseaux-sociaux/08_Couvertures-reseaux_Covers' if 'google' in o else '07_Impression/13_Goodies-merch' if 'Goodies' in o
            else '07_Impression/14_Cachet-tampon_Stamp' if 'Cachet' in o else '07_Impression/15_Vehicule-vitrine_Decals')
    H(j, dest, nm, d['png']['out'] if 'png' in d else None)

# ---------- SVG-native items
LOGO = [('horizontal', '01_Logo-horizontal-principal'), ('stacked', '02_Logo-vertical'), ('symbol', '03_Symbole-DTO'), ('icon', '04_Icone-D-curseur'),
        ('horizontal-compact', '05_Logo-horizontal-compact'), ('wordmark-plain', '06_Ecriture-seule-DevelopTheOne'), ('wordmark', '07_Ecriture-MARKETING-AGENCY')]
SCH = {'color': 'original-fond-clair', 'color-dark': 'inverse-fond-noir', 'on-violet': 'blanc-sur-bleu', 'black': 'noir', 'white': 'blanc'}
for lk, folder in LOGO:
    for sch, fr in SCH.items():
        s = f'{SRC}/logo/svg/dto-{lk}-{sch}.svg'
        if not os.path.exists(s): continue
        px = 2048 if lk == 'icon' else 2000
        svgitems.append(dict(svg=s, dest=f'02_Logos/{folder}', name=f'dto-{lk}_{fr}', png=f'{SRC}/logo/png/{lk}/dto-{lk}-{sch}-{px}px.png',
                             jpg=f'{SRC}/logo/jpg/dto-{lk}-{sch}.jpg', pdf=f'{SRC}/logo/pdf/dto-{lk}-{sch}.pdf', eps=f'{SRC}/logo/eps/dto-{lk}-{sch}.eps'))
APP = '05_Web-et-applications/01_Favicons-et-icones-app'
for n in ['app-icon-gradient', 'app-icon-ink', 'app-icon-violet', 'app-icon-white']:
    svgitems.append(dict(svg=f'{SRC}/icons/svg/{n}.svg', dest=APP, name=n + '-1024', png=f'{SRC}/icons/png/{n}-1024.png', w=1024, h=1024))
for px, src in [(16, 'favicon-16'), (32, 'favicon-32'), (48, 'favicon-48'), (64, 'favicon-64'), (180, 'apple-touch-icon-180'), (192, 'android-chrome-192'), (512, 'android-chrome-512')]:
    svgitems.append(dict(svg=f'{SRC}/icons/svg/favicon-master.svg', dest=APP, name=src, png=f'{SRC}/icons/png/{src}.png', w=px, h=px))
copies.append((f'{SRC}/icons/favicon.ico', APP)); copies.append((f'{SRC}/ready-to-use/10_Site-web_Website/Favicon/site.webmanifest', APP))
PROF = '05_Web-et-applications/02_Photos-de-profil_Profile-pictures'
for plat, sizes in [('instagram', [320, 1080]), ('facebook', [720]), ('whatsapp', [640]), ('tiktok', [720]), ('youtube', [800]), ('linkedin', [400]), ('x-twitter', [400]), ('google-business', [720]), ('telegram-snapchat', [512])]:
    for v in ['gradient', 'ink', 'white']:
        for px in sizes:
            svgitems.append(dict(svg=f'{SRC}/icons/svg/avatar-{v}.svg', dest=PROF, name=f'{plat}-profile-{v}-{px}x{px}', w=px, h=px))
WEBL = '05_Web-et-applications/03_Logo-site-web'
for n in ['horizontal-color', 'horizontal-white', 'horizontal-compact-color', 'horizontal-compact-white', 'icon-color']:
    svgitems.append(dict(svg=f'{SRC}/logo/svg/dto-{n}.svg', dest=WEBL, name=f'site-logo-{n}', w=600, h=None))
copies.append((f'{SRC}/social/facebook-posts/01-link-1200x630.png', '05_Web-et-applications/04_Bannieres-web', 'og-image-share-1200x630.png'))
copies.append((f'{SRC}/ready-to-use/10_Site-web_Website/Code/head-snippet.html', '05_Web-et-applications/10_Code-site-web')); copies.append((f'{SRC}/colors/DTO-palette.css', '05_Web-et-applications/10_Code-site-web'))
for f in glob.glob(f'{SRC}/icons/service-icons/svg/*/*.svg'):
    cw = f.split('/')[-2]; nm = os.path.basename(f)[:-4]
    svgitems.append(dict(svg=f, dest=f'05_Web-et-applications/06_Icones-services_Icons/{cw}', name=nm, png=f'{SRC}/icons/service-icons/png/{cw}/{nm}-512.png', w=512, h=512))
for f in glob.glob(f'{SRC}/patterns/svg/*.svg'):
    nm = os.path.basename(f)[:-4]
    svgitems.append(dict(svg=f, dest='05_Web-et-applications/07_Motifs_Patterns', name=nm, png=f'{SRC}/patterns/png/{nm}-tile-1920.png', w=1920, h=1920))
svgitems.append(dict(svg=f'{SRC}/logo/svg/dto-icon-white.svg', dest='06_Reseaux-sociaux/10_YouTube', name='youtube-watermark-150', w=150, h=None))
json.dump(dict(items=items, svgitems=svgitems, copies=copies), open(os.path.join(G, 'catalog.json'), 'w'))
print(len(items), 'html items,', len(svgitems), 'svg items,', len(copies), 'copies')
