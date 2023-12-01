import datetime
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Spending(Base):
    __tablename__ = "spendings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    total: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    total_id: Mapped[int] = mapped_column(ForeignKey("total_income.id"))
