import mongomock
import pytest
from fastapi.testclient import TestClient

from ..app.database import DB_NAME, PATIENTS_COLLECTION, get_patients_collection
from ..app.main import app


@pytest.fixture(autouse=True)
def _mock_mongo_client(monkeypatch):
    client = mongomock.MongoClient()

    def fake_connect():
        import ..app.database as db

        db._client = client
        return client

    monkeypatch.setattr("..app.database.connect_client", fake_connect)
    yield
    import ..app.database as db

    db.disconnect_client()


@pytest.fixture
def mock_collection():
    client = mongomock.MongoClient()
    return client[DB_NAME][PATIENTS_COLLECTION]


@pytest.fixture
def client(mock_collection):
    def override_get_patients_collection():
        yield mock_collection

    app.dependency_overrides[get_patients_collection] = override_get_patients_collection
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
