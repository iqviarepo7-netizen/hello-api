from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_run_pipeline_popup():
    """Clicking the Run Pipeline button should return the welcome home popup."""
    response = client.post("/run-pipeline")
    assert response.status_code == 200
    json_data = response.json()
    assert "popup" in json_data
    assert json_data["popup"] == "welcome home"
