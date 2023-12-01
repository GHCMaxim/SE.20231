from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

payments = APIRouter(tags=["payments"])


@payments.get("/api/payments", response_model=schemas.payment.Payment)
def get_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = database.payment.get_payments(db, skip=skip, limit=limit)
    return payments


@payments.get("/api/payments/{id}", response_model=schemas.payment.Payment)
def get_payment(id: int, db: Session = Depends(get_db)):
    db_payment = database.payment.get_payment(db, id=id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="payment not found.")
    return db_payment


@payments.get(
    "/api/payments/by_household/{household_id}", response_model=schemas.payment.Payment
)
def get_payment_by_household(household_id: str, db: Session = Depends(get_db)):
    db_payments = database.payment.get_payments_by_household(
        db, household_id=household_id
    )
    return db_payments
