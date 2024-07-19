"""Table Models."""

from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from doctor_management.db.database import Base


class Doctor(Base):
    """Doctor Table."""

    __tablename__ = "Doctors"

    id = Column(
        Integer,
        name="DoctorID",
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    name = Column(String(100), name="Name", nullable=False)
    email = Column(
        String,
        name="Email",
        nullable=False,
        unique=True,
        index=True,
    )
    hashed_password = Column(
        String(255),
        name="PasswordHash",
        nullable=False,
    )
    specialty = Column(String(100), name="Specialty", nullable=False)


class Patient(Base):
    """Patient Table."""

    __tablename__ = "Patients"

    id = Column(
        Integer,
        name="PatientID",
        primary_key=True,
        nullable=False,
    )
    name = Column(String(100), name="Name", nullable=False)
    email = Column(
        String,
        name="Email",
        unique=True,
        index=True,
        nullable=False,
    )
    hashed_password = Column(
        String(255),
        name="PasswordHash",
        nullable=False,
    )


class PDF(Base):
    """PDF Table."""

    __tablename__ = "PDFS"

    id = Column(
        Integer,
        name="PDFID",
        primary_key=True,
        nullable=False,
    )
    doctor_id = Column(
        Integer,
        ForeignKey("Doctors.DoctorID"),
        name="DoctorID",
        nullable=False,
    )
    file_path = Column(String(255), name="FilePath", nullable=False)
    upload_date = Column(
        DateTime,
        name="UploadDate",
        default=datetime.now(UTC),
        nullable=False,
    )


class DoctorPatient(Base):
    """DoctorPatient Relation Table."""

    __tablename__ = "DoctorPatient"

    doctor_id = Column(
        Integer,
        ForeignKey("Doctors.DoctorID"),
        name="DoctorID",
        primary_key=True,
        nullable=False,
    )
    patient_id = Column(
        Integer,
        ForeignKey("Patients.PatientID"),
        name="PatientID",
        primary_key=True,
        nullable=False,
    )
