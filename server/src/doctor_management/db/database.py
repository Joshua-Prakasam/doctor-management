"""DB Connection."""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from doctor_management.config import app_config

__all__ = ["Base", "engine", "Session"]

engine = create_engine(
    str(app_config.pg_dsn),
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """Declarative Base."""
