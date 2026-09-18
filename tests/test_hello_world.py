from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

# New test for the /hello_hi endpoint
def test_hello_hi():
    response = client.get("/hello_hi")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, hi!"}
