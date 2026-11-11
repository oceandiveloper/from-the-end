#!/bin/bash
# Runs at session start, only in Claude Code cloud sessions (CLAUDE_CODE_REMOTE=true).
# Installs what the track production needs. Locally it does nothing.
[ "$CLAUDE_CODE_REMOTE" = "true" ] || exit 0
if ! command -v ffmpeg >/dev/null 2>&1; then
  (sudo -n true 2>/dev/null && SUDO=sudo) || SUDO=
  $SUDO apt-get update -qq >/dev/null 2>&1 && $SUDO apt-get install -y -qq ffmpeg >/dev/null 2>&1 \
    && echo "cloud-setup: ffmpeg installed" || echo "cloud-setup: ffmpeg install FAILED (check network access)"
fi
# Ambient bed for the mixer (generated, no credits)
if [ ! -f build/ambient.wav ] && command -v ffmpeg >/dev/null 2>&1; then
  bash scripts/make_ambient.sh && echo "cloud-setup: build/ambient.wav created"
fi
for v in N8N_MCP_TOKEN AIRTABLE_PAT; do
  [ -n "${!v}" ] || echo "cloud-setup: $v is not set in the cloud environment, MCP server will fail"
done
exit 0
