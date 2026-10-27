"""Assemble every asset into one organised folder and zip it."""
import os, shutil, glob, sys, zipfile
SRC = '/home/user/crm/brand/bayna-agency'; BASE = sys.argv[1]; NAME = 'Bayna-Agency-Brand-Kit'
DST = os.path.join(BASE, NAME); shutil.rmtree(DST, ignore_errors=True)
def cp(src_glob, dst_dir):
    os.makedirs(os.path.join(DST, dst_dir), exist_ok=True); n = 0
    for f in sorted(glob.glob(os.path.join(SRC, src_glob))):
        if os.path.isfile(f): shutil.copy2(f, os.path.join(DST, dst_dir, os.path.basename(f))); n += 1
    assert n, f'nothing matched {src_glob}'
def cptree(src, dst):
    shutil.copytree(os.path.join(SRC, src), os.path.join(DST, dst), dirs_exist_ok=True)

cp('Bayna-Agency-Brand-Guidelines.pdf', '01_Charte-Graphique_Brand-Guidelines')
LOGOS = [('symbol', '01_Symbole-seul_Symbol-only'), ('wordmark-plain', '02_Ecriture-seule_Wordmark-bayna'), ('wordmark', '03_Ecriture-AGENCY_Wordmark-agency'),
         ('arabic-wordmark', '04_Ecriture-arabe-seule_Arabic-wordmark'), ('horizontal', '05_Logo-horizontal_Primary'), ('horizontal-compact', '06_Logo-horizontal-compact'),
         ('stacked', '07_Logo-vertical_Stacked'), ('arabic', '08_Logo-arabe_Arabic'), ('bilingual', '09_Logo-bilingue_Bilingual'), ('bilingual-stacked', '10_Logo-bilingue-vertical_Bilingual-stacked')]
for lk, folder in LOGOS:
    d = f'02_Logos/{folder}'
    pat = lambda ext, sub: f'logo/{sub}/bayna-{lk}-*.{ext}'
    # exact lockup match (avoid 'horizontal' also matching 'horizontal-compact', 'wordmark' matching 'wordmark-plain', 'arabic' matching 'arabic-wordmark')
    for ext, sub, fmt in [('svg', 'svg', 'SVG'), ('jpg', 'jpg', 'JPG'), ('pdf', 'pdf', 'PDF'), ('eps', 'eps', 'EPS'), ('webp', 'webp', 'WEBP')]:
        os.makedirs(os.path.join(DST, d, fmt), exist_ok=True)
        for f in sorted(glob.glob(os.path.join(SRC, pat(ext, sub)))):
            scheme = os.path.basename(f)[len(f'bayna-{lk}-'):].rsplit('.', 1)[0]
            if scheme in ('color', 'color-dark', 'on-violet', 'on-lime', 'black', 'white'):
                shutil.copy2(f, os.path.join(DST, d, fmt))
    os.makedirs(os.path.join(DST, d, 'PNG'), exist_ok=True)
    for f in sorted(glob.glob(os.path.join(SRC, f'logo/png/{lk}/*.png'))): shutil.copy2(f, os.path.join(DST, d, 'PNG'))
cptree('fonts', '03_Polices_Fonts')
cp('colors/*', '04_Couleurs_Colors')
cp('icons/favicon.ico', '05_Icones_Icons/Favicons'); cp('icons/png/favicon-*.png', '05_Icones_Icons/Favicons'); cp('icons/png/apple-touch-icon-180.png', '05_Icones_Icons/Favicons'); cp('icons/png/android-chrome-*.png', '05_Icones_Icons/Favicons')
cp('icons/png/app-icon-*.png', '05_Icones_Icons/App-icons'); cp('icons/svg/app-icon-*.svg', '05_Icones_Icons/App-icons')
cp('icons/png/avatar-*.png', '05_Icones_Icons/Photo-de-profil_Profile-pictures'); cp('icons/svg/avatar-*.svg', '05_Icones_Icons/Photo-de-profil_Profile-pictures')
cptree('icons/service-icons', '05_Icones_Icons/Icones-services_Service-icons')
cptree('patterns', '06_Motifs_Patterns')
S = '07_Reseaux-sociaux_Social-media'
for src, dst in [('instagram-posts', '01_Instagram-posts'), ('instagram-carousel', '02_Instagram-carrousel'), ('instagram-stories', '03_Instagram-stories'), ('reel-covers', '04_Reels-covers'),
                 ('instagram-highlight-covers', '05_Instagram-highlights'), ('linkedin-posts', '06_LinkedIn'), ('facebook-posts', '07_Facebook'), ('editable-pptx', '00_MODIFIABLES_Editable-PowerPoint')]:
    cptree(f'social/{src}', f'{S}/{dst}')
B = '08_Bannieres_Banners'
for src, dst in [('social-headers', '01_Couvertures-reseaux_Social-headers'), ('web', '02_Web-email'), ('display-ads', '03_Publicites-web_Display-ads'), ('print', '04_Grand-format_Large-format')]:
    cptree(f'banners/{src}', f'{B}/{dst}')
V = '09_Videos'
cp('video/logo-intro-*.mp4', f'{V}/01_Intro-logo_Logo-intro'); cp('video/logo-intro-transparent-*', f'{V}/02_Logo-anime-transparent_Transparent')
for f in glob.glob(os.path.join(DST, V, '01_Intro-logo_Logo-intro', '*transparent*')): os.remove(f)
cp('video/end-card-*.mp4', f'{V}/03_Fin-de-video_End-cards'); cp('video/lower-third-*', f'{V}/04_Bandeau-nom_Lower-third')
cp('video/reel-template-*.mp4', f'{V}/05_Reel-template'); cp('video/symbol-loop-*.gif', f'{V}/06_GIF'); cp('video/symbol-loop-*.mp4', f'{V}/06_GIF')
cptree('video/stills', f'{V}/07_Miniatures-filigranes_Thumbnails-watermarks')
for f in glob.glob(os.path.join(DST, V, '**', '*-poster.png'), recursive=True): os.remove(f)
P = '10_Impression_Print'
for src, dst in [('business-cards', '01_Cartes-de-visite_Business-cards'), ('nfc-card', '02_Carte-NFC_NFC-card'), ('thank-you-card', '03_Carte-de-remerciement_Thank-you-card'),
                 ('envelope', '04_Enveloppe_Envelope'), ('letterhead', '05_Papier-en-tete-facture_Letterhead-invoice'), ('folder', '06_Chemise_Folder'), ('notebook', '07_Carnet_Notebook'),
                 ('stickers', '08_Stickers'), ('packaging', '09_Emballage-boite_Packaging-box'), ('badge', '10_Badge'), ('signage', '11_Signaletique_Signage')]:
    cptree(f'print/{src}', f'{P}/{dst}')
    pv = os.path.join(DST, P, dst, 'preview')
    if os.path.isdir(pv): os.rename(pv, os.path.join(DST, P, dst, 'Apercus_Previews'))
cptree('presentation', '11_Presentation')
cp('mockups/*.jpg', '12_Mockups'); cp('mockups/*.png', '12_Mockups/PNG')
cp('email-signature/*', '13_Signature-email')
cptree('wallpapers', '14_Fonds-ecran_Wallpapers/Ecran_Desktop-phone'); cptree('virtual-backgrounds', '14_Fonds-ecran_Wallpapers/Visio_Zoom-Teams-Meet')
shutil.copytree(os.path.join(SRC, 'ready-to-use'), os.path.join(DST, '00_PRET-A-L-EMPLOI_READY-TO-USE'), dirs_exist_ok=True)
shutil.copy2(os.path.join(BASE, 'LISEZ-MOI.txt'), os.path.join(DST, '00_LISEZ-MOI_READ-ME.txt'))
print('staged')
