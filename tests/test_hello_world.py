from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_run_pipeline_page_contains_alert():
    response = client.get("/run-pipeline")
    assert response.status_code == 200
    # Ensure the button and alert script are present
    assert "id=\"run-pipeline\"" in response.text
    assert "alert('welcome home')" in response.text
