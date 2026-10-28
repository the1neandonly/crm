from gl2_base import *
TOC = []   # (part, en, fr, page_index)
def toc(part, en, fr): TOC.append((part, en, fr, len(PAGES)))
def divider(num, en, fr, sub, cls='gradp'):
    add('', f'''<div style="position:absolute;left:120px;top:150px" class="mono hl">{num}</div>
<div style="position:absolute;left:120px;bottom:150px"><div class="big" style="font-size:160px;line-height:.92">{fr if LANG == "fr" else en}</div>
<div class="big" style="font-size:52px;margin-top:26px;opacity:.85;font-weight:600">{en if LANG == "fr" else fr}</div><p style="margin-top:30px;max-width:900px;font-size:24px">{sub}</p></div>
{mark_svg(body="rgba(255,255,255,.1)", slice_c=LIME, height=1300, style="position:absolute;right:-300px;top:-160px")}''', cls, chrome=False)

def build_brand():
    # Cover
    add('', f'''{mark_svg(height=1500, style="position:absolute;right:-260px;top:-150px")}
<div style="position:absolute;left:120px;top:110px">{logo_svg("bilingual","color-dark",width=480)}</div>
<div style="position:absolute;left:120px;bottom:130px">
<div class="big" style="font-size:168px;line-height:.9;letter-spacing:-.04em">Brand<br>Guidelines</div>
<div class="big hl" style="font-weight:600;font-size:44px;margin-top:30px">Charte graphique · الهوية البصرية</div>
<div style="margin-top:46px;font-size:18px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:rgba(255,255,255,.55)">Version 2.0 &nbsp;·&nbsp; Octobre 2026 &nbsp;·&nbsp; Oran, Algérie</div></div>''', 'dark', chrome=False)
    PAGES.append(None)   # contents placeholder (index 1)

    toc('Brand', 'Brand story', 'L’histoire de la marque')
    divider('01', 'The brand.', 'La marque.', 'Who we are, why we exist, where we are going — and how we sound when we speak.')
    # The name
    add('01 The name', f'''{head("01.1", "The name.", "Le nom")}
<div class="row" style="margin-top:40px;gap:100px;align-items:flex-start">
<div style="width:760px"><div class="ar" style="font-weight:700;font-size:300px;line-height:1.15;text-align:left;background:var(--grad);-webkit-background-clip:text;color:transparent;filter:brightness(1.3)">{NAME_AR}</div>
<div class="big" style="font-size:40px;font-weight:600;margin-top:6px">bayna <span class="muted" style="font-family:Manrope;font-weight:500;font-size:24px">/ˈbaj.na/ — Algerian Darija, adjective</span></div>
<p style="margin-top:18px;font-size:24px"><b style="color:#fff">Clear. Obvious. Evident.</b> When something cannot be denied, in Oran we don’t make a speech — we say one word: <span class="ar hl">باينة</span>.</p></div>
<div style="flex:1;padding-top:40px">
<div class="card" style="padding:40px 46px"><div class="lbl hl">In real life · Dans la vraie vie</div>
<div style="font-size:30px;line-height:1.5;margin-top:22px;color:#fff">— Elle va marcher, cette campagne ?<br>— <span class="ar hl" style="font-weight:700">باينة !</span> <span class="muted" style="font-size:22px">(Évidemment.)</span></div></div>
<p style="margin-top:40px;font-size:22px">We chose a word from the street, not from a dictionary — because a brand should speak the language of the people it serves. Our name is our promise: <b style="color:#fff">after Bayna, your value is obvious.</b></p>
<div class="row" style="margin-top:36px;gap:16px">{"".join(f'<span style="border:2px solid rgba(255,255,255,.25);border-radius:999px;padding:10px 22px;font-weight:700;font-size:17px">{w}</span>' for w in ["Clair","Évident","Visible","Prouvé","واضح"])}</div>
</div></div>''', 'dark')
    # Story
    add('01 Our story', f'''{head("01.2", "Our story.", "Notre histoire")}
<div class="row" style="margin-top:50px;gap:110px">
<div style="flex:1.2"><p style="font-size:27px;line-height:1.6;color:#2a2a33">Bayna was born in Oran from a simple observation: <b>Algeria is full of great products and talented entrepreneurs — but too many of them stay invisible.</b></p>
<p style="font-size:23px;margin-top:26px">Messages are unclear. Visuals change from one post to the next. Marketing budgets are spent without anyone knowing what they bring back. Good businesses lose to louder ones.</p>
<p style="font-size:23px;margin-top:26px">We created Bayna to close that gap: one agency that brings together <b>strategy, design and data</b>, so that every brand we work with becomes obvious — to see, to understand, and to choose.</p></div>
<div style="flex:1"><div class="card" style="padding:56px;background:var(--ink);color:#fff;height:100%">
<div class="lbl hl">Our ambition · Notre ambition</div>
<div class="big" style="font-size:64px;line-height:1.05;margin-top:30px">That when people see our clients’ work, they say just one word.</div>
<div class="ar" style="font-size:120px;font-weight:700;color:var(--lime);text-align:left;margin-top:40px">باينة.</div></div></div></div>''', 'light')
    # Why
    whys = [('01', 'Being good isn’t enough.', 'It has to be seen. Visibility is the first job of any brand — before it can convince, it must be noticed.'),
            ('02', 'Clarity sells.', 'A clear brand is remembered, trusted and chosen. Confusion is the most expensive mistake in marketing.'),
            ('03', 'Marketing must prove itself.', 'Every dinar invested should show its result. We measure, we report, we improve — every month.')]
    add('01 Why Bayna', f'''{head("01.3", "Why we exist.", "Pourquoi Bayna")}
<div class="row" style="margin-top:80px;gap:40px">{"".join(f'<div style="flex:1;border-top:3px solid var(--lime);padding-top:34px"><div class="mono hl" style="font-size:22px">{n}</div><div class="big" style="font-size:52px;margin:22px 0 22px;line-height:1.05">{t}</div><p style="font-size:21px">{d}</p></div>' for n,t,d in whys)}</div>''', 'dark')
    # Mission / vision
    add('01 Mission & vision', f'''{head("01.4", "Mission & vision.", "Mission & vision")}
<div class="row" style="margin-top:60px;gap:30px">
<div class="card" style="flex:1;padding:56px;height:600px"><div class="lbl vi">Mission · Ce que nous faisons</div>
<div class="big" style="font-size:66px;line-height:1.05;margin-top:36px">Make every brand we touch <span class="vi">clear</span>, consistent and measurable.</div>
<p style="position:absolute;left:56px;right:56px;bottom:50px;font-size:20px">Today, every day, for every client — from the corner café to the national brand.</p></div>
<div class="card" style="flex:1;padding:56px;height:600px;background:var(--grad);color:#fff"><div class="lbl hl">Vision · Où nous allons</div>
<div class="big" style="font-size:58px;line-height:1.07;margin-top:36px">Become the reference creative &amp; marketing agency of western Algeria — known for work that is both beautiful and proven.</div>
<p style="position:absolute;left:56px;right:56px;bottom:50px;font-size:20px;color:rgba(255,255,255,.85)">And carry Oran’s creativity beyond our borders.</p></div></div>''', 'light')
    # Goals
    goals = [('strategy', 'Clarity', 'Give every client a clear brand platform: positioning, message and identity.'),
             ('social', 'Visibility', 'Grow our clients’ audience on social media, on search — and in the street.'),
             ('analytics', 'Proof', 'Report results every month, in plain language and real numbers.'),
             ('star', 'Local excellence', 'International-level craft for Algerian brands, in their own language.'),
             ('team', 'Partnership', 'Grow with our clients over years, not just deliver one-off projects.'),
             ('idea', 'Talent', 'Train and grow a new generation of creatives from Oran.')]
    add('01 Goals', f'''{head("01.5", "Our goals.", "Nos objectifs")}
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-top:56px">{"".join(f'<div class="card" style="padding:36px 40px;height:300px">{icon_svg(ic, VIOLET, LIME, 64)}<div class="row" style="align-items:baseline;gap:14px;margin-top:26px"><span class="num">0{i+1}</span><h3 style="font-size:34px;margin:0">{t}</h3></div><p style="font-size:19px;margin-top:10px">{d}</p></div>' for i,(ic,t,d) in enumerate(goals))}</div>''', 'light')
    # Values
    vals = [('Clarity', 'Clarté · الوضوح', 'We make complex things simple and visible.'), ('Proof', 'Preuve · الدليل', 'Every idea is measured. Results speak.'),
            ('Boldness', 'Audace · الجرأة', 'Bright ideas, confident execution.'), ('Craft', 'Exigence · الإتقان', 'High-end detail in everything we ship.'),
            ('Proximity', 'Proximité · القرب', 'We speak our clients’ language — French, Darija, Arabic, English.')]
    add('01 Values', f'''{head("01.6", "Our values.", "Nos valeurs")}
<div class="row" style="margin-top:70px;gap:26px">{"".join(f'<div style="flex:1;background:#2E2E37;border-radius:28px;padding:40px 34px;height:520px;position:relative"><div style="width:70px;height:70px;background:{LIME if i==0 else VIOLET};border-radius:50%"></div><div class="big" style="font-size:42px;margin-top:40px">{en}</div><div class="lbl muted" style="margin-top:14px;letter-spacing:.1em;text-transform:none;font-size:17px">{fr}</div><p style="position:absolute;left:34px;right:34px;bottom:40px;font-size:20px">{d}</p></div>' for i,(en,fr,d) in enumerate(vals))}</div>''', 'dark')
    # Personality
    pers = [('Clear', 'cold'), ('Bold', 'loud'), ('Expert', 'arrogant'), ('Local', 'small'), ('Warm', 'casual'), ('Playful', 'childish')]
    add('01 Personality', f'''{head("01.7", "Personality.", "Personnalité")}
<p style="max-width:1100px;margin-top:22px">If Bayna were a person, it would be the friend who tells you the truth about your business — kindly, simply, and with a smile.</p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:56px">{"".join(f'<div class="card" style="padding:40px 44px;height:200px;display:flex;align-items:center;justify-content:space-between"><div><div class="big" style="font-size:54px">{a}</div><div class="muted" style="font-size:22px;margin-top:8px">but never <s>{b}</s></div></div><span class="ok">✓</span></div>' for a,b in pers)}</div>''', 'light')
    # Voice
    dodont = [('Français', '« On rend votre marque évidente. »', '« Nous proposons des solutions marketing innovantes à forte valeur ajoutée. »'),
              ('Darija', '« خلي ماركتك باينة »', 'Mixing three scripts in one line, or slang that excludes.'),
              ('English', '“Make it clear.”', '“Leveraging cross-channel synergies to drive engagement.”')]
    add('01 Voice & tone', f'''{head("01.8", "Voice & tone.", "Ton & langage")}
<div class="row" style="margin-top:46px;gap:60px">
<div style="width:560px">{"".join(f'<div style="padding:22px 0;border-top:1px solid rgba(255,255,255,.14)"><h3 style="font-size:28px">{t}</h3><p style="font-size:18px;margin:0">{d}</p></div>' for t,d in [("Say it simply.","Short sentences. Active verbs. One idea per message."),("Speak like Oran.","Warm, direct, with a touch of humour."),("Prove, don’t promise.","Numbers and examples over adjectives."),("Choose the right language.","French for business · Darija for community · Arabic for institutions · English for the signature.")])}</div>
<div style="flex:1">{"".join(f'<div class="row" style="gap:20px;margin-bottom:22px"><div class="lbl hl" style="width:120px;padding-top:30px">{l}</div><div style="flex:1;background:#2E2E37;border-radius:22px;padding:22px 28px"><div class="row" style="gap:14px;align-items:center"><span class="ok">✓</span><span style="font-size:24px;font-weight:600;{"font-family:Readex Pro;" if l=="Darija" else ""}">{d}</span></div><div class="row" style="gap:14px;align-items:center;margin-top:14px"><span class="no">×</span><span style="font-size:18px;color:rgba(255,255,255,.55)">{n}</span></div></div></div>' for l,d,n in dodont)}</div></div>''', 'dark')
    # Audience & services
    aud = ['SMEs & retailers in Oran and western Algeria', 'Startups & entrepreneurs', 'Restaurants, cafés & hospitality', 'Fashion, beauty & health', 'Real estate & industry', 'Institutions, schools & events']
    add('01 Audience & services', f'''{head("01.9", "Who we serve.", "Nos clients & nos services")}
<div class="row" style="margin-top:50px;gap:60px">
<div style="width:640px"><div class="lbl vi" style="margin-bottom:14px">Audience</div>{"".join(f'<div style="display:flex;gap:18px;align-items:center;padding:18px 0;border-top:1px solid var(--line);font-size:22px;font-weight:600"><span style="width:18px;height:18px;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%;flex:none"></span>{a}</div>' for a in aud)}</div>
<div style="flex:1"><div class="lbl vi" style="margin-bottom:14px">Services</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">{"".join(f'<div class="card" style="padding:24px 28px;display:flex;gap:20px;align-items:center">{icon_svg(ic, VIOLET, LIME, 52)}<div><div style="font-weight:800;font-size:20px">{fr}</div><div class="muted" style="font-size:15px">{en}</div></div></div>' for ic,en,fr in SERVICES)}</div></div></div>''', 'light')
    # Tagline system
    add('01 Tagline', f'''{head("01.10", "One promise, three languages.", "Signature")}
<div class="col" style="margin-top:60px;gap:22px">
{"".join(f'<div style="display:flex;align-items:center;gap:40px;background:{bg};border-radius:28px;padding:36px 50px;color:{c}"><span class="lbl" style="width:140px;opacity:.7">{l}</span><span class="{cl}" style="font-size:76px;font-weight:700;{st}">{t}</span><span style="margin-left:auto;font-size:18px;opacity:.7;max-width:420px;text-align:right">{u}</span></div>' for l,t,u,bg,c,cl,st in [("English","Make it clear.","Primary signature — logo lockups, campaigns, international.","var(--ink)","#fff","big",""),("Français","L’évidence, par le design.","Business documents, proposals, press.","#fff","var(--ink)","big","font-size:64px"),("Darija","خليها باينة","Social media, community, street campaigns.","var(--lime)","var(--ink)","ar","")])}
</div><p style="margin-top:30px">Hashtags: <b>#باينة</b> · <b>#MakeItClear</b> · <b>#BaynaAgency</b></p>''', 'light')
