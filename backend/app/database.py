import logging
import os
from typing import Generator

from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = "hospital_mvp"
PATIENTS_COLLECTION = "patients"
USE_MONGOMOCK = os.getenv("USE_MONGOMOCK", "").lower() in ("1", "true", "yes")

_client: MongoClient | None = None
_using_mongomock = False


def _create_mongomock_client() -> MongoClient:
    import mongomock

    global _using_mongomock
    _using_mongomock = True
    logger.warning(
        "Using in-memory MongoDB (mongomock). Data will not persist. "
        "Start MongoDB or unset USE_MONGOMOCK for a real database."
    )
    return mongomock.MongoClient()


def connect_client() -> MongoClient:
    global _client, _using_mongomock
    if USE_MONGOMOCK:
        _client = _create_mongomock_client()
        return _client

    _client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=2000)
    try:
        _client.admin.command("ping")
        _using_mongomock = False
    except PyMongoError:
        _client.close()
        _client = _create_mongomock_client()
    return _client


def disconnect_client() -> None:
    global _client, _using_mongomock
    if _client is not None:
        _client.close()
        _client = None
    _using_mongomock = False


def get_client() -> MongoClient:
    if _client is None:
        raise RuntimeError("MongoDB client is not connected")
    return _client


def get_database(client: MongoClient | None = None) -> Database:
    c = client if client is not None else get_client()
    return c[DB_NAME]


def get_patients_collection() -> Generator[Collection, None, None]:
    yield get_database()[PATIENTS_COLLECTION]
