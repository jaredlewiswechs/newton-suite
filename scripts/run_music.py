import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from realTinyTalk import run

s = open('realTinyTalk/examples/verified_music_app_reference.tt','r',encoding='utf-16').read()
try:
    res = run(s)
    print('run returned:', res)
except Exception as e:
    import traceback
    traceback.print_exc()
