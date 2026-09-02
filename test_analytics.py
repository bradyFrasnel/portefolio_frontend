import urllib.request
import json
import uuid
data = {
    "visitor_id": str(uuid.uuid4()),
    "event_type": "home",
    "browser": "Chrome",
    "device_type": "desktop"
}
req = urllib.request.Request('https://portefolio-backend-v0e0.onrender.com/api/analytics/', method='POST', headers={'Content-Type': 'application/json'}, data=json.dumps(data).encode('utf-8'))
try:
    res = urllib.request.urlopen(req)
    print("SUCCESS", res.read().decode())
except Exception as e:
    print(e)
    if hasattr(e, 'read'): print(e.read().decode())
