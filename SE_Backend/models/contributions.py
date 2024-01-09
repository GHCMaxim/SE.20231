import uuid
import datetime
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Contributions(Base):
    __tablename__ = "contributions"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    contributor: Mapped[str] = mapped_column(ForeignKey("person.cccd"))
    amount: Mapped[int] = mapped_column(int, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    contribution_time: Mapped[datetime.date] = mapped_column(datetime.date, nullable=False)
