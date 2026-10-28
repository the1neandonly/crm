"""Print-ready files (vector PDF, 3 mm bleed unless noted) + PNG previews."""
import os, sys, json
from kit import *
from icons import icon_svg
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/print'); os.makedirs(HT, exist_ok=True)
jobs, previews = [], {}
PAT = lambda n: f'file://{OUT}/patterns/svg/beyna-pattern-{n}.svg'
CSS = '''.pg{position:relative;overflow:hidden;page-break-after:always}
.ink{background:var(--ink);color:#fff}.grad{background:var(--grad);color:#fff}.paper{background:#FBFAFE;color:var(--ink)}.white{background:#fff;color:var(--ink)}
.limebg{background:var(--lime);color:var(--ink)}.violetbg{background:var(--violet);color:#fff}
.a{position:absolute}.big{font-family:Syne;font-weight:700;letter-spacing:-.025em;line-height:1}.hl{color:var(--lime)}.vi{color:var(--violet)}
.lbl{font-weight:700;letter-spacing:.24em;text-transform:uppercase}.ar{font-family:'Readex Pro';font-weight:700;direction:rtl}
.mu{color:#8a8a96}'''
A = lambda inner, st: f'<div class="a" style="{st}">{inner}</div>'
def doc(folder, name, w, h, pages, preview_scale=3):
    """pages: list of (cls, body). Writes one multi-page PDF + one PNG per page."""
    body = ''.join(f'<div class="pg {c}" style="width:{w}mm;height:{h}mm">{b}</div>' for c, b in pages)
    p = f'{HT}/{name}.html'; open(p, 'w').write(page_doc(body, CSS, f'{w}mm {h}mm'))
    jobs.append(dict(html=p, type='pdf', out=f'{OUT}/print/{folder}/{name}.pdf', w=w, h=h, unit='mm'))
    for i, (c, b) in enumerate(pages):
        pp = f'{HT}/{name}-p{i+1}.html'
        open(pp, 'w').write(page_doc(f'<div class="pg {c}" style="width:{w}mm;height:{h}mm">{b}</div>', CSS, f'{w}mm {h}mm'))
        out = f'{OUT}/print/{folder}/preview/{name}-{i+1}.png'
        jobs.append(dict(html=pp, type='png', out=out, w=w, h=h, unit='mm', scale=preview_scale))
        previews[f'{name}-{i+1}'] = out

B = 3  # bleed
# ---------------- Business cards 85x55 (+bleed)
cw, ch = 85 + 2*B, 55 + 2*B
card_front = ('ink', A('', 'width:90mm;height:90mm;right:-48mm;bottom:-56mm;border-radius:50%;background:radial-gradient(circle,rgba(99,55,255,.55),rgba(99,55,255,0) 65%)') +
              A(logo_svg('stacked', 'color-dark', width='36mm'), 'left:50%;top:50%;transform:translate(-50%,-60%)') +
              A(f'<div class="lbl" style="font-size:5.2pt;color:rgba(255,255,255,.55);text-align:center">{TAG_EN} · {CITY}</div>', 'left:0;right:0;bottom:8.5mm'))
def card_back(ar=False):
    nm = 'الاسم واللقب' if ar else NAME; rl = 'المؤسس والمدير الإبداعي' if ar else ROLE
    al = 'right:8mm;text-align:right;direction:rtl;font-family:Readex Pro' if ar else 'left:8mm'
    return ('paper', A(f'<div class="big" style="font-size:11pt;{"font-family:Readex Pro" if ar else ""}">{nm}</div><div style="font-size:6.4pt;color:var(--violet);font-weight:600;margin-top:1.6mm">{rl}</div>', f'top:9.5mm;{al}') +
            A(mark_svg(height='9mm'), f'{"left" if ar else "right"}:8mm;top:9mm') +
            A(f'<div style="font-size:6.4pt;line-height:1.75;font-weight:500;direction:ltr"><b class="vi">T</b>&nbsp;&nbsp;{PHONE}<br><b class="vi">E</b>&nbsp;&nbsp;{MAIL}<br><b class="vi">W</b>&nbsp;&nbsp;{WEB}<br><b class="vi">A</b>&nbsp;&nbsp;{CITY}</div>', f'{"right" if ar else "left"}:8mm;bottom:9.5mm') +
            A('<div style="width:100%;height:100%;background:var(--grad)"></div>', 'left:0;right:0;bottom:0;height:4.4mm') + A('', f'{"left" if ar else "right"}:8mm;bottom:0;width:4.4mm;height:4.4mm;background:var(--lime)'))
doc('business-cards', 'business-card-85x55-bleed3mm', cw, ch, [card_front, card_back()])
doc('business-cards', 'business-card-arabic-85x55-bleed3mm', cw, ch, [card_front, card_back(True)])
doc('business-cards', 'business-card-gradient-85x55-bleed3mm', cw, ch, [
    ('grad', A(mark_svg(body='#fff', height='19mm'), 'left:50%;top:50%;transform:translate(-50%,-58%)') + A('<div class="lbl" style="font-size:5.4pt;text-align:center">beyna agency</div>', 'left:0;right:0;bottom:9mm')),
    ('ink', A(f'<div class="big" style="font-size:11pt">{NAME}</div><div style="font-size:6.4pt;color:var(--lime);font-weight:600;margin-top:1.6mm">{ROLE}</div>', 'left:8mm;top:9.5mm') +
            A(f'<div style="font-size:6.4pt;line-height:1.75;font-weight:500;color:rgba(255,255,255,.85)">{PHONE}<br>{MAIL}<br>{WEB}</div>', 'left:8mm;bottom:9mm') +
            A(logo_svg('horizontal-compact', 'color-dark', width='22mm'), 'right:8mm;bottom:9.4mm'))])

# ---------------- NFC card (CR80 85.6x54, PVC, 2 mm bleed) — tap-to-share
nb = 2; nw, nh = 85.6 + 2*nb, 54 + 2*nb
nfc_glyph = lambda c: f'<svg viewBox="0 0 24 24" width="100%" height="100%" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><path d="M8.5 8.5a5 5 0 0 1 0 7"/><path d="M12 6a8.5 8.5 0 0 1 0 12"/><path d="M15.5 3.5a12 12 0 0 1 0 17"/><circle cx="5" cy="12" r="1.6" fill="{c}" stroke="none"/></svg>'
doc('nfc-card', 'nfc-card-CR80-85.6x54-bleed2mm', nw, nh, [
    ('grad', A(mark_svg(body='rgba(255,255,255,.14)', slice_c=LIME, height='70mm'), 'right:-12mm;top:-6mm') +
             A(logo_svg('horizontal-compact', 'on-violet', width='34mm'), 'left:8mm;top:8mm') +
             A(f'<div style="width:7mm;height:7mm">{nfc_glyph("#fff")}</div>', 'left:8mm;bottom:8mm') +
             A('<div class="lbl" style="font-size:5pt">Tap to connect</div>', 'left:17mm;bottom:9.6mm')),
    ('ink', A(f'<div class="big" style="font-size:10.5pt">{NAME}</div><div style="font-size:6.2pt;color:var(--lime);font-weight:600;margin-top:1.4mm">{ROLE}</div>', 'left:8mm;top:8.5mm') +
            A(f'<div style="font-size:6pt;line-height:1.7;color:rgba(255,255,255,.8)">{PHONE}<br>{MAIL}<br>{WEB}</div>', 'left:8mm;bottom:8mm') +
            A('<div style="width:17mm;height:17mm;border-radius:2.5mm;background:#fff;display:flex;align-items:center;justify-content:center;font:700 5pt Manrope;color:#24242B;text-align:center">QR<br>votre lien</div>', 'right:8mm;bottom:8mm') +
            A(f'<div style="width:6mm;height:6mm">{nfc_glyph(LIME)}</div>', 'right:8mm;top:8mm'))])
doc('nfc-card', 'nfc-tag-sticker-30mm-round', 36, 36, [
    ('grad', A('', 'inset:0;border-radius:50%') + A(f'<div style="width:12mm;height:12mm">{nfc_glyph("#fff")}</div>', 'left:12mm;top:9mm') + A('<div class="lbl" style="font-size:4pt;text-align:center">Tap · beyna</div>', 'left:0;right:0;top:23mm'))])

# ---------------- Thank-you card A6 105x148
tw, th = 105 + 2*B, 148 + 2*B
doc('thank-you-card', 'thank-you-card-A6-bleed3mm', tw, th, [
    ('grad', A(mark_svg(body='rgba(255,255,255,.12)', slice_c='rgba(255,255,255,.12)', height='150mm'), 'right:-50mm;bottom:-40mm') +
             A('<div class="big" style="font-size:30pt;line-height:.95">Merci.</div>', 'left:12mm;top:44mm') +
             A('<div class="ar" style="font-size:24pt;color:var(--lime)">شكراً</div>', 'left:12mm;top:62mm') +
             A('<div class="big" style="font-size:14pt;color:rgba(255,255,255,.75);font-weight:600">Thank you.</div>', 'left:12mm;top:82mm') +
             A(logo_svg('horizontal-compact', 'on-violet', width='30mm'), 'left:12mm;bottom:13mm')),
    ('paper', A('<div class="lbl vi" style="font-size:6pt">Un petit mot · A little note</div>', 'left:12mm;top:14mm') +
              A(''.join('<div style="height:9mm;border-bottom:.25mm solid rgba(36,36,43,.15)"></div>' for _ in range(8)), 'left:12mm;right:12mm;top:22mm') +
              A('<div class="big" style="font-size:9pt">Merci de nous faire confiance.</div><div style="font-size:7pt;margin-top:2mm;color:#6a6a76">Votre marque est entre de bonnes mains. On la rend باينة.</div>', 'left:12mm;bottom:22mm') +
              A(mark_svg(height='9mm'), 'right:12mm;bottom:22mm') +
              A(f'<div style="font-size:6pt;color:#8a8a96">{WEB} · {INSTA}</div>', 'left:12mm;bottom:12mm'))])
doc('thank-you-card', 'thank-you-tag-50x90mm-bleed3mm', 56, 96, [
    ('ink', A(mark_svg(height='22mm'), 'left:50%;top:22mm;transform:translateX(-50%)') + A('<div class="big" style="font-size:17pt;text-align:center">Merci.</div><div class="ar" style="font-size:13pt;text-align:center;color:var(--lime);margin-top:2mm">شكراً</div>', 'left:0;right:0;top:54mm') + A('', 'left:50%;top:7mm;width:5mm;height:5mm;border-radius:50%;background:#FBFAFE;transform:translateX(-50%)'))])

# ---------------- Envelope DL 220x110
doc('envelope', 'envelope-DL-220x110', 220, 110, [
    ('white', A(logo_svg('horizontal', 'color', width='52mm'), 'left:14mm;top:12mm') +
              A(f'<div style="font-size:7pt;line-height:1.6;color:#6a6a76">{CITY}<br>{WEB}</div>', 'left:14mm;top:34mm') +
              A('', 'right:0;bottom:0;width:36mm;height:36mm;background:var(--grad);border-top-left-radius:36mm') + A('', 'right:14mm;bottom:14mm;width:10mm;height:10mm;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%')),
    ('ink', A(f'<div style="width:100%;height:100%;background:url({PAT("ink")}) 0 0/60mm 60mm"></div>', 'inset:0'))])

# ---------------- Letterhead A4 + invoice
lh_head = (A(logo_svg('horizontal', 'color', width='54mm'), 'left:20mm;top:18mm') +
           A(f'<div style="text-align:right;font-size:7.6pt;line-height:1.7;color:#55555F"><b style="color:var(--ink)">Beyna Agency</b><br>{CITY}<br>{PHONE}<br>{MAIL} · {WEB}</div>', 'right:20mm;top:18mm') +
           A('', 'left:20mm;right:20mm;top:44mm;height:.3mm;background:rgba(36,36,43,.12)'))
lh_foot = (A('<div style="display:flex;justify-content:space-between;font-size:7pt;color:#8a8a96;letter-spacing:.04em"><span><b class="vi">Beyna Agency</b> — Marketing &amp; Communication · باينة</span><span>RC 00/00-0000000 · NIF 000000000000000</span></div>', 'left:20mm;right:60mm;bottom:14mm') +
           A('', 'right:0;bottom:0;width:44mm;height:44mm;background:var(--grad);border-top-left-radius:44mm') + A('', 'right:20mm;bottom:20mm;width:14mm;height:14mm;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%'))
doc('letterhead', 'letterhead-A4', 210, 297, [('white', lh_head + lh_foot + A('<div style="font-size:8.5pt;color:#8a8a96">Oran, le __ / __ / ____</div>', 'left:20mm;top:58mm'))], 2)
rows = ''.join(f'<tr><td>Prestation {i}</td><td style="text-align:center">1</td><td style="text-align:right">0,00 DA</td><td style="text-align:right">0,00 DA</td></tr>' for i in range(1, 6))
inv = (lh_head + lh_foot +
       A(f'''<div class="big" style="font-size:30pt">Facture</div><div style="font-size:8pt;color:#6a6a76;margin-top:2mm">N° 0000-2026 · Date : __/__/2026</div>
<div style="display:flex;justify-content:space-between;margin-top:10mm;font-size:8.5pt;line-height:1.6"><div><div class="lbl vi" style="font-size:6pt;margin-bottom:1.5mm">Client</div><b>Nom de l’entreprise</b><br>Adresse<br>RC · NIF · NIS</div>
<div style="text-align:right"><div class="lbl vi" style="font-size:6pt;margin-bottom:1.5mm">Échéance</div>30 jours<br>Virement bancaire</div></div>
<table style="width:100%;border-collapse:collapse;margin-top:10mm;font-size:8.5pt"><thead><tr style="background:var(--ink);color:#fff"><th style="text-align:left;padding:3mm">Désignation</th><th>Qté</th><th style="text-align:right">P.U. HT</th><th style="text-align:right;padding-right:3mm">Total HT</th></tr></thead>
<tbody>{rows.replace("<td>", "<td style='padding:3mm;border-bottom:.25mm solid rgba(36,36,43,.1)'>")}</tbody></table>
<div style="margin-left:auto;width:70mm;margin-top:6mm;font-size:9pt;line-height:2"><div style="display:flex;justify-content:space-between"><span>Total HT</span><b>0,00 DA</b></div><div style="display:flex;justify-content:space-between"><span>TVA 19 %</span><b>0,00 DA</b></div>
<div style="display:flex;justify-content:space-between;background:var(--lime);padding:1mm 3mm;border-radius:2mm;margin-top:1mm"><span>Total TTC</span><b>0,00 DA</b></div></div>''', 'left:20mm;right:20mm;top:58mm'))
doc('letterhead', 'invoice-facture-A4', 210, 297, [('white', inv)], 2)
doc('letterhead', 'quote-devis-A4', 210, 297, [('white', inv.replace('>Facture<', '>Devis<').replace('Échéance', 'Validité').replace('30 jours<br>Virement bancaire', '30 jours<br>Acompte 50 %'))], 2)

# ---------------- Presentation folder (outer spread 2 × A4 + 10 mm spine)
fw, fh = 2*220 + 10 + 2*B, 310 + 2*B
doc('folder', 'presentation-folder-outer-spread', fw, fh, [
    ('ink', A(f'<div style="width:100%;height:100%;background:url({PAT("ink")}) 0 0/80mm 80mm;opacity:.5"></div>', f'left:{B}mm;top:0;bottom:0;width:220mm') +
            A(logo_svg('horizontal-compact', 'color-dark', width='60mm'), f'left:{B+80}mm;bottom:30mm') +
            A(mark_svg(height='190mm'), f'right:-50mm;bottom:-40mm') +
            A(logo_svg('horizontal', 'color-dark', width='110mm'), f'left:{B+230+30}mm;top:36mm') +
            A('<div class="big" style="font-size:44pt">Make it<br><span class="hl">clear.</span></div>', f'left:{B+230+30}mm;top:110mm'))], 1.2)

# ---------------- Notebook A5 cover
doc('notebook', 'notebook-A5-cover-bleed3mm', 148 + 2*B, 210 + 2*B, [
    ('grad', A(mark_svg(body='#fff', height='70mm'), 'left:50%;top:58mm;transform:translateX(-50%)') + A('<div class="lbl" style="font-size:7pt;text-align:center">Notes · ملاحظات</div>', 'left:0;right:0;bottom:22mm')),
    ('ink', A(f'<div style="width:100%;height:100%;background:url({PAT("ink")}) 0 0/50mm 50mm;opacity:.6"></div>', 'inset:0') + A(logo_svg('horizontal-compact', 'color-dark', width='40mm'), 'left:50%;bottom:20mm;transform:translateX(-50%);background:var(--ink);padding:4mm 6mm;border-radius:3mm'))])

# ---------------- Stickers (die-cut, 2 mm bleed)
doc('stickers', 'sticker-symbol-60mm-round', 64, 64, [('grad', A('', 'inset:0;border-radius:50%') + A(mark_svg(body='#fff', height='30mm'), 'left:50%;top:50%;transform:translate(-48%,-50%)'))])
doc('stickers', 'sticker-darija-80x40mm', 84, 44, [('limebg', A('<div class="ar" style="font-size:30pt;color:var(--ink)">باينة!</div>', 'left:0;right:0;top:5mm;text-align:center'))])
doc('stickers', 'sticker-logo-90x30mm', 94, 34, [('ink', A(logo_svg('horizontal-compact', 'color-dark', width='60mm'), 'left:50%;top:50%;transform:translate(-50%,-50%)'))])
doc('stickers', 'sticker-make-it-clear-70mm-round', 74, 74, [('ink', A('<div class="big" style="font-size:20pt;text-align:center;line-height:1">Make it<br><span class="hl">clear.</span></div>', 'left:0;right:0;top:24mm'))])

# ---------------- Packaging: mailer box panels, tape, tissue, bag
doc('packaging', 'mailer-box-lid-300x220mm', 300 + 2*B, 220 + 2*B, [
    ('ink', A(mark_svg(height='190mm'), 'right:-30mm;top:20mm') + A(logo_svg('horizontal', 'color-dark', width='120mm'), 'left:24mm;top:24mm') +
            A('<div class="big" style="font-size:40pt">Make it<br><span class="hl">clear.</span></div>', 'left:24mm;bottom:28mm'))])
doc('packaging', 'mailer-box-inside-lid-300x220mm', 300 + 2*B, 220 + 2*B, [
    ('grad', A('<div class="big" style="font-size:44pt;text-align:center">Merci <span class="hl">!</span></div><div class="ar" style="font-size:30pt;text-align:center;margin-top:6mm;color:var(--lime)">شكراً على ثقتكم</div>', 'left:0;right:0;top:66mm') +
             A(f'<div class="lbl" style="font-size:8pt;text-align:center">{INSTA} · {WEB}</div>', 'left:0;right:0;bottom:22mm'))])
doc('packaging', 'mailer-box-side-300x80mm', 300 + 2*B, 80 + 2*B, [
    ('limebg', A(logo_svg('horizontal-compact', 'on-lime', width='80mm'), 'left:20mm;top:50%;transform:translateY(-50%)') + A('<div class="ar" style="font-size:26pt;color:var(--ink)">خليها باينة</div>', 'right:20mm;top:50%;transform:translateY(-50%)'))])
tape_unit = ''.join(f'<div style="display:inline-flex;align-items:center;gap:8mm;margin-right:14mm">{mark_svg(body="#fff", height="22mm")}<span class="big" style="font-size:20pt;color:#fff">beyna</span><span class="ar" style="font-size:18pt;color:var(--lime)">باينة</span></div>' for _ in range(7))
doc('packaging', 'packing-tape-50mm-repeat-500mm', 500, 50, [('violetbg', A(f'<div style="white-space:nowrap">{tape_unit}</div>', 'left:10mm;top:50%;transform:translateY(-50%)'))], 1.5)
doc('packaging', 'tissue-paper-500x700mm', 500, 700, [('paper', A(f'<div style="width:100%;height:100%;background:url({PAT("paper")}) 0 0/120mm 120mm"></div>', 'inset:0'))], 1)
doc('packaging', 'paper-bag-front-260x330mm', 260 + 2*B, 330 + 2*B, [
    ('ink', A(mark_svg(height='150mm'), 'left:50%;top:70mm;transform:translateX(-50%)') + A(logo_svg('horizontal-compact', 'color-dark', width='80mm'), 'left:50%;bottom:36mm;transform:translateX(-50%)'))])

# ---------------- Staff badge CR80 vertical + lanyard
doc('badge', 'staff-badge-54x85.6mm-bleed2mm', 58, 89.6, [
    ('ink', A('<div style="width:100%;height:100%;background:var(--grad)"></div>', 'left:0;right:0;top:0;height:34mm') + A('', 'left:50%;top:6mm;width:12mm;height:2.6mm;border-radius:2mm;background:var(--ink);transform:translateX(-50%)') +
            A(mark_svg(body='#fff', height='13mm'), 'left:50%;top:14mm;transform:translateX(-50%)') +
            A('<div style="width:24mm;height:24mm;border-radius:50%;background:#3a3a45;border:1.2mm solid var(--ink);display:flex;align-items:center;justify-content:center;font:600 5pt Manrope;color:rgba(255,255,255,.5)">PHOTO</div>', 'left:50%;top:26mm;transform:translateX(-50%)') +
            A(f'<div class="big" style="font-size:10pt;text-align:center">{NAME}</div><div style="font-size:6pt;text-align:center;color:var(--lime);font-weight:700;margin-top:1.5mm">{ROLE}</div>', 'left:3mm;right:3mm;top:56mm') +
            A('<div class="lbl" style="font-size:4.6pt;text-align:center;color:rgba(255,255,255,.5)">Beyna Agency · Staff</div>', 'left:0;right:0;bottom:6mm'))])
lan = ''.join(f'<span style="display:inline-flex;align-items:center;gap:4mm;margin-right:10mm"><span class="big" style="font-size:9pt;color:#fff">beyna</span>{mark_svg(body=LIME, slice_c="#fff", height="8mm")}</span>' for _ in range(14))
doc('badge', 'lanyard-20x450mm', 450, 20, [('violetbg', A(f'<div style="white-space:nowrap">{lan}</div>', 'left:6mm;top:50%;transform:translateY(-50%)'))], 1.5)

# ---------------- Signage
doc('signage', 'office-sign-1200x400mm', 1200, 400, [('ink', A(logo_svg('horizontal', 'color-dark', width='860mm'), 'left:50%;top:50%;transform:translate(-50%,-50%)'))], 0.5)
doc('signage', 'storefront-fascia-3000x600mm', 3000, 600, [
    ('ink', A(logo_svg('bilingual', 'color-dark', width='1500mm'), 'left:200mm;top:50%;transform:translateY(-50%)') + A(mark_svg(height='900mm'), 'right:-160mm;top:-200mm'))], 0.2)
doc('signage', 'door-vinyl-hours-400x300mm', 400, 300, [
    ('white', A(logo_svg('horizontal-compact', 'color', width='150mm'), 'left:30mm;top:30mm') +
              A('<div style="font-size:16pt;line-height:1.8"><b>Dim – Jeu</b> &nbsp; 09:00 – 17:30<br><b>Ven – Sam</b> &nbsp; Fermé</div>', 'left:30mm;top:110mm') +
              A('<div class="ar" style="font-size:16pt;color:var(--violet)">مرحبا بكم</div>', 'left:30mm;bottom:30mm'))], 0.8)
doc('signage', 'wall-mural-3000x2000mm', 3000, 2000, [
    ('grad', A('<div class="big" style="font-size:400mm;line-height:.9">Make it<br><span class="hl">clear.</span></div>', 'left:200mm;top:520mm') +
             A(mark_svg(body='#fff', height='1000mm'), 'right:220mm;bottom:500mm'))], 0.15)

json.dump(jobs, open('jobs_print.json', 'w')); json.dump(previews, open('previews_print.json', 'w')); print(len(jobs))
