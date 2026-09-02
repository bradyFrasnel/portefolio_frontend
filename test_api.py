import urllib.request
import json
req = urllib.request.Request('https://portefolio-backend-v0e0.onrender.com/api/technologies/', method='POST', headers={'Content-Type': 'application/json'}, data=json.dumps({"nom": "TestTech"}).encode('utf-8'))
try:
    res = urllib.request.urlopen(req)
    print(res.read().decode())
except Exception as e:
    print(e)
    if hasattr(e, 'read'): print(e.read().decode())
