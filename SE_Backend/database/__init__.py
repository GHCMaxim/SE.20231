# ruff: noqa: E402, F401
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///instance/database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from . import (
    away,
    birth,
    household_registration,
    income,
    person,
    payment,
    relationship,
    reward,
    spending,
    user,
    vehicle,
)
