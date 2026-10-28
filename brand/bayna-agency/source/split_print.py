"""Ready-to-use print folder: every print PDF split into separate front / back files, plus PNG/JPG previews."""
import os, glob, subprocess, shutil, sys
os.chdir(sys.argv[1])
SRC = 'print'; DST = 'ready-to-use/13_Impression_Print'
names = {'business-cards': '01_Cartes-de-visite_Business-cards', 'nfc-card': '02_Carte-NFC_NFC-card', 'thank-you-card': '03_Carte-de-remerciement_Thank-you-card', 'envelope': '04_Enveloppe_Envelope',
         'letterhead': '05_Papier-en-tete_Letterhead', 'folder': '06_Chemise_Folder', 'notebook': '07_Carnet_Notebook', 'stickers': '08_Stickers', 'packaging': '09_Emballage_Packaging', 'badge': '10_Badge', 'signage': '11_Signaletique_Signage'}
for folder, nice in names.items():
    for pdf in sorted(glob.glob(f'{SRC}/{folder}/*.pdf')):
        base = os.path.basename(pdf)[:-4]; out = f'{DST}/{nice}/{base}'; os.makedirs(out, exist_ok=True)
        n = int([l for l in subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout.splitlines() if l.startswith('Pages:')][0].split()[1])
        sides = ['recto_front', 'verso_back'] if n == 2 else ([''] if n == 1 else [f'page{i+1}' for i in range(n)])
        for i, side in enumerate(sides):
            tag = f'-{side}' if side else ''
            subprocess.run(['pdfseparate', '-f', str(i+1), '-l', str(i+1), pdf, f'{out}/{base}{tag}-PRINT.pdf'], check=True)
            pv = f'{SRC}/{folder}/preview/{base}-{i+1}.png'
            if os.path.exists(pv):
                shutil.copy2(pv, f'{out}/{base}{tag}.png'); subprocess.run(['convert', pv, '-background', 'white', '-flatten', '-quality', '93', f'{out}/{base}{tag}.jpg'], check=True)
    for extra in glob.glob(f'{SRC}/{folder}/*.docx'): shutil.copy2(extra, f'{DST}/{nice}/')
print('ok')
