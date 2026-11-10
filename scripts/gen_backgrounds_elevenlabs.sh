#!/bin/zsh
# Generates the backgrounds from a JSON list via WF14 (ElevenLabs Music → Bunny → Airtable "Background Tracks").
# One at a time; waits until each file is on the CDN (with ?fresh= so Bunny doesn't cache the 404). Uses ElevenLabs credits.
# Usage: scripts/gen_backgrounds_elevenlabs.sh docs/tracks/backgrounds-v1.json
list=${1:?json list}
n=$(python3 -c "import json,sys;print(len(json.load(open(sys.argv[1]))))" "$list")
for i in $(seq 0 $((n-1))); do
  item=$(python3 -c "import json,sys;print(json.dumps(json.load(open(sys.argv[1]))[int(sys.argv[2])]))" "$list" $i)
  name=$(python3 -c "import json,sys;print(json.loads(sys.argv[1])['name'])" "$item")
  echo "→ $name"
  curl -s -X POST https://n8n.oceandiveloper.com/webhook/fte-backgrounds-generate -H 'Content-Type: application/json' -d "$item" >/dev/null
  ok=0
  for t in $(seq 1 50); do
    sleep 6
    c=$(curl -s -o /dev/null -w '%{http_code}' "https://from-the-end-audio.b-cdn.net/backgrounds/$name.mp3?fresh=$RANDOM$t")
    [ "$c" = 200 ] && { ok=1; break; }
  done
  [ $ok = 1 ] && echo "  ready: https://from-the-end-audio.b-cdn.net/backgrounds/$name.mp3" || { echo "  not on CDN after 5 min, check WF14 executions"; exit 1; }
done
