from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_run_pipeline_endpoint():
    response = client.get("/run-pipeline")
    assert response.status_code == 200
    assert response.json() == {"message": "welcome home"}


def test_root_contains_button():
    response = client.get("/")
    assert response.status_code == 200
    assert 'id="run-pipeline-btn"' in response.text
