import requests, traceback
try:
    r = requests.post('http://localhost:8000/foghorn/query', json={'text':'What is the capital of Texas?'}, timeout=5)
    print('status', r.status_code)
    print(r.text)
except Exception as e:
    print('EXC:', type(e), e)
    traceback.print_exc()