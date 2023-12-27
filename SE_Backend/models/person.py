import uuid
import datetime
from sqlalchemy import Date, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Person(Base):
    __tablename__ = "people"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    dob: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    sex: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
    religion: Mapped[str] = mapped_column(String)
    ethnicity: Mapped[str] = mapped_column(String)
    job: Mapped[str] = mapped_column(String)
    job_location: Mapped[str] = mapped_column(String)
    cccd: Mapped[str] = mapped_column(String)
