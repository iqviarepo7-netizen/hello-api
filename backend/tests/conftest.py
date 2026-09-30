import mongomock
import pytest
from fastapi.testclient import TestClient

from app.database import DB_NAME, PATIENTS_COLLECTION, get_patients_collection
from app.main import app


@pytest.fixture
def client():
    mock_client = mongomock.MongoClient()
    db = mock_client[DB_NAME]

    def override_get_patients_collection():
        yield db[PATIENTS_COLLECTION]

    app.dependency_overrides[get_patients_collection] = override_get_patients_collection
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()
