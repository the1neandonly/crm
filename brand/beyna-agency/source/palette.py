"""Colour palette files: swatch PNGs, Adobe .ase, GIMP/Inkscape .gpl, CSS, JSON, TXT."""
import os, sys, struct, json
from kit import *
OUT = sys.argv[1] + '/colors'; os.makedirs(OUT, exist_ok=True)
COLS = [('Beyna Violet', '#6337FF'), ('Fluo Lime', '#D2FF5A'), ('Deep Violet', '#1B1046'), ('White', '#FFFFFF'),
        ('Gradient Lavender', '#9A7CFF'), ('Gradient Deep Indigo', '#2B1BB5'), ('Paper', '#F5F4F9')]
rgb = lambda h: tuple(int(h[i:i+2], 16) for i in (1, 3, 5))
def cmyk(h):
    r, g, b = [c/255 for c in rgb(h)]; k = 1 - max(r, g, b)
    return (0, 0, 0, 100) if k == 1 else tuple(round(100*x) for x in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))
# ASE
def ase_block(name, h):
    nm = (name + '\0').encode('utf-16-be'); r, g, b = [c/255 for c in rgb(h)]
    body = struct.pack('>H', len(nm)//2) + nm + b'RGB ' + struct.pack('>fffH', r, g, b, 2)
    return struct.pack('>HI', 0x0001, len(body)) + body
data = b'ASEF' + struct.pack('>HHI', 1, 0, len(COLS)) + b''.join(ase_block(n, h) for n, h in COLS)
open(f'{OUT}/Beyna-palette.ase', 'wb').write(data)
open(f'{OUT}/Beyna-palette.gpl', 'w').write('GIMP Palette\nName: Beyna Agency\nColumns: 4\n#\n' + ''.join('%3d %3d %3d\t%s\n' % (*rgb(h), n) for n, h in COLS))
open(f'{OUT}/Beyna-palette.css', 'w').write(':root {\n' + ''.join(f'  --beyna-{n.lower().replace(" ", "-")}: {h};\n' for n, h in COLS) + f'  --beyna-gradient: linear-gradient(135deg, {G0} 0%, {G1} 55%, {G2} 100%);\n}}\n')
json.dump({n: {'hex': h, 'rgb': rgb(h), 'cmyk': cmyk(h)} for n, h in COLS} | {'Beyna Gradient': {'css': f'linear-gradient(135deg, {G0} 0%, {G1} 55%, {G2} 100%)'}}, open(f'{OUT}/Beyna-palette.json', 'w'), indent=2)
open(f'{OUT}/Beyna-palette.txt', 'w').write('BEYNA AGENCY — باينة — COLOUR PALETTE\n\n' + ''.join(f'{n:<22} HEX {h}   RGB {"%d %d %d" % rgb(h):<12}  CMYK {"%d %d %d %d" % cmyk(h)}\n' for n, h in COLS) +
    f'\nBeyna Gradient: 135°, {G0} 0% → {G1} 55% → {G2} 100%\n\nPantone (nearest — confirm on a swatch book): Violet ≈ 2725 C · Lime ≈ 380 C · Deep Violet ≈ 2765 C\nNever set lime text on white.\n')
# swatch PNG sources
jobs = []; HT = os.path.abspath('html/colors'); os.makedirs(HT, exist_ok=True)
def sw(name, bg, label, sub, fg):
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(f'<div style="width:1000px;height:1000px;background:{bg};color:{fg};position:relative;font-family:Manrope"><div style="position:absolute;left:70px;top:70px;font:700 64px Syne;letter-spacing:-.02em">{label}</div><div style="position:absolute;left:70px;bottom:70px;font:500 30px/1.6 \'JetBrains Mono\'">{sub}</div></div>', '', '1000px 1000px'))
    jobs.append(dict(html=p, type='png', out=f'{OUT}/swatch-{name}.png', w=1000, h=1000, unit='px'))
for n, h in COLS:
    r, g, b = rgb(h); c, m, y, k = cmyk(h)
    sw(n.lower().replace(' ', '-'), h, n, f'HEX {h}<br>RGB {r} {g} {b}<br>CMYK {c} {m} {y} {k}', '#1B1046' if sum(rgb(h)) > 450 else '#fff')
sw('beyna-gradient', f'linear-gradient(135deg,{G0} 0%,{G1} 55%,{G2} 100%)', 'Beyna Gradient', f'135°<br>{G0} → {G1} → {G2}', '#fff')
json.dump(jobs, open('jobs_colors.json', 'w')); print(len(jobs))
