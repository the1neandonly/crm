"""Build editable PowerPoint templates: art layer as a locked background picture, every text block as a live text box."""
import json, re, sys, os
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.enum.shapes import MSO_SHAPE
PX = 9525
FONTS = {'Syne': {500: 'Syne Medium', 600: 'Syne SemiBold', 700: ('Syne', True), 800: 'Syne ExtraBold'},
         'Manrope': {300: 'Manrope Light', 400: 'Manrope', 500: 'Manrope Medium', 600: 'Manrope SemiBold', 700: ('Manrope', True), 800: 'Manrope ExtraBold'},
         'Readex Pro': {400: 'Readex Pro', 500: 'Readex Pro Medium', 600: 'Readex Pro SemiBold', 700: ('Readex Pro', True)}}
def font_for(fam, wt):
    m = FONTS.get(fam, FONTS['Manrope']); wt = int(wt)
    v = m.get(wt) or m[min(m, key=lambda k: abs(k - wt))]
    return (v, False) if isinstance(v, str) else v
def rgb(css):
    n = [float(x) for x in re.findall(r'[\d.]+', css)]
    return RGBColor(int(n[0]), int(n[1]), int(n[2])), (n[3] if len(n) > 3 else 1)

def build(items, out, title):
    prs = Presentation(); w, h = items[0]['w'], items[0]['h']
    prs.slide_width, prs.slide_height = Emu(w*PX), Emu(h*PX)
    for it in items:
        s = prs.slides.add_slide(prs.slide_layouts[6])
        pic = s.shapes.add_picture(it['art'], 0, 0, Emu(w*PX), Emu(h*PX)); pic.name = 'Background (art)'
        for bx in it['boxes']:
            x, y, bw, bh = bx['x'], bx['y'], bx['w'], bx['h']
            fill_c, fa = rgb(bx['bg']) if bx['bg'] else (None, 0)
            if bx['border'] or fa > 0:   # pill buttons: draw the shape, text sits inside
                shp = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Emu(int((x - bw*0.05)*PX)), Emu(int(y*PX)), Emu(int(bw*1.1*PX)), Emu(int(bh*PX)))
                shp.adjustments[0] = 0.5
                if fa > 0: shp.fill.solid(); shp.fill.fore_color.rgb = fill_c
                else: shp.fill.background()
                if bx['border']: shp.line.color.rgb = rgb(bx['border'])[0]; shp.line.width = Emu(int(bx['bw']*PX))
                else: shp.line.fill.background()
                shp.shadow.inherit = False; tb = shp; slack = 0
            else:
                slack = bw*0.12
                tb = s.shapes.add_textbox(Emu(int((x - (slack if bx['align'] == 'right' else 0))*PX)), Emu(int(y*PX)), Emu(int((bw + slack)*PX)), Emu(int(bh*PX)))
            tf = tb.text_frame; tf.word_wrap = not (bx['border'] or fa > 0); tf.auto_size = None
            tf.margin_left = tf.margin_right = Emu(int(bx['padL']*PX)) if bx['border'] or fa > 0 else 0
            tf.margin_top = tf.margin_bottom = 0; tf.vertical_anchor = MSO_ANCHOR.MIDDLE if (bx['border'] or fa > 0) else MSO_ANCHOR.TOP
            p = tf.paragraphs[0]
            def style_par(p):
                p.alignment = {'right': PP_ALIGN.RIGHT, 'center': PP_ALIGN.CENTER}.get(bx['align'], PP_ALIGN.LEFT)
                if bx['border'] or fa > 0: p.alignment = PP_ALIGN.CENTER
                if bx['lh']: p.line_spacing = Pt(bx['lh']*0.75)
                if bx['dir'] == 'rtl': p._p.get_or_add_pPr().set('rtl', '1')
            style_par(p)
            for r in bx['runs']:
                if r.get('br'):
                    p = tf.add_paragraph(); style_par(p); continue
                run = p.add_run(); run.text = r['text'].strip('\n') if r['text'].strip() else r['text']
                f = run.font; name, bold = font_for(r['family'], r['weight']); f.name = name; f.bold = bold
                f.size = Pt(bx['size']*0.75); f.color.rgb = rgb(r['color'])[0]
                rPr = run._r.get_or_add_rPr()
                if bx['ls']: rPr.set('spc', str(int(bx['ls']*0.75*100)))
                if r['family'] == 'Readex Pro':
                    for tag in ('a:latin', 'a:cs'):
                        el = rPr.find(qn(tag))
                        if el is None: el = rPr.makeelement(qn(tag), {}); rPr.append(el)
                        el.set('typeface', name)
            # trim leading spaces created by HTML whitespace
            for para in tf.paragraphs:
                if para.runs: para.runs[0].text = para.runs[0].text.lstrip()
        s.notes_slide.notes_text_frame.text = f"{it['title']} — edit the text boxes; the background is a picture. Fonts: install Syne, Manrope, Readex Pro from /fonts."
    os.makedirs(os.path.dirname(out), exist_ok=True); prs.save(out); print('saved', out, len(items))

if __name__ == '__main__':
    data = json.load(open(sys.argv[1])); OUT = sys.argv[2]
    groups = {}
    for it in data: groups.setdefault(it['group'], []).append(it)
    names = {'instagram-posts': 'Instagram-Posts-1080x1350', 'instagram-carousel': 'Instagram-Carousel-1080x1350', 'instagram-stories': 'Instagram-Stories-1080x1920',
             'reel-covers': 'Reel-Covers-1080x1920', 'presentation': 'Presentation-16x9', 'linkedin-posts': 'LinkedIn-Posts-1200x1200', 'facebook-posts': 'Facebook-Posts-1200x630'}
    for g, items in groups.items():
        build(items, f'{OUT}/Beyna-{names.get(g, g)}-EDITABLE.pptx', g)
