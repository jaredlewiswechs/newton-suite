import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from realTinyTalk.lexer import Lexer, TokenType

s = open('realTinyTalk/examples/verified_music_app_reference.tt', 'r', encoding='utf-16').read()
lex = Lexer(s)
tokens = lex.tokenize()

# Print tokens around line 120-130
for t in tokens:
    if 115 <= t.line <= 130:
        print(f"{t.line:3} {t.column:2} {t.type.name:20} {repr(t.value)[:60]}")

# Print last few tokens
print('\nLast tokens:')
for t in tokens[-20:]:
    print(f"{t.line:3} {t.column:2} {t.type.name:20} {repr(t.value)[:60]}")
