try:
    from nina.developer.forge import Pipeline
    print('Imported Pipeline OK')
except Exception as e:
    import traceback
    traceback.print_exc()
    print('Import failed')
