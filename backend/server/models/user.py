import uuid
from sqlalchemy import Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    address: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String, nullable=False)
    sex: Mapped[str] = mapped_column(String, nullable=False)
    cccd: Mapped[str] = mapped_column(String, nullable=False)
    job: Mapped[str] = mapped_column(String)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    permissions: Mapped[int] = mapped_column(Integer, nullable=False)
