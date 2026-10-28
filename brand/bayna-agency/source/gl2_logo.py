from gl2_brand import *
def build_logo():
    toc('Logo', 'Logo', 'Logo')
    divider('02', 'The logo.', 'Le logo.', 'A letter that looks back at you. How it is made, how it is used, and how it must never be used.', 'dark')
    # Symbol
    def piece(kind):
        g = grad_def(f'pc{kind}'); f = f'url(#pc{kind})'
        if kind == 'stem': d = f'<path fill-rule="evenodd" fill="{f}" d="{body_d()} {almond_d(rev=True)}"/>'
        elif kind == 'eye': d = f'<path d="{almond_d()}" fill="#fff" stroke="{VIOLET}" stroke-width="2.5"/>'
        elif kind == 'iris':
            (ix, iy), (px, py), (gx, gy) = eye_centres()
            d = f'<circle cx="{ix}" cy="{iy}" r="{IR}" fill="{LIME}"/><circle cx="{px}" cy="{py}" r="{PR}" fill="{INK}"/><circle cx="{gx}" cy="{gy}" r="{GR}" fill="#fff"/>'
        else: d = mark_paths(f, LIME)
        ghost = '' if kind == 'all' else f'<g opacity=".09">{mark_paths("#24242B", "#24242B")}</g>'
        return f'<svg viewBox="-10 -10 {W+20} {H+20}" height="290"><defs>{g}</defs>{ghost}{d}</svg>'
    parts = [('stem', 'The letter', 'b', 'A lowercase b — the first letter of bayna, cut to Syne’s proportions.'), ('eye', 'The eye', 'Seen', 'Its counter is an eye. باينة: it shows, nobody can miss it.'),
             ('iris', 'The lime iris', 'Insight', 'The idea that stands out, looking forward — toward the name.'), ('all', 'The b', 'Bayna', 'Together: a brand you simply can’t not see.')]
    sym = ''
    for i, (k, t, kw, d) in enumerate(parts):
        sym += (f'<div style="flex:1"><div class="card" style="height:390px;display:flex;align-items:center;justify-content:center;{"background:var(--ink)" if k=="all" else ""}">{piece(k)}</div>'
                f'<div class="row" style="margin-top:24px;align-items:baseline;gap:14px"><h3>{t}</h3><span class="lbl vi">{kw}</span></div><p style="font-size:18px">{d}</p></div>')
        if i < 3: sym += f'<div class="big" style="font-size:64px;color:var(--violet);padding-top:160px">{"+" if i<2 else "="}</div>'
    add('02 The symbol', f'''{head("02.1", "The symbol.", "Le symbole")}
<p style="max-width:1200px;margin-top:22px">A lowercase <b>b</b> whose counter is an eye. باينة means clear, obvious — what everyone can see. The symbol says it before a single word is read: <b>we make brands impossible to miss.</b></p>
<div class="row" style="margin-top:50px;gap:30px;align-items:flex-start">{sym}</div>''')
    # Construction
    cell = 12; ann = 'rgba(210,255,90,.95)'
    gl = ''.join(f'<line x1="{x*cell}" y1="0" x2="{x*cell}" y2="{H}"/>' for x in range(13)) + ''.join(f'<line x1="0" y1="{y*cell}" x2="{W}" y2="{y*cell}"/>' for y in range(17))
    def dh(x1, x2, y, l): return f'<path d="M{x1},{y}H{x2}M{x1},{y-3}v6M{x2},{y-3}v6" stroke="{ann}" stroke-width=".5"/><text x="{(x1+x2)/2}" y="{y-4}" fill="{ann}" font-size="5.5" text-anchor="middle" font-family="JetBrains Mono">{l}</text>'
    def dv(y1, y2, x, l): return f'<path d="M{x},{y1}V{y2}M{x-3},{y1}h6M{x-3},{y2}h6" stroke="{ann}" stroke-width=".5"/><text x="{x-5}" y="{(y1+y2)/2}" fill="{ann}" font-size="5.5" text-anchor="end" dominant-baseline="middle" font-family="JetBrains Mono">{l}</text>'
    ar = ((EW/2)**2 + EH**2) / (2*EH); (ix, iy), _, _ = eye_centres()
    cons = (f'<svg viewBox="-60 -24 {W+90} {H+40}" height="800"><defs>{grad_def("cg")}</defs><g stroke="rgba(255,255,255,.10)" stroke-width=".4">{gl}</g>'
            f'<g opacity=".92">{mark_paths("url(#cg)", LIME)}</g><circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#fff" stroke-width=".5" stroke-dasharray="2 2"/>'
            f'<g fill="none" stroke="#fff" stroke-width=".35" stroke-dasharray="1.5 1.5" opacity=".6"><circle cx="{EX}" cy="{EY + ar - EH}" r="{ar}"/><circle cx="{EX}" cy="{EY - ar + EH}" r="{ar}"/></g>'
            f'<circle cx="{ix}" cy="{iy}" r="{IR}" fill="none" stroke="#fff" stroke-width=".4" stroke-dasharray="1.5 1.5"/><circle cx="{CX}" cy="{CY}" r="1.6" fill="#fff"/>'
            f'{dh(0, S, -8, "3")}{dh(0, W, H+14, "12 — W")}{dv(0, H, -16, "16 — H")}{dv(CY, H, -40, "6 — R")}</svg>')
    specs = [('Grid', '12 × 16 modules (3 : 4)'), ('Stem', '3 modules wide, round cap'), ('Bowl', 'Radius 6 — half the width'), ('Eye', 'Almond 9 × 5⅔ modules, two equal arcs'),
             ('Iris', 'Radius 2½, touches both lids, looks forward'), ('Wordmark', 'The symbol is the b · “ayna” in Syne Bold'), ('Arabic', 'Readex Pro Bold'), ('Baseline', 'Sits on the bowl')]
    add('02 Construction', f'''<div style="position:absolute;right:170px;top:150px">{cons}</div>{head("02.2", "Construction.", "Construction")}
<p style="max-width:640px;margin-top:26px">Every curve and edge sits on a 12 × 16 modular grid. Always use the master files — never redraw the logo.</p>
<table class="spec" style="margin-top:40px;width:640px;border-collapse:collapse">{"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in specs)}</table>''', 'dark')
    # Suite
    def lc(inner, cap, h, bg='#fff', capc='var(--ink)'):
        return f'<div class="card" style="flex:1;height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center">{inner}<div class="cap" style="color:{capc}">{cap}</div></div>'
    add('02 Logo suite', f'''{head("02.3", "Logo suite.", "Déclinaisons du logo")}
<div class="row" style="margin-top:46px">{lc(logo_svg("horizontal","color",width=900), "Primary · Horizontal", 430)}<div style="width:520px">{lc(logo_svg("stacked","color",width=250), "Stacked", 430)}</div></div>
<div class="row" style="margin-top:28px">{lc(mark_svg(height=150), "Symbol", 250)}{lc(logo_svg("horizontal-compact","color",width=440), "Compact", 250)}{lc(logo_svg("wordmark","color",width=420), "Wordmark", 250)}</div>''')
    add('02 Arabic & bilingual', f'''{head("02.4", "Arabic & bilingual.", "Versions arabe & bilingue")}
<p style="max-width:1150px;margin-top:22px">باينة is set in Readex Pro Bold, whose geometric strokes match Syne. In the Arabic lockup the symbol sits on the right, where right-to-left reading begins.</p>
<div class="row" style="margin-top:44px">{lc(logo_svg("arabic","color",width=560), "Arabic · عربي", 380)}{lc(logo_svg("bilingual-stacked","color-dark",width=500), "Bilingual stacked", 380, "var(--ink)", "#fff")}</div>
<div class="row" style="margin-top:28px">{lc(logo_svg("bilingual","color",width=500), "Bilingual horizontal", 260)}{lc(logo_svg("arabic","on-violet",width=420), "Arabic · reversed", 260, "var(--violet)", "#fff")}</div>''')
    # Clear space
    hw, hh, _ = horizontal('color'); Rp = R*820/hw
    cs = (f'<div style="position:relative;padding:{Rp}px;border:2px dashed rgba(99,55,255,.5);display:inline-block">{logo_svg("horizontal","color",width=820)}' +
          ''.join(f'<div style="position:absolute;{pos};width:{Rp}px;height:{Rp}px;background:rgba(99,55,255,.12);display:flex;align-items:center;justify-content:center;font:700 22px Syne;color:var(--violet)">R</div>' for pos in ['left:0;top:0', 'right:0;top:0', 'left:0;bottom:0', 'right:0;bottom:0']) + '</div>')
    mins = [('horizontal', 'Horizontal + AGENCY', '320 px', '55 mm', 320), ('horizontal-compact', 'Compact', '120 px', '25 mm', 120), ('stacked', 'Stacked', '120 px', '30 mm', 120), ('arabic', 'Arabic', '140 px', '30 mm', 140), ('symbol', 'Symbol', '24 px', '6 mm', 24)]
    mn = ''.join(f'<div style="display:flex;align-items:center;gap:30px;padding:18px 0;border-top:1px solid var(--line)"><div style="width:340px;height:90px;display:flex;align-items:center">{mark_svg(height=wpx*H/W) if k=="symbol" else logo_svg(k,"color",width=wpx)}</div><div style="flex:1"><div style="font-weight:700;font-size:20px">{n}</div><div class="mono muted" style="font-size:16px;margin-top:4px">min. {px} · {mm}</div></div></div>' for k, n, px, mm, wpx in mins)
    add('02 Clear space & sizes', f'''{head("02.5", "Clear space & sizes.", "Zone de protection & tailles minimales")}
<div class="row" style="margin-top:50px;gap:80px;align-items:flex-start"><div><div class="card" style="padding:60px">{cs}</div>
<p style="margin-top:28px;max-width:1000px;font-size:19px">Keep a clear zone equal to <b>R</b> — the radius of the bowl — on every side. Below 55 mm / 320 px, switch to the compact version without “AGENCY”.</p></div>
<div style="flex:1"><div class="lbl vi" style="margin-bottom:12px">Minimum sizes · digital / print</div>{mn}</div></div>''')
    tiles = [('color', '#fff', 'Full colour · light', 'var(--ink)'), ('color-dark', INK, 'Full colour · ink', '#fff'), ('on-violet', VIOLET, 'Reversed · violet', '#fff'), ('on-violet', 'var(--grad)', 'Reversed · gradient', '#fff'),
             ('on-lime', LIME, 'On lime', 'var(--ink)'), ('black', '#fff', 'Mono · black', 'var(--ink)'), ('white', INK, 'Mono · white', '#fff'), ('white', '#6B6B78', 'Mono · on images', '#fff')]
    add('02 Colour versions', f'''{head("02.6", "Colour versions.", "Versions couleur")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:50px">{"".join(f'<div class="card" style="height:330px;background:{bg};display:flex;align-items:center;justify-content:center">{logo_svg("horizontal",s,width=330)}<div class="cap" style="color:{cc};opacity:.7">{c}</div></div>' for s,bg,c,cc in tiles)}</div>''')
    hz = lambda st='', s='color', w=330: logo_svg('horizontal', s, width=w, style=st)
    bad_order = f'<div style="display:flex;align-items:center;gap:18px">{logo_svg("wordmark","color",width=230)}{mark_svg(height=70)}</div>'
    bad_font = f'<div style="display:flex;align-items:center;gap:16px">{mark_svg(height=74)}<span style="font:italic 700 66px Georgia,DejaVu Serif,serif">Bayna</span></div>'
    mis = [(hz('transform:scaleX(1.3) scaleY(.8)', w=250), 'Don’t stretch or distort', '#fff'), (hz('transform:rotate(-12deg)'), 'Don’t rotate', '#fff'),
           (hz('filter:hue-rotate(150deg) saturate(1.4)'), 'Don’t change the colours', '#fff'), (hz('filter:drop-shadow(6px 10px 6px rgba(0,0,0,.45))'), 'Don’t add shadows or effects', '#fff'),
           (bad_order, 'Don’t rearrange the elements', '#fff'), (bad_font, 'Don’t change the typeface', '#fff'), (hz(), 'Don’t use low-contrast backgrounds', VIOLET), (logo_svg('horizontal', 'color-dark', width=330), 'Don’t use the dark version on light', '#fff')]
    add('02 Misuse', f'''{head("02.7", "Misuse.", "Usages interdits")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:50px">{"".join(f'<div class="card" style="height:330px;background:{bg};display:flex;align-items:center;justify-content:center">{i}<div class="x">×</div><div class="cap" style="color:{"#fff" if bg!="#fff" else "var(--ink)"};letter-spacing:.06em;text-transform:none;font-size:17px">{c}</div></div>' for i,c,bg in mis)}</div>''')
