from datetime import datetime
from pydantic import BaseModel


class PatientCreate(BaseModel):
  name: str
  age: int
  gender: str
  phone: str
  address: str
  country: str

  class Config:
    schema_extra = {
      "example": {
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "phone": "1234567890",
        "address": "123 Main St",
        "country": "India",
      }
    }


class PatientRead(BaseModel):
  id: str
  name: str
  age: int
  gender: str
  phone: str
  address: str
  country: str
  created_at: datetime

  class Config:
    schema_extra = {
      "example": {
        "id": "1234567890",
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "phone": "1234567890",
        "address": "123 Main St",
        "country": "India",
        "created_at": "2022-01-01T00:00:00+00:00",
      }
    }
