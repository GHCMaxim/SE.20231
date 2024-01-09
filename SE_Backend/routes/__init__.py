# ruff: noqa: E402, F401
from ..database import SessionLocal, engine, Base

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from . import (
    auth,
    aways,
    births,
    household_registrations,
    income,
    payments,
    people,
    relationships,
    rewards,
    spendings,
    statistics,
    users,
    vehicles,
    contributions,
)
