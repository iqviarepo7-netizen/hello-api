from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_successful_login_user1():
    response = client.post("/login", json={"email": "user1@test.com", "password": "Test@123"})
    assert response.status_code == 200
    assert response.json()["detail"] == "Login successful"


def test_successful_login_user2():
    response = client.post("/login", json={"email": "user2@test.com", "password": "Test@123"})
    assert response.status_code == 200
    assert response.json()["detail"] == "Login successful"


def test_invalid_login():
    response = client.post("/login", json={"email": "user1@test.com", "password": "wrong"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
