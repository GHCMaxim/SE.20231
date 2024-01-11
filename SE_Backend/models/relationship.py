from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Relationship(Base):
    __tablename__ = "relationships"

    cccd: Mapped[str] = mapped_column(ForeignKey("people.cccd"), primary_key=True)
    relationship: Mapped[str] = mapped_column(String, nullable=False)
    birth_id: Mapped[int] = mapped_column(ForeignKey("births.id"), nullable=True)
    alive: Mapped[bool] = mapped_column(Boolean, nullable=False)
    death_paper_id: Mapped[int] = mapped_column(Integer, nullable=True)
    household_id: Mapped[str] = mapped_column(ForeignKey("household_registrations.id"))
