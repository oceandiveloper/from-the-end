"""Generate a background loop locally with Meta MusicGen (free, no credits).

Usage:
  .venv-audio/bin/python scripts/gen_background.py <name> "<prompt>" [--seed 1] [--seconds 30] [--model facebook/musicgen-medium]

Writes build/backgrounds/<name>.wav (raw) and build/backgrounds/<name>-loop.mp3 (seamless loop, the player repeats it).

LICENCE: MusicGen weights are CC-BY-NC 4.0 (non-commercial). Every loop made with this script is
"Private only" in Airtable "Background Tracks": Kevin's own listening, never the public app or YouTube.
"""
import argparse, os, subprocess
import numpy as np
import torch
from scipy.io import wavfile
from transformers import AutoProcessor, MusicgenForConditionalGeneration

p = argparse.ArgumentParser()
p.add_argument('name'); p.add_argument('prompt')
p.add_argument('--seed', type=int, default=1)
p.add_argument('--seconds', type=float, default=30)
p.add_argument('--fade', type=float, default=4, help='crossfade seconds at the loop seam')
p.add_argument('--model', default='facebook/musicgen-medium')
a = p.parse_args()

out = 'build/backgrounds'; os.makedirs(out, exist_ok=True)
torch.manual_seed(a.seed)
dev = 'mps' if torch.backends.mps.is_available() else 'cpu'
proc = AutoProcessor.from_pretrained(a.model)
model = MusicgenForConditionalGeneration.from_pretrained(a.model)
try:
    model = model.to(dev)
except Exception:
    dev = 'cpu'
inputs = proc(text=[a.prompt], padding=True, return_tensors='pt').to(dev)
tokens = int(a.seconds * model.config.audio_encoder.frame_rate)
with torch.no_grad():
    audio = model.generate(**inputs, do_sample=True, guidance_scale=3, max_new_tokens=tokens)
sr = model.config.audio_encoder.sampling_rate
x = audio[0, 0].float().cpu().numpy()
x = x / max(1e-6, np.abs(x).max()) * 0.9
wavfile.write(f'{out}/{a.name}.wav', sr, (x * 32767).astype(np.int16))

# Seamless loop: drop the first `fade` seconds, then blend the last `fade` seconds into the
# (dropped) beginning with an equal-power crossfade. The loop ends exactly where it starts.
n = int(a.fade * sr)
loop = x[n:].copy()
t = np.linspace(0, np.pi / 2, n)
loop[-n:] = loop[-n:] * np.cos(t) + x[:n] * np.sin(t)
tmp = f'{out}/{a.name}-loop.wav'
wavfile.write(tmp, sr, (loop * 32767).astype(np.int16))
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', tmp,
                '-ar', '44100', '-ac', '2', '-b:a', '128k',
                f'{out}/{a.name}-loop.mp3'], check=True)
os.remove(tmp)
print(f'{a.name}: {len(loop)/sr:.1f}s loop on {dev} -> {out}/{a.name}-loop.mp3')
