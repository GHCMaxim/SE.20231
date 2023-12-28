from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import get_db
from .. import database

statistics = APIRouter(tags=["statistics"])


@statistics.get("/api/statistics/households", response_model=int)
def get_households(db: Session = Depends(get_db)):
    return database.household_registration.count_households(db)


@statistics.get("/api/statistics/people", response_model=int)
def get_people(db: Session = Depends(get_db)):
    return database.person.count_people(db)


@statistics.get("/api/statistics/rewards", response_model=int)
def get_rewards(db: Session = Depends(get_db)):
    return database.reward.count_rewards(db)


@statistics.get("/api/statistics/income", response_model=list[float])
def get_income(db: Session = Depends(get_db)):
    return database.income.count_income(db)


@statistics.get("/api/statistics/age", response_model=list[int])
def get_age(db: Session = Depends(get_db)):
    return database.person.count_age(db)


@statistics.get("/api/statistics/gender", response_model=list[int])
def get_gender(db: Session = Depends(get_db)):
    return database.person.count_gender(db)

