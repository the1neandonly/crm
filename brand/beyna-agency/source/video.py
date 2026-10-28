"""Motion templates: HTML + CSS keyframes, rendered frame-by-frame (see video_render.js)."""
import os, sys, json
from kit import *
from logo import horizontal, ayna, sub_paths, body_d, almond_d, lid_d, lid_shadow_d, iris_svg, eye_centres, LOGO_SIZE
from brand import *
OUT = sys.argv[1]; HT = os.path.abspath('html/video'); os.makedirs(HT, exist_ok=True)
vids = []
CSS = '''.st{position:relative;overflow:hidden}.ink{background:var(--ink)}.grad{background:var(--grad)}.clear{background:transparent}
.a{position:absolute}.big{font-family:Syne;font-weight:700;letter-spacing:-.03em;line-height:1}.hl{color:var(--lime)}
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
@keyframes lidopen{from{transform:scaleY(1)}to{transform:scaleY(0)}}
@keyframes blink{0%{transform:scaleY(0)}45%{transform:scaleY(1)}100%{transform:scaleY(0)}}
@keyframes look{0%{transform:translateX(0)}25%{transform:translateX(-13px)}60%{transform:translateX(-13px)}100%{transform:translateX(0)}}'''
E = 'cubic-bezier(.2,.8,.2,1)'
def anim(name, dur, delay, ease=E): return f'animation:{name} {dur}s {ease} {delay}s'

def eye_mark(b, s, gid, t0, blink_at, white=True):
    """The animated symbol: the letter rises, the eyelid opens, the iris looks around, then a blink."""
    (ix, iy), (px, py), (gx, gy) = eye_centres()
    sclera = f'<path d="{almond_d()}" fill="#fff"/><path d="{lid_shadow_d()}" fill="#E6E2F5"/>' if white else ''
    iris = iris_svg(ix, iy, px, py, gx, gy, 1, s, INK)
    lid = f'<path d="{almond_d()}" fill="{b}"/>'
    return (f'<g style="transform-origin:50% 100%;{anim("up",.55,t0)}"><path fill-rule="evenodd" fill="{b}" d="{body_d()} {almond_d(rev=True)} {lid_d(rev=True)}"/>{sclera}'
            f'<g style="{anim("popc",.5,t0+.75)}"><g style="{anim("look",1.1,t0+1.25,"ease-in-out")}">{iris}</g></g>'
            f'<g style="transform-origin:50% 50%;{anim("lidopen",.4,t0+.55)}">{lid}</g>'
            f'<g style="transform-origin:50% 50%;{anim("blink",.3,blink_at,"ease-in-out")}">{lid}</g></g>')

def animated_lockup(scheme, t0=0.0, tagline=True):
    """Full horizontal lockup: the eye-b comes alive, then 'ayna' wipes in and AGENCY fades up."""
    b, s, wc, sc, white = {'dark': ('url(#vg)', LIME, '#fff', LIME, True), 'light': ('url(#vg)', LIME, INK, VIOLET, True), 'white': ('#fff', LIME, '#fff', LIME, False)}[scheme]
    tw, th, _ = horizontal('color')
    word, _ = ayna(wc)
    sub, _ = sub_paths('AGENCY', sc, 36, tw, H - 0.697*LOGO_SIZE + 0.72*36, anchor='end', tracking=0.5)
    dx = tw/2 - W/2
    grad = f'<linearGradient id="vg" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="{H}"><stop offset="0" stop-color="{G0}"/><stop offset=".55" stop-color="{G1}"/><stop offset="1" stop-color="{G2}"/></linearGradient>'
    return (f'<svg viewBox="0 0 {tw:.1f} {th:.1f}" width="100%" overflow="visible"><defs>{grad}<clipPath id="wc"><rect x="{W+10}" y="-40" width="{tw}" height="{th+80}" style="transform-origin:0 0;{anim("wipe",.8,t0+2.45)}"/></clipPath></defs>'
            f'<g style="--dx:{dx:.1f}px;{anim("shift",.9,t0+2.15)}">{eye_mark(b, s, "vg", t0, t0+3.55, white)}</g>'
            f'<g clip-path="url(#wc)">{word}</g><g style="{anim("fade",.6,t0+2.9)}">{sub}</g></svg>')

def video(name, w, h, cls, body, dur, fps=30, outs=('mp4',), folder='video'):
    p = f'{HT}/{name}.html'
    open(p, 'w').write(page_doc(f'<div class="st {cls}" style="width:{w}px;height:{h}px">{body}</div>', CSS, f'{w}px {h}px'))
    vids.append(dict(name=name, html=p, w=w, h=h, dur=dur, fps=fps, outs=list(outs), alpha=(cls == 'clear'), out=f'{OUT}/{folder}'))

glow = lambda sz, x, y, d: f'<div class="a" style="left:{x}px;top:{y}px;width:{sz}px;height:{sz}px;border-radius:50%;background:radial-gradient(circle,rgba(99,55,255,.45),rgba(99,55,255,0) 65%);{anim("glow",2.4,d)}"></div>'
tag = lambda fs, d: f'<div class="big" style="font-size:{fs}px;text-align:center;color:#fff;{anim("fadeup",.8,d)}">Make it <span class="hl">clear.</span></div>'

# Logo intros
for nm, w, h, lw, fs in [('logo-intro-16x9-1920x1080', 1920, 1080, 980, 56), ('logo-intro-9x16-1080x1920', 1080, 1920, 860, 60), ('logo-intro-1x1-1080x1080', 1080, 1080, 820, 52)]:
    video(nm, w, h, 'ink', glow(w*1.1, -w*0.05, h/2 - w*0.55, 0) +
          f'<div class="a" style="left:{(w-lw)/2}px;top:{h/2 - lw*0.13}px;width:{lw}px">{animated_lockup("dark")}</div>' +
          f'<div class="a" style="left:0;right:0;top:{h/2 + lw*0.2}px">{tag(fs, 3.3)}</div>', 5.5)
video('logo-intro-transparent-1920x1080', 1920, 1080, 'clear', f'<div class="a" style="left:470px;top:410px;width:980px">{animated_lockup("dark")}</div>', 4.5, outs=('webm', 'mov'))
video('logo-intro-gradient-1920x1080', 1920, 1080, 'grad', f'<div class="a" style="left:470px;top:410px;width:980px">{animated_lockup("white")}</div><div class="a" style="left:0;right:0;top:640px">{tag(56, 3.3)}</div>', 5.5)

# End cards
def endcard(w, h, k):
    return (f'<div class="a" style="left:0;right:0;top:{h*0.26}px;text-align:center;{anim("fadeup",.8,.2)}"><div style="display:inline-block">{mark_svg(body="#fff", height=int(150*k))}</div></div>' +
            f'<div class="a big" style="left:0;right:0;top:{h*0.26 + 200*k}px;text-align:center;color:#fff;font-size:{86*k}px;{anim("fadeup",.8,.5)}">Make it <span class="hl">clear.</span></div>' +
            f'<div class="a" style="left:0;right:0;top:{h*0.26 + 320*k}px;text-align:center;font:500 {32*k}px Manrope;color:rgba(255,255,255,.85);{anim("fadeup",.8,.8)}">{WEB} &nbsp;·&nbsp; {INSTA}</div>' +
            f'<div class="a" style="left:0;right:0;top:{h*0.26 + 400*k}px;text-align:center;{anim("fadeup",.8,1.1)}"><span style="display:inline-block;background:var(--lime);color:var(--ink);font:800 {28*k}px Manrope;padding:{18*k}px {40*k}px;border-radius:999px">Abonnez-vous · Follow</span></div>')
video('end-card-16x9-1920x1080', 1920, 1080, 'grad', endcard(1920, 1080, 1), 5.0)
video('end-card-9x16-1080x1920', 1080, 1920, 'grad', endcard(1080, 1920, 1.15), 5.0)

# Lower third (alpha)
lt = (f'<div class="a" style="left:120px;bottom:120px;height:150px;display:flex;align-items:stretch;overflow:hidden;border-radius:22px;{anim("slidein",.7,.1)}">'
      f'<div style="width:150px;background:var(--grad);display:flex;align-items:center;justify-content:center">{mark_svg(body="#fff", height=84)}</div>'
      f'<div style="background:var(--ink);padding:28px 48px 0 36px;min-width:560px"><div class="big" style="font-size:46px;color:#fff;{anim("fadeup",.6,.5)}">{NAME}</div>'
      f'<div style="font:700 24px Manrope;color:var(--lime);margin-top:10px;{anim("fadeup",.6,.65)}">{ROLE} · Beyna Agency</div></div></div>')
video('lower-third-1920x1080-alpha', 1920, 1080, 'clear', f'<div style="{anim("fadeout",.4,4.4)};position:absolute;inset:0">{lt}</div>', 5.0, outs=('webm', 'mov'))

# Reel template (kinetic type), 9:16
def scene(t_in, t_out, inner):
    return f'<div class="a" style="inset:0;{anim("fade",.3,t_in)}"><div class="a" style="inset:0;{anim("fadeout",.3,t_out)}">{inner}</div></div>'
M = 96
reel = (scene(0, 2.2, f'<div class="a big" style="left:{M}px;top:520px;font-size:560px;color:var(--lime);{anim("popc",.6,.1)};transform-origin:20% 80%">3</div>'
                    f'<div class="a big" style="left:{M}px;right:{M}px;top:1100px;font-size:100px;color:#fff;{anim("fadeup",.6,.6)}">erreurs qui rendent votre marque invisible</div>') +
        ''.join(scene(2.2 + i*1.8, 4.0 + i*1.8,
                      f'<div class="a" style="left:{M}px;top:560px;width:180px;height:180px;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%;{anim("popc",.5,2.3 + i*1.8)}"></div>'
                      f'<div class="a" style="left:{M}px;top:800px;font:500 40px JetBrains Mono;color:var(--lime);{anim("fadeup",.5,2.35 + i*1.8)}">0{i+1}</div>'
                      f'<div class="a big" style="left:{M}px;right:{M}px;top:880px;font-size:130px;color:#fff;{anim("fadeup",.6,2.45 + i*1.8)}">{t}</div>')
                for i, t in enumerate(['Un message flou.', 'Des visuels incohérents.', 'Aucune mesure.'])) +
        f'<div class="a" style="inset:0;background:var(--grad);{anim("fade",.4,7.6)}"></div>' +
        f'<div class="a big" style="left:{M}px;right:{M}px;top:640px;font-size:110px;color:#fff;{anim("fadeup",.6,7.9)}">Rendez votre marque</div>' +
        f'<div class="a" style="left:{M}px;right:{M}px;top:900px;font:700 250px \'Readex Pro\';direction:rtl;text-align:left;color:var(--lime);{anim("fadeup",.6,8.1)}">{NAME_AR}.</div>' +
        f'<div class="a" style="left:{M}px;top:1500px;{anim("fade",.6,8.4)}">{logo_svg("horizontal-compact","on-violet",width=360)}</div>' +
        f'<div class="a" style="left:{M}px;top:120px;opacity:.9">{logo_svg("horizontal-compact","color-dark",width=240)}</div>')
video('reel-template-tips-1080x1920', 1080, 1920, 'ink', reel, 10.0)

# Looping symbol GIF / MP4 (build → hold → loop)
gs = (f'<div class="a" style="left:{300 - 150*W/H:.1f}px;top:110px;width:{300*W/H:.1f}px">'
      f'<svg viewBox="0 0 {W} {H}" width="{300*W/H:.1f}" overflow="visible"><defs><linearGradient id="vg2" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="{H}"><stop offset="0" stop-color="{G0}"/><stop offset=".55" stop-color="{G1}"/><stop offset="1" stop-color="{G2}"/></linearGradient></defs>'
      f'{eye_mark("url(#vg2)", LIME, "vg2", 0, 2.45)}</svg></div>')
video('symbol-loop-600x600', 600, 600, 'ink', f'<div style="position:absolute;inset:0;{anim("fadeout",.35,3.05)}">{gs}</div>', 3.4, fps=25, outs=('mp4', 'gif'))
json.dump(vids, open('videos.json', 'w')); print(len(vids))
