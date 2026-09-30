import re
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Gender = Literal["Male", "Female", "Other"]

PHONE_PATTERN = re.compile(r"^[\d\s+\-()]{7,20}$")

COUNTRIES = ["India", "Vietnam", "Japan", "China", "London"]


class PatientCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=1, le=150)
    gender: Gender
    phone: str = Field(min_length=7, max_length=20)
    address: str = Field(min_length=1)
    country: str | None = Field(default=None)

    @field_validator("name", "address", "phone", mode="before")
    @classmethod
    def strip_strings(cls, v: object) -> object:
        if isinstance(v, str):
            return v.strip()
        return v

    @field_validator("name", "address")
    @classmethod
    def non_empty_after_strip(cls, v: str) -> str:
        if not v:
            raise ValueError("must not be empty")
        return v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not PHONE_PATTERN.match(v):
            raise ValueError("invalid phone number format")
        return v

    @field_validator("country")
    @classmethod
    def validate_country(cls, v: str | None) -> str | None:
        if v is not None and v not in COUNTRIES:
            raise ValueError("invalid country")
        return v


class PatientRead(BaseModel):
    id: str
    name: str
    age: int
    gender: Gender
    phone: str
    address: str
    country: str | None
    created_at: datetime
