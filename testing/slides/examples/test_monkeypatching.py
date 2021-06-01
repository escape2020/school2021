import requests
import json

def is_server_healthy():
    ret = requests.get('https://example.org/healthcheck')
    ret.raise_for_status()
    return ret.json()['healthy']

def test_healthy(monkeypatch):
    with monkeypatch.context() as m:
        def get(url):
            resp = requests.Response()
            resp.url = url
            resp.status_code = 200
            resp._content = json.dumps({'healthy': True}).encode('utf-8')
            return resp

        m.setattr(requests, 'get', get)
        assert is_server_healthy()
