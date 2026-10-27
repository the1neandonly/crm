from gl2_logo import *
def build_visual():
    toc('Visual system', 'Visual system', 'Système visuel')
    divider('03', 'Visual system.', 'Système visuel.', 'Colour, type, icons, patterns, grids, charts and motion — the toolkit behind every Bayna layout.')
    cols = [('Bayna Violet', VIOLET, 'Primary. Headlines, buttons, brand moments.', '≈ 2725 C*'), ('Electric Lime', LIME, 'Highlight. Calls-to-action, accents — use sparingly.', '≈ 380 C*'),
            ('Ink', INK, 'Base. Dark surfaces and all body text.', '≈ 419 C*'), ('White', '#FFFFFF', 'Space. Light surfaces and reversed text.', '—')]
    sw = ''
    for n, h, use, pms in cols:
        tc = '#fff' if lum(h) < .4 else INK; r, g, b = hex2rgb(h); c, m, y, k = cmyk(h)
        bd = 'box-shadow:inset 0 0 0 1px rgba(255,255,255,.18);' if h == INK else ''
        sw += (f'<div style="flex:1"><div style="height:310px;border-radius:28px;background:{h};{bd}padding:30px;color:{tc};position:relative"><div class="big" style="font-size:34px">{n}</div><div class="mono" style="position:absolute;left:30px;bottom:26px;font-size:30px">{h.upper()}</div></div>'
               f'<table class="spec" style="margin-top:20px;border-collapse:collapse;width:100%"><tr><td>RGB</td><td class="mono">{r} {g} {b}</td></tr><tr><td>CMYK</td><td class="mono">{c} {m} {y} {k}</td></tr><tr><td>Pantone</td><td class="mono">{pms}</td></tr></table><p style="font-size:16px;margin-top:14px">{use}</p></div>')
    ratio = [(INK, 45, 'Ink 45%'), ('#FFFFFF', 28, 'White 28%'), (VIOLET, 20, 'Violet & gradient 20%'), (LIME, 7, 'Lime 7%')]
    rb = ''.join(f'<div style="flex:{p};background:{h};height:100%;display:flex;align-items:center;padding-left:16px;font-size:13px;font-weight:700;color:{"#fff" if lum(h)<.4 else INK};white-space:nowrap;overflow:hidden">{l}</div>' for h, p, l in ratio)
    add('03 Colour palette', f'''{head("03.1", "Colour palette.", "Palette de couleurs")}<div class="row" style="margin-top:46px;gap:30px">{sw}</div>
<div style="position:absolute;left:120px;right:120px;bottom:110px"><div class="row" style="justify-content:space-between;align-items:baseline;margin-bottom:12px"><span class="lbl hl">Colour balance</span><span class="muted" style="font-size:14px">* Nearest Pantone — confirm on a physical swatch book. CMYK values are a starting point; ask for a press proof.</span></div>
<div style="display:flex;height:46px;border-radius:12px;overflow:hidden;box-shadow:0 0 0 1px rgba(255,255,255,.14)">{rb}</div></div>''', 'dark')
    pairs = [(LIME, INK), ('#FFFFFF', INK), ('#FFFFFF', VIOLET), (LIME, VIOLET), (INK, LIME), (VIOLET, '#FFFFFF'), (INK, '#FFFFFF'), (LIME, '#FFFFFF')]
    pc = ''.join(f'<div style="background:{bg};border-radius:18px;padding:18px 20px;height:120px;position:relative;{"box-shadow:inset 0 0 0 1px rgba(36,36,43,.1);" if bg=="#FFFFFF" else ""}"><div class="big" style="color:{fg};font-size:40px">Aa</div><div style="position:absolute;right:18px;bottom:14px;font-size:14px;font-weight:800;color:{fg}">{contrast(fg,bg):.1f}:1 · {grade(contrast(fg,bg))}</div></div>' for fg, bg in pairs)
    add('03 Gradient & contrast', f'''{head("03.2", "Gradient & contrast.", "Dégradé & contrastes")}
<div class="row" style="margin-top:46px;gap:60px"><div style="width:900px"><div style="height:520px;border-radius:28px;background:var(--grad);position:relative;overflow:hidden">{mark_svg(body="rgba(255,255,255,.95)", height=300, style="position:absolute;left:60px;bottom:60px")}<div class="mono" style="position:absolute;right:30px;top:28px;color:#fff;font-size:18px">135°</div></div>
<div class="row" style="margin-top:26px;gap:16px">{"".join(f'<div style="flex:1;display:flex;gap:14px;align-items:center"><div style="width:46px;height:46px;border-radius:12px;background:{h}"></div><div><div style="font-weight:700;font-size:16px">{n}</div><div class="mono muted" style="font-size:14px">{h} · {o}</div></div></div>' for n,h,o in [("Lavender",G0,"0%"),("Bayna Violet",G1,"55%"),("Deep Indigo",G2,"100%")])}</div>
<div class="mono" style="margin-top:22px;background:#fff;border-radius:14px;padding:16px 20px;font-size:15px;color:#4a4a55">background: linear-gradient(135deg, {G0} 0%, {G1} 55%, {G2} 100%);</div></div>
<div style="flex:1"><div class="lbl vi" style="margin-bottom:16px">Contrast pairs · WCAG</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{pc}</div><p style="font-size:16px;margin-top:20px">Never set lime text on white. Use lime on Ink or Violet, and Ink on lime.</p></div></div>''')
    add('03 Typography', f'''{head("03.3", "Typography.", "Typographie")}
<div class="row" style="margin-top:46px;gap:30px">
<div class="card" style="flex:1.15;height:560px;padding:44px"><div class="lbl vi">Display · Titres</div><div class="big" style="font-size:210px;letter-spacing:-.04em;line-height:1.05;margin-top:10px">Aa</div>
<div class="big" style="font-size:44px;margin-top:6px">Syne</div><div class="muted" style="font-size:18px;margin:4px 0 22px">Regular → ExtraBold · logo &amp; titles in Bold 700</div>
<div class="big" style="font-size:24px;font-weight:600;letter-spacing:.02em;line-height:1.5;color:#4a4a55">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div></div>
<div class="card" style="flex:1;height:560px;padding:44px"><div class="lbl vi">Text · Texte courant</div><div style="font-size:210px;font-weight:600;letter-spacing:-.04em;line-height:1.05;margin-top:10px">Aa</div>
<div style="font-size:44px;font-weight:700;margin-top:6px">Manrope</div><div class="muted" style="font-size:18px;margin:4px 0 22px">ExtraLight → ExtraBold · body, UI, labels</div>
<div style="font-size:24px;font-weight:500;line-height:1.5;color:#4a4a55">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</div></div>
<div class="card" style="width:520px;height:560px;padding:44px;background:var(--ink);color:#fff"><div class="lbl hl">Hierarchy</div>
<div class="big" style="font-size:58px;margin-top:26px">Headline</div><div class="mono" style="font-size:13px;opacity:.5;margin:8px 0 24px">Syne 700 · −3 % · 1.0</div>
<div class="big" style="font-size:32px;font-weight:600;letter-spacing:-.01em">Sub-headline</div><div class="mono" style="font-size:13px;opacity:.5;margin:8px 0 24px">Syne 600 · −1 %</div>
<div style="font-size:18px;line-height:1.6;color:rgba(255,255,255,.75)">Body copy in Manrope Regular with generous line spacing.</div><div class="mono" style="font-size:13px;opacity:.5;margin:8px 0 24px">Manrope 400 · 1.6</div>
<div class="lbl hl">Label · Étiquette</div><div class="mono" style="font-size:13px;opacity:.5;margin-top:8px">Manrope 700 · caps · +20 %</div></div></div>
<p style="margin-top:26px;font-size:17px">All fonts are free (SIL Open Font License) and included in <span class="mono">/fonts</span>. Install them before opening the editable templates.</p>''')
    add('03 Arabic typography', f'''{head("03.4", "Arabic typography.", "Typographie arabe · الخط العربي")}
<div class="row" style="margin-top:46px;gap:30px">
<div class="card" style="flex:1;height:600px;padding:50px;background:var(--ink);color:#fff"><div class="lbl hl">Readex Pro</div>
<div class="ar" style="font-size:220px;font-weight:700;text-align:left;line-height:1.2">أب</div>
<div class="ar" style="font-size:56px;font-weight:700;text-align:left;margin-top:10px">خليها باينة</div>
<div class="ar" style="font-size:26px;font-weight:400;text-align:left;margin-top:24px;line-height:1.7;color:rgba(255,255,255,.75)">نص عربي واضح وبسيط. جمل قصيرة وفكرة واحدة في كل رسالة.</div></div>
<div style="flex:1"><div class="lbl vi" style="margin-bottom:10px">Bilingual rules · Règles bilingues</div>
{"".join(f'<div style="padding:22px 0;border-top:1px solid var(--line)"><h3 style="font-size:26px">{t}</h3><p style="font-size:19px;margin:0">{d}</p></div>' for t,d in [("Readex Pro for all Arabic text.","Bold 700 for titles, Regular 400 for body. Never fake Arabic with a Latin font."),("Right-aligned, right-to-left.","Arabic blocks align right; Latin blocks align left. Never justify Arabic."),("One script per line.","Put French and Arabic on separate lines or separate blocks, never mixed in one sentence."),("Optical size.","Arabic looks smaller than Latin at the same size: set it about 10–15 % larger."),("Numbers.","Use Western digits (0–9) in both languages for consistency.")])}</div></div>''')
    add('03 Iconography', f'''{head("03.5", "Iconography.", "Iconographie")}
<p style="max-width:1100px;margin-top:22px">Solid, geometric icons on a 48-unit grid with 2–4 unit rounding. Each carries one lime accent — the slice again. Supplied as SVG &amp; PNG in five colourways.</p>
<div style="display:grid;grid-template-columns:repeat(8,1fr);gap:22px;margin-top:44px">{"".join(f'<div class="card" style="height:190px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">{icon_svg(n, VIOLET, LIME, 74)}<div class="mono muted" style="font-size:13px">{n}</div></div>' for n in ICONS)}</div>''')
    add('03 Patterns & elements', f'''{head("03.6", "Patterns & elements.", "Motifs & éléments graphiques")}
<div class="row" style="margin-top:46px;gap:24px">{"".join(f'<div style="flex:1;height:420px;border-radius:28px;overflow:hidden;position:relative">{img(f"patterns/png/bayna-pattern-{n}-tile-1920.png","width:100%;height:100%;object-fit:cover")}<div class="cap" style="color:{"#fff" if n in ("ink","violet","mono") else "var(--ink)"};background:{"rgba(36,36,43,.8)" if n in ("ink","violet","mono") else "rgba(255,255,255,.85)"};padding:8px 14px;border-radius:10px">{n}</div></div>' for n in ["ink","violet","paper","lime","mono"])}</div>
<div class="row" style="margin-top:36px;gap:40px">{"".join(f'<div style="flex:1;display:flex;gap:22px"><div style="width:44px;height:44px;flex:none;background:var(--lime);border-top-left-radius:44px;margin-top:4px"></div><div><h3 style="font-size:26px">{t}</h3><p style="font-size:18px">{d}</p></div></div>' for t,d in [("The slice","A lime quarter-circle marks the single most important thing on a layout."),("The pattern","Quarter circles, halves and dots on a square grid. Seamless tiles supplied."),("The crop","Scale the symbol up and let it bleed off the edge — never shrink it into a corner.")])}</div>''', 'dark')
    # Layout grid
    def gridviz(w, h, sc, m, safe=None, label=''):
        return (f'<div style="position:relative;width:{w*sc}px;height:{h*sc}px;background:var(--ink);border-radius:18px;overflow:hidden">'
                f'<div style="position:absolute;left:{m*sc}px;right:{m*sc}px;top:{m*sc}px;bottom:{m*sc}px;border:2px dashed var(--lime)"></div>'
                + ''.join(f'<div style="position:absolute;top:{m*sc}px;bottom:{m*sc}px;left:{(m + i*(w-2*m)/6)*sc}px;width:{(w-2*m)/6*sc - 8}px;background:rgba(99,55,255,.22)"></div>' for i in range(6))
                + (f'<div style="position:absolute;left:0;right:0;top:0;height:{safe[0]*sc}px;background:rgba(255,79,94,.25)"></div><div style="position:absolute;left:0;right:0;bottom:0;height:{safe[1]*sc}px;background:rgba(255,79,94,.25)"></div>' if safe else '')
                + f'<div style="position:absolute;left:12px;bottom:10px;font:700 13px Manrope;color:#fff;letter-spacing:.1em">{label}</div></div>')
    add('03 Layout grid', f'''{head("03.7", "Layout grid.", "Grille de mise en page")}
<div class="row" style="margin-top:40px;gap:44px;align-items:flex-end">{gridviz(1080,1350,.4,88,label="POST 1080×1350")}{gridviz(1080,1920,.3,88,(250,340),"STORY 1080×1920")}{gridviz(1920,1080,.24,120,label="16:9 1920×1080")}
<div style="width:440px">{"".join(f'<div style="padding:16px 0;border-top:1px solid var(--line)"><b style="font-size:19px">{t}</b><p style="font-size:17px;margin:4px 0 0">{d}</p></div>' for t,d in [("Margins","88 px on social (8 %), 120 px on 16:9."),("Columns","6 columns, 8 px gutters."),("Story safe zones","Keep text out of the top 250 px and bottom 340 px (red)."),("Hierarchy","One headline, one message, one call-to-action.")])}</div></div>''')
    # Charts
    months = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin']; vb = [32, 41, 38, 52, 61, 78]; bw_, gp, ch, mx = 86, 34, 330, 90
    bars = ''.join(f'<path d="M{i*(bw_+gp)},{ch} V{ch-v/mx*ch+4} Q{i*(bw_+gp)},{ch-v/mx*ch} {i*(bw_+gp)+4},{ch-v/mx*ch} H{i*(bw_+gp)+bw_-4} Q{i*(bw_+gp)+bw_},{ch-v/mx*ch} {i*(bw_+gp)+bw_},{ch-v/mx*ch+4} V{ch} Z" fill="{LIME if i==5 else "#7B5CFF"}"/><text x="{i*(bw_+gp)+bw_/2}" y="{ch+30}" fill="rgba(255,255,255,.55)" font-size="16" text-anchor="middle" font-family="Manrope" font-weight="600">{months[i]}</text>' for i, v in enumerate(vb))
    bars += f'<text x="{5*(bw_+gp)+bw_/2}" y="{ch-78/mx*ch-14}" fill="#fff" font-size="22" font-weight="800" text-anchor="middle" font-family="Manrope">78</text>'
    tw = 6*(bw_+gp)-gp
    bar_svg = f'<svg viewBox="0 -10 {tw} {ch+50}" width="560">' + ''.join(f'<line x1="0" x2="{tw}" y1="{ch-v/mx*ch}" y2="{ch-v/mx*ch}" stroke="rgba(255,255,255,.08)"/>' for v in (30, 60, 90)) + f'<line x1="0" x2="{tw}" y1="{ch}" y2="{ch}" stroke="rgba(255,255,255,.3)"/>{bars}</svg>'
    segs = [(0.46, '#7B5CFF', 'Social'), (0.29, '#B9A6FF', 'Search'), (0.25, LIME, 'Referral')]; cx = cy = 170; ro, ri = 160, 104; a0 = -90; dn = ''
    for f, c, n in segs:
        a1 = a0 + f*360 - 1.2; pt = lambda a, r: (cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a))); lg = 1 if a1 - a0 > 180 else 0
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = pt(a0, ro), pt(a1, ro), pt(a1, ri), pt(a0, ri)
        dn += f'<path d="M{x0:.2f},{y0:.2f} A{ro},{ro} 0 {lg},1 {x1:.2f},{y1:.2f} L{x2:.2f},{y2:.2f} A{ri},{ri} 0 {lg},0 {x3:.2f},{y3:.2f} Z" fill="{c}"/>'; a0 = a1 + 1.2
    dn_svg = f'<svg viewBox="0 0 340 340" width="250">{dn}<text x="170" y="168" fill="#fff" font-size="44" font-weight="800" text-anchor="middle" font-family="Syne">25%</text><text x="170" y="198" fill="rgba(255,255,255,.55)" font-size="15" font-weight="600" text-anchor="middle" font-family="Manrope">referral</text></svg>'
    legend = ''.join(f'<div style="display:flex;align-items:center;gap:12px;font-size:17px;font-weight:600;margin-top:12px"><span style="width:14px;height:14px;border-radius:4px;background:{c}"></span>{n}<span class="muted" style="margin-left:auto">{round(f*100)}%</span></div>' for f, c, n in segs)
    kp = ''.join(f'<div style="flex:1;background:#2E2E37;border-radius:22px;padding:20px 28px"><div class="lbl muted">{n}</div><div class="big" style="font-size:40px;margin-top:6px">{v}</div><div style="font-weight:800;color:var(--lime);margin-top:4px">{d} <span class="muted" style="font-weight:600">vs last month</span></div></div>' for n, v, d in [('Reach', '1.2M', '+18%'), ('Leads', '3 480', '+42%'), ('CPA', '640 DA', '−21%')])
    add('03 Data & charts', f'''{head("03.8", "Data & charts.", "Graphiques & reporting")}
<p style="max-width:1250px;margin-top:22px">Reports are part of the brand. Charts sit on Ink, data is Violet, and <span class="hl">lime is reserved for the one number that matters</span>. Every series is labelled — colour is never the only key. <span class="muted">(Sample data.)</span></p>
<div class="row" style="margin-top:34px;gap:28px"><div style="background:#2E2E37;border-radius:28px;padding:28px 38px;width:760px"><div class="lbl muted">Monthly leads · sample</div><div style="margin-top:22px">{bar_svg}</div></div>
<div style="background:#2E2E37;border-radius:28px;padding:34px 38px;flex:1;display:flex;gap:40px;align-items:center">{dn_svg}<div style="flex:1"><div class="lbl muted">Traffic by source · sample</div>{legend}<p style="font-size:15px;margin-top:22px">The donut echoes the symbol: three quarters in violet, the highlighted slice in lime.</p></div></div></div>
<div class="row" style="margin-top:24px;gap:28px">{kp}</div>''', 'dark')
    fr = 'frames/logo-intro-16x9-1920x1080'
    strip = ''.join(f'<div style="flex:1"><img src="file://{lowimg(f'/tmp/claude-0/-home-user-crm/9822160d-7d4c-5a0c-b763-6d89aa660c2f/scratchpad/{fr}/f{n:04d}.png')}" style="width:100%;border-radius:14px;display:block"><div class="mono muted" style="font-size:14px;margin-top:10px">{n/30:.1f}s</div></div>' for n in (8, 22, 34, 60, 80, 149))
    add('03 Motion', f'''{head("03.9", "Motion.", "Animation")}
<p style="max-width:1200px;margin-top:22px">The logo builds itself the way a report reveals its result: the bar rises, the pie turns in, the lime slice pops — then the name appears. Use the supplied MP4 / MOV / WebM files; never re-animate the logo by hand.</p>
<div class="row" style="margin-top:44px;gap:16px">{strip}</div>
<div class="row" style="margin-top:44px;gap:40px">{"".join(f'<div style="flex:1;border-top:2px solid var(--lime);padding-top:20px"><h3 style="font-size:26px">{t}</h3><p style="font-size:18px">{d}</p></div>' for t,d in [("Ease out, never bounce twice.","cubic-bezier(.2,.8,.2,1). One small overshoot on the slice only."),("Fast in, calm hold.","Elements arrive in 0.4–0.8 s, then hold. Logos stay on screen ≥ 2 s."),("Build, don’t decorate.","Motion reveals information — bars grow, slices highlight, text wipes in.")])}</div>''', 'dark')
