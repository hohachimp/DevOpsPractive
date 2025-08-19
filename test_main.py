from fastapi.testclient import TestClient
from main import app

def test_health():
    client = TestClient(app)
    r = client.get("/health-check")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"
