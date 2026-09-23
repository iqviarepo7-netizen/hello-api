from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_fallback():
    response = client.get("/hello_fallback")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

def test_hello_vanakam():
    response = client.get("/hello_vanakam_enaku_saaaavee_illai")
    assert response.status_code == 200
    assert response.json() == {"message": "Vanakam, enaku saaavee illai"}
