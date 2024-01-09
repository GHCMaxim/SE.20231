import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Income(Base):
    __tablename__ = "income"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    total: Mapped[int] = mapped_column(Integer, nullable=False)
    income_time: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)


class TotalIncome(Base):
    __tablename__ = "total_income"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    total: Mapped[int] = mapped_column(Integer, nullable=False)
    calc_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
