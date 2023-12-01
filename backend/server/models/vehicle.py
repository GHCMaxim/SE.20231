from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    license_plate: Mapped[str] = mapped_column(String, primary_key=True)
    vehicle_type: Mapped[str] = mapped_column(String, nullable=False)
    owner: Mapped[int] = mapped_column(Integer, nullable=False)
