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


def update_payment(db: Session, id: int, payment: schemas.payment.PaymentModify):
    db.query(models.Payment).filter(models.Payment.id == id).update(
        payment.model_dump()
    )
    db.commit()
    return db.query(models.Payment).filter(models.Payment.id == payment.id).first()


def update_payment_type(
    db: Session, id: int, payment_type: schemas.payment.PaymentTypeModify
):
    db.query(models.PaymentType).filter(models.PaymentType.id == id).update(
        payment_type.model_dump()
    )
    db.commit()
    return (
        db.query(models.PaymentType)
        .filter(models.PaymentType.id == payment_type.id)
        .first()
    )
