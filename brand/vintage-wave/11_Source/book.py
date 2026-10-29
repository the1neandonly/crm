"""Vintage Wave brand guidelines — 1920x1080 pages."""
import os
from base import *
from apps import *
PAGES, SECTIONS = [], []
BCSS = '''
.pg{width:1920px;height:1080px;position:relative;overflow:hidden;background:var(--cr);page-break-after:always;padding:120px 120px 100px}
.pg.dark{background:var(--es);color:var(--cr)} .pg.rust{background:var(--ru);color:var(--cr)} .pg.kraft{background:var(--kr)}
.hd{position:absolute;left:120px;right:120px;top:50px;display:flex;justify-content:space-between;font:700 13px 'DM Sans';letter-spacing:.24em;opacity:.55}
.ft{position:absolute;left:120px;right:120px;bottom:40px;display:flex;justify-content:space-between;font:500 13px 'DM Sans';letter-spacing:.14em;opacity:.45}
.eb{font:700 15px 'DM Sans';letter-spacing:.26em;color:var(--ru);text-transform:uppercase} .dark .eb,.rust .eb{color:var(--am)}
h1{font:900 150px/.92 Fraunces;letter-spacing:-.02em} h2{font:900 70px/1.02 Fraunces;letter-spacing:-.015em;margin-top:14px} h2 i,h1 i{font-weight:600;color:var(--ru)} .dark h2 i,.dark h1 i,.rust h1 i{color:var(--am)}
h3{font:700 26px/1.2 Fraunces}
p{font:400 20px/1.6 'DM Sans';color:#5A4036} .dark p,.rust p{color:rgba(243,236,225,.78)}
.card{background:#FBF7F0;border:1.5px solid rgba(42,23,18,.12);border-radius:10px} .dark .card{background:#3A2219;border-color:rgba(243,236,225,.12)}
.row{display:flex;gap:28px} .lbl{font:700 13px 'DM Sans';letter-spacing:.2em;text-transform:uppercase;opacity:.6}
table.t{border-collapse:collapse;width:100%} table.t td{padding:12px 0;border-top:1.5px solid rgba(42,23,18,.14);font:400 18px 'DM Sans'} table.t td:first-child{font-weight:700;width:30%}
.cap{font:500 14px 'DM Sans';letter-spacing:.06em;opacity:.6;margin-top:12px}
.pg .grain{display:none} .pg.cover .grain{display:block}
'''
def page(sec, title, body, cls=''):
    PAGES.append(f'<section class="pg {cls}"><div class="hd"><span>VINTAGE WAVE — BRAND GUIDELINES</span><span>{sec} · {title.upper()}</span></div>{body}<div class="ft"><span>v1.0 · 2026</span><span>{len(PAGES)+1:02d}</span></div></section>')
def head(num, t, sub=''):
    return f'<div class="eb">{num}</div><h2>{t}</h2>' + (f'<p style="max-width:1100px;margin-top:18px">{sub}</p>' if sub else '')
def fit(w, h, html, s): return f'<div style="width:{w*s:.0f}px;height:{h*s:.0f}px;position:relative;overflow:hidden"><div style="position:absolute;left:0;top:0;width:{w}px;height:{h}px;transform:scale({s});transform-origin:0 0">{html}</div></div>'
def art(name, s, shadow=True):
    w, h, b = ARTBOARDS[name](); return f'<div style="{"box-shadow:0 18px 40px rgba(42,23,18,.18)" if shadow else ""}">{fit(w, h, b, s)}</div>'
def divider(num, t, sub, cls='dark'):
    SECTIONS.append((num, t, len(PAGES) + 1))
    PAGES.append(f'<section class="pg {cls}"><div style="position:absolute;right:-200px;top:50%;transform:translateY(-50%);opacity:.09">{logo("symbol", "cream", height=760)}</div>'
                 f'<div style="position:absolute;left:120px;bottom:140px"><div class="eb">{num}</div><h1 style="margin-top:24px">{t}</h1><p style="max-width:760px;margin-top:30px">{sub}</p></div>'
                 f'<div class="grain l"></div><div class="ft"><span>v1.0 · 2026</span><span>{len(PAGES)+1:02d}</span></div></section>')
# Cover + contents
PAGES.append(f'''<section class="pg dark cover"><div style="position:absolute;left:50%;top:45%;transform:translate(-50%,-50%)">{logo("stacked", "cream", width=760)}</div>
<div style="position:absolute;left:0;right:0;bottom:120px;text-align:center;font:700 16px DM Sans;letter-spacing:.4em;opacity:.7">BRAND GUIDELINES · THRIFT & VINTAGE ONLINE STORE · 2026</div><div class="grain l"></div></section>''')
TOC = len(PAGES); PAGES.append('')
# 01 Brand
divider('01', 'The <i>brand</i>', 'A second life for clothes with a first story. Who we are, what we believe, how we speak.')
page('01', 'Story', f'''<div class="row" style="gap:90px;align-items:center;height:100%"><div style="width:860px">{head("01.1 — Our story", "Every piece has <i>already lived.</i>")}
<p style="margin-top:30px;font-size:22px">Vintage Wave started with a pile of forgotten jackets and a simple idea: the best clothes are often the ones already made. We hunt, clean, mend, measure and photograph each piece by hand, then send it out on its next wave — to someone who will love it again.</p>
<p style="margin-top:20px;font-size:22px">The symbol says it: a sun rising over two waves. The first wave is the life a piece already had. The second is the one it starts with you.</p></div>
<div style="flex:1;display:flex;justify-content:center">{logo("badge", "rust", width=520)}</div></div>''')
vals = [('Curated', 'Fewer, better pieces. Every item is chosen, not dumped.'), ('Honest', 'Real photos, real flaws, real measurements. No surprises.'), ('Circular', 'Keep clothes in use. Buy back, resell, repair.'), ('Warm', 'Hand-written notes, slow replies done well, a community — not a warehouse.')]
page('01', 'Mission & values', f'''{head("01.2 — Mission & values", "Make second-hand <i>the first choice.</i>")}
<div class="row" style="margin-top:56px">{"".join(f'<div class="card" style="flex:1;padding:36px;height:470px;position:relative"><div style="font:900 70px Fraunces;color:var(--ru)">0{k+1}</div><h3 style="font-size:36px;margin-top:20px">{t}</h3><p style="margin-top:16px">{d}</p></div>' for k, (t, d) in enumerate(vals))}</div>''')
voice_ex = [('Product description', 'Classic 80s trucker in medium stonewash. Soft from years of wear, copper buttons intact. Light fading on the collar — see photo 4. Fits like a modern M/L.'),
            ('Instagram caption', 'Friday 19:00. 48 pieces, one of each. Wool for the first cold mornings, denim that already knows how to fade. Set your alarm.'),
            ('DM reply', 'Hi Sara! Yes, it’s still available. Pit to pit is 56 cm, length 64 cm. I can hold it for you until tonight — shall I?'),
            ('Sold out', 'All gone in 41 minutes. Thank you for giving these pieces a second life. Next drop: Friday, same time.')]
page('01', 'Voice', f'''{head("01.3 — Voice", "Warm, <i>honest</i>, a little nostalgic.", "We talk like a friend who knows clothes: specific about the piece, open about flaws, never pushy. Short sentences. Real numbers. A touch of story.")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:40px">{"".join(f'<div class="card" style="padding:26px 30px"><div class="lbl">{t}</div><p style="margin-top:10px;font-size:19px;color:var(--es)">{d}</p></div>' for t, d in voice_ex)}</div>
<div class="row" style="margin-top:22px;gap:22px"><div class="card" style="flex:1;padding:20px 26px"><b style="color:var(--sa)">We say</b> <span style="font:400 17px DM Sans">pre-loved · one of a kind · found a new home · honest wear</span></div><div class="card" style="flex:1;padding:20px 26px"><b style="color:var(--ru)">We avoid</b> <span style="font:400 17px DM Sans">used · cheap · old stuff · “perfect condition” when it isn’t</span></div></div>''')
aud = [('The style hunter', '18–30 · wants pieces nobody else has · follows drops, shares finds.'), ('The conscious buyer', '25–40 · buys less, buys better · cares where clothes come from.'), ('The collector', 'Any age · knows brands and eras · checks labels, stitching, fabric.')]
page('01', 'Audience', f'''{head("01.4 — Who we dress", "Three kinds of <i>treasure hunters.</i>")}
<div class="row" style="margin-top:56px">{"".join(f'<div class="card" style="flex:1;padding:36px"><div style="height:240px;border-radius:8px;overflow:hidden">{photo(g, 470, 240, b, f)}</div><h3 style="font-size:32px;margin-top:26px">{t}</h3><p style="margin-top:12px">{d}</p></div>' for (t, d), (g, b, f) in zip(aud, [("jacket", KRAFT, DENIM), ("sweater", "#E3D6C3", RUST), ("bag", "#EADCC6", MAPLE)]))}</div>''')
# 02 Logo
divider('02', 'The <i>logo</i>', 'A sun over two waves: the life a piece had, and the one it starts with you.')
page('02', 'The logo', f'''<div class="row" style="gap:80px;align-items:center;height:100%"><div style="flex:1;display:flex;justify-content:center">{logo("stacked", "espresso", width=700)}</div>
<div style="width:640px">{head("02.1 — Primary logo", "Symbol <i>+</i> wordmark.")}<table class="t" style="margin-top:36px"><tr><td>The sun</td><td>A rising sun or pearl — the find, the treasure.</td></tr><tr><td>Wave one</td><td>The first life of the garment.</td></tr><tr><td>Wave two</td><td>Its second life, with a new owner.</td></tr><tr><td>Wordmark</td><td>Hand-cut capitals, kept exactly as drawn — never retyped.</td></tr></table>
<p style="margin-top:24px;font-size:17px">The artwork is a faithful vector rebuild of the original logo — use only the supplied files.</p></div></div>''')
page('02', 'Lockups', f'''{head("02.2 — Lockups", "One family, <i>six shapes.</i>")}
<div style="display:grid;grid-template-columns:1fr 1.4fr 1fr;gap:22px;margin-top:40px">
{"".join(f'<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo(k, "espresso", **sz)}<div class="cap" style="position:absolute;left:22px;bottom:16px">{c}</div></div>' for k, c, sz in [("stacked", "Primary · stacked", {"height": 220}), ("horizontal", "Horizontal · website, email", {"width": 560}), ("badge", "Badge · stickers, boxes, tags", {"height": 250}), ("symbol", "Symbol · profile picture, favicon", {"height": 170}), ("tagline", "Wordmark + descriptor · labels", {"width": 560}), ("wordmark", "Wordmark · small spaces", {"width": 360})])}</div>''')
cs_w = 620; X = cs_w*0.16
page('02', 'Clear space', f'''{head("02.3 — Clear space & sizes", "Give it <i>room to breathe.</i>")}
<div class="row" style="margin-top:50px;gap:80px;align-items:flex-start"><div class="card" style="padding:60px"><div style="position:relative;padding:{X:.0f}px;outline:2px dashed rgba(166,61,30,.5)">{logo("stacked", "espresso", width=cs_w)}
{"".join(f'<div style="position:absolute;{pos};width:{X:.0f}px;height:{X:.0f}px;background:rgba(166,61,30,.10);display:flex;align-items:center;justify-content:center;font:900 22px Fraunces;color:var(--ru)">S</div>' for pos in ["left:0;top:0", "right:0;top:0", "left:0;bottom:0", "right:0;bottom:0"])}</div>
<p style="margin-top:22px;font-size:17px;max-width:{cs_w + 2*X:.0f}px">Clear space = S, the diameter of the sun in the symbol, on every side.</p></div>
<div style="flex:1"><table class="t"><tr><td>Primary · stacked</td><td>min. 120 px · 30 mm</td></tr><tr><td>Horizontal</td><td>min. 160 px · 40 mm</td></tr><tr><td>Badge</td><td>min. 90 px · 22 mm</td></tr><tr><td>Symbol</td><td>min. 24 px · 6 mm</td></tr><tr><td>Wordmark</td><td>min. 90 px · 20 mm</td></tr></table></div></div>''')
tiles = [('cream', ESPRESSO, 'Cream on espresso · primary'), ('espresso', CREAM, 'Espresso on cream'), ('rust', CREAM, 'Rust on cream'), ('amber', ESPRESSO, 'Amber on espresso'), ('cream', RUST, 'Cream on rust'), ('espresso', KRAFT, 'Espresso on kraft'), ('black', '#FFFFFF', 'Black · one colour'), ('white', '#6B5248', 'White · on photos')]
page('02', 'Colour versions', f'''{head("02.4 — Colour versions", "Always <i>one colour</i>, always contrast.")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px">{"".join(f'<div style="height:300px;border-radius:10px;background:{bg};display:flex;align-items:center;justify-content:center;position:relative">{logo("stacked", s, height=190)}<div style="position:absolute;left:18px;bottom:12px;font:700 13px DM Sans;letter-spacing:.1em;color:{"#FFF" if bg in (ESPRESSO, RUST, "#6B5248") else ESPRESSO};opacity:.7">{c}</div></div>' for s, bg, c in tiles)}</div>''')
hz = lambda st='', s='espresso', h=180: logo('stacked', s, height=h, style=st)
donts = [(hz('transform:scaleX(1.4) scaleY(.8)'), 'Stretch'), (hz('transform:rotate(-14deg)'), 'Rotate'), (hz(s='amber'), 'Low contrast'), (hz('filter:drop-shadow(8px 10px 4px rgba(0,0,0,.5))'), 'Add effects'),
         (f'<div style="display:flex;align-items:center;gap:16px">{logo("wordmark", "espresso", width=220)}{logo("symbol", "espresso", height=50)}</div>', 'Rearrange'), (f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px">{logo("symbol", "espresso", height=110)}<span style="font:italic 700 40px Georgia,serif">Vintage Wave</span></div>', 'Retype'),
         (f'<div style="display:flex;flex-direction:column;align-items:center">{logo("symbol", "rust", height=110)}{logo("wordmark", "espresso", width=260)}</div>', 'Mix colours'), (f'<div style="background:{photo("jacket", 300, 220, KRAFT, DENIM, grain=False)};position:relative">{photo("jacket", 300, 220, KRAFT, DENIM, grain=False)}<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{logo("stacked", "rust", height=150)}</div></div>', 'Busy photos')]
page('02', 'Misuse', f'''{head("02.5 — Misuse", "Please <i>don’t.</i>")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px">{"".join(f'<div class="card" style="height:300px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;{"background:"+ESPRESSO if t == "Low contrast" else ""}">{i}<div style="position:absolute;left:18px;bottom:12px;font:700 14px DM Sans;color:{RUST}">✕ {t}</div></div>' for i, t in donts)}</div>''')
# 03 Colour
divider('03', 'The <i>colours</i>', 'Taken from autumn leaves, faded denim and kraft paper.', 'rust')
from logo import ESPRESSO as E
pal = [('Espresso', ESPRESSO, 'Base · dark backgrounds, text'), ('Cream', CREAM, 'Base · light backgrounds, logo on dark'), ('Rust', RUST, 'Accent · drops, sale, highlights'), ('Amber', AMBER, 'Accent · prices, italics on dark'),
       ('Maple', MAPLE, 'Deep accent · sold, contrast'), ('Denim', DENIM, 'Cool accent · the wave'), ('Sage', SAGE, 'Natural accent · mint grade'), ('Kraft', KRAFT, 'Packaging · backdrops')]
def hex2rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [c/255 for c in hex2rgb(h)]; k = 1 - max(r, g, b); return tuple(round(100*v) for v in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))
def sw(n, h, d, big):
    r, g, b = hex2rgb(h); c, m, y, k = cmyk(h); tc = CREAM if sum(hex2rgb(h)) < 400 else ESPRESSO
    return (f'<div style="border-radius:10px;overflow:hidden;border:1.5px solid rgba(42,23,18,.12)"><div style="height:{250 if big else 150}px;background:{h};padding:20px;color:{tc};display:flex;flex-direction:column;justify-content:space-between"><div style="font:900 {32 if big else 22}px Fraunces">{n}</div><div style="font:700 {20 if big else 15}px DM Sans">{h.upper()}</div></div>'
            f'<div style="padding:12px 20px;background:#FBF7F0;font:400 14px DM Sans;line-height:1.6">RGB {r} {g} {b} · CMYK {c} {m} {y} {k}<br><span style="opacity:.7">{d}</span></div></div>')
page('03', 'Palette', f'''{head("03.1 — Palette", "Warm, <i>worn-in</i> colours.")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:34px">{"".join(sw(*p, True) for p in pal[:4])}</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:18px">{"".join(sw(*p, False) for p in pal[4:])}</div>''')
page('03', 'Proportions', f'''{head("03.2 — Proportions & pairs", "Mostly <i>cream and espresso.</i>")}
<div style="margin-top:46px;height:160px;display:flex;border-radius:10px;overflow:hidden"><div style="flex:45;background:{CREAM};border:1.5px solid rgba(42,23,18,.12);padding:22px;font:700 20px DM Sans">Cream 45 %</div><div style="flex:30;background:{ESPRESSO};color:{CREAM};padding:22px;font:700 20px DM Sans">Espresso 30 %</div><div style="flex:12;background:{RUST};color:{CREAM};padding:22px;font:700 18px DM Sans">Rust 12 %</div><div style="flex:7;background:{AMBER};padding:22px 14px;font:700 16px DM Sans">Amber</div><div style="flex:6;background:linear-gradient(90deg,{DENIM},{SAGE},{KRAFT})"></div></div>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:16px;margin-top:40px">{"".join(f'<div style="height:200px;border-radius:10px;background:{b};color:{f};display:flex;flex-direction:column;justify-content:center;align-items:center;gap:6px"><div style="font:900 52px Fraunces">Aa</div><div style="font:700 13px DM Sans;letter-spacing:.1em">{n}</div></div>' for b, f, n in [(ESPRESSO, CREAM, "CREAM / ESPRESSO"), (CREAM, ESPRESSO, "ESPRESSO / CREAM"), (RUST, CREAM, "CREAM / RUST"), (ESPRESSO, AMBER, "AMBER / ESPRESSO"), (AMBER, ESPRESSO, "ESPRESSO / AMBER"), (KRAFT, ESPRESSO, "ESPRESSO / KRAFT")])}</div>
<p style="margin-top:22px;font-size:17px">Never set amber or kraft text on cream — too little contrast. Denim and sage stay small: icons, grades, details.</p>''')
# 04 Type
divider('04', 'The <i>type</i>', 'A soft vintage serif, a clean sans and a hand-written note.')
page('04', 'Families', f'''{head("04.1 — Typefaces", "Three voices, <i>one tone.</i>")}
<div class="row" style="margin-top:44px"><div class="card" style="flex:1.3;padding:40px;height:600px"><div class="lbl">Fraunces · headlines</div><div style="font:900 170px/1 Fraunces;margin-top:24px">Aa <i style="font-weight:600;color:var(--ru)">Aa</i></div><p style="margin-top:30px;color:var(--es)">Black 900 for headlines, SemiBold Italic for the warm, nostalgic word. Soft, retro, editorial.</p></div>
<div class="card" style="flex:1;padding:40px;height:600px"><div class="lbl">DM Sans · text & UI</div><div style="font:700 150px/1 DM Sans;margin-top:30px">Aa</div><p style="margin-top:30px;color:var(--es)">Regular 400 for text, Bold 700 uppercase with wide tracking for labels, prices and buttons.</p></div>
<div class="card" style="flex:1;padding:40px;height:600px;background:var(--kr)"><div class="lbl">Caveat · the hand</div><div class="hand" style="font:700 150px/1 Caveat;color:var(--ru);margin-top:24px">4 500 DA</div><p style="margin-top:30px;color:var(--es)">Only for hand-written moments: prices on tags, notes, the thank-you card. Never for paragraphs.</p></div></div>''')
lv = [('Display', '900 · 120/110', 'font:900 72px/1 Fraunces', 'New drop.'), ('Headline', '900 · 56/60', 'font:900 48px Fraunces', 'Levi’s trucker jacket'), ('Accent', '600 italic', 'font:600 italic 40px Fraunces;color:var(--ru)', 'something old is on its way'),
      ('Label', 'DM Sans 700 · +0.2em', 'font:700 16px DM Sans;letter-spacing:.24em', 'FRIDAY · 19:00 · 1 OF 1'), ('Body', 'DM Sans 400 · 18/28', 'font:400 20px/1.5 DM Sans', 'Soft from years of wear, copper buttons intact.'), ('Price · hand', 'Caveat 700', 'font:700 46px Caveat;color:var(--ru)', '2 800 DA')]
page('04', 'Hierarchy', f'''{head("04.2 — Hierarchy", "From the drop <i>to the tag.</i>")}<div style="margin-top:36px">{"".join(f'<div style="display:flex;align-items:center;gap:40px;padding:16px 0;border-top:1.5px solid rgba(42,23,18,.14)"><div style="width:300px"><div style="font:700 15px DM Sans">{n}</div><div style="font:400 14px DM Sans;opacity:.6">{m}</div></div><div style="{st}">{t}</div></div>' for n, m, st, t in lv)}</div>''')
# 05 Elements
divider('05', 'Graphic <i>elements</i>', 'Waves, grain, dots and garments — the details that make it ours.', 'rust')
page('05', 'Pattern & texture', f'''{head("05.1 — Pattern & texture", "The wave, <i>on repeat.</i>")}
<div class="row" style="margin-top:40px">{"".join(f'<div style="width:400px"><div style="height:420px;border-radius:10px;overflow:hidden">{wave_pattern(f, b, 400, 420, 130)}</div><div class="cap">{c}</div></div>' for f, b, c in [(CREAM, ESPRESSO, "Tissue · box inside"), (ESPRESSO, CREAM, "Website footer · tissue"), (AMBER, RUST, "Sale · campaigns")])}
<div style="width:380px"><div style="height:420px;border-radius:10px;background:var(--kr);position:relative;overflow:hidden"><div class="grain" style="opacity:.45;display:block"></div></div><div class="cap">Paper grain · 10–20 % over flat colour</div></div></div>''')
page('05', 'Icons & grades', f'''{head("05.2 — Category icons, grades & badges", "Small signals, <i>big clarity.</i>")}
<div style="margin-top:10px">{art("category-icons", 0.8, False)}</div><div class="row" style="margin-top:6px;gap:20px">{art("condition-grades", 0.5)}{art("product-badges", 0.6)}</div>''')
# 06 Product & listings
divider('06', 'Product <i>& listings</i>', 'How every piece is photographed, described, graded and priced.')
shots = [('01 · Front', 'jacket'), ('02 · Back', 'jacket'), ('03 · Label', 'tee'), ('04 · Detail / flaw', 'jeans'), ('05 · On body or hanger', 'sweater')]
page('06', 'Photography', f'''{head("06.1 — Product photography", "Five honest photos <i>per piece.</i>")}
<div class="row" style="margin-top:36px;gap:18px">{"".join(f'<div style="flex:1">{photo(k, 300, 375, KRAFT if i % 2 == 0 else "#E3D6C3", DENIM if k in ("jacket", "jeans") else RUST, radius=6)}<div style="font:700 16px DM Sans;margin-top:12px">{t}</div></div>' for i, (t, k) in enumerate(shots))}</div>
<div class="row" style="margin-top:28px;gap:22px">{"".join(f'<div class="card" style="flex:1;padding:22px 26px"><h3 style="font-size:21px">{t}</h3><p style="font-size:16px;margin-top:6px">{d}</p></div>' for t, d in [("Backdrop", "Kraft paper, cream linen or a warm white wall. Same backdrop for a whole drop."), ("Light", "Daylight by a window, no flash. Shoot between 10:00 and 16:00."), ("Framing", "4:5 vertical, piece centred, 10 % margin. Steam everything first."), ("Honesty", "Always photograph flaws, the label and the fabric tag.")])}</div>''')
page('06', 'Listing rules', f'''{head("06.2 — Listing formula", "Every listing, <i>the same way.</i>")}
<div class="row" style="margin-top:40px;gap:40px"><div style="flex:1"><div class="card" style="padding:30px"><div class="lbl">Title</div><div style="font:900 34px Fraunces;margin-top:10px">Brand + item + detail · era · size</div><div class="hand" style="font:700 34px Caveat;color:var(--ru);margin-top:8px">Levi’s trucker jacket, stonewash · 80s · M</div></div>
<div class="card" style="padding:30px;margin-top:20px"><div class="lbl">Description · 3 sentences</div><p style="margin-top:10px;color:var(--es)">1. What it is and why it’s special.<br>2. How it feels and how it fits.<br>3. Any flaw, with the photo number.</p></div>
<div class="card" style="padding:30px;margin-top:20px"><div class="lbl">Always add</div><p style="margin-top:10px;color:var(--es)">Flat measurements in cm · grade · fabric · price in DA · “1 of 1”</p></div></div>
<div style="width:620px">{art("size-measuring-guide", 0.52)}<div class="cap">Measuring guide · supplied for the website and stories</div></div></div>''')
page('06', 'Condition grades', f'''<div class="row" style="gap:70px;align-items:center;height:100%"><div style="width:620px">{head("06.3 — Condition grades", "Five dots, <i>five grades.</i>", "One shared scale on the website, tags, posts and DMs. When in doubt, grade down — customers forgive honesty, not surprises.")}</div>{art("condition-grades", 0.86)}</div>''')
# 07 Shop
divider('07', 'The online <i>shop</i>', 'Website, product page, cards and badges.', 'rust')
page('07', 'Website', f'{head("07.1 — Home page", "A boutique, <i>not a warehouse.</i>")}<div style="margin-top:30px;display:flex;justify-content:center">{art("website-home-1440", 0.6)}</div>')
page('07', 'Product page', f'{head("07.2 — Product page", "Everything a buyer <i>needs to say yes.</i>")}<div style="margin-top:30px;display:flex;justify-content:center">{art("product-page-1440", 0.64)}</div>')
page('07', 'Product cards', f'{head("07.3 — Product cards & badges", "Photo first, <i>facts below.</i>")}<div style="margin-top:36px">{art("product-cards", 1.15, False)}</div>')
# 08 Social
divider('08', 'Social <i>media</i>', 'A weekly rhythm built around the Friday drop.')
cal = [('Mon', 'Story teaser · “something’s coming”'), ('Wed', 'Post · product spotlight + price'), ('Thu', 'Story · countdown sticker'), ('Fri 19:00', 'Post + stories · NEW DROP'), ('Sat', 'Story · sold stamps'), ('Sun', 'Post · guide or values')]
page('08', 'Rhythm', f'''{head("08.1 — Posting rhythm", "Build up <i>to Friday.</i>")}
<div class="row" style="margin-top:44px;gap:16px">{"".join(f'<div class="card" style="flex:1;padding:24px;height:230px;{"background:var(--es);color:var(--cr)" if d.startswith("Fri") else ""}"><div style="font:900 34px Fraunces">{d}</div><p style="margin-top:12px;font-size:17px;{"color:rgba(243,236,225,.8)" if d.startswith("Fri") else ""}">{t}</p></div>' for d, t in cal)}</div>
<div class="row" style="margin-top:30px;gap:22px">{"".join(f'<div class="card" style="flex:1;padding:22px 26px"><h3 style="font-size:21px">{t}</h3><p style="font-size:16px;margin-top:6px">{d}</p></div>' for t, d in [("Grid", "Alternate dark and light posts; one rust post per row."), ("Captions", "Item · era · size · price · grade. Then one line of story."), ("Claiming", "First “claim” in DMs wins; hold 2 hours, then release."), ("Hashtags", "#vintagewave #thriftDZ #vintagealgerie + item and era.")])}</div>''')
page('08', 'Posts', f'''{head("08.2 — Post templates", "Five posts, <i>endless drops.</i>")}<div class="row" style="margin-top:34px;gap:20px;justify-content:center">{"".join(art(n, 0.28) for n in ["ig-post-new-drop", "ig-post-product-spotlight", "ig-post-sold", "ig-post-quote", "ig-post-carousel-cover"])}</div>''')
page('08', 'Stories & highlights', f'''{head("08.3 — Stories & highlights", "Daily, <i>casual, useful.</i>")}<div class="row" style="margin-top:30px;gap:18px;align-items:flex-start">{"".join(art(n, 0.25) for n in ["ig-story-just-in", "ig-story-this-or-that", "ig-story-drop-countdown", "ig-story-sold-out"])}
<div style="flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{"".join(f'<div style="text-align:center"><div style="width:110px;height:110px;border-radius:50%;overflow:hidden;margin:0 auto;box-shadow:0 0 0 3px {CREAM},0 0 0 5px rgba(42,23,18,.2)">{fit(1080, 1920, highlight(l, k)[2], 110/620*0.6)[0:0]}<div style="width:110px;height:110px;position:relative;overflow:hidden"><div style="position:absolute;left:{-(1080*0.177-110)/2:.0f}px;top:{-(1920*0.177-110)/2:.0f}px">{fit(1080, 1920, highlight(l, k)[2], 0.177)}</div></div></div><div style="font:700 13px DM Sans;margin-top:10px;letter-spacing:.1em">{l.upper()}</div></div>' for l, k in HL)}</div></div>''')
# 09 Packaging
divider('09', 'Packaging <i>& unboxing</i>', 'The moment the parcel opens is our shop window.', 'rust')
steps = ['Fold the piece, hang tag on', 'Wrap in wave tissue', 'Seal with the badge sticker', 'Add the hand-written thank-you card', 'Add the care card', 'Box or mailer, tape, label']
page('09', 'Unboxing', f'''{head("09.1 — The unboxing ritual", "Six steps, <i>every order.</i>")}
<div class="row" style="margin-top:40px;gap:16px">{"".join(f'<div class="card" style="flex:1;padding:26px;height:200px"><div style="font:900 52px Fraunces;color:var(--ru)">{i+1}</div><p style="margin-top:10px;font-size:18px;color:var(--es)">{s}</p></div>' for i, s in enumerate(steps))}</div>
<div class="row" style="margin-top:30px;gap:24px;align-items:flex-start">{art("mailer-box-lid", 0.36)}{art("mailer-box-inside", 0.36)}{art("poly-mailer", 0.27)}</div>''')
page('09', 'Tags & cards', f'''{head("09.2 — Tags, cards & stickers", "The small things <i>people keep.</i>")}
<div class="row" style="margin-top:30px;gap:30px;align-items:flex-start">{art("hang-tag-front-back", 0.62, False)}<div style="display:grid;gap:20px">{art("thank-you-card-front-back", 0.48)}{art("care-card", 0.48)}</div></div>''')
page('09', 'Stickers & tape', f'''{head("09.3 — Stickers, tissue & tape", "Brand every <i>layer.</i>")}
<div class="row" style="margin-top:30px;gap:30px;align-items:flex-start">{art("sticker-sheet", 0.6)}<div style="display:grid;gap:22px">{art("tissue-paper", 0.33)}{art("packing-tape", 0.34)}</div></div>''')
# 10 Print & email
divider('10', 'Print <i>& email</i>', 'Business card, price stickers and the drop newsletter.')
page('10', 'Print & email', f'''{head("10.1 — Business card & email", "Same warmth, <i>everywhere.</i>")}
<div class="row" style="margin-top:30px;gap:40px;align-items:flex-start"><div style="display:grid;gap:30px">{art("business-card-front-back", 0.55)}<div class="row" style="gap:30px;align-items:center">{art("price-sticker-round", 0.6, False)}<p style="max-width:520px">Round price stickers, filled in by hand with a brown marker. Prices always in DA, no decimals.</p></div></div>{art("email-new-drop", 0.52)}</div>''')
# back cover
PAGES.append(f'''<section class="pg dark"><div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%)">{logo("badge", "cream", width=420)}</div>
<div style="position:absolute;left:0;right:0;bottom:120px;text-align:center"><p>Questions about the brand · hello@vintagewave.shop · @vintagewave</p></div><div class="grain l"></div></section>''')
toc = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:16px 0;border-top:1.5px solid rgba(42,23,18,.14)"><div style="display:flex;gap:30px;align-items:baseline"><span style="font:700 16px DM Sans;color:var(--ru)">{n}</span><span style="font:900 36px Fraunces">{t}</span></div><span style="font:500 16px DM Sans">{p:02d}</span></div>' for n, t, p in SECTIONS)
PAGES[TOC] = f'<section class="pg"><div class="hd"><span>VINTAGE WAVE — BRAND GUIDELINES</span><span>CONTENTS</span></div>{head("Contents", "What’s <i>inside.</i>")}<div style="margin-top:40px;width:1200px">{toc}</div><div class="ft"><span>v1.0 · 2026</span><span>02</span></div></section>'
open(os.path.abspath('../html/book.html'), 'w').write(doc(''.join(PAGES), BCSS)); print('pages', len(PAGES))
