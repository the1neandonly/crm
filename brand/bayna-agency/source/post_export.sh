#!/bin/bash
# JPG / EPS / WEBP / ICO derivatives after render.js
set -e
OUT=$1; JOBS=$2
cd $OUT
python3 - "$JOBS" <<'PY'
import json,subprocess,os,sys
for j in json.load(open(sys.argv[1])):
    if 'jpg' in j:
        os.makedirs(os.path.dirname(j['jpg']),exist_ok=True)
        subprocess.run(['convert',j['out'],'-background','white','-flatten','-quality','95','-sampling-factor','4:4:4','-density','300','-units','PixelsPerInch',j['jpg']],check=True)
PY
rm -rf logo/_tmp; mkdir -p logo/eps logo/webp
for f in logo/pdf/*.pdf; do pdftocairo -eps "$f" "logo/eps/$(basename "${f%.pdf}").eps"; done
for f in logo/png/*/*-2000px.png logo/png/symbol/*-2048px.png; do b=$(basename "$f"); convert "$f" -quality 92 "logo/webp/${b%-*px.png}.webp"; done
convert icons/png/favicon-master-{16,32,48,64}.png icons/favicon.ico
cd icons/png && mv favicon-master-180.png apple-touch-icon-180.png && mv favicon-master-192.png android-chrome-192.png && mv favicon-master-512.png android-chrome-512.png && for s in 16 32 48 64; do mv favicon-master-$s.png favicon-$s.png; done
