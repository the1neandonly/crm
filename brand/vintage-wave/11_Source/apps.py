"""Thrift-store artboards: each returns (width, height, html)."""
from base import *
SHOP = 'vintagewave.shop'; IG = '@vintagewave'
ITEMS = [('jacket', 'Levi’s trucker jacket', '80s · M', 'Excellent', '4 500', DENIM, KRAFT), ('sweater', 'Hand-knit wool sweater', '70s · L', 'Very good', '2 800', RUST, CREAM),
         ('jeans', 'Levi’s 501, high waist', '90s · W28', 'Good', '3 200', DENIM, '#E3D6C3'), ('dress', 'Floral midi dress', '70s · S', 'Mint', '3 900', AMBER, '#EADCC6'),
         ('bag', 'Leather shoulder bag', '80s · One size', 'Excellent', '3 500', MAPLE, KRAFT), ('tee', 'Faded band tee', '90s · M', 'Good', '1 900', ESPRESSO, '#E8DFCF')]
def nav(w):
    links = ''.join(f'<span>{t}</span>' for t in ['New drop', 'Women', 'Men', 'Accessories', 'Sold archive', 'About'])
    return (f'<div style="height:84px;display:flex;align-items:center;justify-content:space-between;padding:0 56px;border-bottom:1.5px solid rgba(42,23,18,.14)">'
            f'{logo("horizontal", "espresso", height=46)}<div style="display:flex;gap:30px;font:500 15px DM Sans">{links}</div>'
            f'<div style="display:flex;gap:18px;font:500 15px DM Sans"><span>Search</span><span>Bag (2)</span></div></div>')
def card(it, w=300, show_price=True):
    k, name, meta, cond, price, fg, bg = it
    return (f'<div style="width:{w}px"><div style="position:relative">{photo(k, w, int(w*1.25), bg, fg, radius=6)}'
            f'<div style="position:absolute;left:12px;top:12px">{badge("1 OF 1", CREAM, ESPRESSO, 11)}</div></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:12px"><div style="font:600 18px Fraunces">{name}</div>'
            + (f'<div style="font:700 17px DM Sans;white-space:nowrap">{price} DA</div>' if show_price else '') +
            f'</div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span style="font:400 14px DM Sans;color:#6B5248">{meta}</span>{cond_badge(cond, 10)}</div></div>')
def a_website():
    W, H = 1440, 1100
    grid = ''.join(card(it, 300) for it in ITEMS[:4])
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;overflow:hidden">{nav(W)}'
         f'<div style="display:flex;height:520px;border-bottom:1.5px solid rgba(42,23,18,.14)"><div style="flex:1;padding:70px 56px;position:relative;background:var(--es);color:var(--cr);overflow:hidden">'
         f'<div style="font:700 14px DM Sans;letter-spacing:.24em;color:var(--am)">NEW DROP · FRIDAY 19:00</div>'
         f'<div style="font:900 86px/0.98 Fraunces;letter-spacing:-.02em;margin-top:22px">Pre-loved pieces,<br><i style="font-weight:600;color:var(--am)">new waves.</i></div>'
         f'<div style="font:400 19px/1.55 DM Sans;opacity:.82;margin-top:24px;max-width:520px">Hand-picked vintage and second-hand clothing. One of each, cleaned, measured and graded — shipped across Algeria.</div>'
         f'<div style="display:flex;gap:14px;margin-top:34px"><span style="padding:16px 26px;background:var(--am);color:var(--es);font:700 16px DM Sans;letter-spacing:.06em">SHOP THE DROP</span>'
         f'<span style="padding:16px 26px;border:1.5px solid rgba(243,236,225,.5);font:700 16px DM Sans;letter-spacing:.06em">HOW WE GRADE</span></div>'
         f'<div style="position:absolute;right:-90px;bottom:-60px;opacity:.10">{logo("symbol", "cream", height=330)}</div><div class="grain l"></div></div>'
         f'<div style="width:560px;position:relative">{photo("jacket", 560, 520, KRAFT, DENIM, "Levi’s trucker · 80s · M")}<div style="position:absolute;right:26px;top:26px;transform:rotate(6deg)">'
         f'<div class="hand" style="background:var(--cr);padding:12px 18px;font:700 32px Caveat;box-shadow:0 6px 16px rgba(0,0,0,.2)">4 500 DA</div></div></div></div>'
         f'<div style="padding:40px 56px"><div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font:700 34px Fraunces">Just in</div><div style="font:500 15px DM Sans;text-decoration:underline">See all 48 pieces</div></div>'
         f'<div style="display:flex;gap:28px;margin-top:24px">{grid}</div></div></div>')
    return W, H, b
def a_product():
    W, H = 1440, 1000
    k, name, meta, cond, price, fg, bg = ITEMS[0]
    thumbs = ''.join(f'<div style="width:96px;height:120px;border:{"2px solid var(--es)" if i == 0 else "1px solid rgba(42,23,18,.15)"}">{photo(k, 96 - (4 if i == 0 else 2), 120 - (4 if i == 0 else 2), bg, fg, grain=False)}</div>' for i in range(4))
    meas = ''.join(f'<div style="display:flex;justify-content:space-between;padding:10px 0;border-top:1px solid rgba(42,23,18,.14);font:400 16px DM Sans"><span>{a}</span><span style="font-weight:700">{b}</span></div>' for a, b in [('Pit to pit', '56 cm'), ('Length', '64 cm'), ('Sleeve', '61 cm'), ('Shoulders', '47 cm')])
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);overflow:hidden">{nav(W)}<div style="display:flex;gap:56px;padding:40px 56px">'
         f'<div style="display:flex;gap:16px"><div style="display:grid;gap:12px;align-content:start">{thumbs}</div>{photo(k, 600, 750, bg, fg, "Front")}</div>'
         f'<div style="flex:1;padding-top:10px"><div style="font:500 14px DM Sans;letter-spacing:.2em;color:#6B5248">JACKETS · 80S · 1 OF 1</div>'
         f'<div style="font:900 52px/1.05 Fraunces;margin-top:14px">{name}</div><div style="font:700 30px DM Sans;margin-top:16px">{price} DA</div>'
         f'<div style="display:flex;gap:10px;margin-top:18px;align-items:center">{cond_badge(cond, 13)}<span style="font:400 15px DM Sans;color:#6B5248">Size M · fits like a modern M/L</span></div>'
         f'<div style="margin-top:26px;padding:16px 26px;background:var(--es);color:var(--cr);font:700 17px DM Sans;letter-spacing:.08em;text-align:center">ADD TO BAG — ONLY ONE</div>'
         f'<div style="font:400 17px/1.6 DM Sans;margin-top:24px;max-width:560px">Classic 80s trucker in medium stonewash. Soft from years of wear, copper buttons intact. Light fading on the collar — see photo 4.</div>'
         f'<div style="margin-top:22px;max-width:560px"><div style="font:700 14px DM Sans;letter-spacing:.18em;margin-bottom:6px">MEASUREMENTS · FLAT</div>{meas}</div>'
         f'<div style="font:400 14px DM Sans;color:#6B5248;margin-top:18px">Delivery 48–72 h · Cash on delivery or CCP / BaridiMob · Returns 7 days</div></div></div></div>')
    return W, H, b
def a_cards():
    W, H = 1440, 620
    return W, H, f'<div style="width:{W}px;height:{H}px;background:var(--cr);padding:50px 56px;display:flex;gap:28px">{"".join(card(it, 207) for it in ITEMS)}</div>'
def a_conditions():
    W, H = 1200, 760
    rows = ''.join(f'<div style="display:flex;align-items:center;gap:30px;padding:24px 0;border-top:1.5px solid rgba(42,23,18,.14)"><div style="width:270px">{cond_badge(n, 15)}</div><div style="font:400 20px DM Sans">{d}</div></div>' for n, d, c in COND)
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:var(--cr);padding:56px 64px"><div style="font:900 48px Fraunces">Condition grades</div>'
                  f'<div style="font:400 19px DM Sans;color:#6B5248;margin:10px 0 26px">Every piece is checked by hand. Five dots, five grades — always honest, always photographed.</div>{rows}</div>')
def a_badges():
    W, H = 1200, 420
    items = [badge('NEW DROP', AMBER, ESPRESSO, 22), badge('1 OF 1', ESPRESSO, CREAM, 22), badge('SOLD', RUST, CREAM, 22), badge('−30 %', MAPLE, CREAM, 22), badge('LAST CHANCE', DENIM, CREAM, 22), badge('RESERVED', SAGE, CREAM, 22)]
    stamp = (f'<div style="width:190px;height:190px;border-radius:50%;border:5px solid {RUST};display:flex;align-items:center;justify-content:center;transform:rotate(-12deg);color:{RUST}">'
             f'<div style="text-align:center"><div style="font:900 46px Fraunces;letter-spacing:.04em">SOLD</div><div style="font:700 13px DM Sans;letter-spacing:.24em">FOUND A HOME</div></div></div>')
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:var(--cr);padding:56px 64px;display:flex;gap:60px;align-items:center"><div style="flex:1;display:flex;flex-wrap:wrap;gap:20px">{"".join(items)}'
                  f'<div class="hand" style="font:700 44px Caveat;color:var(--ru);transform:rotate(-4deg);margin-top:10px">price drop · 2 800 DA</div></div>{stamp}</div>')
def a_sizeguide():
    W, H = 1200, 800
    ar = AMBER
    line = lambda x1, y1, x2, y2, l, lx, ly: (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ar}" stroke-width="2.5" stroke-dasharray="7 6"/>'
                                              f'<circle cx="{x1}" cy="{y1}" r="5" fill="{ar}"/><circle cx="{x2}" cy="{y2}" r="5" fill="{ar}"/><text x="{lx}" y="{ly}" font-family="DM Sans" font-weight="700" font-size="20" fill="{ESPRESSO}">{l}</text>')
    tee = (f'<svg viewBox="0 0 420 460" width="420"><path transform="scale(4.2)" d="{G["tee"]}" fill="{CREAM}" stroke="{ESPRESSO}" stroke-width=".6"/>'
           + line(126, 180, 294, 180, 'A · pit to pit', 140, 168) + line(210, 58, 210, 370, 'B · length', 222, 300) + line(176, 54, 66, 136, 'C', 92, 86) + '</svg>')
    jeans = (f'<svg viewBox="0 0 420 460" width="420"><path transform="scale(4.2)" d="{G["jeans"]}" fill="{CREAM}" stroke="{ESPRESSO}" stroke-width=".6"/>'
             + line(118, 60, 302, 60, 'D · waist (×2)', 136, 48) + line(214, 160, 312, 378, 'E · inseam', 250, 260) + line(118, 140, 302, 140, 'F · hips', 150, 128) + '</svg>')
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:#EADFCF;padding:50px 64px;position:relative"><div style="font:900 48px Fraunces">How we measure</div>'
                  f'<div style="font:400 19px DM Sans;color:#6B5248;margin-top:10px">Laid flat, buttoned, in centimetres. Compare with a piece you already love.</div>'
                  f'<div style="display:flex;gap:80px;margin-top:20px;justify-content:center">{tee}{jeans}</div><div class="grain"></div></div>')
def a_icons():
    W, H = 1200, 420
    names = [('tee', 'Tops'), ('sweater', 'Knitwear'), ('jacket', 'Jackets'), ('jeans', 'Denim'), ('dress', 'Dresses'), ('shoe', 'Shoes'), ('bag', 'Bags'), ('hat', 'Hats')]
    cells = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><div style="width:110px;height:110px;border-radius:50%;background:var(--kr);display:flex;align-items:center;justify-content:center">{garment(k, ESPRESSO, 70)}</div><div style="font:700 16px DM Sans;letter-spacing:.12em">{n.upper()}</div></div>' for k, n in names)
    return W, H, f'<div style="width:{W}px;height:{H}px;background:var(--cr);padding:60px;display:flex;justify-content:space-between;align-items:center">{cells}</div>'
# ---- Social
def ig_new_drop():
    W, H = 1080, 1350
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--es);color:var(--cr);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:80px;top:80px">{logo("horizontal", "cream", height=56)}</div>'
         f'<div style="position:absolute;left:80px;top:250px;font:700 22px DM Sans;letter-spacing:.3em;color:var(--am)">FRIDAY · 19:00</div>'
         f'<div style="position:absolute;left:80px;top:300px;font:900 190px/0.9 Fraunces;letter-spacing:-.02em">New<br><i style="font-weight:600;color:var(--am)">drop.</i></div>'
         f'<div style="position:absolute;left:80px;right:80px;bottom:80px;display:flex;gap:18px">{"".join(photo(it[0], 220, 280, it[6], it[5], radius=4) for it in ITEMS[:4])}</div>'
         f'<div style="position:absolute;right:80px;top:300px;transform:rotate(8deg)">{logo("badge", "amber", height=210)}</div><div class="grain l"></div></div>')
    return W, H, b
def ig_spotlight():
    W, H = 1080, 1350; k, name, meta, cond, price, fg, bg = ITEMS[1]
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;overflow:hidden">{photo(k, 1080, 1000, bg, fg)}'
         f'<div style="position:absolute;left:60px;top:60px">{badge("1 OF 1", ESPRESSO, CREAM, 20)}</div>'
         f'<div style="position:absolute;right:70px;top:640px;transform:rotate(-6deg);background:var(--cr);padding:16px 26px;box-shadow:0 10px 24px rgba(0,0,0,.2)"><div class="hand" style="font:700 64px Caveat;color:var(--ru)">{price} DA</div></div>'
         f'<div style="position:absolute;left:60px;right:60px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end"><div><div style="font:900 56px/1.05 Fraunces">{name}</div>'
         f'<div style="font:500 24px DM Sans;color:#6B5248;margin-top:12px">{meta} · DM to claim</div></div>{cond_badge(cond, 18)}</div></div>')
    return W, H, b
def ig_sold():
    W, H = 1080, 1350; k, name, meta, cond, price, fg, bg = ITEMS[0]
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;overflow:hidden">{photo(k, 1080, 1350, bg, fg)}'
         f'<div style="position:absolute;inset:0;background:rgba(42,23,18,.28)"></div>'
         f'<div style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%) rotate(-12deg);width:520px;height:520px;border-radius:50%;border:12px solid {CREAM};display:flex;align-items:center;justify-content:center;color:{CREAM}">'
         f'<div style="text-align:center"><div style="font:900 150px/1 Fraunces">SOLD</div><div style="font:700 26px DM Sans;letter-spacing:.3em;margin-top:10px">FOUND A NEW HOME</div></div></div>'
         f'<div style="position:absolute;left:60px;bottom:56px;color:{CREAM};font:500 26px DM Sans">Missed it? Turn on notifications for Friday’s drop.</div></div>')
    return W, H, b
def ig_quote():
    W, H = 1080, 1350
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--ru);color:var(--cr);position:relative;overflow:hidden;padding:100px 90px">'
         f'<div style="font:900 30px DM Sans;letter-spacing:.3em;color:var(--am)">WHY SECOND-HAND</div>'
         f'<div style="font:600 92px/1.08 Fraunces;margin-top:60px;letter-spacing:-.01em">The most sustainable piece is the one that <i style="color:var(--am)">already exists.</i></div>'
         f'<div style="position:absolute;left:90px;bottom:90px">{logo("horizontal", "cream", height=52)}</div><div style="position:absolute;right:-120px;bottom:-40px;opacity:.12">{logo("symbol", "cream", height=380)}</div><div class="grain l"></div></div>')
    return W, H, b
def ig_carousel():
    W, H = 1080, 1350
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--kr);position:relative;overflow:hidden;padding:90px">'
         f'<div style="font:700 26px DM Sans;letter-spacing:.3em">GUIDE · 1/5</div><div style="font:900 120px/0.95 Fraunces;margin-top:40px">How to spot<br>real vintage<br><i style="font-weight:600;color:var(--ma)">denim.</i></div>'
         f'<div style="position:absolute;right:90px;bottom:200px;transform:rotate(-8deg)">{garment("jeans", DENIM, 360)}</div>'
         f'<div style="position:absolute;left:90px;bottom:90px;font:700 26px DM Sans;letter-spacing:.12em">SWIPE →</div><div class="grain"></div></div>')
    return W, H, b
def st_just_in():
    W, H = 1080, 1920; k, name, meta, cond, price, fg, bg = ITEMS[3]
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--es);color:var(--cr);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:80px;top:250px;font:900 150px/0.9 Fraunces">Just<br><i style="font-weight:600;color:var(--am)">in.</i></div>'
         f'<div style="position:absolute;left:80px;right:80px;top:640px">{photo(k, 920, 900, bg, fg, radius=8)}</div>'
         f'<div style="position:absolute;left:80px;top:1580px;font:600 44px Fraunces">{name} · {meta}</div><div class="hand" style="position:absolute;right:80px;top:1560px;font:700 72px Caveat;color:var(--am)">{price} DA</div>'
         f'<div style="position:absolute;left:0;right:0;bottom:180px;text-align:center;font:700 24px DM Sans;letter-spacing:.3em;opacity:.7">LINK IN BIO · {SHOP.upper()}</div><div class="grain l"></div></div>')
    return W, H, b
def st_poll():
    W, H = 1080, 1920
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:0;right:0;top:250px;text-align:center;font:900 110px Fraunces">This <i style="font-weight:600;color:var(--ru)">or</i> that?</div>'
         f'<div style="position:absolute;left:70px;top:480px">{photo("jacket", 450, 760, KRAFT, DENIM, "A", 8)}</div><div style="position:absolute;right:70px;top:480px">{photo("sweater", 450, 760, "#E3D6C3", RUST, "B", 8)}</div>'
         f'<div style="position:absolute;left:140px;right:140px;top:1340px;height:150px;border-radius:24px;border:3px dashed rgba(42,23,18,.35);display:flex;align-items:center;justify-content:center;font:500 28px DM Sans;color:rgba(42,23,18,.5)">poll sticker here</div>'
         f'<div style="position:absolute;left:0;right:0;bottom:200px;display:flex;justify-content:center">{logo("horizontal", "espresso", height=50)}</div></div>')
    return W, H, b
def st_countdown():
    W, H = 1080, 1920
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--ru);color:var(--cr);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:50%;top:330px;transform:translateX(-50%)">{logo("badge", "cream", height=330)}</div>'
         f'<div style="position:absolute;left:0;right:0;top:780px;text-align:center;font:900 160px/0.92 Fraunces">Drop in<br><i style="font-weight:600;color:var(--am)">3 days.</i></div>'
         f'<div style="position:absolute;left:140px;right:140px;top:1240px;height:170px;border-radius:24px;border:3px dashed rgba(243,236,225,.45);display:flex;align-items:center;justify-content:center;font:500 28px DM Sans;opacity:.7">countdown sticker here</div>'
         f'<div style="position:absolute;left:0;right:0;bottom:200px;text-align:center;font:700 26px DM Sans;letter-spacing:.3em">FRIDAY · 19:00 · {SHOP.upper()}</div><div class="grain l"></div></div>')
    return W, H, b
def st_sold_out():
    W, H = 1080, 1920
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--es);color:var(--cr);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:0;right:0;top:620px;text-align:center;font:900 190px/0.9 Fraunces">All<br><i style="font-weight:600;color:var(--am)">gone.</i></div>'
         f'<div style="position:absolute;left:0;right:0;top:1060px;text-align:center;font:400 36px/1.5 DM Sans;opacity:.85">The whole drop found new homes<br>in 41 minutes. Thank you.</div>'
         f'<div style="position:absolute;left:0;right:0;bottom:220px;display:flex;justify-content:center">{logo("stacked", "cream", height=170)}</div><div class="grain l"></div></div>')
    return W, H, b
HL = [('New', 'tee'), ('Women', 'dress'), ('Men', 'jacket'), ('Denim', 'jeans'), ('Bags', 'bag'), ('Sold', None), ('Reviews', None), ('Shipping', None)]
def highlight(label, kind, bg=ESPRESSO):
    W, H = 1080, 1920
    if kind: icon = garment(kind, CREAM, 360)
    elif label == 'Sold': icon = f'<div style="font:900 120px Fraunces;color:{CREAM}">SOLD</div>'
    elif label == 'Reviews': icon = f'<div style="font:900 220px/1 Fraunces;color:{CREAM}">“</div>'
    else: icon = f'<svg viewBox="0 0 100 100" width="300"><path d="M14 34 L50 18 L86 34 L86 70 L50 86 L14 70 Z M14 34 L50 50 L86 34 M50 50 L50 86" fill="none" stroke="{CREAM}" stroke-width="5" stroke-linejoin="round"/></svg>'
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:{bg};position:relative;overflow:hidden"><div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:620px;height:620px;border-radius:50%;'
                  f'border:4px solid rgba(243,236,225,.25);display:flex;align-items:center;justify-content:center">{icon}</div><div class="grain l"></div></div>')
def a_profile():
    S = 1080
    return S, S, f'<div style="width:{S}px;height:{S}px;background:var(--es);position:relative;display:flex;align-items:center;justify-content:center">{logo("symbol", "cream", width=700)}<div class="grain l"></div></div>'
# ---- Tags, packaging, print
def a_hangtag():
    W, H = 360, 640
    hole = '<div style="position:absolute;left:50%;top:40px;width:34px;height:34px;margin-left:-17px;border-radius:50%;background:#C9BFAF;box-shadow:inset 0 2px 4px rgba(0,0,0,.3)"></div>'
    front = (f'<div style="width:{W}px;height:{H}px;background:var(--es);position:relative;border-radius:14px 14px 4px 4px;clip-path:polygon(18% 0,82% 0,100% 9%,100% 100%,0 100%,0 9%);color:var(--cr)">{hole}'
             f'<div style="position:absolute;left:0;right:0;top:170px;display:flex;justify-content:center">{logo("stacked", "cream", width=250)}</div>'
             f'<div style="position:absolute;left:0;right:0;bottom:50px;text-align:center;font:700 13px DM Sans;letter-spacing:.3em;opacity:.7">PRE-LOVED · RE-LOVED</div><div class="grain l"></div></div>')
    back = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;border-radius:14px 14px 4px 4px;clip-path:polygon(18% 0,82% 0,100% 9%,100% 100%,0 100%,0 9%);border:1px solid rgba(42,23,18,.2)">{hole}'
            f'<div style="position:absolute;left:36px;right:36px;top:120px;font:400 16px DM Sans">'
            + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1.5px dashed rgba(42,23,18,.3)"><span style="font:700 12px DM Sans;letter-spacing:.2em">{a}</span><span class="hand" style="font:700 30px Caveat;color:var(--ru)">{b}</span></div>' for a, b in [('ITEM', 'Trucker jkt'), ('ERA', '80s'), ('SIZE', 'M'), ('GRADE', 'Excellent'), ('PRICE', '4 500 DA')])
            + f'</div><div style="position:absolute;left:0;right:0;bottom:38px;text-align:center;font:500 13px DM Sans;letter-spacing:.14em">{SHOP.upper()}</div></div>')
    return W*2 + 50, H, f'<div style="display:flex;gap:50px">{front}{back}</div>'
def a_price_sticker():
    S = 400
    return S, S, (f'<div style="width:{S}px;height:{S}px;border-radius:50%;background:var(--am);position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--es)">'
                  f'<div style="font:700 18px DM Sans;letter-spacing:.3em">PRICE</div><div class="hand" style="font:700 110px/1 Caveat">2 800</div><div style="font:700 24px DM Sans;letter-spacing:.2em">DA</div>'
                  f'<div style="position:absolute;inset:14px;border-radius:50%;border:2px dashed rgba(42,23,18,.45)"></div></div>')
def a_thankyou():
    W, H = 874, 620
    f = (f'<div style="width:{W}px;height:{H}px;background:var(--es);color:var(--cr);position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center">'
         f'<div style="font:600 italic 120px Fraunces;color:var(--am)">Thank you</div><div style="font:700 18px DM Sans;letter-spacing:.3em;margin-top:14px">FOR SHOPPING SECOND-HAND</div>'
         f'<div style="position:absolute;bottom:40px">{logo("horizontal", "cream", height=40)}</div><div class="grain l"></div></div>')
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;overflow:hidden;padding:64px 70px">'
         f'<div class="hand" style="font:700 46px/1.25 Caveat;color:var(--es)">Hi Sara,<br>this jacket had a whole life before you — enjoy writing its next chapter.<br>— Amel, Vintage Wave</div>'
         f'<div style="position:absolute;left:70px;right:70px;bottom:56px;display:flex;justify-content:space-between;font:500 16px DM Sans;border-top:1.5px solid rgba(42,23,18,.2);padding-top:18px">'
         f'<span>Tag us {IG} · 10 % off your next piece: <b>WAVE10</b></span><span>{SHOP}</span></div><div class="grain"></div></div>')
    return W*2 + 50, H, f'<div style="display:flex;gap:50px">{f}{b}</div>'
def a_carecard():
    W, H = 874, 620
    tips = [('Wash cold, inside out', 'Gentle cycle, 30 °C max.'), ('Air dry flat', 'No tumble dryer — it shrinks old fibres.'), ('Mend, don’t bin', 'A loose button is a 5-minute fix.'), ('Pass it on', 'Done with it? Sell it back to us.')]
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:var(--kr);position:relative;overflow:hidden;padding:60px 70px"><div style="font:900 50px Fraunces">Care for your vintage</div>'
                  f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px 40px;margin-top:36px">' + ''.join(f'<div><div style="font:700 21px DM Sans">0{i+1} · {t}</div><div style="font:400 18px DM Sans;margin-top:6px;color:#4A2E24">{d}</div></div>' for i, (t, d) in enumerate(tips))
                  + f'</div><div style="position:absolute;right:60px;bottom:50px">{logo("symbol", "espresso", height=70)}</div><div class="grain"></div></div>')
def wave_pattern(fg, bg, w, h, s=140):
    tile = f'<svg xmlns="http://www.w3.org/2000/svg" width="{s*2}" height="{s}"><rect width="{s*2}" height="{s}" fill="{bg}"/>{symbol(fg, s*0.15, s*0.25, s*0.5)}{symbol(fg, s*1.15, s*0.25, s*0.5)}</svg>'
    import urllib.parse
    url = 'data:image/svg+xml;utf8,' + urllib.parse.quote(tile)
    return f'<div style="width:{w}px;height:{h}px;background:url(\'{url}\') 0 0/{s*2}px {s}px;position:relative"></div>'
def a_tissue():
    return 1200, 1200, f'<div style="position:relative">{wave_pattern("rgba(42,23,18,.85)", CREAM, 1200, 1200, 200)}</div>'
def a_mailer():
    W, H = 900, 1200
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:var(--ru);color:var(--cr);position:relative;overflow:hidden;border-radius:6px">'
                  f'<div style="position:absolute;left:0;right:0;top:0;height:80px;background:rgba(0,0,0,.12);display:flex;align-items:center;justify-content:center;font:700 16px DM Sans;letter-spacing:.3em">PEEL & SEAL · REUSE ME</div>'
                  f'<div style="position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center">{logo("stacked", "cream", width=520)}</div>'
                  f'<div style="position:absolute;left:0;right:0;top:780px;text-align:center;font:600 italic 54px Fraunces;color:var(--am)">Something old is on its way.</div>'
                  f'<div style="position:absolute;left:70px;right:70px;bottom:70px;height:190px;border:2px dashed rgba(243,236,225,.55);display:flex;align-items:center;justify-content:center;font:500 20px DM Sans;opacity:.8">shipping label</div><div class="grain l"></div></div>')
def a_box():
    W, H = 1200, 800
    lid = (f'<div style="width:{W}px;height:{H}px;background:var(--kr);position:relative;overflow:hidden"><div style="position:absolute;inset:40px;border:3px solid rgba(42,23,18,.8)"></div>'
           f'<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)">{logo("badge", "espresso", height=420)}</div><div class="grain"></div></div>')
    return W, H, lid
def a_box_inside():
    W, H = 1200, 800
    return W, H, (f'<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden">{wave_pattern("rgba(217,150,43,.9)", ESPRESSO, W, H, 160)}'
                  f'<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);background:var(--es);padding:40px 60px;text-align:center;color:var(--cr)"><div style="font:600 italic 64px Fraunces;color:var(--am)">Hello, old friend.</div>'
                  f'<div style="font:700 16px DM Sans;letter-spacing:.3em;margin-top:12px">UNWRAP SLOWLY · IT HAS STORIES</div></div></div>')
def a_stickers():
    W, H = 1200, 800
    s = [f'<div style="width:280px;height:280px">{logo("badge", "espresso", height=280)}</div>',
         f'<div style="width:280px;height:280px;border-radius:50%;background:var(--ru);display:flex;align-items:center;justify-content:center;text-align:center;color:var(--cr)"><div style="font:600 italic 46px/1.05 Fraunces">pre-loved<br><span style="font:700 18px DM Sans;letter-spacing:.24em;font-style:normal">RE-LOVED</span></div></div>',
         f'<div style="width:380px;height:150px;border-radius:75px;background:var(--es);display:flex;align-items:center;justify-content:center">{logo("wordmark", "cream", width=300)}</div>',
         f'<div style="width:300px;height:180px;background:var(--am);display:flex;align-items:center;justify-content:center;text-align:center;transform:rotate(-6deg)"><div style="font:900 34px/1.1 Fraunces">thank you for<br>shopping second-hand</div></div>',
         f'<div style="width:220px;height:220px;border-radius:50%;background:var(--de);display:flex;align-items:center;justify-content:center">{logo("symbol", "cream", width=160)}</div>',
         a_price_sticker()[2].replace('width:400px;height:400px', 'width:230px;height:230px').replace('110px/1', '60px/1')]
    return W, H, f'<div style="width:{W}px;height:{H}px;background:#E8DFD2;padding:60px;display:flex;flex-wrap:wrap;gap:50px;align-items:center;justify-content:center">{"".join(s)}</div>'
def a_tape():
    W, H = 1600, 150
    seg = f'<div style="display:flex;align-items:center;gap:30px;padding:0 30px">{logo("symbol", "cream", height=70)}<span style="font:700 26px DM Sans;letter-spacing:.3em;color:var(--cr)">SECOND LIFE INSIDE</span></div>'
    return W, H, f'<div style="width:{W}px;height:{H}px;background:var(--ru);display:flex;align-items:center;overflow:hidden">{seg*3}</div>'
def a_bizcard():
    W, H = 1050, 600
    f = (f'<div style="width:{W}px;height:{H}px;background:var(--es);position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center">{logo("stacked", "cream", width=420)}<div class="grain l"></div></div>')
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--cr);position:relative;overflow:hidden;padding:80px 90px"><div style="font:900 52px Fraunces">Amel Kaci</div><div style="font:500 22px DM Sans;color:#6B5248;margin-top:6px">Founder · Curator</div>'
         f'<div style="font:400 24px/1.8 DM Sans;margin-top:60px">+213 (0) 555 00 00 00<br>hello@vintagewave.shop<br>{IG} · {SHOP}</div><div style="position:absolute;right:80px;bottom:80px">{logo("symbol", "rust", height=90)}</div><div class="grain"></div></div>')
    return W*2 + 60, H, f'<div style="display:flex;gap:60px">{f}{b}</div>'
def a_email():
    W, H = 640, 1500
    items = ''.join(f'<div style="width:270px">{card(it, 270)}</div>' for it in ITEMS[:4])
    return W, H, (f'<div style="width:{W}px;height:{H}px;background:var(--cr)"><div style="background:var(--es);padding:40px;display:flex;justify-content:center">{logo("horizontal", "cream", height=42)}</div>'
                  f'<div style="padding:46px 40px 20px;text-align:center"><div style="font:700 14px DM Sans;letter-spacing:.3em;color:var(--ru)">FRIDAY 19:00 · 48 PIECES</div><div style="font:900 60px/1 Fraunces;margin-top:16px">The autumn drop<br><i style="font-weight:600;color:var(--ru)">is live.</i></div>'
                  f'<div style="font:400 17px/1.6 DM Sans;color:#6B5248;margin-top:16px">Wool, denim and leather, hand-picked this month. One of each — first come, first served.</div>'
                  f'<div style="display:inline-block;margin-top:24px;padding:16px 30px;background:var(--es);color:var(--cr);font:700 15px DM Sans;letter-spacing:.12em">SHOP THE DROP</div></div>'
                  f'<div style="display:flex;flex-wrap:wrap;gap:20px;padding:20px 40px">{items}</div><div style="text-align:center;font:400 13px DM Sans;color:#8A7468;padding:20px">{SHOP} · {IG} · Unsubscribe</div></div>')
def a_pattern(fg, bg):
    return lambda: (1600, 1000, wave_pattern(fg, bg, 1600, 1000, 180))
ARTBOARDS = {
 'website-home-1440': a_website, 'product-page-1440': a_product, 'product-cards': a_cards, 'condition-grades': a_conditions, 'product-badges': a_badges,
 'size-measuring-guide': a_sizeguide, 'category-icons': a_icons,
 'ig-post-new-drop': ig_new_drop, 'ig-post-product-spotlight': ig_spotlight, 'ig-post-sold': ig_sold, 'ig-post-quote': ig_quote, 'ig-post-carousel-cover': ig_carousel,
 'ig-story-just-in': st_just_in, 'ig-story-this-or-that': st_poll, 'ig-story-drop-countdown': st_countdown, 'ig-story-sold-out': st_sold_out, 'profile-picture-1080': a_profile,
 **{f'ig-highlight-{l.lower()}': (lambda l=l, k=k: highlight(l, k)) for l, k in HL},
 'hang-tag-front-back': a_hangtag, 'price-sticker-round': a_price_sticker, 'thank-you-card-front-back': a_thankyou, 'care-card': a_carecard,
 'poly-mailer': a_mailer, 'mailer-box-lid': a_box, 'mailer-box-inside': a_box_inside, 'tissue-paper': a_tissue, 'sticker-sheet': a_stickers, 'packing-tape': a_tape,
 'business-card-front-back': a_bizcard, 'email-new-drop': a_email,
 'pattern-wave-espresso': a_pattern(CREAM, ESPRESSO), 'pattern-wave-cream': a_pattern(ESPRESSO, CREAM), 'pattern-wave-rust': a_pattern(AMBER, RUST),
}
