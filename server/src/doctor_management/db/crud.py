"""CRUD Utils."""

from __future__ import annotations

from typing import TYPE_CHECKING

from doctor_management.db import models
from doctor_management.utils import get_password_hash

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

    from doctor_management import schemas


def create_doctor(
    db: Session,
    user: schemas.CreateDoctor,
) -> models.Doctor:
    """Create a new doctor."""
    hashed_password = get_password_hash(user.password)
    db_doctor = models.Doctor(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        specialty=user.specialty,
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_doctor_by_email(
    db: Session,
    email: str,
) -> models.Doctor | None:
    """Get doctor by email."""
    return (
        db.query(models.Doctor)
        .filter(models.Doctor.email == email)
        .first()
    )
