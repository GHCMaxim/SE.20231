from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class Birth(Base):
    __tablename__ = "births"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    book_number: Mapped[str] = mapped_column(String, nullable=False)
