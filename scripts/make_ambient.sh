#!/bin/zsh
# Erzeugt 40 Min Ambient (Brown Noise + langsam atmender A/E/A-Drone) nach build/ambient.wav. Lizenzfrei, keine Credits.
mkdir -p build
ffmpeg -y -loglevel error \
 -f lavfi -i "anoisesrc=color=brown:amplitude=0.5:duration=2400:sample_rate=44100" \
 -f lavfi -i "aevalsrc='0.10*sin(2*PI*110*t)*(0.75+0.25*sin(2*PI*0.07*t))':d=2400:s=44100" \
 -f lavfi -i "aevalsrc='0.06*sin(2*PI*164.81*t)*(0.7+0.3*sin(2*PI*0.05*t+1))':d=2400:s=44100" \
 -f lavfi -i "aevalsrc='0.04*sin(2*PI*220.5*t)*(0.65+0.35*sin(2*PI*0.09*t+2))':d=2400:s=44100" \
 -filter_complex "[0]lowpass=f=400,volume=0.35[n];[n][1][2][3]amix=inputs=4:normalize=0,lowpass=f=1200,aecho=0.8:0.7:120|240:0.3|0.2,pan=stereo|c0=c0|c1=c0,afade=t=in:d=8[out]" \
 -map "[out]" -c:a pcm_s16le build/ambient.wav
