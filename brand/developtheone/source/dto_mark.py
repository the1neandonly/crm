"""DevelopTheOne mark — faithful vector rebuild of the original {DTO} logo (units: 3x the original pixels)."""
import math
BLUE = '#0F66B6'; INK = '#0A0B0D'; WHITE = '#FFFFFF'; GRAY = '#A5A8AA'
MW, MH = 1005, 438                     # full {DTO} mark box (x 0..1005, y 0..438)

BRACE = ('M155,5 L120,5 C85,5 68,25 68,60 L68,165 C68,190 50,207 18,215 C50,223 68,240 68,265 L68,375 C68,410 85,432 120,432 L155,432 '
         'L155,398 L125,398 C108,398 103,388 103,370 L103,270 C103,245 90,225 68,215 C90,205 103,185 103,160 L103,68 C103,50 108,40 125,40 L155,40 Z')
def brace(right_x=None, ink=INK):
    """Left brace as drawn in the original; pass right_x to mirror it as the closing brace ending at right_x."""
    if right_x is None: return f'<path d="{BRACE}" fill="{ink}"/>'
    return f'<path d="{BRACE}" fill="{ink}" transform="translate({right_x + 18},0) scale(-1,1)"/>'

def cursor(x, y, ink, fill, rot=-14, sc=1.15, sw=10):
    pts = '0,0 0,150 36,116 62,176 86,166 60,108 112,106'
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({sc})"><polygon points="{pts}" fill="{fill}" stroke="{ink}" '
            f'stroke-width="{sw/sc:.2f}" stroke-linejoin="round"/></g>')

def burst(x, y, col, r0=24, r1=48, w=8):
    out = []
    for a in (182, 212, 240, 268, 300):
        c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
        out.append(f'<line x1="{x + c*r0:.1f}" y1="{y + s*r0:.1f}" x2="{x + c*r1:.1f}" y2="{y + s*r1:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
    return ''.join(out)

def letter_d(ink, fill, gray, ox=0):
    # outer D: black stroke on top/right/bottom, light left stem (as in the original), solid inner D
    return (f'<rect x="{ox+178}" y="{52}" width="40" height="330" fill="{fill}" stroke="{gray}" stroke-width="5"/>'
            f'<path d="M{ox+178},71 H{ox+272} A146.5,146.5 0 0 1 {ox+272},364 H{ox+178}" fill="none" stroke="{ink}" stroke-width="42"/>'
            f'<path d="M{ox+222},128 H{ox+262} A86,86 0 0 1 {ox+262},300 H{ox+222} Z" fill="{ink}"/>')

def arc(cx, cy, r, a0, a1):
    p = lambda a: (cx + r*math.cos(math.radians(a)), cy + r*math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = p(a0), p(a1); large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'M{x0:.1f},{y0:.1f} A{r},{r} 0 {large},1 {x1:.1f},{y1:.1f}'

def letter_t_wave_o(ink, fill, gray):
    cx, cy = 747, 250
    wave = 'M452,200 C495,182 522,240 575,234 S655,168 712,170 S772,162 792,158'
    n1 = (cx + 100*math.cos(math.radians(-62)), cy + 100*math.sin(math.radians(-62)))
    n2 = (cx + 60*math.cos(math.radians(35)), cy + 60*math.sin(math.radians(35)))
    return (f'<path d="M438,106 H628 L620,150 H446 Z" fill="{fill}" stroke="{gray}" stroke-width="5" stroke-linejoin="round"/>'
            f'<rect x="514" y="150" width="36" height="210" fill="{ink}"/>'
            f'<path d="{arc(cx, cy, 100, -62, 168)}" fill="none" stroke="{ink}" stroke-width="40"/>'
            f'<path d="{arc(cx, cy, 60, 35, 212)}" fill="none" stroke="{ink}" stroke-width="22" stroke-linecap="round"/>'
            f'<path d="{wave}" fill="none" stroke="{ink}" stroke-width="56" stroke-linecap="round"/>'
            f'<path d="{wave}" fill="none" stroke="{fill}" stroke-width="22" stroke-linecap="round"/>'
            f'<circle cx="{n1[0]:.1f}" cy="{n1[1]:.1f}" r="21" fill="{fill}" stroke="{ink}" stroke-width="7"/>'
            f'<circle cx="{n2[0]:.1f}" cy="{n2[1]:.1f}" r="23" fill="{fill}" stroke="{ink}" stroke-width="7"/>')

def full_mark(ink=INK, fill=WHITE, gray=GRAY, burst_c=None):
    """{DTO}: braces, D + clicking cursor, T, wave, O with nodes."""
    bc = burst_c or fill
    return (brace(ink=ink) + brace(987, ink=ink) + letter_d(ink, fill, gray) +
            letter_t_wave_o(ink, fill, gray) + burst(296, 228, bc if bc != 'none' else ink) + cursor(300, 235, ink, fill))

# Icon: {D} with the clicking cursor — square-ish, for avatars, favicons and big decorative crops
IW, IH = 560, 438
def icon_mark(ink=INK, fill=WHITE, gray=GRAY, burst_c=None, braces=True):
    bc = burst_c or fill
    br = (brace(ink=ink) + brace(IW - 18, ink=ink)) if braces else ''
    return (br + letter_d(ink, fill, gray) + burst(296, 228, bc if bc != 'none' else ink) + cursor(300, 235, ink, fill))
