import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class HouseholdRegistration(Base):
    __tablename__ = "household_registrations"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    creation_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
