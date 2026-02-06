import io
import sys
from pathlib import Path

from realTinyTalk import run


def test_verified_music_demo_runs():
    path = Path(__file__).parent.parent / 'examples' / 'verified_music_app_reference.tt'
    assert path.exists(), "Example file missing"

    s = path.read_text(encoding='utf-16')

    buf = io.StringIO()
    old = sys.stdout
    try:
        sys.stdout = buf
        run(s)
    finally:
        sys.stdout = old

    out = buf.getvalue()
    assert 'curve target @ 0.5: 0.72' in out
    assert 'karaoke frame:' in out
    assert 'tracks loaded: 4' in out
