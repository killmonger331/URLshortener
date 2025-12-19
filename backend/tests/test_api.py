from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["ok"] is True


def test_shorten_and_redirect():
    res = client.post("/shorten", json={"url": "https://example.com"})
    assert res.status_code == 200
    data = res.json()
    assert "code" in data
    assert "short_url" in data

    code = data["code"]
    r2 = client.get(f"/{code}", allow_redirects=False)
    assert r2.status_code in (301, 302, 307, 308)
    assert r2.headers["location"] == "https://example.com"
