"""DTO Schemas."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, EmailStr


class Token(BaseModel):
    """Token schema."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Token Data Schema."""

    id: int | None = None


class BaseDoctor(BaseModel):
    """Doctor schema."""

    name: str
    email: str
    specialty: str


class CreateDoctor(BaseDoctor):
    """Create Doctor DTO."""

    password: str


class LoginDoctorDTO(BaseModel):
    """Login Doctor DTO."""

    email: EmailStr
    password: str


class Doctor(BaseDoctor):
    """Doctor without password."""

    id: int

    model_config = ConfigDict(from_attributes=True)


class DoctorInDB(Doctor):
    """Doctor DTO in DB."""

    hashed_password: str

    model_config = ConfigDict(from_attributes=True)
