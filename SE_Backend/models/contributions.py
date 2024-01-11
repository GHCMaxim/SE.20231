import uuid
import datetime
from sqlalchemy import String, Uuid, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Contributions(Base):
    __tablename__ = "contributions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    contributor: Mapped[str] = mapped_column(ForeignKey("people.cccd"))
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    contribution_time: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    contribution_event: Mapped[int] = mapped_column(ForeignKey("contribution_events.id"))
    
class ContributionEvent(Base):
    __tablename__ = "contribution_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    total_amount = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    event_time: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
