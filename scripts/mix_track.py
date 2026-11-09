import json, subprocess, os, sys, urllib.request
plan_file, track, title, tail, fade = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
# Optional 6th arg: output name (default = track). Segments always come from tracks/{track}/.
name = sys.argv[6] if len(sys.argv) > 6 else track
plan = json.load(open(plan_file))
b = f'build/{track}'; os.makedirs(f'{b}/seg', exist_ok=True); os.makedirs(f'{b}/parts', exist_ok=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
total = 0.0; lst = open(f'{b}/list.txt','w')
for i, p in enumerate(plan):
    out = f'{b}/parts/{i:03d}.wav'
    if p['type'] == 'voice':
        seg = f"{b}/seg/{p['key']}.mp3"
        urllib.request.urlretrieve(f"https://from-the-end-audio.b-cdn.net/tracks/{track}/{p['key']}.mp3", seg)
        vol = 0.7 if p['module'] == 'drift' else 1.0
        # Trim ElevenLabs' leading/trailing silence; if the next item is voice too, leave a short breath gap.
        nxt = plan[i+1] if i + 1 < len(plan) else None
        gap = 0.6 if nxt and nxt['type'] == 'voice' else 0.2
        trim = 'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse'
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',seg,'-af',f'{trim},volume={vol},apad=pad_dur={gap}','-ar','44100','-ac','2','-c:a','pcm_s16le',out], check=True)
    else:
        subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-t',str(p['seconds']),'-c:a','pcm_s16le',out], check=True)
    total += dur(out); lst.write(f"file 'parts/{i:03d}.wav'\n")
lst.close()
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',f'{b}/list.txt','-af','loudnorm=I=-20:TP=-2:LRA=11','-ar','44100','-c:a','pcm_s16le',f'{b}/voice.wav'], check=True)
# 1) Voice only (no background): what the bot plays; the app mixes its own background later.
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{b}/voice.wav','-af','apad=pad_dur=3,pan=mono|c0=0.5*c0+0.5*c1',
  '-c:a','libmp3lame','-b:a','96k','-id3v2_version','3','-metadata',f'title={title}','-metadata','artist=From The End', f'{b}/{name}-voice.mp3'], check=True)
# 2) With generated ambient background.
length = total + tail
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{b}/voice.wav','-i','build/ambient.wav',
  '-filter_complex', f"[1]atrim=0:{length},volume=0.22,afade=t=out:st={length-fade}:d={fade}[amb];[0]apad=whole_dur={length}[v];[v][amb]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95,pan=mono|c0=0.5*c0+0.5*c1[out]",
  '-map','[out]','-c:a','libmp3lame','-b:a','96k','-id3v2_version','3','-metadata',f'title={title}','-metadata','artist=From The End', f'{b}/{name}.mp3'], check=True)
print(f'voice {total/60:.1f} min -> {b}/{name}-voice.mp3 | with ambient {length/60:.1f} min -> {b}/{name}.mp3')
