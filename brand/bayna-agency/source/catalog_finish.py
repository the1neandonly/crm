"""JPG + SVG for every item, extra copies, videos, fonts, guidelines, mockups."""
import os, sys, json, shutil, subprocess, glob, base64
G = os.path.dirname(os.path.abspath(__file__)); OUT = sys.argv[1]; SRC = '/home/user/crm/brand/bayna-agency'
cat = json.load(open(os.path.join(G, 'catalog.json')))
def jpg(png, out, srcjpg=None):
    if srcjpg and os.path.exists(srcjpg): shutil.copy2(srcjpg, out)
    else: subprocess.run(['convert', png, '-background', 'white', '-flatten', '-quality', '92', '-sampling-factor', '4:4:4', out], check=True)
for it in cat['items']:
    d = os.path.join(OUT, it['dest']); b = os.path.join(d, it['name'])
    jpg(b + '.png', b + '.jpg', it.get('jpg'))
    subprocess.run(['pdftocairo', '-svg', b + '.pdf', b + '.svg'], check=True)
for it in cat['svgitems']:
    d = os.path.join(OUT, it['dest']); b = os.path.join(d, it['name'])
    shutil.copy2(it['svg'], b + '.svg'); jpg(b + '.png', b + '.jpg', it.get('jpg'))
    if it.get('eps') and os.path.exists(it['eps']): shutil.copy2(it['eps'], b + '.eps')
for c in cat['copies']:
    src, dest = c[0], c[1]; os.makedirs(os.path.join(OUT, dest), exist_ok=True)
    shutil.copy2(src, os.path.join(OUT, dest, c[2] if len(c) > 2 else os.path.basename(src)))
# guidelines, fonts
os.makedirs(f'{OUT}/01_Charte-graphique', exist_ok=True)
shutil.copy2(f'{SRC}/Bayna-Agency-Charte-Graphique-FR.pdf', f'{OUT}/01_Charte-graphique/Bayna-Charte-Graphique-FRANCAIS.pdf')
shutil.copy2(f'{SRC}/Bayna-Agency-Brand-Guidelines.pdf', f'{OUT}/01_Charte-graphique/Bayna-Brand-Guidelines-ENGLISH.pdf')
shutil.copytree(f'{SRC}/fonts', f'{OUT}/03_Polices_Fonts', dirs_exist_ok=True)
# videos (+ poster PNG/JPG)
V = f'{OUT}/09_Videos'; os.makedirs(V, exist_ok=True)
for f in glob.glob(f'{SRC}/video/*'):
    if os.path.isfile(f) and not f.endswith('.mov'): shutil.copy2(f, V)
for f in glob.glob(f'{V}/*-poster.png'):
    jpg(f, f[:-4] + '.jpg')
print('finish ok')
# transparent videos: QuickTime Animation (alpha), far lighter than ProRes
for n in ['logo-intro-transparent-1920x1080', 'lower-third-1920x1080-alpha']:
    shutil.copy2(f'/tmp/claude-0/-home-user-crm/9822160d-7d4c-5a0c-b763-6d89aa660c2f/scratchpad/movlite/{n}-qtrle.mov', f'{V}/{n}.mov')
# mockups: photo scenes → PNG, JPG, PDF and SVG that wrap the image
M = f'{OUT}/10_Mockups'; os.makedirs(M, exist_ok=True)
for f in sorted(glob.glob(f'{SRC}/mockups/*.png')):
    nm = os.path.basename(f)[:-4]; b = f'{M}/bayna-mockup-{nm}'
    shutil.copy2(f, b + '.png'); shutil.copy2(f[:-4] + '.jpg', b + '.jpg')
    subprocess.run(['convert', b + '.jpg', '-density', '150', '-units', 'PixelsPerInch', b + '.pdf'], check=True)
    data = base64.b64encode(open(b + '.jpg', 'rb').read()).decode()
    open(b + '.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 2400 1600" width="2400" height="1600"><image width="2400" height="1600" xlink:href="data:image/jpeg;base64,{data}"/></svg>')
print('videos + mockups ok')
