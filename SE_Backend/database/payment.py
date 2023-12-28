from sqlalchemy.orm import Session

from .. import models, schemas


def get_payment(db: Session, id: int):
    return db.query(models.Payment).filter(models.Person.id == id).first()


def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).offset(skip).limit(limit).all()


def get_payments_by_household(
    db: Session, household_id: str, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.Payment).filter(models.Payment.household == household_id).all()
    )


def create_payment(db: Session, payment: schemas.payment.PaymentCreate):
    db_payment = models.Payment(
        type_id=payment.type_id,
        creation_date=payment.creation_date,
        expiration_date=payment.expiration_date,
        price=payment.price,
        household=payment.household,
        income_id=payment.income_id,
    )

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return db_payment


def get_payment_type(db: Session, id: int):
    return db.query(models.PaymentType).filter(models.PaymentType.id == id).first()


def get_payment_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PaymentType).offset(skip).limit(limit).all()


def create_payment_type(db: Session, payment_type: schemas.payment.PaymentTypeCreate):
    db_payment_type = models.PaymentType(
        name=payment_type.name,
        rate=payment_type.rate,
        active=payment_type.active,
    )

    db.add(db_payment_type)
    db.commit()
    db.refresh(db_payment_type)

    return db_payment_type

def put_payment(id: int, payment: schemas.payment.PaymentModify, db: Session):
    db.query(models.Payment).filter(models.Payment.id == id).update(payment.dict())
    db.commit()
    return db.query(models.Payment).filter(models.Payment.id == id).first()

def put_payment_type(id: int, payment_type: schemas.payment.PaymentTypeModify, db: Session):
    db.query(models.PaymentType).filter(models.PaymentType.id == id).update(payment_type.dict())
    db.commit()
    return db.query(models.PaymentType).filter(models.PaymentType.id == id).first()

