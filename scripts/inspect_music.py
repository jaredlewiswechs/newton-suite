with open('realTinyTalk/examples/verified_music_app_reference.tt', 'r', encoding='utf-16') as f:
    lines = f.readlines()

for i in range(1, 201):
    s = lines[i-1] if i-1 < len(lines) else ''
    print(f"{i:4}: {repr(s)}")
