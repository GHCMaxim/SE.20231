from ..database import SessionLocal, engine, Base

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from . import (
    household_registrations,
    payments,
    people,
    rewards,
    users,
)  # noqa: E402, F401
