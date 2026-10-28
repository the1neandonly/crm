"""Gymliink brand guidelines book — 1920x1080 pages, rendered to one PDF."""
import os, sys
from base import *
from apps import *
import concepts
PAGES = []
BCSS = '''
.pg{width:1920px;height:1080px;position:relative;overflow:hidden;background:var(--bg);page-break-after:always;padding:120px 120px 100px}
.pg.light{background:var(--lbg);color:#0A0A0B} .pg.volt{background:var(--volt);color:var(--vink)}
.hd{position:absolute;left:120px;right:120px;top:48px;display:flex;justify-content:space-between;font:500 14px 'Geist Mono';color:var(--tx2);letter-spacing:.08em}
.light .hd{color:#6B6B73} .volt .hd{color:rgba(18,22,10,.6)}
.ft{position:absolute;left:120px;right:120px;bottom:40px;display:flex;justify-content:space-between;font:400 13px 'Geist Mono';color:#55555C}
.eb{font:500 15px 'Geist Mono';color:var(--volt);letter-spacing:.12em;text-transform:uppercase} .light .eb{color:#4E6A0A}
h1{font:600 120px/1 Geist;letter-spacing:-.045em} h2{font:600 64px/1.05 Geist;letter-spacing:-.035em;margin-top:14px} h3{font:600 26px/1.2 Geist;letter-spacing:-.01em}
p{font:400 20px/1.55 Geist;color:var(--tx2)} .light p{color:#55555C}
.card{background:var(--s1);border:1px solid var(--line);border-radius:24px} .light .card{background:#fff;border-color:#E3E3DF}
.row{display:flex;gap:28px} .lbl{font:500 13px 'Geist Mono';color:var(--tx2);letter-spacing:.1em;text-transform:uppercase}
.hair{height:1px;background:var(--line)}
table.t{border-collapse:collapse;width:100%} table.t td{padding:12px 0;border-top:1px solid var(--line);font:400 17px Geist} table.t td:first-child{color:var(--tx2);width:34%}
.cap{font:400 14px Geist;color:var(--tx2);margin-top:12px}
'''
SECTIONS = []
def page(title_num, title, body, cls='', fr=''):
    n = len(PAGES) + 1
    PAGES.append(f'<section class="pg {cls}"><div class="hd"><span>GYMLIINK — BRAND GUIDELINES</span><span>{title_num} · {title.upper()}</span></div>{body}'
                 f'<div class="ft"><span>v1.0 · 2026</span><span>{n:02d}</span></div></section>')
def head(num, en, fr, sub=''):
    return f'<div class="eb">{num} — {fr}</div><h2>{en}</h2>' + (f'<p style="max-width:1100px;margin-top:18px">{sub}</p>' if sub else '')
def fit(w, h, html, s):
    return f'<div style="width:{w*s:.0f}px;height:{h*s:.0f}px;position:relative"><div style="position:absolute;left:0;top:0;width:{w}px;height:{h}px;transform:scale({s});transform-origin:0 0">{html}</div></div>'
def art(name, s):
    w, h, b = ARTBOARDS[name](); return fit(w, h, b, s)
def divider(num, en, fr, sub):
    SECTIONS.append((num, en, fr, len(PAGES) + 1))
    PAGES.append(f'<section class="pg"><div style="position:absolute;right:-180px;top:50%;transform:translateY(-50%);opacity:.08">{logo("symbol", "white", height=1200)}</div>'
                 f'<div style="position:absolute;left:120px;bottom:140px"><div class="eb">{num}</div><h1 style="margin-top:22px">{en}</h1><div style="font:500 30px Geist;color:var(--tx2);margin-top:18px">{fr}</div>'
                 f'<p style="max-width:760px;margin-top:30px">{sub}</p></div><div class="ft"><span>v1.0 · 2026</span><span>{len(PAGES)+1:02d}</span></div></section>')
# ---------------- Cover
PAGES.append(f'''<section class="pg"><div style="position:absolute;left:52%;top:50%;width:1300px;height:1300px;margin:-650px 0 0 -650px;border-radius:50%;background:radial-gradient(circle,rgba(197,240,74,.13),rgba(197,240,74,0) 60%)"></div>
<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%)">{logo("symbol", "color-dark", height=420)}</div>
<div style="position:absolute;left:120px;bottom:110px">{logo("horizontal", "color-dark", height=64)}<div style="font:400 22px Geist;color:var(--tx2);margin-top:22px">Brand guidelines · Charte graphique · <span class="ar" style="display:inline;font-family:'Plex Arabic',Geist">الهوية البصرية</span></div></div>
<div class="mono" style="position:absolute;right:120px;bottom:116px;text-align:right;font:500 15px 'Geist Mono';color:var(--tx2);line-height:1.8">VERSION 1.0<br>2026 · ALGÉRIE<br>GYMLIINK.COM</div></section>''')
TOC_AT = len(PAGES); PAGES.append('')
# ---------------- 01 Brand
divider('01', 'The brand', 'La marque', 'Why Gymliink exists, how it behaves and how it speaks — in French and in Arabic.')
aud = [('storefront', 'Gym owners & front desk', 'Members, QR check-in, till, class planning, payments.'), ('barbell', 'Coaches', 'Clients and training programs.'),
       ('identification-card', 'Members', 'Digital card with QR, booking, workouts, progress, payments.'), ('handshake', 'Partners', 'Refer gyms, earn commissions.'), ('gear', 'Platform team', 'Manages every gym on Gymliink.')]
page('01', 'Mission', f'''{head("01.1", "Mission.", "Mission")}
<div class="row" style="margin-top:46px;gap:80px"><div style="width:820px"><div style="font:500 44px/1.25 Geist;letter-spacing:-.02em">Give every gym in Algeria calm, precise tools for members, money and classes — and give every member a gym that knows them.</div>
<p style="margin-top:34px;max-width:760px">Gymliink is one platform on the web (gymliink.com) and on iOS and Android. Prices are in DA, payments go through Edahabia, CIB, CCP and BaridiMob, and the conversation with members happens on WhatsApp first. The product is bilingual: French, and Arabic set right-to-left.</p></div>
<div style="flex:1;display:grid;gap:14px">{"".join(f'<div class="card" style="padding:20px 24px;display:flex;gap:18px;align-items:center">{ic(i, 30, VOLT)}<div><div style="font:600 19px Geist">{t}</div><div style="font:400 15px Geist;color:var(--tx2);margin-top:3px">{d}</div></div></div>' for i, t, d in aud)}</div></div>''')
traits = [('Precise', 'Précis', 'دقيق', 'Exact numbers, clear states, no ambiguity — the product handles money and access.', 'Vague, approximate, “about”.'),
          ('Calm', 'Calme', 'هادئ', 'Quiet interfaces, short sentences, generous space. The gym is loud; Gymliink is not.', 'Shouting, hype, exclamation marks.'),
          ('Trustworthy', 'Fiable', 'موثوق', 'Says what happened, what it costs, what comes next. Never hides a fee.', 'Jargon, guilt, hidden conditions.')]
page('01', 'Personality', f'''{head("01.2", "Three traits.", "Trois traits de personnalité")}
<div class="row" style="margin-top:56px">{"".join(f'<div class="card" style="flex:1;padding:40px;height:600px;position:relative"><div class="mono" style="font:500 15px Geist Mono;color:var(--volt)">0{k+1}</div><div style="font:600 56px Geist;letter-spacing:-.03em;margin-top:30px">{en}</div><div style="font:500 24px Geist;color:var(--tx2);margin-top:8px">{fr} · <span style="font-family:Plex Arabic,Geist">{ar}</span></div><p style="margin-top:36px">{d}</p><div style="position:absolute;left:40px;right:40px;bottom:40px"><div class="hair"></div><div class="lbl" style="margin-top:18px">Never</div><div style="font:400 18px Geist;margin-top:8px">{no}</div></div></div>' for k, (en, fr, ar, d, no) in enumerate(traits))}</div>''')
voice = [('Welcome', 'Bienvenue chez Atlas Gym, Yasmine. Votre carte est prête : présentez-la à l’entrée.', 'مرحباً بك في Atlas Gym يا ياسمين. بطاقتك جاهزة: قدّمها عند الدخول.'),
         ('Payment reminder', 'Votre abonnement mensuel (4 500 DA) arrive à échéance le 12 mars. Payez en 30 secondes par Edahabia ou BaridiMob.', 'ينتهي اشتراكك الشهري (4 500 دج) يوم 12 مارس. ادفع في 30 ثانية عبر الذهبية أو بريدي موب.'),
         ('Error', 'Le paiement n’a pas abouti. Aucun montant n’a été débité. Réessayez ou choisissez CCP.', 'لم تتم عملية الدفع. لم يُخصم أي مبلغ. أعد المحاولة أو اختر الحساب البريدي.')]
def bubble(fr, ar):
    return (f'<div style="background:#1F2C22;border-radius:18px 18px 18px 4px;padding:18px 20px;font:400 18px/1.5 Geist;max-width:560px">{fr}<div class="mono" style="font:400 12px Geist Mono;color:#8FA58F;text-align:right;margin-top:6px">09:30</div></div>'
            f'<div style="background:#1F2C22;border-radius:18px 18px 4px 18px;padding:18px 20px;font:400 19px/1.6 \'Plex Arabic\',Geist;direction:rtl;max-width:560px;margin:12px 0 0 auto">{ar}<div class="mono" style="font:400 12px Geist Mono;color:#8FA58F;text-align:left;margin-top:6px">09:30</div></div>')
page('01', 'Voice', f'''{head("01.3", "Voice.", "Ton de voix · FR / AR", "Short sentences. The facts first: what, how much, when. One action. No emojis, no exclamation marks in system messages. Western digits and DA amounts in both languages.")}
<div class="row" style="margin-top:40px;gap:24px"><div style="flex:1;display:grid;gap:16px">{"".join(f'<div class="card" style="padding:22px 26px"><div class="lbl">{t}</div><div style="font:400 19px/1.5 Geist;margin-top:10px">{fr}</div><div style="font:400 20px/1.7 \'Plex Arabic\',Geist;direction:rtl;color:var(--tx2);margin-top:8px">{ar}</div></div>' for t, fr, ar in voice)}</div>
<div class="card" style="width:640px;padding:26px;background:#0E1511"><div class="lbl" style="display:flex;gap:10px;align-items:center">{ic("whatsapp-logo", 18, OK)} WhatsApp · renewal reminder</div><div style="margin-top:20px">{bubble("Bonjour Karim, votre abonnement chez Atlas Gym expire dans 3 jours. Renouvelez ici : gymliink.com/r/7781. À bientôt.", "مرحباً كريم، اشتراكك في Atlas Gym ينتهي بعد 3 أيام. جدّد من هنا: gymliink.com/r/7781 — نراك قريباً.")}</div></div></div>''')
# ---------------- 02 Logo
divider('02', 'The logo', 'Le logo', 'Two i’s, two links: the member and the gym, connected. Explored, constructed, and set in every version.')
CON = [('A', 'Le lien « ii »', 'The two i’s of the name become two interlocked links — member and gym, connected. Selected: ownable, simple, legible at 16 px.', concepts.A),
       ('B', 'Check-in', 'The scan frame of a QR code and the tick of entry — the member’s daily gesture. Strong, but generic to scanning apps.', concepts.B),
       ('C', 'Le maillon g', 'A lowercase g built from two chain links — Gym + Link in one letter. Clever, but heavy and hard to read small.', concepts.C)]
cc = ''.join(f'''<div class="card" style="flex:1;padding:34px;height:640px;position:relative;{"border-color:var(--volt)" if k == "A" else ""}"><div style="display:flex;justify-content:space-between"><span class="lbl">Concept {k}</span>{'<span style="font:600 13px Geist Mono;color:var(--vink);background:var(--volt);padding:4px 10px;border-radius:999px">SELECTED</span>' if k == "A" else ''}</div>
<div style="height:300px;display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 120 120" height="230">{fn()}</svg></div><h3>{n}</h3><p style="margin-top:12px;font-size:18px">{d}</p></div>''' for k, n, d, fn in CON)
page('02', 'Concepts', f'{head("02.1", "Three concepts, one choice.", "Trois pistes explorées")}<div class="row" style="margin-top:44px">{cc}</div>')
# construction
X = DR*2
gl = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="130" />' for x in range(0, 121, 5)) + ''.join(f'<line x1="0" y1="{y}" x2="120" y2="{y}"/>' for y in range(0, 131, 5))
ann = 'rgba(197,240,74,.95)'
def dim(x1, y1, x2, y2, l, dx=0, dy=-3):
    return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{ann}" stroke-width=".35"/><text x="{(x1+x2)/2 + dx}" y="{(y1+y2)/2 + dy}" fill="{ann}" font-size="3.6" font-family="Geist Mono" text-anchor="middle">{l}</text>'
cons = (f'<svg viewBox="5 0 110 130" height="820"><g stroke="rgba(255,255,255,.07)" stroke-width=".25">{gl}</g>'
        f'<g opacity=".9">{symbol(TXT, TXT, VOLT, SX0, SY0)}</g>'
        f'<g opacity=".45"><path d="{rrect(*LA, 25)}" fill="none" stroke="#fff" stroke-width=".2" stroke-dasharray="1 1.4"/><path d="{rrect(*LB, 25)}" fill="none" stroke="#fff" stroke-width=".2" stroke-dasharray="1 1.4"/></g>'
        f'<line x1="10" y1="{WEAVE_Y}" x2="110" y2="{WEAVE_Y}" stroke="{ann}" stroke-width=".3" stroke-dasharray="2 1.4"/>'
        + dim(25, 124, 75, 124, '5 · link width') + dim(45, 128, 75, 128, '', 0, 0) + dim(16, 36, 16, 118, '8.2', -4, 8) + dim(25, 30, 35, 30, '1 · stroke') + dim(97, 8.5, 97, 23.5, 'X', 3, 1)
        + f'<text x="7" y="{WEAVE_Y - 1.5}" fill="{ann}" font-size="3.2" font-family="Geist Mono">over ↑ / under ↓</text></svg>')
specs = [('Links', 'Two capsules 5 × 8.2 units, stroke 1, offset by 2 strokes'), ('Weave', 'Left link passes over above the line, under below — gap 0.4'), ('Tittles', 'Diameter X = 1.5 units, centred on the link axes'),
         ('Volt', 'Only the right tittle — the member — carries Volt'), ('Small size', 'Below 24 px use the optical version: heavier, no gap'), ('Grid', 'Units of 10 px on the master artwork')]
page('02', 'Construction', f'''<div style="position:absolute;right:160px;top:130px">{cons}</div>{head("02.2", "Construction.", "Construction du symbole")}
<p style="max-width:680px;margin-top:22px">Two capsule links — the stems of the two i’s — interlock like a chain. Their tittles sit above as two heads: a member and a gym, linked.</p>
<table class="t" style="width:680px;margin-top:40px">{"".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in specs)}</table>''')
wbig, wwid = wordmark_svg(TXT, TXT, VOLT, 300, 0, 300*0.719)
kern = [('g·y', '−25'), ('m·l', '−25'), ('l·ı', '−12'), ('ı·ı', '−10'), ('ı·n', '−18'), ('n·k', '−25')]
page('02', 'Wordmark', f'''{head("02.3", "Wordmark.", "Logotype", "Geist SemiBold, lowercase, set tight and kerned by hand. The i’s lose their square dots for round tittles that echo the symbol — the second one in Volt.")}
<div style="margin:80px 0 0 0"><svg viewBox="-10 -20 {wwid+20} {300*0.95}" width="1500">{wbig}<line x1="-10" y1="{300*0.719}" x2="{wwid+10}" y2="{300*0.719}" stroke="{VOLT}" stroke-width="1" stroke-dasharray="6 6" opacity=".5"/>
<line x1="-10" y1="{300*(0.719-0.546)}" x2="{wwid+10}" y2="{300*(0.719-0.546)}" stroke="#fff" stroke-width="1" stroke-dasharray="6 6" opacity=".25"/></svg></div>
<div class="row" style="margin-top:60px;gap:16px">{"".join(f'<div class="card" style="flex:1;padding:18px 22px"><div class="mono" style="font:500 22px Geist Mono">{a}</div><div class="lbl" style="margin-top:6px">{b} / 1000 em</div></div>' for a, b in kern)}</div>''')
lockup_cards = [('horizontal', 'Horizontal · primary', 300, 1), ('stacked', 'Stacked', 190, 0.8), ('arabic', 'Arabic · عربي', 300, 1), ('arabic-stacked', 'Arabic stacked', 190, 0.8), ('bilingual', 'Bilingual', 300, 1)]
page('02', 'Lockups', f'''{head("02.4", "Lockups.", "Déclinaisons · horizontal, vertical, arabe")}
<div style="display:grid;grid-template-columns:1.25fr 1fr 1.25fr;gap:24px;margin-top:44px">
<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo("horizontal", "color-dark", width=470)}<div class="cap" style="position:absolute;left:24px;bottom:18px">Horizontal · primary</div></div>
<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo("stacked", "color-dark", height=220)}<div class="cap" style="position:absolute;left:24px;bottom:18px">Stacked</div></div>
<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo("arabic", "color-dark", width=430)}<div class="cap" style="position:absolute;left:24px;bottom:18px">Arabic · RTL — the symbol leads on the right</div></div>
<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo("bilingual", "color-dark", width=470)}<div class="cap" style="position:absolute;left:24px;bottom:18px">Bilingual</div></div>
<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo("arabic-stacked", "color-dark", height=220)}<div class="cap" style="position:absolute;left:24px;bottom:18px">Arabic stacked</div></div>
<div class="card" style="height:330px;display:flex;align-items:center;justify-content:center;position:relative">{logo("wordmark", "color-dark", width=430)}<div class="cap" style="position:absolute;left:24px;bottom:18px">Wordmark</div></div></div>
<p style="margin-top:26px;font-size:17px">The Arabic name جيم لينك is set in IBM Plex Sans Arabic SemiBold at 84 % of the Latin size, so both scripts carry the same visual weight.</p>''')
hw, hh, _ = lk_horizontal('color-dark'); sc_ = 760/hw; Xp = X*1.08*WS/SH*sc_*2
mins = [('horizontal', 'Horizontal', '96 px', '24 mm'), ('stacked', 'Stacked', '56 px', '16 mm'), ('arabic', 'Arabic', '104 px', '26 mm'), ('symbol', 'Symbol', '24 px', '6 mm'), ('symbol-small', 'Symbol · small optical', '16 px', '4 mm')]
page('02', 'Clear space', f'''{head("02.5", "Clear space & minimum sizes.", "Zone de protection & tailles minimales")}
<div class="row" style="margin-top:50px;gap:70px;align-items:flex-start"><div><div class="card" style="padding:70px"><div style="position:relative;padding:{Xp:.0f}px;outline:1px dashed rgba(197,240,74,.6)">{logo("horizontal", "color-dark", width=760)}
{"".join(f'<div style="position:absolute;{pos};width:{Xp:.0f}px;height:{Xp:.0f}px;background:rgba(197,240,74,.10);display:flex;align-items:center;justify-content:center;font:500 18px Geist Mono;color:var(--volt)">2X</div>' for pos in ['left:0;top:0', 'right:0;top:0', 'left:0;bottom:0', 'right:0;bottom:0'])}</div></div>
<p style="margin-top:24px;max-width:960px;font-size:18px">Keep a clear zone of 2X on every side — X being the diameter of a tittle. Nothing enters it: text, edges, other logos.</p></div>
<div style="flex:1">{"".join(f'<div style="display:flex;align-items:center;gap:26px;padding:18px 0;border-top:1px solid var(--line)"><div style="width:180px;height:70px;display:flex;align-items:center">{logo(k, "color-dark", height=(int(px[:-3]) if k.startswith("symbol") else None), width=(None if k.startswith("symbol") else int(px[:-3])))}</div><div><div style="font:600 18px Geist">{n}</div><div class="mono" style="font:400 15px Geist Mono;color:var(--tx2);margin-top:4px">min. {px} · {mm}</div></div></div>' for k, n, px, mm in mins)}</div></div>''')
tiles = [('color-dark', BG, 'Full colour · dark', TXT2), ('color-light', LBG, 'Full colour · light', '#55555C'), ('volt', BG, 'Single colour · Volt', TXT2),
         ('black', '#FFFFFF', 'Black', '#55555C'), ('white', BG, 'White', TXT2), ('on-volt', VOLT, 'Reversed · on Volt', INK_ON_VOLT)]
page('02', 'Versions', f'''{head("02.6", "Versions.", "Versions couleur")}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:44px">{"".join(f'<div style="height:330px;border-radius:24px;background:{bg};border:1px solid {LINE};display:flex;align-items:center;justify-content:center;position:relative">{logo("horizontal", s, width=400)}<div style="position:absolute;left:24px;bottom:18px;font:400 14px Geist;color:{cc}">{c}</div></div>' for s, bg, c, cc in tiles)}</div>''')
hz = lambda st='', s='color-dark', w=300: logo('horizontal', s, width=w, style=st)
bad_order = f'<div style="display:flex;align-items:center;gap:14px">{logo("wordmark", "color-dark", width=210)}{logo("symbol", "color-dark", height=56)}</div>'
bad_font = f'<div style="display:flex;align-items:center;gap:12px">{logo("symbol", "color-dark", height=56)}<span style="font:italic 700 50px Georgia,serif">GymLink</span></div>'
dos = [(hz(), 'Use the master files', BG), (hz(s='color-light'), 'Light version on light grounds', LBG), (hz(s='on-volt'), 'Reversed on Volt', VOLT), (logo('symbol-small', 'color-dark', height=60), 'Small optical symbol ≤ 24 px', BG)]
donts = [(hz('transform:scaleX(1.35) scaleY(.8)', w=230), 'Stretch'), (hz('transform:rotate(-10deg)'), 'Rotate'), (hz('filter:hue-rotate(160deg)'), 'Recolour'),
         (hz('filter:drop-shadow(0 10px 8px rgba(197,240,74,.6))'), 'Glow or shadow'), (bad_order, 'Rearrange'), (bad_font, 'Retype'), (hz(s='color-dark'), 'Low contrast'), (hz(s='volt'), 'Volt on light')]
page('02', 'Do / Don’t', f'''{head("02.7", "Do’s & don’ts.", "Bons usages & interdits")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:40px">{"".join(f'<div style="height:190px;border-radius:20px;background:{bg};border:1px solid {LINE};display:flex;align-items:center;justify-content:center;position:relative">{i}<div style="position:absolute;left:18px;bottom:12px;font:500 14px Geist;color:{OK}">✓ {t}</div></div>' for i, t, bg in dos)}
{"".join(f'<div style="height:190px;border-radius:20px;background:{"#3A3A40" if t == "Low contrast" else (LBG if t == "Volt on light" else BG)};border:1px solid {LINE};display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden">{i}<div style="position:absolute;left:18px;bottom:12px;font:500 14px Geist;color:{BAD}">✕ {t}</div></div>' for i, t in donts)}</div>''')
# App icons
def squircle(png_svg, size, label, bg=None):
    return f'<div style="text-align:center"><div style="width:{size}px;height:{size}px;border-radius:{size*0.2237:.0f}px;overflow:hidden;margin:0 auto;box-shadow:0 0 0 1px {LINE}{";background:"+bg if bg else ""}">{png_svg}</div><div class="cap">{label}</div></div>'
_argv = sys.argv; sys.argv = [sys.argv[0], os.path.abspath('../_scratch_export')]
import export as _e
sys.argv = _argv
def isvg(svg, size): return svg.replace('<svg ', f'<svg style="display:block;width:{size}px;height:{size}px" ', 1)
ios = squircle(isvg(_e.icon(1024), 170), 170, 'iOS · default') + squircle(isvg(_e.icon(1024, bg=False), 170), 170, 'iOS · dark', '#000') + squircle(isvg(_e.tinted(1024), 170), 170, 'iOS · tinted')
fg, bgl, mono_ = _e.icon(432, bg=False, frac=0.40), _e.icons if False else None, _e.icon(432, bg=False, frac=0.40, scheme='white')
bg_svg = f'<svg viewBox="0 0 432 432"><defs>{_e.GLOW}</defs><rect width="432" height="432" fill="{BG}"/><rect width="432" height="432" fill="url(#glow)"/></svg>'
layer = lambda svg, lab, extra='': f'<div style="text-align:center"><div style="width:150px;height:150px;border-radius:18px;background:repeating-conic-gradient(#1D1D20 0 25%,#141416 0 50%) 0 0/20px 20px;overflow:hidden;margin:0 auto;{extra}">{isvg(svg, 150)}</div><div class="cap">{lab}</div></div>'
mask = lambda r, lab: f'<div style="text-align:center"><div style="width:150px;height:150px;border-radius:{r};overflow:hidden;margin:0 auto;position:relative">{isvg(bg_svg.replace("<svg ", "<svg style=position:absolute;inset:0;width:150px;height:150px ", 1), 170)}<div style="position:absolute;inset:0">{isvg(fg, 150)}</div></div><div class="cap">{lab}</div></div>'
page('02', 'App icons', f'''{head("02.8", "App icons.", "Icônes d’application · iOS & Android")}
<div class="row" style="margin-top:30px;gap:40px"><div class="card" style="flex:1;padding:28px 36px"><div class="lbl">iOS · 1024 px, rounded-mask preview</div><div class="row" style="margin-top:20px;justify-content:space-around">{ios}</div>
<p style="margin-top:16px;font-size:16px">Default on #0A0A0B with a subtle Volt glow. Dark: transparent ground, the system supplies the black. Tinted: grayscale, the system applies the tint.</p></div></div>
<div class="card" style="padding:28px 36px;margin-top:18px"><div class="lbl">Android adaptive · 432 px layers · 66 % safe zone</div><div class="row" style="margin-top:26px;justify-content:space-between">{layer(fg, "Foreground")}{layer(bg_svg, "Background")}{layer(mono_, "Monochrome · themed")}{mask("50%", "Circle mask")}{mask("38px", "Squircle mask")}{mask("22px", "Rounded square")}</div></div>''')
# tiny & huge
tab = (f'<div style="width:560px;border-radius:14px 14px 0 0;background:#202124;padding:10px 12px 0;display:flex;gap:8px"><div style="background:#35363A;border-radius:10px 10px 0 0;padding:10px 14px;display:flex;align-items:center;gap:10px;font:400 14px Geist;color:#E8EAED;width:250px">'
       f'{isvg(_e.icon(16, frac=0.78, small=True, glow=False, rx=3), 16)}Gymliink — Tableau de bord<span style="margin-left:auto;color:#9AA0A6">✕</span></div><div style="padding:10px 14px;font:400 14px Geist;color:#9AA0A6">+</div></div>'
       f'<div style="width:560px;height:46px;background:#35363A;border-radius:0 0 14px 14px;display:flex;align-items:center;padding:0 16px;font:400 14px Geist Mono;color:#BDC1C6">gymliink.com/app</div>')
avatar = ''.join(f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1px solid var(--line)"><div style="width:24px;height:24px;border-radius:7px;background:var(--bg);box-shadow:0 0 0 1px var(--line);display:flex;align-items:center;justify-content:center">{logo("symbol-small", "color-dark", height=17)}</div><div style="font:500 15px Geist;flex:1">{t}</div><span class="mono" style="font:400 13px Geist Mono;color:var(--tx2)">{h}</span></div>'
                 for t, h in [('Gymliink · Paiement reçu 4 500 DA', '09:12'), ('Gymliink · Cours de 18:00 confirmé', '08:40'), ('Gymliink · Bienvenue chez Atlas Gym', 'hier')])
wall = (f'<div style="width:100%;height:640px;border-radius:24px;overflow:hidden;position:relative;background:linear-gradient(180deg,#26262A 0%,#1A1A1D 70%,#111113 100%)">'
        f'<div style="position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.015) 0 2px,transparent 2px 160px)"></div>'
        f'<div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(180deg,#151517,#0C0C0D)"></div>'
        f'<div style="position:absolute;left:50%;top:46px;transform:translateX(-50%);filter:drop-shadow(0 0 40px rgba(197,240,74,.18))">{logo("symbol", "color-dark", height=420)}</div>'
        f'<div style="position:absolute;left:50%;bottom:150px;width:160px;height:300px;margin-left:-520px;background:linear-gradient(180deg,#2E2E33,#1D1D20);border-radius:4px"></div>'
        f'<div style="position:absolute;left:28px;bottom:20px;font:400 14px Geist Mono;color:#6B6B73">WALL SIGNAGE · 2.4 M · BRUSHED ALUMINIUM + VOLT LED TITTLE</div></div>')
page('02', 'Tiny & huge', f'''{head("02.9", "16 px to 4 metres.", "Du plus petit au plus grand")}
<div class="row" style="margin-top:40px;gap:30px"><div style="width:600px;display:grid;gap:26px"><div class="card" style="padding:26px"><div class="lbl">16 px · browser tab</div><div style="margin-top:18px">{tab}</div></div>
<div class="card" style="padding:26px"><div class="lbl">24 px · in-app avatar</div><div style="margin-top:10px">{avatar}</div></div></div><div style="flex:1">{wall}</div></div>''')
# ---------------- 03 Colour
divider('03', 'Colour', 'Couleur', 'Dark-first neutrals, one signature accent. Volt is a highlighter — used sparingly, always meaningful.')
pal = [('Volt', VOLT, 'Signature accent · actions, active state, one key number'), ('Volt Ink', INK_ON_VOLT, 'Text and icons on Volt'), ('Volt Deep', VOLT_DEEP, 'New · Volt for light grounds (graphics only)'),
       ('Volt Text', '#4E6A0A', 'New · Volt-tinted text on light (AA)'), ('Background', BG, 'Dark theme ground'), ('Surface 1', S1, 'Cards'), ('Surface 2', S2, 'Raised / inputs'), ('Surface 3', S3, 'Hover / selected'),
       ('Line', LINE, 'Hairlines 1 px'), ('Text', TXT, 'Primary text on dark'), ('Text 2', TXT2, 'Secondary text'), ('Light bg', LBG, 'Light theme ground')]
def sw(n, h, d, big=False):
    r, g, b = hex2rgb(h); c, m, y, k = cmyk(h); tc = INK_ON_VOLT if lum(h) > .4 else TXT
    return (f'<div style="border-radius:20px;overflow:hidden;border:1px solid var(--line)"><div style="height:{230 if big else 120}px;background:{h};padding:18px;color:{tc};display:flex;flex-direction:column;justify-content:space-between">'
            f'<div style="font:600 {28 if big else 18}px Geist">{n}</div><div class="mono" style="font:500 {22 if big else 15}px Geist Mono">{h.upper()}</div></div>'
            f'<div style="padding:12px 18px;background:var(--s1);font:400 13px Geist Mono;color:var(--tx2);line-height:1.6">RGB {r} {g} {b}<br>CMYK {c} {m} {y} {k}<br><span style="font-family:Geist">{d}</span></div></div>')
page('03', 'Palette', f'''{head("03.1", "Palette.", "Palette · HEX / RGB / CMYK")}
<div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:16px;margin-top:36px">{sw(*pal[0], big=True)}{"".join(sw(*p, big=True) for p in pal[1:4])}</div>
<div style="display:grid;grid-template-columns:repeat(8,1fr);gap:16px;margin-top:16px">{"".join(sw(*p) for p in pal[4:])}</div>''')
sem = [('Success', OK, 'Active · paid · checked in'), ('Warning', WARN, 'Expiring soon · pending'), ('Danger', BAD, 'Expired · failed payment'), ('Info', INFO, 'Paused · tips · partner')]
page('03', 'Proportions', f'''{head("03.2", "Proportions & semantic colours.", "Proportions & couleurs d’état")}
<div style="margin-top:46px;height:150px;display:flex;border-radius:22px;overflow:hidden;border:1px solid var(--line)"><div style="flex:70;background:{BG};padding:22px;font:600 20px Geist">Neutrals · 70 %</div><div style="flex:21;background:{S2};padding:22px;font:600 20px Geist">Surfaces · 21 %</div><div style="flex:6;background:{VOLT};padding:22px 14px;font:600 18px Geist;color:{INK_ON_VOLT}">Volt<br>&lt; 10 %</div><div style="flex:3;background:linear-gradient(180deg,{OK},{WARN},{BAD},{INFO})"></div></div>
<div class="row" style="margin-top:44px">{"".join(f'<div class="card" style="flex:1;padding:24px"><div style="height:90px;border-radius:14px;background:{h}"></div><div style="font:600 20px Geist;margin-top:16px">{n}</div><div class="mono" style="font:400 15px Geist Mono;color:var(--tx2)">{h}</div><p style="font-size:16px;margin-top:10px">{d}</p><div style="margin-top:14px">{pill(n, k, size=13)}</div></div>' for (n, h, d), k in zip(sem, ["active", "expiring", "expired", "info"]))}</div>
<div class="row" style="margin-top:28px;gap:14px;align-items:center"><div class="lbl">Volt glow (the only gradient)</div><div style="width:420px;height:70px;border-radius:14px;background:radial-gradient(ellipse at 50% 50%,rgba(197,240,74,.22),rgba(197,240,74,0) 70%),{BG};border:1px solid var(--line)"></div><p style="font-size:16px">Radial, Volt at 10–22 % opacity, never behind text-heavy areas.</p></div>''')
pairs = [(TXT, BG, 'Text on background'), (TXT2, BG, 'Text 2 on background'), (TXT, S1, 'Text on surface 1'), (TXT2, S2, 'Text 2 on surface 2'), (INK_ON_VOLT, VOLT, 'Volt Ink on Volt'), (VOLT, BG, 'Volt on background'),
         (BG, LBG, 'Ink on light bg'), ('#4E6A0A', '#FFFFFF', 'Volt Text on white'), (OK, BG, 'Success on background'), (BAD, BG, 'Danger on background'), (VOLT, '#FFFFFF', 'Volt on white'), (TXT2, LBG, 'Text 2 on light bg')]
def grade(r): return 'AAA' if r >= 7 else 'AA' if r >= 4.5 else 'AA large' if r >= 3 else 'Fail'
page('03', 'Accessibility', f'''{head("03.3", "Accessible pairs.", "Paires accessibles · contraste WCAG")}
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:40px">{"".join(f'<div style="border-radius:18px;border:1px solid var(--line);overflow:hidden"><div style="height:120px;background:{b};color:{f};display:flex;align-items:center;justify-content:center;font:600 34px Geist">Aa 4 500 DA</div><div style="padding:12px 16px;background:var(--s1);display:flex;justify-content:space-between;font:400 14px Geist"><span class="t2">{n}</span><span class="mono" style="font-family:Geist Mono;color:{OK if contrast(f, b) >= 4.5 else (WARN if contrast(f, b) >= 3 else BAD)}">{contrast(f, b):.1f}:1 · {grade(contrast(f, b))}</span></div></div>' for f, b, n in pairs)}</div>
<p style="margin-top:24px;font-size:16px">Volt never carries text on white or light grounds (1.4:1). On light, use Volt Text #4E6A0A for links and Volt Deep for graphics.</p>''')
def mini_ui(light):
    bg, s1, tx, t2, ln = (LBG, '#FFFFFF', '#0A0A0B', '#5C5C66', '#E3E3DF') if light else (BG, S1, TXT, TXT2, LINE)
    rows = ''.join(f'<div style="display:flex;align-items:center;gap:12px;padding:13px 0;border-top:1px solid {ln}"><div style="width:36px;height:36px;border-radius:50%;background:{"#ECECE8" if light else S3};display:flex;align-items:center;justify-content:center;font:600 13px Geist;color:{tx}">{i}</div><div style="flex:1;font:500 16px Geist;color:{tx}">{n}</div>{pill(*p, size=12)}</div>'
                   for i, n, p in [('YB', 'Yasmine Benali', ('Actif', 'active')), ('KH', 'Karim Haddad', ('Expire bientôt', 'expiring')), ('SM', 'Sofiane Mekki', ('Expiré', 'expired'))])
    return (f'<div style="flex:1;border-radius:24px;background:{bg};border:1px solid {LINE};padding:30px"><div style="display:flex;justify-content:space-between;align-items:center">{logo("horizontal", "color-light" if light else "color-dark", height=28)}'
            f'<span style="padding:9px 14px;border-radius:10px;background:{VOLT};color:{INK_ON_VOLT};font:600 14px Geist">Nouveau membre</span></div>'
            f'<div style="display:flex;gap:12px;margin-top:24px">' + ''.join(f'<div style="flex:1;border-radius:14px;background:{s1};border:1px solid {ln};padding:14px"><div style="font:400 12px Geist;color:{t2}">{k}</div><div class="mono" style="font:500 22px Geist Mono;color:{tx};margin-top:4px">{v}</div></div>' for k, v in [('Membres actifs', '412'), ('Encaissé ce mois', '186 500 DA')])
            + f'</div><div style="border-radius:16px;background:{s1};border:1px solid {ln};padding:4px 18px;margin-top:14px">{rows}</div></div>')
page('03', 'Themes', f'{head("03.4", "Dark & light themes.", "Thèmes sombre & clair", "Dark is the default. Light follows the system setting: #F4F4F2 ground, white surfaces, ink text — Volt stays the accent for buttons and active states.")}<div class="row" style="margin-top:40px">{mini_ui(False)}{mini_ui(True)}</div>')
# ---------------- 04 Type
divider('04', 'Typography', 'Typographie', 'Geist for interface and display, Geist Mono for numbers and IDs, IBM Plex Sans Arabic for Arabic.')
page('04', 'Families', f'''{head("04.1", "Three families.", "Familles de caractères")}
<div class="row" style="margin-top:44px">
<div class="card" style="flex:1.2;padding:36px;height:640px"><div class="lbl">Geist · UI & display</div><div style="font:600 190px/1 Geist;letter-spacing:-.05em;margin-top:30px">Aa</div><div style="font:400 24px/1.5 Geist;margin-top:26px">Light · Regular · <span style="font-weight:500">Medium</span> · <span style="font-weight:600">SemiBold</span></div><p style="margin-top:20px">abcdefghijklmnopqrstuvwxyz<br>ABCDEFGHIJKLMNOPQRSTUVWXYZ</p></div>
<div class="card" style="flex:1;padding:36px;height:640px"><div class="lbl">Geist Mono · numbers, codes, IDs</div><div class="mono" style="font:500 92px/1 Geist Mono;margin-top:42px">4 500<br><span class="v">DA</span></div><div class="mono" style="font:400 22px/1.7 Geist Mono;color:var(--tx2);margin-top:30px">GL-0042-7781<br>0123456789 · 18:00 · 12/03</div></div>
<div class="card" style="flex:1;padding:36px;height:640px"><div class="lbl">IBM Plex Sans Arabic · العربية</div><div class="ar" style="font:600 150px/1.2 'Plex Arabic',Geist;margin-top:20px">أب</div><div class="ar" style="font:500 34px 'Plex Arabic',Geist;margin-top:10px">جيم لينك · اشتراك نشط</div><div class="ar" style="font:400 20px/1.8 'Plex Arabic',Geist;color:var(--tx2);margin-top:22px">نص عربي واضح وهادئ. جمل قصيرة وفكرة واحدة في كل رسالة.</div></div></div>''')
scale = [('Large Title', 34, 41, 600), ('Title 1', 28, 34, 600), ('Title 2', 22, 28, 600), ('Title 3', 20, 25, 600), ('Headline', 17, 22, 600), ('Body', 17, 22, 400), ('Callout', 16, 21, 400), ('Subheadline', 15, 20, 400), ('Footnote', 13, 18, 400), ('Caption', 12, 16, 400)]
page('04', 'Type scale', f'''{head("04.2", "Type scale.", "Échelle typographique · pt / interligne")}
<div style="margin-top:34px">{"".join(f'<div style="display:flex;align-items:baseline;gap:30px;padding:{8 if s < 20 else 10}px 0;border-top:1px solid var(--line)"><div class="mono" style="width:210px;font:400 14px Geist Mono;color:var(--tx2)">{n} · {s}/{lh} · {w}</div><div style="flex:1;font:{w} {s*1.5:.0f}px/{lh*1.5:.0f}px Geist;letter-spacing:{"-.02em" if s >= 20 else "0"}">Votre abonnement est actif</div><div style="width:460px;font:{w} {s*1.5*1.08:.0f}px/{lh*1.5*1.25:.0f}px \'Plex Arabic\',Geist;direction:rtl">اشتراكك نشط</div></div>' for n, s, lh, w in scale)}</div>''')
page('04', 'Arabic & numerals', f'''{head("04.3", "Arabic pairing, numerals & DA.", "Arabe, chiffres et format DA")}
<div class="row" style="margin-top:44px;gap:30px"><div style="flex:1">{"".join(f'<div style="padding:20px 0;border-top:1px solid var(--line)"><h3 style="font-size:22px">{t}</h3><p style="font-size:17px;margin-top:6px">{d}</p></div>' for t, d in [("Size", "Set Plex Arabic 8 % larger than Geist at the same level, line-height 1.6 (vs 1.3)."), ("Weight", "One step lighter: Geist SemiBold pairs with Plex Arabic Medium in running text, SemiBold in titles."), ("Direction", "Arabic screens mirror fully: navigation, icons with direction, progress. Numbers, codes and card IDs stay LTR."), ("Never", "No faux-bold, no Latin fonts for Arabic, no mixed scripts in one line of body text.")])}</div>
<div style="flex:1"><div class="card" style="padding:34px"><div class="lbl">Amounts</div><div class="mono" style="font:500 64px Geist Mono;margin-top:16px">4 500 DA</div><div class="ar" style="font:500 50px 'Plex Arabic',Geist;margin-top:8px">4 500 دج</div>
<table class="t" style="margin-top:22px"><tr><td>Thousands</td><td>Narrow space · 186 500</td></tr><tr><td>Currency</td><td>DA after the number, one space · دج in Arabic</td></tr><tr><td>Digits</td><td>Western 0–9 in both languages, tabular</td></tr><tr><td>Dates</td><td>12/03/2026 · 12 mars · 12 مارس</td></tr><tr><td>Card ID</td><td class="mono" style="font-family:Geist Mono">GL-0042-7781</td></tr></table></div></div></div>''')
# ---------------- 05 Icons & imagery
divider('05', 'Icons & imagery', 'Icônes & images', 'Phosphor Light, thin and precise. Photography of real Algerian gyms in natural light.')
icn = ['qr-code', 'scan', 'identification-card', 'calendar', 'credit-card', 'wallet', 'receipt', 'users', 'user', 'barbell', 'person-simple-run', 'timer', 'chart-line', 'bell', 'whatsapp-logo', 'lock', 'check-circle', 'warning', 'storefront', 'handshake', 'link', 'ticket', 'clock', 'gear']
page('05', 'Iconography', f'''{head("05.1", "Iconography.", "Iconographie · Phosphor Light")}
<div class="row" style="margin-top:40px;gap:40px"><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:14px;width:1040px">{"".join(f'<div class="card" style="height:132px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px">{ic(n, 40, VOLT if n == "qr-code" else TXT)}<div class="mono" style="font:400 11px Geist Mono;color:var(--tx2)">{n}</div></div>' for n in icn)}</div>
<div style="flex:1">{"".join(f'<div style="padding:18px 0;border-top:1px solid var(--line)"><h3 style="font-size:21px">{t}</h3><p style="font-size:16px;margin-top:6px">{d}</p></div>' for t, d in [("Weight", "Phosphor Light — 1.5 px line at 24 px. Never mix with Fill or Bold."), ("Sizes", "20 · 24 · 32 px on screen; keep the line optically constant."), ("Colour", "Text or Text 2. Volt only for the active tab or the single key action."), ("Direction", "Mirror arrows and progress icons in Arabic; never mirror logos, QR or numbers.")])}</div></div>''')
illus = (f'<svg viewBox="0 0 520 300" width="100%" style="display:block"><g fill="none" stroke="{TXT2}" stroke-width="1.2"><rect x="60" y="40" width="150" height="230" rx="22"/><rect x="88" y="90" width="94" height="94" rx="10"/>'
         f'<path d="M260 155 h90"/><path d="M380 70 v190 M380 70 h80 v190"/><circle cx="440" cy="165" r="3"/></g><circle cx="135" cy="137" r="18" fill="{VOLT}"/><circle cx="350" cy="155" r="5" fill="{VOLT}"/>'
         f'<text x="60" y="292" fill="{TXT2}" font-family="Geist Mono" font-size="11">hairline 1.2 · one Volt point · no fills</text></svg>')
photos = [('Front desk, 7 am', 'Natural window light, real staff, the check-in moment.'), ('Training floor', 'Members aged 18–35 training, mid-action, unposed.'), ('Coach & member', 'Programs on a phone, a conversation — not a pose.')]
page('05', 'Illustration & photography', f'''{head("05.2", "Illustration & photography.", "Illustration & direction photo")}
<div class="row" style="margin-top:40px;gap:28px"><div class="card" style="width:600px;padding:30px"><div class="lbl">Illustration</div><div style="margin-top:20px">{illus}</div><p style="font-size:16px;margin-top:14px">Hairline diagrams of real moments — scanning, paying, booking. One Volt point marks the action.</p></div>
<div style="flex:1"><div class="row" style="gap:18px">{"".join(f'<div style="flex:1"><div style="height:330px;border-radius:20px;background:linear-gradient(160deg,#2B2B2F 0%,#18181B 55%,#0F0F10 100%);border:1px solid var(--line);position:relative;overflow:hidden"><div style="position:absolute;left:-30%;top:-20%;width:90%;height:80%;background:radial-gradient(circle,rgba(255,240,215,.12),rgba(0,0,0,0) 65%)"></div><div class="mono" style="position:absolute;left:16px;bottom:14px;font:400 12px Geist Mono;color:#77777F">PHOTO · {t.upper()}</div></div><h3 style="font-size:19px;margin-top:14px">{t}</h3><p style="font-size:15px;margin-top:4px">{d}</p></div>' for t, d in photos)}</div>
<div class="row" style="margin-top:22px;gap:18px"><div class="card" style="flex:1;padding:20px"><div style="color:{OK};font:600 16px Geist">Do</div><p style="font-size:15px;margin-top:6px">Real Algerian gyms and people · natural light · honest sweat · women and men · local streets and signage.</p></div><div class="card" style="flex:1;padding:20px"><div style="color:{BAD};font:600 16px Geist">Don’t</div><p style="font-size:15px;margin-top:6px">Stock bodybuilders · oiled torsos · neon filters · dumbbell close-ups · flexing.</p></div></div></div></div>''')
# ---------------- 06 UI
divider('06', 'UI elements', 'Éléments d’interface', 'The building blocks already in the product — buttons, chips, cards, status pills and the QR membership card.')
btn = lambda t, st: f'<span style="display:inline-flex;align-items:center;justify-content:center;height:52px;padding:0 24px;border-radius:14px;font:600 17px Geist;{st}">{t}</span>'
chip = lambda t, on=False: f'<span style="display:inline-flex;height:36px;align-items:center;padding:0 14px;border-radius:999px;font:500 15px Geist;{"background:var(--volt);color:var(--vink)" if on else "background:var(--s2);border:1px solid var(--line);color:var(--tx)"}">{t}</span>'
page('06', 'Components', f'''{head("06.1", "Buttons, chips, cards, status.", "Boutons, chips, cartes, statuts")}
<div class="row" style="margin-top:40px;gap:24px"><div class="card" style="flex:1;padding:30px"><div class="lbl">Buttons</div><div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:20px">{btn("Payer 4 500 DA", "background:var(--volt);color:var(--vink)")}{btn("Réserver", "background:var(--s2);border:1px solid var(--line);color:var(--tx)")}{btn("Annuler", "color:var(--tx2)")}{btn("Supprimer le membre", "background:rgba(255,107,94,.12);color:var(--bad)")}</div>
<div style="display:flex;gap:12px;margin-top:14px;direction:rtl">{btn("ادفع 4 500 دج", "background:var(--volt);color:var(--vink);font-family:Plex Arabic,Geist")}{btn("احجز", "background:var(--s2);border:1px solid var(--line);color:var(--tx);font-family:Plex Arabic,Geist")}</div>
<div class="lbl" style="margin-top:30px">Chips</div><div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:16px">{chip("Tous", True)}{chip("Yoga")}{chip("Crossfit")}{chip("Musculation")}{chip("Cardio")}</div></div>
<div class="card" style="flex:1;padding:30px"><div class="lbl">Status pills · FR / AR</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:14px 30px;margin-top:20px">{pill("Actif", "active")}{pill("نشط", "active", True)}{pill("Expire bientôt", "expiring")}{pill("ينتهي قريباً", "expiring", True)}{pill("Expiré", "expired")}{pill("منتهي", "expired", True)}{pill("En pause", "paused")}{pill("متوقف مؤقتاً", "paused", True)}</div>
<div class="lbl" style="margin-top:30px">Card</div><div style="margin-top:16px;border-radius:20px;background:var(--s2);border:1px solid var(--line);padding:20px;display:flex;gap:16px;align-items:center">{ic("calendar", 28, TXT)}<div style="flex:1"><div style="font:600 17px Geist">Crossfit · 18:00</div><div style="font:400 14px Geist;color:var(--tx2)">Coach Amine · 8 places restantes</div></div>{btn("Réserver", "background:var(--volt);color:var(--vink);height:42px;font-size:15px")}</div></div></div>''')
anat = [('Gym & plan', 'Who issued the card and which membership.'), ('Status', 'Active, expiring soon, expired or paused — always visible.'), ('QR', 'White tile, rounded finders, 4-module quiet zone; brightness boosts on open.'), ('Identity', 'Member name, validity date and card ID in Geist Mono.')]
page('06', 'QR membership card', f'''{head("06.2", "The QR membership card.", "La carte membre QR")}
<div class="row" style="margin-top:36px;gap:60px;align-items:flex-start"><div style="display:flex;gap:30px">{membercard_ui(False, 360)}{membercard_ui(True, 360)}</div>
<div style="flex:1">{"".join(f'<div style="display:flex;gap:18px;padding:18px 0;border-top:1px solid var(--line)"><div class="mono" style="font:500 16px Geist Mono;color:var(--volt)">0{k+1}</div><div><h3 style="font-size:20px">{t}</h3><p style="font-size:16px;margin-top:4px">{d}</p></div></div>' for k, (t, d) in enumerate(anat))}</div></div>''')
# ---------------- 07 Applications
divider('07', 'Applications', 'Applications', 'The brand at work: cards, screens, paper, walls and feeds.')
def appage(title, fr, items, sub=''):
    page('07', title, f'{head("07", title + ".", fr, sub)}<div class="row" style="margin-top:34px;gap:40px;align-items:flex-start;justify-content:center">{items}</div>')
appage('Membership card', 'Carte membre · physique & dans l’app', f'<div style="padding-top:60px">{art("membership-card-physical-front-back", 0.62)}<div class="cap">Physical card · CR80 PVC, matte, Volt back · front / back</div></div><div>{art("membership-card-app-fr", 0.72)}</div>')
appage('Check-in', 'Écran de check-in', f'<div>{art("checkin-screen", 0.8)}<div class="cap">Front desk · success state</div></div><div>{art("membership-card-app-ar", 0.8)}<div class="cap">Member app · Arabic RTL</div></div>')
appage('Receipt & poster', 'Reçu imprimé & affiche d’accueil', f'<div>{art("receipt-thermal-80mm", 0.62)}<div class="cap">Thermal receipt · 80 mm</div></div><div>{art("poster-A3-scan-to-enter", 0.48)}<div class="cap">Front-desk poster · A3 · “Scan to enter”</div></div>')
appage('Sticker & partner card', 'Vitrophanie & carte partenaire', f'<div>{art("window-sticker-powered-by", 0.62)}<div class="cap">Window sticker · Ø 20 cm</div></div><div style="padding-top:80px">{art("partner-referral-card-front-back", 0.56)}<div class="cap">Partner referral card · 85 × 55 mm · front / back</div></div>')
appage('Instagram', 'Modèles Instagram · posts & stories', ''.join(f'<div>{art(n, s)}</div>' for n, s in [('instagram-post-1', 0.4), ('instagram-post-2', 0.4), ('instagram-story-1', 0.36), ('instagram-story-2', 0.36)]))
browser = lambda inner: f'<div style="border-radius:14px;overflow:hidden;border:1px solid var(--line)"><div style="height:34px;background:#1D1D20;display:flex;align-items:center;gap:8px;padding:0 14px">{"".join(f"<i style=width:11px;height:11px;border-radius:50%;background:{c};display:block></i>" for c in ["#FF5F57", "#FEBC2E", "#28C840"])}<span class="mono" style="margin-left:16px;font:400 12px Geist Mono;color:var(--tx2)">gymliink.com</span></div>{inner}</div>'
page('07', 'Digital', f'''{head("07", "Email, WhatsApp & website.", "E-mail, WhatsApp & site web")}
<div class="row" style="margin-top:30px;gap:36px;align-items:flex-start"><div style="width:860px">{browser(art("website-hero-1440x900", 0.595))}<div class="cap">gymliink.com · hero</div></div>
<div style="flex:1"><div>{art("email-header-1200x400", 0.62)}<div class="cap">Email header · 1200 × 400</div></div><div class="row" style="margin-top:26px;gap:26px;align-items:center"><div style="width:220px;height:220px;border-radius:50%;overflow:hidden">{art("whatsapp-profile-640", 0.344)}</div><div><h3 style="font-size:20px">WhatsApp Business</h3><p style="font-size:15px;margin-top:6px">Profile picture 640 px, symbol inside the circle-safe area. Messages follow the voice rules.</p></div></div></div></div>''')
# back cover
PAGES.append(f'''<section class="pg"><div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);text-align:center">{logo("stacked", "color-dark", height=260)}</div>
<div style="position:absolute;left:0;right:0;bottom:120px;text-align:center"><p>Questions about the brand: brand@gymliink.com · gymliink.com</p><div class="ar" style="text-align:center;font:400 20px 'Plex Arabic',Geist;color:var(--tx2);margin-top:10px">جيم لينك · الهوية البصرية</div></div></section>''')
# table of contents
toc = ''.join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:22px 0;border-top:1px solid var(--line)"><div style="display:flex;gap:30px;align-items:baseline"><span class="mono" style="font:500 18px Geist Mono;color:var(--volt)">{n}</span><span style="font:600 38px Geist;letter-spacing:-.02em">{en}</span><span style="font:400 22px Geist;color:var(--tx2)">{fr}</span></div><span class="mono" style="font:400 18px Geist Mono;color:var(--tx2)">{p:02d}</span></div>' for n, en, fr, p in SECTIONS)
PAGES[TOC_AT] = f'<section class="pg"><div class="hd"><span>GYMLIINK — BRAND GUIDELINES</span><span>CONTENTS</span></div>{head("", "Contents.", "Sommaire")}<div style="margin-top:50px;width:1300px">{toc}</div><div class="ft"><span>v1.0 · 2026</span><span>02</span></div></section>'
html = doc(''.join(PAGES), BCSS)
open(os.path.abspath('../html/book.html'), 'w').write(html); print('pages', len(PAGES))
