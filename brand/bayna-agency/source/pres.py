"""Editable 16:9 presentation template, built with the social template system (text blocks → PPTX)."""
import sys, json
sys.argv = [sys.argv[0], sys.argv[1]]
import social
from social import tpl, T, A, logo, big_mark, templates, jobs
from kit import *
from brand import *
templates.clear(); jobs.clear()
G = 'presentation'; W_, H_ = 1920, 1080
tpl(G, '01-cover', W_, H_, 'ink', A(big_mark(1400, ''), 'right:-300px;top:-160px') + A(logo('horizontal-compact', 'color-dark', 300), 'left:120px;top:100px') +
    T('Proposition commerciale', 120, 380, 'font-size:22px;color:var(--lime)', 'lbl', 900) +
    T('Titre de la<br>présentation.', 120, 430, 'font-size:120px', 'big', 1100) +
    T('Nom du client · Mois 2026', 120, 720, 'font-size:28px;color:rgba(255,255,255,.7)', 'sub', 900), 'Cover')
tpl(G, '02-agenda', W_, H_, 'paper', T('Sommaire', 120, 120, 'font-size:20px;color:var(--violet)', 'lbl', 600) + T('Au programme.', 120, 170, 'font-size:84px', 'big', 1200) +
    ''.join(T(f'0{i+1}', 120, 380 + i*120, 'font-size:26px;color:var(--violet);font-family:JetBrains Mono', 'sub', 80) + T(t, 230, 372 + i*120, 'font-size:48px;letter-spacing:-.015em', 'big', 1300)
            for i, t in enumerate(['Le contexte', 'Notre lecture', 'La stratégie', 'Le plan d’action', 'Budget & planning'])) +
    A(logo('horizontal-compact', 'color', 200), 'right:120px;top:120px'), 'Agenda')
tpl(G, '03-section', W_, H_, 'grad', T('01', 120, 330, 'font-size:40px;color:var(--lime);font-family:JetBrains Mono', 'sub', 200) +
    T('Titre de<br>section.', 120, 400, 'font-size:150px', 'big', 1200) + A(mark_svg(body='#fff', height=120), 'right:120px;bottom:100px'), 'Section')
tpl(G, '04-content', W_, H_, 'paper', A(logo('horizontal-compact', 'color', 200), 'right:120px;top:80px') +
    T('Sous-titre', 120, 220, 'font-size:20px;color:var(--violet)', 'lbl', 600) + T('Titre de la diapositive.', 120, 270, 'font-size:80px', 'big', 1300) +
    T('Zone de texte. Une idée par diapositive, des phrases courtes, un chiffre clé en lime sur fond sombre si nécessaire.', 120, 420, 'font-size:30px;color:#4a4a55;line-height:1.6', 'sub', 950) +
    A('', 'right:-1px;bottom:-1px;width:360px;height:360px;background:var(--grad);border-top-left-radius:360px') + A('', 'right:120px;bottom:120px;width:110px;height:110px;background:radial-gradient(circle at 60% 50%,var(--ink) 0 27%,var(--lime) 28%);border-radius:50%'), 'Content')
tpl(G, '05-key-figure', W_, H_, 'ink', T('Chiffre clé', 120, 200, 'font-size:22px;color:var(--lime)', 'lbl', 600) +
    T('+00%', 110, 260, 'font-size:380px;color:var(--lime);letter-spacing:-.05em', 'big', 1500) +
    T('Ce que ce chiffre prouve, en une phrase.', 120, 720, 'font-size:60px;letter-spacing:-.02em', 'big', 1300) + A(mark_svg(height=110), 'right:120px;bottom:100px'), 'Key figure')
tpl(G, '06-three-columns', W_, H_, 'paper', T('Notre approche', 120, 120, 'font-size:20px;color:var(--violet)', 'lbl', 600) + T('Trois étapes, un résultat.', 120, 170, 'font-size:80px', 'big', 1500) +
    ''.join(A('', f'left:{120 + i*580}px;top:400px;width:540px;height:520px;background:#fff;border-radius:32px') +
            A('', f'left:{170 + i*580}px;top:450px;width:90px;height:90px;background:{["var(--violet)","var(--violet)","var(--lime)"][i]};border-radius:50%') +
            T(t, 170 + i*580, 590, 'font-size:44px', 'big', 440) + T('Décrivez cette étape en deux ou trois lignes.', 170 + i*580, 670, 'font-size:26px;color:#4a4a55;line-height:1.55', 'sub', 440)
            for i, t in enumerate(['Comprendre', 'Créer', 'Prouver'])), 'Three columns')
tpl(G, '07-thank-you', W_, H_, 'grad', T('Merci.', 120, 330, 'font-size:200px', 'big', 1000) + T('شكراً', 120, 560, 'font-size:120px;color:var(--lime);text-align:left', 'ar', 800) +
    T(f'{NAME} · {MAIL} · {PHONE}', 120, 820, 'font-size:28px;color:rgba(255,255,255,.85)', 'sub', 1400) + A(logo('horizontal-compact', 'on-violet', 280), 'right:120px;top:100px'), 'Thank you')
json.dump(templates, open('templates_pres.json', 'w')); json.dump(jobs, open('jobs_pres.json', 'w')); print(len(templates))
