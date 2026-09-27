from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_hello_vanakam():
    response = client.get("/hello_vanakam")
    assert response.status_code == 200
    assert response.json() == {"message": "Vanakam!"}
