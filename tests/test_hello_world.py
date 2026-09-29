from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_returns_message():
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    # Ensure the response is a non‑empty JSON object with a 'message' field
    assert isinstance(json_data, dict) and json_data
    assert "message" in json_data
    assert json_data["message"] == "Hello, world!"
