import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
try:
    import core.cdl as cdl
    print('Imported core.cdl OK')
except Exception as e:
    import traceback
    traceback.print_exc()
    print('Import failed')
