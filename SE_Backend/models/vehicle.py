from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    license_plate: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_type: Mapped[str] = mapped_column(String, nullable=False)
    owner: Mapped[str] = mapped_column(ForeignKey("household_registrations.id"))
