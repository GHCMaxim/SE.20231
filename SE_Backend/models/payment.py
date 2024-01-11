import uuid
import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("payment_types.id"))
    creation_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    expiration_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    household: Mapped[str] = mapped_column(ForeignKey("household_registrations.id"))
    income_id: Mapped[int] = mapped_column(ForeignKey("income.id"))
    paid: Mapped[bool] = mapped_column(Boolean, nullable=False)


class PaymentType(Base):
    __tablename__ = "payment_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False)
