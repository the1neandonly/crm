"""Application artboards: each returns (width, height, html). Used in the book and exported on their own."""
from base import *
GYM, MEMBER, MID, URL = 'Atlas Gym · Oran', 'Yasmine Benali', 'GL-0042-7781', 'https://gymliink.com/m/GL-0042-7781'
HAIR = 'border:1px solid var(--line)'
def sb(dark=True):   # iOS status bar
    c = TXT if dark else BG
    return (f'<div style="height:54px;display:flex;align-items:center;justify-content:space-between;padding:14px 34px 0 40px;font:600 17px Geist;color:{c}">'
            f'<span>9:41</span><span style="display:flex;gap:7px;align-items:center">{ic("cell-signal-full" if False else "wifi-high", 19, c)}<span style="width:27px;height:13px;border:1.5px solid {c};border-radius:4px;display:inline-block;position:relative"><i style="position:absolute;inset:2px 5px 2px 2px;background:{c};border-radius:1.5px"></i></span></span></div>')
def phone(inner, light=False):
    bg = LBG if light else BG
    return (f'<div style="width:430px;height:884px;border-radius:66px;background:#1A1A1D;padding:20px;box-shadow:0 0 0 2px #2E2E33,0 40px 80px rgba(0,0,0,.45)">'
            f'<div style="width:390px;height:844px;border-radius:48px;background:{bg};overflow:hidden;position:relative">'
            f'<div style="position:absolute;left:50%;top:11px;width:124px;height:36px;margin-left:-62px;background:#000;border-radius:20px;z-index:3"></div>{sb(not light)}{inner}</div></div>')
def membercard_ui(ar=False, w=342):
    d = 'rtl' if ar else 'ltr'; F = "'Plex Arabic',Geist" if ar else 'Geist'
    t = ({'gym': 'أطلس جيم · وهران', 'sub': 'اشتراك شهري', 'val': 'صالح حتى 12 مارس 2026', 'st': 'نشط', 'scan': 'قدّم الرمز عند المدخل'} if ar else
         {'gym': GYM, 'sub': 'Abonnement mensuel', 'val': 'Valide jusqu’au 12 mars 2026', 'st': 'Actif', 'scan': 'Présentez ce code à l’entrée'})
    return (f'<div style="width:{w}px;border-radius:24px;background:var(--s1);{HAIR};padding:22px;direction:{d};font-family:{F}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><div style="display:flex;gap:10px;align-items:center">'
            f'<div style="width:34px;height:34px;border-radius:10px;background:var(--s3);display:flex;align-items:center;justify-content:center">{ic("barbell", 20, TXT)}</div>'
            f'<div><div style="font:600 15px {F}">{t["gym"]}</div><div style="font:400 13px {F};color:var(--tx2)">{t["sub"]}</div></div></div>{pill(t["st"], "active", ar, 13)}</div>'
            f'<div style="margin:22px auto 14px;width:{w-120}px;padding:12px;border-radius:18px;background:#fff">{qr_svg(URL, w-144, BG, "#fff", 1)}</div>'
            f'<div style="text-align:center;font:400 13px {F};color:var(--tx2)">{t["scan"]}</div>'
            f'<div style="height:1px;background:var(--line);margin:18px 0"></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><div style="font:600 17px {F}">{"ياسمين بن علي" if ar else MEMBER}</div>'
            f'<div style="font:400 13px {F};color:var(--tx2);margin-top:3px">{t["val"]}</div></div><div class="mono" style="font:500 13px \'Geist Mono\';color:var(--tx2);direction:ltr">{MID}</div></div></div>')
def a_app_card():
    tab = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:4px;color:{VOLT if i == 1 else TXT2};font:500 10px Geist">{ic(n, 24, VOLT if i == 1 else TXT2)}{l}</div>'
                  for i, (n, l) in enumerate([('house', 'Accueil'), ('identification-card', 'Carte'), ('calendar', 'Cours'), ('chart-line', 'Progrès'), ('user', 'Profil')]))
    inner = (f'<div style="padding:8px 24px 0"><div style="font:600 34px/41px Geist;letter-spacing:-.02em">Ma carte</div><div style="font:400 15px Geist;color:var(--tx2);margin-top:4px">Bonjour Yasmine</div></div>'
             f'<div style="padding:22px 24px">{membercard_ui()}</div>'
             f'<div style="position:absolute;left:0;right:0;bottom:0;height:84px;border-top:1px solid var(--line);background:rgba(20,20,22,.92);display:flex;justify-content:space-around;padding-top:10px">{tab}</div>')
    return 470, 924, f'<div style="padding:20px">{phone(inner)}</div>'
def a_app_card_ar():
    inner = (f'<div style="padding:8px 24px 0;direction:rtl"><div class="ar" style="font:600 34px/44px \'Plex Arabic\',Geist">بطاقتي</div><div class="ar" style="font:400 15px \'Plex Arabic\',Geist;color:var(--tx2)">مرحباً ياسمين</div></div>'
             f'<div style="padding:22px 24px">{membercard_ui(True)}</div>')
    return 470, 924, f'<div style="padding:20px">{phone(inner)}</div>'
def a_checkin():
    inner = (f'<div style="position:absolute;inset:54px 0 0;display:flex;flex-direction:column;align-items:center;padding:30px 28px">'
             f'<div style="font:500 13px \'Geist Mono\';color:var(--tx2);letter-spacing:.12em">CHECK-IN · 07:42</div>'
             f'<div style="margin-top:70px;width:168px;height:168px;border-radius:50%;background:radial-gradient(circle,rgba(197,240,74,.22),rgba(197,240,74,0) 70%);display:flex;align-items:center;justify-content:center">'
             f'<div style="width:112px;height:112px;border-radius:50%;background:var(--volt);display:flex;align-items:center;justify-content:center">{ic("check", 56, INK_ON_VOLT)}</div></div>'
             f'<div style="font:600 28px/34px Geist;margin-top:36px;letter-spacing:-.01em">Accès autorisé</div><div class="ar" style="font:500 18px \'Plex Arabic\',Geist;color:var(--tx2);margin-top:6px;text-align:center">تم السماح بالدخول</div>'
             f'<div style="margin-top:34px;width:100%;border-radius:20px;background:var(--s1);{HAIR};padding:18px;display:flex;gap:14px;align-items:center">'
             f'<div style="width:48px;height:48px;border-radius:50%;background:var(--s3);display:flex;align-items:center;justify-content:center;font:600 17px Geist">YB</div>'
             f'<div style="flex:1"><div style="font:600 17px Geist">{MEMBER}</div><div style="font:400 13px Geist;color:var(--tx2)">Mensuel · expire le 12/03</div></div>{pill("Actif", "active", size=13)}</div>'
             f'<div style="margin-top:12px;width:100%;display:flex;gap:12px">'
             + ''.join(f'<div style="flex:1;border-radius:16px;background:var(--s1);{HAIR};padding:14px"><div style="font:400 12px Geist;color:var(--tx2)">{k}</div><div class="mono" style="font:500 20px \'Geist Mono\';margin-top:6px">{v}</div></div>' for k, v in [('Visites ce mois', '14'), ('Série', '6 j')])
             + f'</div><div style="position:absolute;bottom:40px;left:28px;right:28px;height:54px;border-radius:16px;background:var(--s2);{HAIR};display:flex;align-items:center;justify-content:center;font:500 17px Geist">Scanner le suivant</div></div>')
    return 470, 924, f'<div style="padding:20px">{phone(inner)}</div>'
def a_card_physical():
    W, H = 856, 540
    front = (f'<div style="width:{W}px;height:{H}px;border-radius:34px;background:var(--bg);position:relative;overflow:hidden;box-shadow:inset 0 0 0 1px var(--line)">'
             f'<div style="position:absolute;right:-120px;top:-160px;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(197,240,74,.13),rgba(197,240,74,0) 65%)"></div>'
             f'<div style="position:absolute;left:56px;top:52px">{logo("horizontal", "color-dark", height=46)}</div>'
             f'<div style="position:absolute;right:56px;top:58px;font:500 15px \'Geist Mono\';color:var(--tx2);letter-spacing:.14em">MEMBER</div>'
             f'<div style="position:absolute;left:56px;bottom:56px"><div style="font:500 15px Geist;color:var(--tx2)">{GYM}</div><div style="font:600 38px Geist;letter-spacing:-.02em;margin-top:6px">{MEMBER}</div>'
             f'<div class="mono" style="font:500 20px \'Geist Mono\';color:var(--tx2);margin-top:10px;letter-spacing:.06em">{MID}</div></div>'
             f'<div style="position:absolute;right:56px;bottom:56px;width:150px;height:150px;padding:10px;border-radius:18px;background:#fff">{qr_svg(URL, 130, BG, "#fff", 1)}</div></div>')
    back = (f'<div style="width:{W}px;height:{H}px;border-radius:34px;background:var(--volt);position:relative;overflow:hidden;color:var(--vink)">'
            f'<div style="position:absolute;left:56px;top:56px">{logo("symbol", "on-volt", height=120)}</div>'
            f'<div style="position:absolute;left:56px;bottom:56px;font:500 20px Geist;line-height:1.5">Scannez à l’entrée · <span class="ar" style="font-family:\'Plex Arabic\',Geist">امسح عند الدخول</span><br><span class="mono" style="font-family:\'Geist Mono\'">gymliink.com</span></div>'
            f'<div style="position:absolute;right:56px;top:56px;font:500 14px \'Geist Mono\';text-align:right;line-height:1.6">CARTE PERSONNELLE<br>NON CESSIBLE</div></div>')
    return W*2 + 60, H, f'<div style="display:flex;gap:60px">{front}{back}</div>'
def a_receipt():
    rows = [('Abonnement mensuel', '4 500'), ('Frais d’inscription', '1 000'), ('Remise parrainage', '−500')]
    r = ''.join(f'<div style="display:flex;justify-content:space-between"><span>{a}</span><span>{b}</span></div>' for a, b in rows)
    body = (f'<div style="width:576px;padding:44px 40px;background:#FBFBF8;color:#111;font:400 20px/1.6 \'Geist Mono\'">'
            f'<div style="display:flex;justify-content:center">{logo("horizontal", "black", height=42)}</div>'
            f'<div style="text-align:center;margin-top:16px">{GYM}<br>12 bd de l’ALN, Oran<br>RC 31/00-0000000 · NIF 000000000000000</div>'
            f'<div style="border-top:2px dashed #999;margin:22px 0"></div>'
            f'<div style="display:flex;justify-content:space-between"><span>Reçu</span><span>N° 2026-03-0412</span></div><div style="display:flex;justify-content:space-between"><span>Date</span><span>12/02/2026 18:04</span></div>'
            f'<div style="display:flex;justify-content:space-between"><span>Membre</span><span>{MID}</span></div><div style="display:flex;justify-content:space-between"><span>Caisse</span><span>Accueil · Nadia</span></div>'
            f'<div style="border-top:2px dashed #999;margin:22px 0"></div>{r}'
            f'<div style="border-top:2px solid #111;margin:18px 0 12px"></div><div style="display:flex;justify-content:space-between;font-weight:600;font-size:26px"><span>TOTAL</span><span>5 000 DA</span></div>'
            f'<div style="display:flex;justify-content:space-between;margin-top:8px"><span>Payé par</span><span>Edahabia ···· 4417</span></div>'
            f'<div style="text-align:right;font-family:\'Plex Arabic\',Geist;direction:rtl;margin-top:10px">المجموع: 5 000 دج · شكراً لزيارتكم</div>'
            f'<div style="border-top:2px dashed #999;margin:22px 0"></div><div style="display:flex;gap:22px;align-items:center"><div style="width:150px">{qr_svg("https://gymliink.com/r/2026-03-0412", 150, "#111", "#FBFBF8", 1, False)}</div>'
            f'<div style="font-size:17px;line-height:1.5">Reçu numérique et historique de paiements dans l’app gymliink.<br>Valide jusqu’au 12/03/2026.</div></div>'
            f'<div style="text-align:center;margin-top:24px;font-size:16px;color:#555">Merci · Propulsé par gymliink.com</div></div>')
    return 576, 1240, body
def a_poster():
    W, H = 1123, 1587
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--bg);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:50%;top:47%;width:1100px;height:1100px;margin:-550px 0 0 -550px;border-radius:50%;background:radial-gradient(circle,rgba(197,240,74,.12),rgba(197,240,74,0) 62%)"></div>'
         f'<div style="position:absolute;left:90px;top:90px">{logo("horizontal", "color-dark", height=58)}</div><div class="mono" style="position:absolute;right:90px;top:104px;font:500 20px \'Geist Mono\';color:var(--tx2)">{GYM.upper()}</div>'
         f'<div style="position:absolute;left:90px;top:250px;font:600 120px/1 Geist;letter-spacing:-.04em">Scannez<br>pour entrer.</div>'
         f'<div class="ar" style="position:absolute;right:90px;top:520px;font:600 72px \'Plex Arabic\',Geist">امسح للدخول</div>'
         f'<div style="position:absolute;left:50%;top:700px;margin-left:-260px;width:520px;height:520px;padding:34px;border-radius:44px;background:#fff;box-shadow:0 0 0 14px rgba(197,240,74,.25)">{qr_svg("https://gymliink.com/checkin/atlas-oran", 452, BG, "#fff", 1)}</div>'
         f'<div style="position:absolute;left:90px;right:90px;bottom:90px;display:flex;justify-content:space-between;align-items:flex-end;font:400 24px/1.5 Geist;color:var(--tx2)">'
         f'<div>1. Ouvrez l’app gymliink<br>2. Touchez <span style="color:var(--tx)">Check-in</span><br>3. Scannez ce code</div><div class="mono" style="font-family:\'Geist Mono\';text-align:right">Pas de compte ?<br><span class="v">gymliink.com</span></div></div></div>')
    return W, H, b
def a_sticker():
    S = 900
    b = (f'<div style="width:{S}px;height:{S}px;border-radius:50%;background:var(--bg);position:relative;box-shadow:inset 0 0 0 4px var(--volt)">'
         f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px">'
         f'<div style="font:500 30px \'Geist Mono\';letter-spacing:.24em;color:var(--tx2)">GYM POWERED BY</div>{logo("horizontal", "color-dark", width=520)}'
         f'<div class="ar" style="font:500 32px \'Plex Arabic\',Geist;color:var(--tx2);text-align:center">قاعة مدعومة بـ جيم لينك</div>'
         f'<div style="margin-top:6px;padding:10px 26px;border-radius:999px;background:var(--volt);color:var(--vink);font:600 26px Geist">Check-in par QR</div></div></div>')
    return S, S, b
def a_partner():
    W, H = 856, 540
    f = (f'<div style="width:{W}px;height:{H}px;border-radius:30px;background:var(--s1);box-shadow:inset 0 0 0 1px var(--line);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:56px;top:52px">{logo("horizontal", "color-dark", height=42)}</div><div style="position:absolute;right:56px;top:54px">{pill("Partenaire", "info", size=16)}</div>'
         f'<div style="position:absolute;left:56px;top:190px;font:600 44px/1.1 Geist;letter-spacing:-.02em">Équipez votre salle.<br><span class="t2">On vous offre le 1<sup>er</sup> mois.</span></div>'
         f'<div style="position:absolute;left:56px;bottom:56px"><div style="font:400 15px Geist;color:var(--tx2)">Code partenaire</div><div class="mono" style="font:600 34px \'Geist Mono\';color:var(--volt);letter-spacing:.08em">KARIM-ORAN-25</div></div>'
         f'<div style="position:absolute;right:56px;bottom:56px;width:140px;padding:10px;border-radius:16px;background:#fff">{qr_svg("https://gymliink.com/p/KARIM-ORAN-25", 120, BG, "#fff", 1)}</div></div>')
    bk = (f'<div style="width:{W}px;height:{H}px;border-radius:30px;background:var(--bg);box-shadow:inset 0 0 0 1px var(--line);position:relative;overflow:hidden">'
          f'<div style="position:absolute;left:56px;top:56px"><div style="font:600 30px Geist">Karim Haddad</div><div style="font:400 18px Geist;color:var(--tx2);margin-top:4px">Partenaire agréé · Oran</div></div>'
          f'<div style="position:absolute;left:56px;top:190px;display:grid;gap:16px;font:400 20px Geist">'
          + ''.join(f'<div style="display:flex;gap:14px;align-items:center">{ic(i, 26, VOLT)}<span>{t}</span></div>' for i, t in [('phone', '+213 (0) 555 00 00 00'), ('whatsapp-logo', 'WhatsApp · même numéro'), ('globe', 'gymliink.com/partenaires')])
          + f'</div><div class="ar" style="position:absolute;right:56px;bottom:56px;font:500 22px \'Plex Arabic\',Geist;color:var(--tx2)">أحِل قاعة واربح عمولة على كل اشتراك</div></div>')
    return W*2 + 60, H, f'<div style="display:flex;gap:60px">{f}{bk}</div>'
def ig_post(kind):
    W, H = 1080, 1350
    if kind == 1:
        inner = (f'<div style="position:absolute;left:88px;top:88px">{logo("horizontal", "color-dark", height=48)}</div>'
                 f'<div style="position:absolute;left:88px;top:330px;font:600 112px/1.02 Geist;letter-spacing:-.045em">Votre carte<br>de membre,<br><span class="v">dans la poche.</span></div>'
                 f'<div style="position:absolute;left:88px;bottom:88px;font:400 30px/1.45 Geist;color:var(--tx2);max-width:640px">Check-in par QR, paiement Edahabia ou BaridiMob, réservation des cours.</div>'
                 f'<div style="position:absolute;right:88px;bottom:88px;transform:rotate(-6deg);transform-origin:right bottom">{membercard_ui(False, 300)}</div>')
    else:
        inner = (f'<div style="position:absolute;inset:0;background:var(--volt)"></div><div style="position:absolute;left:88px;top:88px">{logo("horizontal", "on-volt", height=48)}</div>'
                 f'<div style="position:absolute;left:88px;top:300px;color:var(--vink)"><div class="mono" style="font:500 30px \'Geist Mono\'">CHIFFRE DU MOIS</div><div style="font:600 300px/1 Geist;letter-spacing:-.06em;margin-top:20px">12 400</div>'
                 f'<div style="font:500 44px/1.2 Geist;letter-spacing:-.02em;margin-top:30px;max-width:820px">check-ins scannés en février dans les salles gymliink.</div></div>'
                 f'<div class="ar" style="position:absolute;right:88px;bottom:88px;color:var(--vink);font:600 40px \'Plex Arabic\',Geist">12 400 دخول في فبراير</div>')
    return W, H, f'<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:var(--bg)">{inner}</div>'
def ig_story(kind):
    W, H = 1080, 1920
    if kind == 1:
        inner = (f'<div style="position:absolute;left:88px;top:260px">{logo("horizontal", "color-dark", height=52)}</div>'
                 f'<div style="position:absolute;left:88px;top:520px;font:600 128px/1.02 Geist;letter-spacing:-.045em">Rappel :<br>votre abonnement<br><span class="v">expire dans 3 jours.</span></div>'
                 f'<div class="ar" style="position:absolute;right:88px;top:1250px;font:600 58px/1.4 \'Plex Arabic\',Geist">اشتراكك ينتهي بعد 3 أيام</div>'
                 f'<div style="position:absolute;left:88px;right:88px;bottom:360px;height:120px;border-radius:30px;background:var(--volt);color:var(--vink);display:flex;align-items:center;justify-content:center;font:600 40px Geist">Renouveler · 4 500 DA</div>')
    else:
        inner = (f'<div style="position:absolute;left:50%;top:44%;width:1400px;height:1400px;margin:-700px 0 0 -700px;border-radius:50%;background:radial-gradient(circle,rgba(197,240,74,.14),rgba(197,240,74,0) 60%)"></div>'
                 f'<div style="position:absolute;left:50%;top:420px;margin-left:-160px">{logo("symbol", "color-dark", height=380)}</div>'
                 f'<div style="position:absolute;left:0;right:0;top:960px;text-align:center;font:600 96px/1.05 Geist;letter-spacing:-.04em">Nouveau :<br>réservez vos cours.</div>'
                 f'<div class="ar" style="position:absolute;left:0;right:0;top:1230px;text-align:center;font:500 52px \'Plex Arabic\',Geist;direction:rtl;color:var(--tx2)">احجز حصصك من التطبيق</div>'
                 f'<div class="mono" style="position:absolute;left:0;right:0;bottom:340px;text-align:center;font:500 34px \'Geist Mono\';color:var(--volt)">gymliink.com</div>')
    return W, H, f'<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:var(--bg)">{inner}</div>'
def a_email():
    W, H = 1200, 400
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--bg);position:relative;overflow:hidden;box-shadow:inset 0 -1px 0 var(--line)">'
         f'<div style="position:absolute;right:-80px;top:-260px;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(197,240,74,.14),rgba(197,240,74,0) 62%)"></div>'
         f'<div style="position:absolute;left:72px;top:64px">{logo("horizontal", "color-dark", height=44)}</div>'
         f'<div style="position:absolute;left:72px;bottom:70px;font:600 52px/1.1 Geist;letter-spacing:-.03em">Votre reçu de février<span class="v">.</span></div>'
         f'<div class="mono" style="position:absolute;right:72px;bottom:76px;font:500 20px \'Geist Mono\';color:var(--tx2)">REÇU N° 2026-03-0412</div></div>')
    return W, H, b
def a_whatsapp():
    S = 640
    b = (f'<div style="width:{S}px;height:{S}px;background:var(--bg);position:relative;overflow:hidden">'
         f'<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 48%,rgba(197,240,74,.16),rgba(197,240,74,0) 55%)"></div>'
         f'<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)">{logo("symbol", "color-dark", height=300)}</div></div>')
    return S, S, b
def a_website():
    W, H = 1440, 900
    nav = ''.join(f'<span>{t}</span>' for t in ['Produit', 'Salles', 'Coachs', 'Membres', 'Partenaires', 'Tarifs'])
    b = (f'<div style="width:{W}px;height:{H}px;background:var(--bg);position:relative;overflow:hidden">'
         f'<div style="position:absolute;left:50%;top:60%;width:1600px;height:1000px;margin:-500px 0 0 -800px;background:radial-gradient(ellipse,rgba(197,240,74,.11),rgba(197,240,74,0) 60%)"></div>'
         f'<div style="height:76px;display:flex;align-items:center;justify-content:space-between;padding:0 64px;border-bottom:1px solid var(--line)">{logo("horizontal", "color-dark", height=30)}'
         f'<div style="display:flex;gap:34px;font:400 15px Geist;color:var(--tx2)">{nav}</div><div style="display:flex;gap:12px;align-items:center"><span style="font:400 15px Geist;color:var(--tx2)">FR · <span class="ar" style="font-family:\'Plex Arabic\',Geist">عربي</span></span>'
         f'<span style="padding:10px 18px;border-radius:10px;background:var(--volt);color:var(--vink);font:600 15px Geist">Demander une démo</span></div></div>'
         f'<div style="position:absolute;left:64px;top:170px;width:640px">{pill("Nouveau · Paiement BaridiMob", "info", size=14)}'
         f'<div style="font:600 76px/1.02 Geist;letter-spacing:-.045em;margin-top:28px">Le logiciel calme<br>des salles de sport<br><span class="v">en Algérie.</span></div>'
         f'<div style="font:400 20px/1.55 Geist;color:var(--tx2);margin-top:26px;max-width:560px">Membres, check-in par QR, caisse, planning des cours et paiements en DA — sur le web et sur iOS et Android.</div>'
         f'<div style="display:flex;gap:12px;margin-top:36px"><span style="padding:16px 24px;border-radius:12px;background:var(--volt);color:var(--vink);font:600 17px Geist">Essayer 30 jours</span>'
         f'<span style="padding:16px 24px;border-radius:12px;background:var(--s2);border:1px solid var(--line);font:500 17px Geist">Voir l’app membre</span></div>'
         f'<div style="display:flex;gap:26px;margin-top:44px;font:400 14px \'Geist Mono\';color:var(--tx2)"><span>EDAHABIA</span><span>CIB</span><span>CCP</span><span>BARIDIMOB</span></div></div>'
         f'<div style="position:absolute;right:64px;top:150px;width:600px;height:660px;border-radius:24px;background:var(--s1);border:1px solid var(--line);overflow:hidden">'
         f'<div style="height:52px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:10px;padding:0 20px;font:500 14px Geist;color:var(--tx2)">{ic("storefront", 18, TXT2)} Atlas Gym · Tableau de bord</div>'
         f'<div style="padding:22px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">'
         + ''.join(f'<div style="border-radius:14px;background:var(--s2);padding:14px"><div style="font:400 12px Geist;color:var(--tx2)">{k}</div><div class="mono" style="font:500 22px \'Geist Mono\';margin-top:6px">{v}</div></div>' for k, v in [('Membres actifs', '412'), ('Check-ins auj.', '138'), ('Encaissé', '186 500 DA')])
         + '</div><div style="padding:0 22px">'
         + ''.join(f'<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1px solid var(--line)"><div style="width:34px;height:34px;border-radius:50%;background:var(--s3);font:600 13px Geist;display:flex;align-items:center;justify-content:center">{i}</div><div style="flex:1;font:500 15px Geist">{n}</div>{pill(*p, size=12)}</div>'
                   for i, n, p in [('YB', 'Yasmine Benali', ('Actif', 'active')), ('KH', 'Karim Haddad', ('Expire bientôt', 'expiring')), ('SM', 'Sofiane Mekki', ('Expiré', 'expired')), ('LA', 'Lina Amrani', ('En pause', 'paused')), ('RB', 'Rania Bouzid', ('Actif', 'active'))])
         + '</div></div></div>')
    return W, H, b
ARTBOARDS = {
    'membership-card-app-fr': a_app_card, 'membership-card-app-ar': a_app_card_ar, 'checkin-screen': a_checkin, 'membership-card-physical-front-back': a_card_physical,
    'receipt-thermal-80mm': a_receipt, 'poster-A3-scan-to-enter': a_poster, 'window-sticker-powered-by': a_sticker, 'partner-referral-card-front-back': a_partner,
    'instagram-post-1': lambda: ig_post(1), 'instagram-post-2': lambda: ig_post(2), 'instagram-story-1': lambda: ig_story(1), 'instagram-story-2': lambda: ig_story(2),
    'email-header-1200x400': a_email, 'whatsapp-profile-640': a_whatsapp, 'website-hero-1440x900': a_website,
}
