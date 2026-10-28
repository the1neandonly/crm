import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os
FONTDIR = os.path.join(os.path.dirname(__file__), '..', 'fonts')
_cache = {}
def _load(name):
    if name not in _cache:
        p = os.path.join(FONTDIR, name)
        blob = hb.Blob.from_file_path(p)
        face = hb.Face(blob); font = hb.Font(face)
        _cache[name] = (TTFont(p), font, face.upem)
    return _cache[name]
def text_path(text, fontname, size, x=0, y=0, tracking=0.0, anchor='start'):
    """Return (svg path d, width). y = baseline. tracking in em units."""
    tt, font, upem = _load(fontname)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    s = size / upem
    pen_x = 0; parts = []
    infos, poss = buf.glyph_infos, buf.glyph_positions
    total = sum(p.x_advance for p in poss) + tracking*upem*(len(poss)-1)
    w = total * s
    ox = x - (w if anchor=='end' else w/2 if anchor=='middle' else 0)
    for i,(inf,pos) in enumerate(zip(infos,poss)):
        gname = order[inf.codepoint]
        sp = SVGPathPen(gs)
        tp = TransformPen(sp, (s,0,0,-s, ox + (pen_x+pos.x_offset)*s, y - pos.y_offset*s))
        gs[gname].draw(tp)
        parts.append(sp.getCommands())
        pen_x += pos.x_advance + tracking*upem
    return ' '.join(parts), w
def cap_height(fontname, size):
    tt,_,upem = _load(fontname)
    os2 = tt['OS/2']; return getattr(os2,'sCapHeight',700)*size/upem
def x_height(fontname, size):
    tt,_,upem = _load(fontname)
    return getattr(tt['OS/2'],'sxHeight',500)*size/upem
def ascender_b(fontname, size):
    """height of 'b' glyph top"""
    tt,_,upem = _load(fontname)
    gs = tt.getGlyphSet(); from fontTools.pens.boundsPen import BoundsPen
    bp = BoundsPen(gs); gs[tt.getBestCmap()[ord('b')]].draw(bp); return bp.bounds[3]*size/upem
