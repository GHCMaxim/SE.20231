import uuid
import datetime
import random
from sqlalchemy import func
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
    id = uuid.uuid4()
    db_payment = models.Payment(
        id = id,
        name= payment.name,
        type_id=payment.type_id,
        creation_date=payment.creation_date,
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
        id = payment_type.id,
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

def create_monthly_payments(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    # Check if there exists any payment in the current month
    db_payment = db.query(models.Payment).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").first()
    if db_payment is not None:
        db.refresh(db_payment)
        return "Hoá đơn đã được tạo rồi."
    else:
        db.refresh(db_payment)
        household_ids = db.query(models.HouseholdRegistration.id).all()
        for household_id in household_ids:
            vehicle_count = [db.query(models.Vehicle).filter(models.Vehicle.owner == household_id).filter(models.Vehicle.vehicle_type == "1").count(), db.query(models.Vehicle).filter(models.Vehicle.owner == household_id).filter(models.Vehicle.vehicle_type == "2").count()]
            
            house_type = db.query(models.HouseholdRegistration.house_type).filter(models.HouseholdRegistration.id == household_id).first()
            house_size = db.query(models.HouseholdRegistration.size).filter(models.HouseholdRegistration.id == household_id).first()
            income_uuid = uuid.uuid4()
            id1 = uuid.uuid4()
            id2 = uuid.uuid4()
            id3 = uuid.uuid4()
            id4 = uuid.uuid4()
            id5 = uuid.uuid4()
            id6 = uuid.uuid4()
            db_payment_vehicle1 = models.Payment(
                id = id1,
                name = f"Tiền gửi xe máy tháng {current_month}/{current_year} ", 
                type_id = 1,
                creation_date = f"{current_year}-{current_month}-10",
                price = vehicle_count[0] * db.query(models.PaymentType).filter(models.PaymentType.id == 1).first().rate,
                household = household_id,
                income_id = income_uuid,
                paid = False
            )
            db_payment_vehicle2 = models.Payment(
                id = id2,
                name = f"Tiền gửi xe máy tháng {current_month}/{current_year} ", 
                type_id = 2,
                creation_date = f"{current_year}-{current_month}-10",
                price = vehicle_count[1] * db.query(models.PaymentType).filter(models.PaymentType.id == 2).first().rate,
                household = household_id,
                income_id = income_uuid,
                paid = False
            )
            db_payment_house = models.Payment(
                id = id3,
                name = f"Tiền quản lý chung cư tháng {current_month}/{current_year} ",
                type_id = house_type + 2,
                creation_date = f"{current_year}-{current_month}-10",
                price = house_size * db.query(models.PaymentType).filter(models.PaymentType.id == house_type + 2).first().rate,
                household = household_id,
                income_id = income_uuid,
                paid = False,
            )
            db_payment_service1 = models.Payment(
                id = id4,
                name = f"Tiền điện tháng {current_month}/{current_year} ",
                type_id = 6,
                creation_date = f"{current_year}-{current_month}-10",
                price = random.randint(2000, 10000)/10 * db.query(models.PaymentType).filter(models.PaymentType.id == 6).first().rate,
                household = household_id,
                income_id = income_uuid,
                paid = False,
            )   
            db_payment_service2 = models.Payment(
                id = id5,
                name = f"Tiền nước tháng {current_month}/{current_year} ",
                type_id = 7,
                creation_date = f"{current_year}-{current_month}-10",
                price = random.randint(2000, 10000)/10 * db.query(models.PaymentType).filter(models.PaymentType.id == 7).first().rate,
                household = household_id,
                income_id = income_uuid,
                paid = False,
            )
            db_payment_service3 = models.Payment(
                id = id6,
                name = f"Tiền nước tháng {current_month}/{current_year} ",
                type_id = 7,
                creation_date = f"{current_year}-{current_month}-10",
                price = db.query(models.PaymentType).filter(models.PaymentType.id == 7).first().rate,
                household = household_id,
                income_id = income_uuid,
                paid = False,
            )
            db.add(db_payment_vehicle1)
            db.add(db_payment_vehicle2)
            db.add(db_payment_house)
            db.add(db_payment_service1)
            db.add(db_payment_service2)
            db.add(db_payment_service3)
            db.commit()
            db.refresh(db_payment_vehicle1)
            db.refresh(db_payment_vehicle2)
            db.refresh(db_payment_house)
            db.refresh(db_payment_service1)
            db.refresh(db_payment_service2)
            db.refresh(db_payment_service3)
        return "Đã tạo xong hóa đơn tháng này."