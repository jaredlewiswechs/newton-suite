import sys
from pathlib import Path
# Add nina dir to path
sys.path.insert(0, str(Path.cwd() / 'nina'))
try:
    from nina.developer.forge import Pipeline
    print('Imported Pipeline OK')
except Exception as e:
    import traceback
    traceback.print_exc()
    print('Import failed')
