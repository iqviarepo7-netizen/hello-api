import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_run_pipeline_returns_welcome_message():
    response = client.get("/run-pipeline")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome home"}
