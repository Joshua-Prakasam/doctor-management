"""Entry point for server."""

from __future__ import annotations

from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from doctor_management import schemas
from doctor_management.db import crud, database, models
from doctor_management.dependency import get_db
from doctor_management.utils import (
    create_access_token,
    verify_password,
)

ACCESS_TOKEN_EXPIRE_MINUTES = 30


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def authenticate_doctor(
    db: database.Session,
    email: str,
    password: str,
) -> models.Doctor | False:
    """Get authenticated doctor."""
    doctor = crud.get_doctor_by_email(db, email)
    if not doctor:
        return False
    if not verify_password(password, str(doctor.hashed_password)):
        return False
    return doctor


@app.post("/doctors", response_model=schemas.Doctor)
def create_doctor(
    user: schemas.CreateDoctor,
    db: Annotated[database.Session, Depends(get_db)],
) -> models.Doctor:
    """Endpoint to register a doctor."""
    db_user = crud.get_doctor_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )
    return crud.create_doctor(db=db, user=user)


@app.post("/token")
async def login_for_access_token(
    form_data: schemas.LoginDoctorDTO,
    db: Annotated[database.Session, Depends(get_db)],
) -> schemas.Token:
    """Get Login Token."""
    doctor = authenticate_doctor(
        db,
        form_data.email,
        form_data.password,
    )
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    access_token = create_access_token(
        data={"sub": str(doctor.id)},
        expires_delta=access_token_expires,
    )
    return schemas.Token(access_token=access_token)
