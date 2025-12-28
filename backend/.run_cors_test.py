import os
import importlib
import sys
from fastapi.testclient import TestClient

os.environ['ALLOWED_ORIGIN_REGEX'] = r'https://ur-lshortener-.*\.vercel\.app$'
import app.main as main_mod
importlib.reload(main_mod)
app = main_mod.app
client = TestClient(app)

origin = 'https://ur-lshortener-nr25t5yo5-richards-projects-c0a9c9b4.vercel.app'
res = client.options('/shorten', headers={'Origin': origin, 'Access-Control-Request-Method': 'POST'})
print('status', res.status_code)
print('ACAO', res.headers.get('access-control-allow-origin'))
if res.status_code in (200,204) and res.headers.get('access-control-allow-origin') == origin:
    print('OK')
    sys.exit(0)
else:
    print('FAIL')
    sys.exit(2)
