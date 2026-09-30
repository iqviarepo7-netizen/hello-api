from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional


class PatientBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=1, le=150)
    gender: str = Field(...)
    phone: str = Field(..., min_length=1, max_length=20)
    address: str = Field(..., min_length=1, max_length=500)
    country: str = Field(...)

    @field_validator('gender')
    def gender_must_be_valid(cls, v):
        allowed = {'Male', 'Female', 'Other'}
        if v not in allowed:
            raise ValueError(f'Gender must be one of {allowed}')
        return v

    @field_validator('country')
    def country_must_be_valid(cls, v):
        allowed = {'India', 'Vietnam', 'Japan', 'China', 'London'}
        if v not in allowed:
            raise ValueError(f'Country must be one of {allowed}')
        return v


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
