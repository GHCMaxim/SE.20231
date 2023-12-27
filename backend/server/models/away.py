from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class AwayType(Base):
    __tablename__ = "away_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class Away(Base):
    __tablename__ = "away"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    household_id: Mapped[str] = mapped_column(ForeignKey("household_registrations.id"))
    away_type_id: Mapped[int] = mapped_column(ForeignKey("away_types.id"))
    description: Mapped[str] = mapped_column(String, nullable=False)