"""Motion templates: HTML + CSS keyframes, rendered frame-by-frame (see video_render.js)."""
import os, sys, json
from kit import *
from logo import horizontal, wordmark_paths, mark_paths, SIZE, BASE, GAP as WGAP
import dto_mark as DM, math
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/video'); os.makedirs(HT, exist_ok=True)
vids = []
CSS = '''.st{position:relative;overflow:hidden}.ink{background:var(--ink)}.grad{background:var(--grad)}.clear{background:transparent}
.a{position:absolute}.big{font-family:Montserrat;font-weight:700;letter-spacing:-.03em;line-height:1}.hl{color:var(--lime)}
*{animation-fill-mode:both!important;animation-play-state:paused!important}
svg g,svg rect{transform-box:fill-box}
@keyframes up{from{transform:scaleY(0)}to{transform:scaleY(1)}}
@keyframes pop{0%{transform:scale(0) rotate(-90deg)}70%{transform:scale(1.06) rotate(4deg)}100%{transform:scale(1) rotate(0)}}
@keyframes popc{0%{transform:scale(0)}65%{transform:scale(1.25)}100%{transform:scale(1)}}
@keyframes shift{from{transform:translateX(var(--dx))}to{transform:translateX(0)}}
@keyframes wipe{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes fadeup{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes fadeout{from{opacity:1}to{opacity:0}}
@keyframes slidein{from{transform:translateX(-110%)}to{transform:translateX(0)}}
@keyframes slideout{from{transform:translateX(0)}to{transform:translateX(-120%)}}
@keyframes glow{from{transform:scale(.6);opacity:0}to{transform:scale(1);opacity:1}}
@keyframes spin{from{transform:rotate(0)}to{transform:rotate(360deg)}}
@keyframes dash{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
@keyframes bracel{from{transform:translateX(var(--bx));opacity:0}to{transform:translateX(0);opacity:1}}
@keyframes fly{from{transform:translate(var(--cx),var(--cy));opacity:0}to{transform:translate(0,0);opacity:1}}
@keyframes click{0%{transform:scale(1)}50%{transform:scale(.86)}100%{transform:scale(1)}}
@keyframes burst{from{transform:scale(0);opacity:0}to{transform:scale(1);opacity:1}}
@keyframes drop{from{transform:translateY(-60px);opacity:0}to{transform:translateY(0);opacity:1}}'''
E = 'cubic-bezier(.2,.8,.2,1)'
def anim(name, dur, delay, ease=E): return f'animation:{name} {dur}s {ease} {delay}s'

def animated_lockup(scheme, t0=0.0, tagline=True):
    """DTO build: braces open → D draws → cursor flies in and clicks → T, cable and O connect → name wipes in."""
    ink, fill, gray, wc = {'dark': ('#FFFFFF', INK, '#6B7177', LIME), 'light': (INK, '#FFFFFF', DM.GRAY, VIOLET), 'white': ('#FFFFFF', VIOLET, '#9CC4EA', '#FFFFFF')}[scheme]
    word, ww = wordmark_paths(wc, SIZE, DM.MW + WGAP, BASE)
    tw, th = DM.MW + WGAP + ww, DM.MH
    dx = tw/2 - DM.MW/2
    cx, cy = 747, 250
    n1 = (cx + 100*math.cos(math.radians(-62)), cy + 100*math.sin(math.radians(-62)))
    n2 = (cx + 60*math.cos(math.radians(35)), cy + 60*math.sin(math.radians(35)))
    wave = 'M452,200 C495,182 522,240 575,234 S655,168 712,170 S772,162 792,158'
    draw = lambda d, sw, col, dl, du=.6, cap='butt': f'<path d="{d}" pathLength="1" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="{cap}" style="stroke-dasharray:1;{anim("dash", du, t0+dl)}"/>'
    svg = (f'<svg viewBox="0 0 {tw:.1f} {th:.1f}" width="100%" overflow="visible"><defs><clipPath id="wc"><rect x="{DM.MW+10}" y="-40" width="{ww+60}" height="{th+80}" style="transform-origin:0 0;{anim("wipe",.8,t0+2.25)}"/></clipPath></defs>'
           f'<g style="--dx:{dx:.1f}px;{anim("shift",.85,t0+2.0)}">'
           f'<g style="--bx:120px;{anim("bracel",.6,t0)}">{DM.brace(ink=ink)}</g><g style="--bx:-120px;{anim("bracel",.6,t0)}">{DM.brace(987, ink=ink)}</g>'
           f'<g style="{anim("fade",.3,t0+.35)}"><rect x="178" y="52" width="40" height="330" fill="{fill}" stroke="{gray}" stroke-width="5"/></g>'
           + draw('M178,71 H272 A146.5,146.5 0 0 1 272,364 H178', 42, ink, .35, .7) +
           f'<g style="transform-origin:30% 50%;{anim("popc",.45,t0+.8)}"><path d="M222,128 H262 A86,86 0 0 1 262,300 H222 Z" fill="{ink}"/></g>'
           f'<g style="transform-origin:300px 235px;{anim("burst",.35,t0+1.45)}">{DM.burst(296, 228, fill)}</g>'
           f'<g style="--cx:260px;--cy:220px;{anim("fly",.6,t0+.9)}"><g style="transform-origin:300px 235px;{anim("click",.25,t0+1.35)}">{DM.cursor(300, 235, ink, fill)}</g></g>'
           f'<g style="{anim("drop",.5,t0+1.2)}"><path d="M438,106 H628 L620,150 H446 Z" fill="{fill}" stroke="{gray}" stroke-width="5" stroke-linejoin="round"/><rect x="514" y="150" width="36" height="210" fill="{ink}"/></g>'
           + draw(DM.arc(cx, cy, 100, -62, 168), 40, ink, 1.35, .7) + draw(DM.arc(cx, cy, 60, 35, 212), 22, ink, 1.45, .6, 'round')
           + draw(wave, 56, ink, 1.3, .6, 'round') + draw(wave, 22, fill, 1.38, .6, 'round') +
           f'<g style="transform-origin:{n1[0]:.0f}px {n1[1]:.0f}px;{anim("popc",.4,t0+1.75)}"><circle cx="{n1[0]:.1f}" cy="{n1[1]:.1f}" r="21" fill="{fill}" stroke="{ink}" stroke-width="7"/></g>'
           f'<g style="transform-origin:{n2[0]:.0f}px {n2[1]:.0f}px;{anim("popc",.4,t0+1.85)}"><circle cx="{n2[0]:.1f}" cy="{n2[1]:.1f}" r="23" fill="{fill}" stroke="{ink}" stroke-width="7"/></g>'
           f'</g><g clip-path="url(#wc)">{word}</g></svg>')
    return svg

def video(name, w, h, cls, body, dur, fps=30, outs=('mp4',), folder='video'):
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(f'<div class="st {cls}" style="width:{w}px;height:{h}px">{body}</div>', CSS, f'{w}px {h}px'))
    vids.append(dict(name=name, html=p, w=w, h=h, dur=dur, fps=fps, outs=list(outs), alpha=(cls == 'clear'), out=f'{OUT}/{folder}'))

glow = lambda sz, x, y, d: f'<div class="a" style="left:{x}px;top:{y}px;width:{sz}px;height:{sz}px;border-radius:50%;background:radial-gradient(circle,rgba(15,102,182,.45),rgba(15,102,182,0) 65%);{anim("glow",2.4,d)}"></div>'
tag = lambda fs, d: f'<div class="big" style="font-size:{fs}px;text-align:center;color:#fff;{anim("fadeup",.8,d)}">Become <span class="hl">the one.</span></div>'

# Logo intros
for nm, w, h, lw, fs in [('logo-intro-16x9-1920x1080', 1920, 1080, 980, 56), ('logo-intro-9x16-1080x1920', 1080, 1920, 860, 60), ('logo-intro-1x1-1080x1080', 1080, 1080, 820, 52)]:
    video(nm, w, h, 'ink', glow(w*1.1, -w*0.05, h/2 - w*0.55, 0) +
          f'<div class="a" style="left:{(w-lw)/2}px;top:{h/2 - lw*0.13}px;width:{lw}px">{animated_lockup("dark")}</div>' +
          f'<div class="a" style="left:0;right:0;top:{h/2 + lw*0.2}px">{tag(fs, 2.9)}</div>', 5.0)
video('logo-intro-transparent-1920x1080', 1920, 1080, 'clear', f'<div class="a" style="left:470px;top:410px;width:980px">{animated_lockup("dark")}</div>', 4.0, outs=('webm', 'mov'))
video('logo-intro-gradient-1920x1080', 1920, 1080, 'grad', f'<div class="a" style="left:470px;top:410px;width:980px">{animated_lockup("white")}</div><div class="a" style="left:0;right:0;top:640px">{tag(56, 2.9)}</div>', 5.0)

# End cards
def endcard(w, h, k):
    return (f'<div class="a" style="left:0;right:0;top:{h*0.26}px;text-align:center;{anim("fadeup",.8,.2)}"><div style="display:inline-block">{mark_svg(body="#fff", height=int(150*k))}</div></div>' +
            f'<div class="a big" style="left:0;right:0;top:{h*0.26 + 200*k}px;text-align:center;color:#fff;font-size:{86*k}px;{anim("fadeup",.8,.5)}">Become <span class="hl">the one.</span></div>' +
            f'<div class="a" style="left:0;right:0;top:{h*0.26 + 320*k}px;text-align:center;font:500 {32*k}px Inter;color:rgba(255,255,255,.85);{anim("fadeup",.8,.8)}">{WEB} &nbsp;·&nbsp; {INSTA}</div>' +
            f'<div class="a" style="left:0;right:0;top:{h*0.26 + 400*k}px;text-align:center;{anim("fadeup",.8,1.1)}"><span style="display:inline-block;background:var(--lime);color:var(--ink);font:800 {28*k}px Inter;padding:{18*k}px {40*k}px;border-radius:999px">Abonnez-vous · Follow</span></div>')
video('end-card-16x9-1920x1080', 1920, 1080, 'grad', endcard(1920, 1080, 1), 5.0)
video('end-card-9x16-1080x1920', 1080, 1920, 'grad', endcard(1080, 1920, 1.15), 5.0)

# Lower third (alpha)
lt = (f'<div class="a" style="left:120px;bottom:120px;height:150px;display:flex;align-items:stretch;overflow:hidden;border-radius:22px;{anim("slidein",.7,.1)}">'
      f'<div style="width:150px;background:var(--grad);display:flex;align-items:center;justify-content:center">{mark_svg(body="#fff", height=84)}</div>'
      f'<div style="background:var(--ink);padding:28px 48px 0 36px;min-width:560px"><div class="big" style="font-size:46px;color:#fff;{anim("fadeup",.6,.5)}">{NAME}</div>'
      f'<div style="font:700 24px Inter;color:var(--lime);margin-top:10px;{anim("fadeup",.6,.65)}">{ROLE} · DevelopTheOne</div></div></div>')
video('lower-third-1920x1080-alpha', 1920, 1080, 'clear', f'<div style="{anim("fadeout",.4,4.4)};position:absolute;inset:0">{lt}</div>', 5.0, outs=('webm', 'mov'))

# Reel template (kinetic type), 9:16
def scene(t_in, t_out, inner):
    return f'<div class="a" style="inset:0;{anim("fade",.3,t_in)}"><div class="a" style="inset:0;{anim("fadeout",.3,t_out)}">{inner}</div></div>'
M = 96
reel = (scene(0, 2.2, f'<div class="a big" style="left:{M}px;top:520px;font-size:560px;color:var(--lime);{anim("popc",.6,.1)};transform-origin:20% 80%">3</div>'
                    f'<div class="a big" style="left:{M}px;right:{M}px;top:1100px;font-size:100px;color:#fff;{anim("fadeup",.6,.6)}">erreurs qui rendent votre marque invisible</div>') +
        ''.join(scene(2.2 + i*1.8, 4.0 + i*1.8,
                      f'<div class="a" style="left:{M}px;top:560px;width:180px;height:180px;background:var(--lime);border-top-left-radius:180px;{anim("popc",.5,2.3 + i*1.8)}"></div>'
                      f'<div class="a" style="left:{M}px;top:800px;font:500 40px JetBrains Mono;color:var(--lime);{anim("fadeup",.5,2.35 + i*1.8)}">0{i+1}</div>'
                      f'<div class="a big" style="left:{M}px;right:{M}px;top:880px;font-size:130px;color:#fff;{anim("fadeup",.6,2.45 + i*1.8)}">{t}</div>')
                for i, t in enumerate(['Un message flou.', 'Des visuels incohérents.', 'Aucune mesure.'])) +
        f'<div class="a" style="inset:0;background:var(--grad);{anim("fade",.4,7.6)}"></div>' +
        f'<div class="a big" style="left:{M}px;right:{M}px;top:640px;font-size:110px;color:#fff;{anim("fadeup",.6,7.9)}">Faites de votre marque</div>' +
        f'<div class="a big" style="left:{M}px;right:{M}px;top:900px;font-size:150px;color:var(--lime);{anim("fadeup",.6,8.1)}">la référence.</div>' +
        f'<div class="a" style="left:{M}px;top:1500px;{anim("fade",.6,8.4)}">{logo_svg("horizontal-compact","on-violet",width=360)}</div>' +
        f'<div class="a" style="left:{M}px;top:120px;opacity:.9">{logo_svg("horizontal-compact","color-dark",width=240)}</div>')
video('reel-template-tips-1080x1920', 1080, 1920, 'ink', reel, 10.0)

# Looping icon GIF / MP4: {D} builds, cursor clicks, burst — then loops
ic = (f'<div class="a" style="left:90px;top:120px;width:420px"><svg viewBox="0 0 {DM.IW} {DM.IH}" width="420" overflow="visible">'
      f'<g style="--bx:60px;{anim("bracel",.5,0)}">{DM.brace(ink="#FFFFFF")}</g><g style="--bx:-60px;{anim("bracel",.5,0)}">{DM.brace(DM.IW - 18, ink="#FFFFFF")}</g>'
      f'<g style="{anim("fade",.4,.3)}">{DM.letter_d("#FFFFFF", INK, "#6B7177")}</g>'
      f'<g style="transform-origin:300px 235px;{anim("burst",.3,1.35)}">{DM.burst(296, 228, LIME)}</g>'
      f'<g style="--cx:200px;--cy:160px;{anim("fly",.55,.75)}"><g style="transform-origin:300px 235px;{anim("click",.25,1.25)}">{DM.cursor(300, 235, "#FFFFFF", VIOLET)}</g></g></svg></div>')
video('icon-loop-600x600', 600, 600, 'ink', f'<div style="position:absolute;inset:0;{anim("fadeout",.35,2.65)}">{ic}</div>', 3.0, fps=25, outs=('mp4', 'gif'))
json.dump(vids, open('videos.json', 'w')); print(len(vids))
