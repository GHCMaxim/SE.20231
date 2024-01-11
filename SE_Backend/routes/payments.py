from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from .. import schemas, database

payments = APIRouter(tags=["payments"])


@payments.get("/api/payments", response_model=list[schemas.payment.Payment])
def get_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_payments = database.payment.get_payments(db, skip=skip, limit=limit)
    return db_payments


@payments.get("/api/payments/{id}", response_model=schemas.payment.Payment)
def get_payment(id: int, db: Session = Depends(get_db)):
    db_payment = database.payment.get_payment(db, id=id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="payment not found.")
    return db_payment


@payments.get(
    "/api/payments/by_household/{household_id}",
    response_model=list[schemas.payment.Payment],
)
def get_payment_by_household(household_id: str, db: Session = Depends(get_db)):
    db_payments = database.payment.get_payments_by_household(
        db, household_id=household_id
    )
    return db_payments


@payments.post("/api/payments", response_model=schemas.payment.Payment)
def post_payment(payment: schemas.payment.PaymentCreate, db: Session = Depends(get_db)):
    return database.payment.create_payment(db, payment=payment)


@payments.get("/api/payment_types", response_model=list[schemas.payment.PaymentType])
def get_payment_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payment_types = database.payment.get_payment_types(db, skip=skip, limit=limit)
    return payment_types


@payments.get("/api/payment_types/{id}", response_model=schemas.payment.PaymentType)
def get_payment_type(id: int, db: Session = Depends(get_db)):
    db_payment_type = database.payment.get_payment_type(db, id=id)
    if db_payment_type is None:
        raise HTTPException(status_code=404, detail="payment type not found.")
    return db_payment_type


@payments.post("/api/payments", response_model=schemas.payment.PaymentType)
def post_payment_type(
    payment_type: schemas.payment.PaymentTypeCreate, db: Session = Depends(get_db)
):
    return database.payment.create_payment_type(db, payment_type=payment_type)


@payments.put("/api/payments/{id}", response_model=schemas.payment.Payment)
def put_payment(
    id: int, payment: schemas.payment.PaymentModify, db: Session = Depends(get_db)
):
    db_payment = database.payment.get_payment(db, id=id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="payment not found.")
    return database.payment.update_payment(db, id, payment=payment)


@payments.put("/api/payment_types/{id}", response_model=schemas.payment.PaymentType)
def put_payment_type(
    id: int,
    payment_type: schemas.payment.PaymentTypeModify,
    db: Session = Depends(get_db),
):
    db_payment_type = database.payment.get_payment_type(db, type=type)
    if db_payment_type is None:
        raise HTTPException(status_code=404, detail="payment type not found.")
    return database.payment.update_payment_type(db, id, payment_type=payment_type)

@payments.put("/api/payments/monthly/create", response_model=str)
def create_monthly_payments(db: Session = Depends(get_db)):
    return database.payment.create_monthly_payments(db)