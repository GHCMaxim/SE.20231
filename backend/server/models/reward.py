import datetime
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Reward(Base):
    __tablename__ = "rewards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    reward_type_id: Mapped[int] = mapped_column(ForeignKey("reward_types.id"))
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    recipient: Mapped[str] = mapped_column(ForeignKey("people.id"))
    spending_id: Mapped[int] = mapped_column(ForeignKey("spendings.id"))


class RewardType(Base):
    __tablename__ = "reward_types"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
