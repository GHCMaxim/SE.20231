import time
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
    id = int(time.time()*1000)
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

    response = []*db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().count()
    households = db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().all()
    print(households)
    for i in households:
        household = i[0]
        vehicle_type_1 = db.query(models.Vehicle.vehicle_type).filter(models.Vehicle.owner == household).filter(models.Vehicle.vehicle_type == "1").count()
        vehicle_type_2 = db.query(models.Vehicle.vehicle_type).filter(models.Vehicle.owner == household).filter(models.Vehicle.vehicle_type == "2").count()
        total_payment = vehicle_type_1 * 70000 + vehicle_type_2 * 1200000
        paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id == 0).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).first()
        response.append({"household": household, "vehicle_count_type1": vehicle_type_1, "vehicle_count_type2": vehicle_type_2, "price": total_payment, "paid": paid[0]})
    return response


def find_monthly_house_payment(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    response = []*db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().count()
    households = db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().all()
    for i in households:
        household = i[0]
        house_type = db.query(models.HouseholdRegistration.house_type).filter(models.HouseholdRegistration.id == household).first()
        house_size = db.query(models.HouseholdRegistration.size).filter(models.HouseholdRegistration.id == household).first()
        paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id.in_([3, 4, 5])).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10,0,0)).first()
        price = db.query(models.Payment.price).filter(models.Payment.household == household).filter(models.Payment.type_id.in_([3, 4, 5])).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10,0,0)).first()
        response.append({"household": household, "house_type": house_type[0], "size": house_size[0], "price": price[0], "paid": paid[0]})
    return response

def find_monthly_service_payment(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    response = []*db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().count()
    households = db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().all()
    for i in households:
        household = i[0]
        service_payment = db.query(models.Payment.price).filter(models.Payment.household == household).filter(models.Payment.type_id == -1).filter(models.Payment.creation_date == (datetime.datetime(current_year, current_month, 10,0,0))).first()
        paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id == -1).filter(models.Payment.creation_date == (datetime.datetime(current_year, current_month, 10,0,0))).first()
        response.append({"household": household, "service_payment": service_payment[0], "paid": paid[0]})
    return response

def find_monthly_payment(db: Session):
    index = 0
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    response = [{}]*db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().count()
    households = db.query(models.Payment.household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).distinct().all()
    for i in households:
        household = i[0]
        vehicle_payment_paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id == 0).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10, 0, 0)).first()
        house_payment_paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id.in_([3, 4, 5])).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10,0,0)).first()
        service_payment_paid = db.query(models.Payment.paid).filter(models.Payment.household == household).filter(models.Payment.type_id == -1).filter(models.Payment.creation_date == (datetime.datetime(current_year, current_month, 10,0,0))).first()
        total_payment = db.query(func.sum(models.Payment.price)).filter(models.Payment.household == household).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10,0,0)).all()
        print(total_payment)
        total_paid = db.query(models.Payment.price).filter(models.Payment.household == household).filter(models.Payment.paid == True).filter(models.Payment.creation_date == datetime.datetime(current_year, current_month, 10,0,0)).all()
        if total_paid == []:
            total_paid = 0
        response[index].update({"household": household, "vehicle_payment": vehicle_payment_paid[0], "house_payment": house_payment_paid[0], "service_payment": service_payment_paid[0], "total_payment": total_payment[0][0], "total_paid": total_paid})
        index += 1
    return response
def create_monthly_payments(db: Session):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    income_id_b = int(f"{current_year}{current_month}10")
    db_payment = db.query(models.Income).filter(models.Income.id == income_id_b).first()
    if db_payment is not None:
        return "Hoá đơn đã được tạo rồi."
    else:
        db_income= models.Income(
            id = income_id_b,
            description = f"Thu nhập tháng {current_month}/{current_year} ",
            income_time = datetime.date(current_year, current_month, 10),
            total = 0,
        )
        household_ids = db.query(models.HouseholdRegistration.id).all()
        for i in household_ids:
            household_id = i[0]
            vehicle_count = [db.query(models.Vehicle).filter(models.Vehicle.owner == household_id).filter(models.Vehicle.vehicle_type == "1").count(), db.query(models.Vehicle).filter(models.Vehicle.owner == household_id).filter(models.Vehicle.vehicle_type == "2").count()]
            
            house_type = db.query(models.HouseholdRegistration.house_type).filter(models.HouseholdRegistration.id == household_id).first()
            house_size = db.query(models.HouseholdRegistration.size).filter(models.HouseholdRegistration.id == household_id).first()
            id1 = int(time.time()*1000) +1
            id2 = int(time.time()*1000) +2
            id3 = int(time.time()*1000) +3
            if vehicle_count[0] == 0 and vehicle_count[1] == 0:
                    db_payment_vehicle1 = models.Payment(
                    id = id1,
                    name = f"Tiền gửi xe tháng {current_month}/{current_year} ", 
                    type_id = 0,
                    creation_date = datetime.date(current_year, current_month, 10),
                    price = vehicle_count[0] * db.query(models.PaymentType).filter(models.PaymentType.id == 1).first().rate + vehicle_count[1] * db.query(models.PaymentType).filter(models.PaymentType.id == 2).first().rate,
                    household = household_id,
                    income_id = income_id_b,
                    paid = True
                )
            else:
                    db_payment_vehicle1 = models.Payment(
                    id = id1,
                    name = f"Tiền gửi xe tháng {current_month}/{current_year} ", 
                    type_id = 0,
                    creation_date = datetime.date(current_year, current_month, 10),
                    price = vehicle_count[0] * db.query(models.PaymentType).filter(models.PaymentType.id == 1).first().rate + vehicle_count[1] * db.query(models.PaymentType).filter(models.PaymentType.id == 2).first().rate,
                    household = household_id,
                    income_id = income_id_b,
                    paid = False
                )
            db_payment_house = models.Payment(
                id = id3,
                name = f"Tiền quản lý chung cư tháng {current_month}/{current_year} ",
                type_id = house_type[0] + 2,
                creation_date = datetime.date(current_year, current_month, 10),
                price = house_size[0] * db.query(models.PaymentType).filter(models.PaymentType.id == house_type[0] + 2).first().rate,
                household = household_id,
                income_id = income_id_b,
                paid = False,
            )
            db_payment_service = models.Payment(
                id = id2,
                name = f"Tiền quản lý dịch vụ tháng {current_month}/{current_year} ",
                type_id = -1,
                creation_date = datetime.date(current_year, current_month, 10),
                price = random.randint(2000, 10000)/10 * db.query(models.PaymentType).filter(models.PaymentType.id == 6).first().rate + random.randint(2000, 10000)/10 * db.query(models.PaymentType).filter(models.PaymentType.id == 7).first().rate + db.query(models.PaymentType).filter(models.PaymentType.id == 8).first().rate,
                household = household_id,
                income_id = income_id_b,
                paid = False,
            )
            db.add(db_income)
            db.add(db_payment_vehicle1)
            db.add(db_payment_house)
            db.add(db_payment_service)
            db.commit()
            db.refresh(db_payment_vehicle1)
            db.refresh(db_payment_house)
            db.refresh(db_payment_service)
        return "Đã tạo xong hóa đơn tháng này."