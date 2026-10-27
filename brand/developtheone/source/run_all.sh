set -e
cd /tmp/claude-0/-home-user-crm/9822160d-7d4c-5a0c-b763-6d89aa660c2f/scratchpad/gen_dto
python3 social.py /home/user/crm/brand/developtheone && node render_html.js jobs_social.json
python3 banners.py /home/user/crm/brand/developtheone && node render_html.js jobs_banners.json
python3 printkit.py /home/user/crm/brand/developtheone && node render_html.js jobs_print.json
python3 digital.py /home/user/crm/brand/developtheone && node render_html.js jobs_digital.json
python3 pres.py /home/user/crm/brand/developtheone && node render_html.js jobs_pres.json
python3 palette.py /home/user/crm/brand/developtheone && node render_html.js jobs_colors.json
echo ALLDONE
