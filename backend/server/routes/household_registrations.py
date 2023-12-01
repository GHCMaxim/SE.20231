from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

household_registrations = APIRouter(tags=["household_registrations"])


@household_registrations.get(
    "/api/household_registrations",
    response_model=schemas.household_registration.HouseholdRegistration,
)
def get_household_registration(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    payments = database.payment.get_payments(db, skip=skip, limit=limit)
    return payments


@household_registrations.get(
    "/api/household_registrations/{id}",
    response_model=schemas.household_registration.HouseholdRegistration,
)
def get_household_registrations(id: int, db: Session = Depends(get_db)):
    db_payment = database.payment.get_payment(db, id=id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="household not found.")
    return db_payment


@household_registrations.post(
    "/api/household_registrations",
    response_model=schemas.household_registration.HouseholdRegistration,
)
def post_household(
    household: schemas.household_registration.HouseholdRegistrationCreate,
    db: Session = Depends(get_db),
):
    db_household = database.household_registration.get_household_registration(
        db, id=household.id
    )
    if db_household:
        raise HTTPException(status_code=400, detail="household already registered.")
    return database.household_registration.create_household_registration(
        db, household=household
    )
