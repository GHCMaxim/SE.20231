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

def find_monthly_vehicle_payment(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    return db.query(models.Payment.household, 
                    func.count(models.Vehicle.vehicle_type == "1").label("vehicle_count_type1"),    
                    func.count(models.Vehicle.vehicle_type == "2").label("vehicle_count_type2"),
                    models.Payment.price,
                    models.Payment.paid
                    ).join(models.Vehicle, models.Vehicle.owner == models.Payment.household).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").filter(models.Payment.type_id == 0).group_by(models.Payment.household).all()

def find_monthly_house_payment(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    return db.query(models.Payment.household,
                    models.HouseholdRegistration.house_type,
                    models.HouseholdRegistration.size,
                    models.Payment.price,
                    models.Payment.paid).join(models.HouseholdRegistration, models.HouseholdRegistration.id == models.Payment.household).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").filter(models.Payment.type_id.in_([2, 3, 4])).all()

def find_monthly_service_payment(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    return db.query(models.Payment).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").filter(models.Payment.type_id == -1).all()

def find_monthly_payment(db: Session):
    response = []
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    households = db.query(models.HouseholdRegistration.id).all()
    for i in households:
        household = i[0]
        vehicle_payment = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id == 0).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").first()
        house_payment_paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id.in_([3, 4, 5])).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").all()
        service_payment_paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id == -1).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").all()
        total_payment = vehicle_payment + house_payment_paid + service_payment_paid
        total_paid = db.query(models.Payment.price).filter(models.Payment.household == household).filter(models.Payment.paid == True).filter(models.Payment.creation_date == f"{current_year}-{current_month}-10").all()
        response.append([household, vehicle_payment, house_payment_paid, service_payment_paid, total_payment, total_paid])
    return response
def create_monthly_payments(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
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
            db_payment_vehicle1 = models.Payment(
                id = id1,
                name = f"Tiền gửi xe tháng {current_month}/{current_year} ", 
                type_id = 0,
                creation_date = f"{current_year}-{current_month}-10",
                price = vehicle_count[0] * db.query(models.PaymentType).filter(models.PaymentType.id == 1).first().rate + vehicle_count[1] * db.query(models.PaymentType).filter(models.PaymentType.id == 2).first().rate,
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
            db_payment_service = models.Payment(
                id = id2,
                name = f"Tiền quản lý dịch vụ tháng {current_month}/{current_year} ",
                type_id = -1,
                creation_date = f"{current_year}-{current_month}-10",
                price = random.randint(2000, 10000)/10 * db.query(models.PaymentType).filter(models.PaymentType.id == 6).first().rate + random.randint(2000, 10000)/10 * db.query(models.PaymentType).filter(models.PaymentType.id == 7).first().rate + db.query(models.PaymentType).filter(models.PaymentType.id == 8).first().rate,
                household = household_id,
                income_id = None,
                paid = False,
            )
            db.add(db_payment_vehicle1)
            db.add(db_payment_house)
            db.add(db_payment_service)
            db.commit()
            db.refresh(db_payment_vehicle1)
            db.refresh(db_payment_house)
            db.refresh(db_payment_service)
        return "Đã tạo xong hóa đơn tháng này."