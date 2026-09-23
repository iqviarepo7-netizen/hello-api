import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_fallback():
    response = client.get("/hello_fallback")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("message") == "Hello, world!"
