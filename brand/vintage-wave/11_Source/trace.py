"""Trace the white logo out of the photo into clean vector paths (potrace)."""
import numpy as np, potrace, sys
from PIL import Image, ImageFilter
src = Image.open(sys.argv[1]).convert('RGB')
def trace(box, scale, out, thr=185, BLUR=1.3):
    im = src.crop(box); im = im.resize((im.width*scale, im.height*scale), Image.LANCZOS).filter(ImageFilter.GaussianBlur(scale*BLUR))
    a = np.asarray(im).astype(int); mn = a.min(axis=2); mx = a.max(axis=2)
    mask = (mn > thr) & (mx - mn < 70)          # bright and unsaturated = the cream logo
    bm = potrace.Bitmap(~mask)
    path = bm.trace(turdsize=60*scale, alphamax=1.25, opticurve=True, opttolerance=0.6)
    parts = []
    for curve in path:
        s = curve.start_point; d = [f'M{s.x/scale:.2f},{s.y/scale:.2f}']
        for seg in curve.segments:
            if seg.is_corner: d.append(f'L{seg.c.x/scale:.2f},{seg.c.y/scale:.2f} L{seg.end_point.x/scale:.2f},{seg.end_point.y/scale:.2f}')
            else: d.append(f'C{seg.c1.x/scale:.2f},{seg.c1.y/scale:.2f} {seg.c2.x/scale:.2f},{seg.c2.y/scale:.2f} {seg.end_point.x/scale:.2f},{seg.end_point.y/scale:.2f}')
        parts.append(''.join(d) + 'Z')
    d = ' '.join(parts)
    xs = [float(v.split(',')[0]) for v in __import__('re').findall(r'-?[\d.]+,-?[\d.]+', d)]; ys = [float(v.split(',')[1]) for v in __import__('re').findall(r'-?[\d.]+,-?[\d.]+', d)]
    open(out, 'w').write(f'{min(xs):.2f} {min(ys):.2f} {max(xs):.2f} {max(ys):.2f}\n{d}\n')
    print(out, len(parts), round(min(xs)), round(min(ys)), round(max(xs)), round(max(ys)))
trace((240, 330, 840, 676), 4, 'symbol.path', BLUR=1.8)
trace((300, 680, 820, 780), 6, "word.path", thr=190, BLUR=0.5)
