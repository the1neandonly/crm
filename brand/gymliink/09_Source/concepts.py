import json
from geo import *
T = 12; G = 5   # stroke weight, weave gap
def A(c=TXT, v=VOLT):   # Le lien « ii » — two i's / two people, interlocked like a chain
    t, g = 10, 4; a = (25, 36, 50, 82); b = (45, 36, 50, 82)
    out = weave(ring(*a, t), ring(*b, t), ring(*a, t, g), ring(*b, t, g), 77, c)
    return out + f'<circle cx="50" cy="16" r="7.5" fill="{c}"/><circle cx="70" cy="16" r="7.5" fill="{v}"/>'
def B(c=TXT, v=VOLT):   # Check-in — the scan frame of a QR code, the check of entry
    L, w = 30, 11
    br = ''.join(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>' for d in
                 [f'M14,{14+L} V22 a8,8 0 0,1 8,-8 H{14+L}', f'M{106-L},14 H98 a8,8 0 0,1 8,8 V{14+L}', f'M106,{106-L} V98 a8,8 0 0,1 -8,8 H{106-L}', f'M{14+L},106 H22 a8,8 0 0,1 -8,-8 V{106-L}'])
    return br + f'<rect x="38" y="38" width="44" height="44" rx="10" fill="{v}"/><path d="M49,61 l8,8 l15,-17" fill="none" stroke="{INK_ON_VOLT}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
def C(c=TXT, v=VOLT):   # Le maillon « g » — a lowercase g made of two chain links
    r1 = (14, 14, 60, 60); r2 = (58, 30, 38, 84); m = uid('m')
    return (f'<defs><mask id="{m}" maskUnits="userSpaceOnUse" x="-50" y="-50" width="300" height="300"><rect x="-50" y="-50" width="300" height="300" fill="#fff"/>'
            f'<path fill-rule="evenodd" d="{ring(*r2, 11, 4)}" fill="#000"/></mask></defs>'
            f'<path fill-rule="evenodd" fill="{c}" mask="url(#{m})" d="{ring(*r1, 11)}"/><path fill-rule="evenodd" fill="{v}" d="{ring(*r2, 11)}"/>')
def word(c=TXT, v=VOLT, size=100, x=0, y=0):
    """gymliink — Geist SemiBold, dotless i's with round tittles, second tittle in Volt."""
    d1, w1 = text_path('gyml', 'Geist-SemiBold.ttf', size, x, y, tracking=-0.025)
    d2, w2 = text_path('ıı', 'Geist-SemiBold.ttf', size, x + w1 - 0.012*size, y, tracking=-0.01)
    d3, w3 = text_path('nk', 'Geist-SemiBold.ttf', size, x + w1 + w2 - 0.03*size, y, tracking=-0.025)
    s = 0.0665*size; base = x + w1 - 0.012*size
    i1 = base + 0.1345*size; i2 = i1 + 0.259*size
    dots = f'<circle cx="{i1:.2f}" cy="{y-0.655*size:.2f}" r="{s:.2f}" fill="{c}"/><circle cx="{i2:.2f}" cy="{y-0.655*size:.2f}" r="{s:.2f}" fill="{v}"/>'
    return f'<path d="{d1} {d2} {d3}" fill="{c}"/>' + dots, w1 + w2 + w3 - 0.042*size
def _board():
    CON = [('A', 'Le lien « ii »', 'Les deux i deviennent deux maillons — le membre et la salle, connectés.', A),
           ('B', 'Check-in', 'Le cadre de scan du QR et la coche d’entrée — le geste quotidien du membre.', B),
           ('C', 'Le maillon g', 'Un g minuscule fait de deux maillons — Gym + Link en une seule lettre.', C)]
    cards = []
    for k, (key, name, why, fn) in enumerate(CON):
        x = 40 + k*620
        wd, ww = word(TXT, VOLT, 70, 0, 0); wl, _ = word('#0A0A0B', '#7FA61A', 70, 0, 0)
        cards.append(f'''<g transform="translate({x},140)"><rect width="590" height="860" rx="28" fill="{S1}" stroke="{LINE}"/>
    <text x="36" y="56" fill="{VOLT}" font-family="Geist Mono" font-size="16" letter-spacing="3">CONCEPT {key}</text>
    <text x="36" y="98" fill="{TXT}" font-family="Geist" font-weight="600" font-size="34">{name}</text>
    <text x="36" y="132" fill="{TXT2}" font-family="Geist" font-size="16">{why}</text>
    <g transform="translate(175,180) scale(2)">{fn()}</g>
    <g transform="translate({295 - ww/2},520)">{wd}</g>
    <rect x="24" y="580" width="542" height="160" rx="18" fill="{LBG}"/><g transform="translate(60,600) scale(1)">{fn('#0A0A0B', '#7FA61A' if fn is A else VOLT)}</g>
    <g transform="translate(200,695)">{wl}</g>
    <g transform="translate(36,764)"><rect width="72" height="72" rx="17" fill="{BG}" stroke="{LINE}"/><g transform="translate(12,12) scale(.4)">{fn()}</g></g>
    <g transform="translate(130,764)"><rect width="72" height="72" rx="17" fill="{VOLT}"/><g transform="translate(12,12) scale(.4)">{fn(INK_ON_VOLT, INK_ON_VOLT)}</g></g>
    <g transform="translate(228,786)"><rect width="32" height="32" rx="7" fill="{BG}" stroke="{LINE}"/><g transform="translate(4,4) scale(.2)">{fn()}</g></g>
    <g transform="translate(276,794)"><g transform="scale(.1333)">{fn()}</g></g>
    <text x="310" y="806" fill="{TXT2}" font-family="Geist Mono" font-size="13">72 · 32 · 16 px</text></g>''')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1940" height="1040" viewBox="0 0 1940 1040"><rect width="100%" height="100%" fill="{BG}"/>'
           f'<text x="40" y="84" fill="{TXT}" font-family="Geist" font-weight="600" font-size="44" letter-spacing="-1">gymliink — 3 concepts de logo</text>{"".join(cards)}</svg>')
    open('../concepts.svg', 'w').write(svg)
    json.dump([{'type': 'png', 'svg': '../concepts.svg', 'out': '../Gymliink-3-concepts.png', 'w': 1940, 'h': 1040}], open('../jc.json', 'w'))
if __name__ == '__main__':
    _board()
