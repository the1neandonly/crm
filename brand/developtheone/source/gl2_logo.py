from gl2_brand import *
import dto_mark as DM
def build_logo():
    toc('Logo', 'Logo', 'Logo')
    divider('02', 'The logo.', 'Le logo.', tr('Code, a click, a connection and a community — inside two braces. How it is built, how it is used, and how it must never be used.', 'Du code, un clic, une connexion et une communauté — entre deux accolades. Comment il est construit, comment l’utiliser — et comment ne jamais l’utiliser.'), 'dark')
    ghost = f'<g opacity=".08">{DM.full_mark("#0A0B0D", "#0A0B0D", "#0A0B0D")}</g>'
    pieces = {
        'braces': DM.brace(ink=INK) + DM.brace(987, ink=INK),
        'd': DM.letter_d(INK, '#fff', DM.GRAY) + DM.burst(296, 228, '#fff') + DM.cursor(300, 235, INK, '#fff'),
        't': f'<path d="M438,106 H628 L620,150 H446 Z" fill="#fff" stroke="{DM.GRAY}" stroke-width="5"/><rect x="514" y="150" width="36" height="210" fill="{INK}"/>'
             '<path d="M452,200 C495,182 522,240 575,234 S655,168 712,170 S772,162 792,158" fill="none" stroke="#0A0B0D" stroke-width="56" stroke-linecap="round"/><path d="M452,200 C495,182 522,240 575,234 S655,168 712,170 S772,162 792,158" fill="none" stroke="#fff" stroke-width="22" stroke-linecap="round"/>',
        'o': DM.letter_t_wave_o(INK, '#fff', DM.GRAY).split('<path d="M452')[0].split('<rect x="514"')[0] if False else None}
    o_full = DM.letter_t_wave_o(INK, '#fff', DM.GRAY)
    o_only = ''.join(p for p in o_full.split('/>') if ('A100' in p or 'A60' in p or '<circle' in p) and p) .replace('<path', '<path').replace('"', '"')
    o_only = '/>'.join(x for x in o_full.split('/>') if ('A100,' in x or 'A60,' in x or '<circle' in x)) + '/>'
    pieces['o'] = o_only
    pieces['all'] = DM.full_mark()
    parts = [('braces', tr('The braces', 'Les accolades'), 'Code', tr('Everything we build starts as code.', 'Tout ce que nous construisons commence par du code.')),
             ('d', tr('D + cursor', 'D + curseur'), tr('Action', 'Action'), tr('Develop — and the click that turns a visitor into a client.', 'Développer — et le clic qui transforme un visiteur en client.')),
             ('t', tr('T + cable', 'T + câble'), tr('Connection', 'Connexion'), tr('The link between a brand and its people.', 'Le lien entre une marque et ses publics.')),
             ('o', tr('O + nodes', 'O + nœuds'), tr('Community', 'Communauté'), tr('The one, at the centre of its network.', 'La référence, au centre de son réseau.'))]
    cards = ''.join(f'<div style="flex:1"><div class="card" style="height:300px;display:flex;align-items:center;justify-content:center"><svg viewBox="-10 -10 1025 458" width="92%">{ghost}{pieces[k]}</svg></div>'
                    f'<div class="row" style="margin-top:20px;align-items:baseline;gap:12px"><h3 style="font-size:26px">{t}</h3><span class="lbl vi">{kw}</span></div><p style="font-size:17px">{d}</p></div>' for k, t, kw, d in parts)
    add(tr('02 The symbol', '02 Le symbole'), f'''{head("02.1", "The symbol.", "Le symbole")}
<p style="max-width:1300px;margin-top:22px">{tr("The DTO mark tells our whole job in one line: inside the braces of code, a click develops the brand, a cable connects it, and the O puts it at the centre of its network.", "La marque DTO raconte tout notre métier en une ligne : entre les accolades du code, un clic développe la marque, un câble la connecte, et le O la place au centre de son réseau.")}</p>
<div class="row" style="margin-top:40px;gap:26px;align-items:flex-start">{cards}</div>
<div class="card" style="margin-top:30px;height:150px;background:var(--ink);display:flex;align-items:center;justify-content:center;gap:40px"><svg viewBox="0 0 1005 438" height="110">{DM.full_mark("#fff", INK, "#6B7177")}</svg><span class="big" style="font-size:40px;color:#fff">= {tr("the one.", "la référence.")}</span></div>''')
    gl = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="438"/>' for x in range(0, 1006, 67)) + ''.join(f'<line x1="0" y1="{y}" x2="1005" y2="{y}"/>' for y in range(0, 439, 73))
    ann = 'rgba(74,163,240,.95)'
    cons = (f'<svg viewBox="-60 -50 1125 560" width="1180"><g stroke="rgba(255,255,255,.10)" stroke-width="1.5">{gl}</g><g opacity=".95">{DM.full_mark("#fff", INK, "#6B7177")}</g>'
            f'<path d="M0,470 H1005 M0,460 v20 M1005,460 v20" stroke="{ann}" stroke-width="3"/><text x="502" y="505" fill="{ann}" font-size="24" text-anchor="middle" font-family="JetBrains Mono">W = 2.3 H</text>'
            f'<path d="M-30,0 V438 M-40,0 h20 M-40,438 h20" stroke="{ann}" stroke-width="3"/><text x="-40" y="225" fill="{ann}" font-size="24" text-anchor="end" font-family="JetBrains Mono">H</text>'
            f'<circle cx="747" cy="250" r="5" fill="{ann}"/><circle cx="747" cy="250" r="100" fill="none" stroke="{ann}" stroke-width="2" stroke-dasharray="8 8"/>'
            f'<path d="M300,235 l-120,0" stroke="{ann}" stroke-width="2" stroke-dasharray="6 6"/><text x="170" y="228" fill="{ann}" font-size="22" text-anchor="end" font-family="JetBrains Mono">−14°</text></svg>')
    specs = [(tr('Ratio', 'Ratio'), tr('Mark 2.3 : 1 — braces enclose D, T and O', 'Symbole 2,3 : 1 — les accolades encadrent D, T et O')), (tr('Braces', 'Accolades'), tr('Pointed beak, flat ends, full height', 'Pointe centrale, extrémités plates, pleine hauteur')),
             ('D', tr('Double outline + solid core, light left stem', 'Double contour + cœur plein, fût gauche clair')), (tr('Cursor', 'Curseur'), tr('White pointer, black outline, −14°, click burst', 'Pointeur blanc, contour noir, −14°, éclat de clic')),
             (tr('Cable', 'Câble'), tr('Black tube with white core, links T to O', 'Tube noir à cœur blanc, relie le T au O')), ('O', tr('Open ring + inner arc + 2 nodes', 'Anneau ouvert + arc intérieur + 2 nœuds')),
             (tr('Wordmark', 'Logotype'), tr('Montserrat Bold, DTO Blue, cap height = 27 % of H', 'Montserrat Bold, bleu DTO, hauteur de capitale = 27 % de H'))]
    add(tr('02 Construction', '02 Construction'), f'''<div style="position:absolute;right:110px;top:300px">{cons}</div>{head("02.2", "Construction.", "Construction")}
<p style="max-width:560px;margin-top:22px">{tr("Redrawn as clean vectors from the original logo the community already knows. Always use the master files — never redraw it.", "Redessiné en vectoriel propre à partir du logo original que la communauté connaît déjà. Utilisez toujours les fichiers originaux — ne le redessinez jamais.")}</p>
<table class="spec" style="margin-top:30px;width:560px;border-collapse:collapse">{"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in specs)}</table>''', 'dark')
    def lc(inner, cap, h, bg='#fff', capc='var(--ink)'):
        return f'<div class="card" style="flex:1;height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center">{inner}<div class="cap" style="color:{capc}">{cap}</div></div>'
    add(tr('02 Logo suite', '02 Déclinaisons'), f'''{head("02.3", "Logo suite.", "Déclinaisons du logo")}
<div class="row" style="margin-top:46px">{lc(logo_svg("horizontal","color",width=1000), tr("Primary · Horizontal", "Principal · Horizontal"), 400)}</div>
<div class="row" style="margin-top:26px">{lc(logo_svg("stacked","color",width=300), tr("Stacked", "Vertical"), 300)}{lc(logo_svg("symbol","color",width=330), tr("Symbol", "Symbole"), 300)}{lc(logo_svg("icon","color",width=170), tr("Icon", "Icône"), 300)}{lc(logo_svg("wordmark","color",width=360), tr("Wordmark", "Logotype"), 300)}</div>''')
    apps = ''.join(f'<img src="{F(f"icons/png/{n}.png")}" style="width:170px;border-radius:38px;box-shadow:0 20px 40px -18px rgba(18,14,40,.35)">' for n in ['app-icon-gradient-1024', 'app-icon-ink-1024', 'app-icon-violet-1024', 'app-icon-white-1024'])
    favs = ''.join(f'<div style="text-align:center"><img src="{F(f"icons/png/{n}.png")}" style="width:{px}px;height:{px}px;image-rendering:auto"><div class="mono muted" style="font-size:13px;margin-top:8px">{lab}</div></div>' for n, px, lab in [('favicon-16', 16, '16'), ('favicon-32', 32, '32'), ('favicon-64', 64, '64'), ('apple-touch-icon-180', 90, '180'), ('android-chrome-512', 120, '512')])
    add(tr('02 Icon & app icons', '02 Icône & app'), f'''{head("02.4", "Icon & app icons.", "Icône & icônes d’application")}
<p style="max-width:1200px;margin-top:22px">{tr("When space is small or square, the braces, the D and the clicking cursor carry the brand alone: profile pictures, favicons, app icons, stickers.", "Quand l’espace est petit ou carré, les accolades, le D et le curseur qui clique portent seuls la marque : photos de profil, favicons, icônes d’application, stickers.")}</p>
<div class="row" style="margin-top:40px;gap:26px">{lc(logo_svg("icon","color",width=230), tr("Icon · colour", "Icône · couleur"), 330)}{lc(logo_svg("icon","color-dark",width=230), tr("Icon · dark", "Icône · fond foncé"), 330, "var(--ink)", "#fff")}{lc(logo_svg("icon","on-violet",width=230), tr("Icon · blue", "Icône · bleu"), 330, "var(--violet)", "#fff")}</div>
<div class="row" style="margin-top:34px;gap:26px;align-items:center">{apps}<div class="row" style="margin-left:40px;gap:26px;align-items:flex-end">{favs}</div></div>''')
    hw, hh, _ = horizontal('color'); X = 90*820/hw
    cs = (f'<div style="position:relative;padding:{X}px;border:2px dashed rgba(15,102,182,.5);display:inline-block">{logo_svg("horizontal","color",width=820)}' +
          ''.join(f'<div style="position:absolute;{pos};width:{X}px;height:{X}px;background:rgba(15,102,182,.12);display:flex;align-items:center;justify-content:center;font:700 22px Montserrat;color:var(--violet)">X</div>' for pos in ['left:0;top:0', 'right:0;top:0', 'left:0;bottom:0', 'right:0;bottom:0']) + '</div>')
    mins = [('horizontal', tr('Horizontal', 'Horizontal'), '180 px', '45 mm', 180), ('stacked', tr('Stacked', 'Vertical'), '120 px', '30 mm', 120), ('symbol', tr('Symbol', 'Symbole'), '90 px', '22 mm', 90), ('icon', tr('Icon', 'Icône'), '24 px', '6 mm', 24), ('wordmark-plain', tr('Wordmark', 'Logotype'), '100 px', '25 mm', 100)]
    mn = ''.join(f'<div style="display:flex;align-items:center;gap:30px;padding:16px 0;border-top:1px solid var(--line)"><div style="width:240px;height:80px;display:flex;align-items:center">{logo_svg(k,"color",width=wpx)}</div><div style="flex:1"><div style="font-weight:700;font-size:20px">{n}</div><div class="mono muted" style="font-size:16px;margin-top:4px">min. {px} · {mm}</div></div></div>' for k, n, px, mm, wpx in mins)
    add(tr('02 Clear space & sizes', '02 Zone de protection'), f'''{head("02.5", "Clear space & sizes.", "Zone de protection & tailles minimales")}
<div class="row" style="margin-top:50px;gap:70px;align-items:flex-start"><div><div class="card" style="padding:50px">{cs}</div>
<p style="margin-top:26px;max-width:1000px;font-size:19px">{tr("Keep a clear zone equal to <b>X</b> — the width of one brace — on every side. Below the minimum sizes, switch to the icon.", "Gardez une zone libre égale à <b>X</b> — la largeur d’une accolade — sur chaque côté. En dessous des tailles minimales, utilisez l’icône.")}</p></div>
<div style="flex:1"><div class="lbl vi" style="margin-bottom:12px">{tr("Minimum sizes · digital / print", "Tailles minimales · écran / impression")}</div>{mn}</div></div>''')
    tiles = [('color', '#fff', tr('Original · on white', 'Original · fond blanc'), 'var(--ink)'), ('color-dark', INK, tr('Reversed · Code Black', 'Inversé · noir'), '#fff'),
             ('on-violet', VIOLET, tr('Reversed · DTO Blue', 'Inversé · bleu DTO'), '#fff'), ('on-violet', 'var(--grad)', tr('Reversed · gradient', 'Inversé · dégradé'), '#fff'),
             ('color', '#F2F6FB', tr('Original · on Ice', 'Original · fond glace'), 'var(--ink)'), ('black', '#fff', tr('Mono · black', 'Mono · noir'), 'var(--ink)'),
             ('white', INK, tr('Mono · white', 'Mono · blanc'), '#fff'), ('white', '#5E6A78', tr('Mono · on images', 'Mono · sur photo'), '#fff')]
    add(tr('02 Colour versions', '02 Versions couleur'), f'''{head("02.6", "Colour versions.", "Versions couleur")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:50px">{"".join(f'<div class="card" style="height:330px;background:{bg};display:flex;align-items:center;justify-content:center">{logo_svg("horizontal",s,width=360)}<div class="cap" style="color:{cc};opacity:.7">{c}</div></div>' for s,bg,c,cc in tiles)}</div>''')
    hz = lambda st='', s='color', w=360: logo_svg('horizontal', s, width=w, style=st)
    bad_order = f'<div style="display:flex;align-items:center;gap:16px">{logo_svg("wordmark-plain","color",width=220)}{logo_svg("symbol","color",width=120)}</div>'
    bad_font = f'<div style="display:flex;align-items:center;gap:12px">{logo_svg("symbol","color",width=130)}<span style="font:italic 700 34px Georgia,DejaVu Serif,serif;color:#0F66B6">DevelopTheOne</span></div>'
    mis = [(hz('transform:scaleX(1.25) scaleY(.75)', w=280), tr('Don’t stretch or distort', 'Ne pas étirer ni déformer'), '#fff'), (hz('transform:rotate(-12deg)'), tr('Don’t rotate', 'Ne pas faire pivoter'), '#fff'),
           (hz('filter:hue-rotate(150deg) saturate(1.4)'), tr('Don’t change the colours', 'Ne pas changer les couleurs'), '#fff'), (hz('filter:drop-shadow(6px 10px 6px rgba(0,0,0,.45))'), tr('Don’t add shadows or effects', 'Ne pas ajouter d’ombres ni d’effets'), '#fff'),
           (bad_order, tr('Don’t rearrange the elements', 'Ne pas réorganiser les éléments'), '#fff'), (bad_font, tr('Don’t change the typeface', 'Ne pas changer la typographie'), '#fff'),
           (hz(), tr('Don’t use low-contrast backgrounds', 'Ne pas utiliser de fond peu contrasté'), VIOLET), (logo_svg('horizontal', 'color-dark', width=360), tr('Don’t use the dark version on light', 'Ne pas utiliser la version foncée sur fond clair'), '#fff')]
    add(tr('02 Misuse', '02 Usages interdits'), f'''{head("02.7", "Misuse.", "Usages interdits")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:50px">{"".join(f'<div class="card" style="height:330px;background:{bg};display:flex;align-items:center;justify-content:center;overflow:hidden">{i}<div class="x">×</div><div class="cap" style="color:{"#fff" if bg!="#fff" else "var(--ink)"};letter-spacing:.06em;text-transform:none;font-size:17px">{c}</div></div>' for i,c,bg in mis)}</div>''')
