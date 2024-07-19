"""Request Dependency."""

from typing import Any, Generator

from doctor_management.db.database import Session, SessionLocal


def get_db() -> Generator[Session, Any, None]:
    """Get DB Session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
