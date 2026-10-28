"""Final delivery: one light ZIP (~60 MB) of the complete catalog."""
import os, sys, shutil, subprocess
from multiprocessing import Pool
from PIL import Image
SRC, DST = sys.argv[1], sys.argv[2]          # complete catalog folder, light copy folder (zip top folder)
shutil.rmtree(DST, ignore_errors=True); shutil.copytree(SRC, DST)
for d in ['09_Videos']:
    for f in os.listdir(os.path.join(DST, d)):
        if '-poster.' in f: os.remove(os.path.join(DST, d, f))
for d in ['10_Mockups', '05_Web-et-applications/08_Fonds-ecran-et-visio']:
    p = os.path.join(DST, d)
    for r, _, fs in os.walk(p):
        for f in fs:
            if f.endswith(('.svg', '.pdf')): os.remove(os.path.join(r, f))
files = [os.path.join(r, f) for r, _, n in os.walk(DST) for f in n]
LOSSLESS = ('02_Logos', 'Goodies', 'Cachet', '06_Icones', 'Favicon')
def png(p):
    a = os.path.getsize(p); im = Image.open(p); im.load(); t = p + '.t.png'
    keep = any(k in p for k in LOSSLESS) or (im.mode == 'RGBA' and im.getextrema()[3][0] < 255)
    if keep: im.save(t, optimize=True)
    else: im.convert('RGB').quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG).save(t, optimize=True)
    if os.path.getsize(t) < a: os.replace(t, p)
    else: os.remove(t)
def jpg(p):
    if '02_Logos' in p: return
    t = p + '.t.jpg'
    subprocess.run(['convert', p, '-quality', '78', '-sampling-factor', '4:2:0', '-strip', '-interlace', 'JPEG', '-density', '300', '-units', 'PixelsPerInch', t], check=True)
    if os.path.getsize(t) < os.path.getsize(p): os.replace(t, p)
    else: os.remove(t)
with Pool(4) as pool:
    pool.map(png, [f for f in files if f.endswith('.png')]); pool.map(jpg, [f for f in files if f.endswith('.jpg')])
print('ok')
