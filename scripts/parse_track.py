import re, json, sys
src = open(sys.argv[1], encoding='utf-8').read()
out = sys.argv[2]
plan = []; cur = None; buf = []; n = 0
def flush():
    global buf, n
    t = ' '.join(x.strip() for x in buf if x.strip()).strip()
    if t and cur:
        n += 1
        plan.append({'type': 'voice', 'module': cur, 'key': f'{cur}-{n:02d}', 'text': t})
    buf = []
for line in src.splitlines():
    m = re.match(r'^## \d+\.\s+(.+)$', line)
    if m:
        flush(); n = 0
        name = re.sub(r'\(.*?\)', '', m.group(1)).split(':')[0]
        cur = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-'); continue
    if line.startswith('#') or line.startswith('---') or line.startswith('|'):
        flush()
        if line.startswith('## '): cur = None
        continue
    if cur is None: continue
    p = re.match(r'^\[pause (\d+)s\]', line.strip())
    if p:
        flush(); plan.append({'type': 'pause', 'module': cur, 'seconds': int(p.group(1))}); continue
    if line.strip().startswith('*('): continue
    if line.strip(): buf.append(line)
    else: flush()
flush()
voices = [p for p in plan if p['type']=='voice']
for i, v in enumerate(voices):
    v['previousText'] = voices[i-1]['text'] if i>0 and voices[i-1]['module']==v['module'] else ''
    v['nextText'] = voices[i+1]['text'] if i+1<len(voices) and voices[i+1]['module']==v['module'] else ''
json.dump(plan, open(out,'w'), indent=1, ensure_ascii=False)
print(len(voices), 'voice segments,', sum(len(v['text']) for v in voices), 'chars,', sum(p['seconds'] for p in plan if p['type']=='pause'), 's pauses; modules:', sorted({v['module'] for v in voices}))
