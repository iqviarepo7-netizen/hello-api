from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PatientBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    age: int = Field(..., ge=1, le=150)
    gender: str = Field(..., pattern="^(Male|Female|Other)$")
    phone: str = Field(..., min_length=1, max_length=50)
    address: str = Field(..., min_length=1, max_length=500)
    country: str = Field(..., pattern="^(India|Vietnam|Japan|China|London)$")


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: str
    created_at: datetime
