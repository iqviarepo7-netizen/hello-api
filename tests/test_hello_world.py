from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_world_endpoint():
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}
