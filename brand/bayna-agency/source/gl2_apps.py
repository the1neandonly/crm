from gl2_visual import *
def mock(name, en, fr, note, cls='light'):
    n = sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1
    add(f'04 {en}', f'''<div style="width:470px">{head(f"04.{n}", en + ".", fr)}<p style="margin-top:28px;font-size:20px">{note}</p></div>
<div style="position:absolute;right:120px;top:150px;width:1140px;height:760px;border-radius:28px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(18,14,40,.45)">{img(f"mockups/{name}.jpg","width:100%;height:100%;object-fit:cover")}</div>''', cls)
def build_apps():
    toc('Applications', 'Applications', 'Applications')
    divider('04', 'Applications.', 'Applications.', 'How Bayna looks everywhere — on screens, on paper, on products and on the street.')
    P = lambda p, h, extra='': img(p, f'height:{h}px;border-radius:18px;box-shadow:0 24px 50px -20px rgba(18,14,40,.4);{extra}')
    PW = lambda p, w: img(p, f'width:{w}px;border-radius:18px;box-shadow:0 24px 50px -20px rgba(18,14,40,.4)')
    posts = [f'social/instagram-posts/{n}.png' for n in ['01-tagline', '02-services', '03-announcement', '04-testimonial', '05-result', '06-hiring', '07-event', '08-darija', '09-greeting', '10-portfolio']]
    add('04 Instagram posts', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Instagram posts.", "Publications Instagram")}
<p style="margin-top:18px;max-width:1300px">10 post templates (1080 × 1350) — supplied as PNG/JPG and as an <b>editable PowerPoint</b> (works in PowerPoint, Keynote, Google Slides &amp; Canva).</p>
<div style="display:grid;grid-template-columns:repeat(5,250px);gap:18px;margin-top:30px">{"".join(img(p,"width:100%;border-radius:14px;box-shadow:0 20px 40px -18px rgba(18,14,40,.4)") for p in posts)}</div>''')
    car = [f'social/instagram-carousel/{n}.png' for n in ['01-cover', '02-slide', '03-slide', '04-slide', '05-cta']]
    add('04 Carousel', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Carousel.", "Carrousel")}
<p style="margin-top:18px;max-width:1300px">Educational carousels follow one rhythm: a bold cover → one idea per slide → a clear call-to-action.</p>
<div class="row" style="margin-top:50px;gap:14px">{"".join(img(p,"width:320px;border-radius:14px;box-shadow:0 20px 40px -18px rgba(18,14,40,.4)") for p in car)}</div>''')
    st = [f'social/instagram-stories/{n}.png' for n in ['01-new-post', '02-question', '03-offer', '04-link', '05-testimonial', '06-countdown', '07-darija']]
    add('04 Stories', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Stories.", "Stories")}
<div class="row" style="margin-top:44px;gap:16px">{"".join(img(p,"width:220px;border-radius:16px;box-shadow:0 20px 40px -18px rgba(0,0,0,.6)") for p in st)}</div>
<p style="margin-top:30px;max-width:1400px">7 story templates with reserved zones for Instagram stickers (question, link, countdown). Keep text inside the safe zone: 250 px from the top, 340 px from the bottom.</p>''', 'dark')
    hl = ''.join(f'<div style="text-align:center"><img src="{F(f"social/instagram-highlight-covers/highlight-{n}-{v}.png")}" style="width:130px;height:130px;border-radius:50%;object-fit:cover;display:block;box-shadow:0 0 0 4px #fff,0 0 0 6px rgba(36,36,43,.15)"><div style="font-size:15px;font-weight:700;margin-top:14px">{n.title()}</div></div>' for n, v in [('about', 'gradient'), ('services', 'gradient'), ('work', 'ink'), ('clients', 'ink'), ('process', 'gradient'), ('social', 'gradient'), ('video', 'ink'), ('contact', 'ink')])
    add('04 Reels & highlights', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Reels & highlights.", "Reels & stories à la une")}
<div class="row" style="margin-top:44px;gap:60px"><div class="row" style="gap:16px">{"".join(img(f"social/reel-covers/{n}.png","width:230px;border-radius:16px;box-shadow:0 20px 40px -18px rgba(18,14,40,.4)") for n in ["01-tips","02-behind-the-scenes","03-case-study"])}</div>
<div style="flex:1"><div class="lbl vi" style="margin-bottom:26px">Highlight covers · 8 × 2 colourways</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:30px 20px">{hl}</div>
<p style="margin-top:36px;font-size:18px">Reel covers keep the title in the central 1080 × 1440 area so it survives the profile-grid crop.</p></div></div>''')
    vf = 'file:///tmp/claude-0/-home-user-crm/9822160d-7d4c-5a0c-b763-6d89aa660c2f/scratchpad/frames'
    add('04 Video', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Video.", "Vidéo")}
<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:24px;margin-top:40px">
<div><img src="{vf}/logo-intro-16x9-1920x1080/f0149.png" style="width:100%;border-radius:16px;display:block"><div class="lbl hl" style="margin-top:12px">Logo intro · 16:9 · 9:16 · 1:1 · MP4</div></div>
<div><img src="{vf}/lower-third-1920x1080-alpha/f0060.png" style="width:100%;border-radius:16px;display:block;background:#555"><div class="lbl hl" style="margin-top:12px">Lower third · MOV / WebM alpha</div></div>
<div><img src="{vf}/end-card-16x9-1920x1080/f0149.png" style="width:100%;border-radius:16px;display:block"><div class="lbl hl" style="margin-top:12px">End card · 16:9 · 9:16</div></div></div>
<div class="row" style="margin-top:30px;gap:24px;align-items:flex-start"><img src="{F("video/stills/youtube-thumbnail-template-1280x720.png")}" style="width:520px;border-radius:16px">
<div class="row" style="gap:12px">{"".join(f'<img src="{vf}/reel-template-tips-1080x1920/f{n:04d}.png" style="width:120px;border-radius:10px">' for n in (30,100,160,280))}</div>
<p style="flex:1;font-size:17px">Also supplied: transparent logo animation (MOV ProRes 4444 / WebM), animated reel template, looping symbol GIF, watermark PNGs and a story frame overlay.</p></div>''', 'dark')
    add('04 Banners', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Banners & headers.", "Bannières")}
<div class="col" style="margin-top:36px;gap:22px">
<div class="row" style="gap:22px;align-items:flex-start">{PW("banners/social-headers/linkedin-personal-1584x396.png", 960)}{PW("banners/social-headers/x-twitter-header-1500x500.png", 690)}</div>
<div class="row" style="gap:22px;align-items:flex-start">{PW("banners/social-headers/facebook-cover-1640x624.png", 600)}{PW("banners/web/website-hero-1920x800.png", 560)}{PW("banners/web/email-header-1200x400.png", 470)}</div>
<div class="row" style="gap:22px;align-items:flex-start">{PW("banners/social-headers/youtube-channel-art-2560x1440.png", 380)}{PW("banners/web/blog-cover-1600x900.png", 380)}{PW("banners/social-headers/linkedin-company-1128x191.png", 870)}</div></div>''')
    ads = ['300x250', '336x280', '300x600', '160x600', '1080x1080', '1200x628']
    add('04 Display ads', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Display ads.", "Publicité display")}
<div class="row" style="margin-top:40px;gap:22px;align-items:flex-end">{"".join(P(f"banners/display-ads/ad-{a}.png", {"300x250":190,"336x280":210,"300x600":400,"160x600":400,"1080x1080":250,"1200x628":190}[a]) for a in ads)}</div>
<div class="col" style="margin-top:26px;gap:16px"><div class="row" style="gap:20px;align-items:center">{P("banners/display-ads/ad-970x250.png", 120)}{P("banners/display-ads/ad-320x100.png", 100)}</div><div class="row" style="gap:20px;align-items:center">{P("banners/display-ads/ad-728x90.png", 80)}{P("banners/display-ads/ad-320x50.png", 50)}</div></div>''', 'light')
    mock('01-business-cards', 'Business cards', 'Cartes de visite', '85 × 55 mm · 3 mm bleed · French, Arabic and gradient versions. Print on 400 g uncoated or soft-touch laminated board.')
    mock('02-nfc-card', 'NFC card', 'Carte NFC', 'CR80 PVC card (85.6 × 54 mm) with an NFC chip — one tap opens the digital contact card. Matching round NFC sticker.')
    mock('05-stationery-flatlay', 'Stationery', 'Papeterie', 'A4 letterhead (PDF + editable Word), invoice &amp; quote, DL envelope, A5 notebook, stickers.')
    mock('03-thank-you-card', 'Thank-you card', 'Carte de remerciement', 'A6 card (Merci · شكراً · Thank you) with a handwriting side, plus a 50 × 90 mm gift tag.')
    mock('04-packaging-box', 'Packaging', 'Emballage', 'Mailer box (lid, inside lid, sides), branded tape, tissue paper and paper bag artwork.')
    add('04 Packaging artwork', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Packaging artwork.", "Fichiers emballage")}
<div class="row" style="margin-top:44px;gap:22px;align-items:flex-start">{P("print/packaging/preview/mailer-box-lid-300x220mm-1.png", 330)}{P("print/packaging/preview/mailer-box-inside-lid-300x220mm-1.png", 330)}{P("print/packaging/preview/paper-bag-front-260x330mm-1.png", 330)}</div>
<div class="row" style="margin-top:24px;gap:22px">{P("print/packaging/preview/mailer-box-side-300x80mm-1.png", 120)}{P("print/packaging/preview/tissue-paper-500x700mm-1.png", 230)}</div>
<div style="margin-top:20px">{P("print/packaging/preview/packing-tape-50mm-repeat-500mm-1.png", 70)}</div>''')
    mock('06-merch', 'Merch', 'Goodies', 'T-shirt (chest symbol + wordmark), tote bag, mug. Use the SVG / PDF logos for screen printing and embroidery.')
    mock('07-badge-lanyard', 'Staff badge', 'Badge', 'Vertical CR80 badge with photo zone and a repeating violet lanyard (20 × 450 mm).')
    mock('13-stickers', 'Stickers', 'Stickers', 'Die-cut stickers: symbol, logo, “باينة!” and “Make it clear.” — plus the NFC tag.')
    mock('11-instagram-phone', 'Instagram', 'Instagram', 'Profile with highlight covers and the post grid — every template in the kit working together.')
    mock('12-website-laptop', 'Website', 'Site web', 'Hero banner, service icons and the colour system applied to the agency website.')
    mock('08-office-signage', 'Office signage', 'Signalétique', 'Office sign 1200 × 400 mm on standoffs — dibond or acrylic. Vector PDF supplied.')
    mock('09-storefront', 'Storefront', 'Façade', 'Bilingual fascia 3000 × 600 mm and opening-hours door vinyl.')
    mock('14-wall-mural', 'Reception wall', 'Accueil', 'Wall mural 3000 × 2000 mm for the reception or meeting room.')
    mock('10-rollup-billboard', 'Roll-up & billboard', 'Kakémono & affichage', 'Roll-up 850 × 2000 mm (real size) and a 4 × 3 m billboard (1:10 scale), both vector PDF.')
    add('04 Presentations & email', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Presentations & email.", "Présentations & e-mail")}
<div class="row" style="margin-top:40px;gap:20px">{"".join(P(f"presentation/preview/{n}.png", 230) for n in ["01-cover","03-section","04-content"])}</div>
<div class="row" style="margin-top:20px;gap:20px">{"".join(P(f"presentation/preview/{n}.png", 230) for n in ["05-key-figure","06-three-columns","07-thank-you"])}</div>
<div class="row" style="margin-top:26px;gap:24px;align-items:center">{P("email-signature/email-signature-fr-600x180.png", 130)}{P("email-signature/email-signature-ar-600x180.png", 130)}<p style="font-size:17px;flex:1">7-slide editable PowerPoint · email signatures in French &amp; Arabic.</p></div>''')
    add('04 Wallpapers & backgrounds', f'''{head(f"04.{sum(1 for p in PAGES if p and p[0].startswith('04 ')) + 1}", "Wallpapers & video calls.", "Fonds d’écran & visio")}
<div class="row" style="margin-top:44px;gap:22px;align-items:flex-start"><div class="col" style="gap:22px">{P("wallpapers/desktop-ink-2560x1440.png", 250)}{P("virtual-backgrounds/virtual-background-ink-1920x1080.png", 250)}</div>
<div class="col" style="gap:22px">{P("wallpapers/desktop-pattern-2560x1440.png", 250)}{P("virtual-backgrounds/virtual-background-paper-1920x1080.png", 250)}</div>
{P("wallpapers/phone-ink-1290x2796.png", 520)}{P("wallpapers/phone-pattern-1290x2796.png", 520)}</div>''', 'dark')

def build_toolkit():
    toc('Toolkit', 'Toolkit', 'Boîte à outils')
    folders = [('logo/', 'SVG · PNG · JPG · WEBP · PDF · EPS — 8 lockups × 6 colourways'), ('fonts/', 'Syne, Manrope, Readex Pro (TTF + licence)'), ('icons/', 'Favicons, app icons, avatars, 16 service icons'),
               ('patterns/', '5 seamless patterns (SVG + PNG)'), ('social/', 'Posts, carousel, stories, reels, highlights + editable PPTX'), ('banners/', 'Social headers, web, 10 ad sizes, roll-up, billboard, poster'),
               ('video/', 'Logo intros, end cards, lower third, reel, GIF, thumbnails'), ('print/', 'Cards, NFC, thank-you, envelope, letterhead, invoice, folder, packaging, badge, signage'),
               ('presentation/', 'Editable 16:9 PowerPoint'), ('mockups/', '14 mockup scenes (PNG + JPG)'), ('wallpapers/ · virtual-backgrounds/', 'Desktop, phone, Zoom / Teams / Meet'), ('email-signature/', 'French & Arabic')]
    add('05 Toolkit', f'''{head("05", "What’s in the kit.", "Contenu du kit")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 70px;margin-top:46px">{"".join(f'<div style="display:flex;gap:26px;align-items:baseline;padding:18px 0;border-top:1px solid var(--line)"><span class="mono vi" style="font-size:19px;width:340px;flex:none">{a}</span><span style="font-size:19px">{b}</span></div>' for a,b in folders)}</div>
<div class="row" style="margin-top:40px;gap:30px">{"".join(f'<div style="flex:1;background:{bg};color:{c};border-radius:22px;padding:26px 30px"><div class="lbl" style="opacity:.75">{t}</div><div style="font-size:18px;margin-top:10px;line-height:1.5">{d}</div></div>' for t,d,bg,c in [("Before printing","Replace the placeholder name, phone, e-mail, website, RC &amp; NIF. Confirm Pantone references with your printer.","var(--ink)","#fff"),("Editing templates","Install the fonts first, then open the .pptx / .docx files. Backgrounds are locked pictures; text stays live.","#fff","var(--ink)"),("Questions","Keep this guide with every supplier: printers, developers, photographers, video editors.","var(--lime)","var(--ink)")])}</div>''')
    add('', f'''<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-62%);text-align:center">{logo_svg("bilingual-stacked","on-violet",width=560)}
<div class="big" style="font-size:52px;margin-top:70px">Make it clear.</div><div style="font-size:24px;margin-top:12px;color:rgba(255,255,255,.8)">L’évidence, par le design. &nbsp;·&nbsp; <span class="ar">خليها باينة</span></div></div>
<div style="position:absolute;left:120px;right:120px;bottom:70px;display:flex;justify-content:space-between;font-size:17px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.75)"><span>Bayna Agency</span><span>Oran, Algérie</span><span>{WEB}</span></div>''', 'gradp', chrome=False)

if __name__ == '__main__':
    build_brand(); build_logo(); build_visual(); build_apps(); build_toolkit()
    # contents (index 1) — page numbers known now
    groups = {}
    for part, en, fr, idx in TOC: groups.setdefault(part, []).append((en, fr, idx))
    parts = [('01', 'The brand', 'La marque', TOC[0][3]), ('02', 'Logo', 'Le logo', TOC[1][3]), ('03', 'Visual system', 'Système visuel', TOC[2][3]), ('04', 'Applications', 'Applications', TOC[3][3]), ('05', 'Toolkit', 'Boîte à outils', TOC[4][3])]
    def secs(lo, hi): return [(s, i) for i, p in enumerate(PAGES) if p and lo <= i < hi and p[0] and i not in (lo,) for s in [p[0]]]
    bounds = [p[3] for p in parts] + [len(PAGES)]
    cols = ''
    for k, (n, en, fr, start) in enumerate(parts):
        subs = []; seen = set()
        for i in range(start, bounds[k+1]):
            pg = PAGES[i]
            if pg and pg[0] and pg[0] not in seen:
                seen.add(pg[0]); subs.append((pg[0].split(' ', 1)[1] if ' ' in pg[0] else pg[0], i + 1))
        cols += (f'<div style="break-inside:avoid;margin-bottom:34px"><div style="display:flex;gap:18px;align-items:baseline;border-bottom:2px solid var(--ink);padding-bottom:10px"><span class="mono vi" style="font-size:18px">{n}</span><span class="big" style="font-size:28px">{en}</span><span class="muted" style="font-size:17px">{fr}</span><span class="mono muted" style="margin-left:auto;font-size:16px">p.{start+1:02d}</span></div>'
                 + ''.join(f'<div style="display:flex;font-size:14px;padding:3px 0;border-bottom:1px solid var(--line)"><span>{t}</span><span class="mono muted" style="margin-left:auto">{pn:02d}</span></div>' for t, pn in subs) + '</div>')
    PAGES[1] = ('Contents', 'light', f'{head("00", "Contents.", "Sommaire")}<div style="column-count:4;column-gap:56px;margin-top:28px">{cols}</div>', True)
    n = render(f'{HT}/guidelines2.html'); print('pages', n)
