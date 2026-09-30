from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.collection import Collection
from pymongo.errors import PyMongoError

from app.database import get_patients_collection
from app.schemas import PatientCreate, PatientRead

router = APIRouter(prefix="/patients", tags=["patients"])


def document_to_patient(doc: dict) -> PatientRead:
    return PatientRead(
        id=str(doc["_id"]),
        name=doc["name"],
        age=doc["age"],
        gender=doc["gender"],
        phone=doc["phone"],
        address=doc["address"],
        country=doc["country"],
        created_at=doc["created_at"],
    )

@router.post("", response_model=PatientRead, status_code=status.HTTP_201_CREATED)
def create_patient(
    payload: PatientCreate,
    collection: Collection = Depends(get_patients_collection),
):
    doc = {
        **payload.model_dump(),
        "created_at": datetime.now(timezone.utc),
    }
    try:
        result = collection.insert_one(doc)
        doc["_id"] = result.inserted_id
    except PyMongoError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        )
    return document_to_patient(doc)

@router.get("", response_model=list[PatientRead])
def list_patients(collection: Collection = Depends(get_patients_collection)):
    try:
        cursor = collection.find().sort("created_at", -1)
        return [document_to_patient(doc) for doc in cursor]
    except PyMongoError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable",
        )
