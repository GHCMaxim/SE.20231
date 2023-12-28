import uuid
from datetime import datetime

from SE_Backend import models
from SE_Backend.database import SessionLocal

db = SessionLocal()

person_id = uuid.uuid4()

user = models.User(
    id=person_id,
    address="Ha Noi",
    name="Nguyen Van A",
    sex="M",
    cccd="123456789012",
    job="Sinh vien",
    username="username",
    password="password",
    permissions=1,
)

person = models.Person(
    id=person_id,
    name="Nguyen Van A",
    dob=datetime(1999, 1, 1),
    sex="M",
    religion="Khong",
    ethnicity="Kinh",
    job="Sinh vien",
    job_location="Ha Noi",
    cccd="123456789012",
    phone_number="0123456789",
)

birth = models.Birth(id=1, book_number=1)

relationship = models.Relationship(
    cccd="123456789012",
    relationship="Chu ho",
    birth_id=1,
    alive=True,
    death_paper_id=None,
    household_id=1,
)

household = models.HouseholdRegistration(
    id=1,
    name="Ho gia dinh A",
    location="Ha Noi",
    creation_date=datetime(2021, 1, 1),
    owner="123456789012",
)

total_income = models.TotalIncome(
    id=1,
    total=100000,
    calc_date=datetime.now(),
    description="what",
)

income = models.Income(
    id=1,
    description="yes",
    total=100000,
    income_time=datetime.now(),
    total_income_id=1,
)

spendings = models.Spending(
    id=1,
    date=datetime(2021, 1, 1),
    total=100000,
    description="Mua thuc pham",
    household_id=1,
    total_id=1,
)

reward_type = models.RewardType(
    id=1,
    name="Phat sinh hoat",
    description="Phat sinh hoat",
    active=True,
)

reward = models.Reward(
    id=1,
    reward_type_id=1,
    date=datetime(2021, 1, 1),
    recipient=person_id,
    spending_id=1,
)

vehicle = models.Vehicle(
    license_plate="30a1-12345",
    vehicle_type="Xe may",
    owner="123456789012",
)

away_type = models.AwayType(
    id=1,
    name="Di hoc",
    description="Di hoc",
    status=True,
)

away = models.Away(
    id=1,
    household_id=1,
    cccd="123456789012",
    away_type_id=1,
    description="Di hoc",
)

payment = models.Payment(
    id=1,
    name="Phi nuoc",
    type_id=1,
    creation_date=datetime(2021, 1, 1),
    expiration_date=datetime(2021, 1, 1),
    price=100000,
    household=1,
    income_id=1,
)

payment_type = models.PaymentType(
    id=1,
    name="Phi nuoc",
    rate=100000,
    active=True,
)

db.add(user)
db.add(person)
db.add(relationship)
db.add(household)
db.add(birth)
db.add(total_income)
db.add(income)
db.add(spendings)
db.add(reward_type)
db.add(reward)
db.add(vehicle)
db.add(away_type)
db.add(away)
db.add(payment_type)
db.add(payment)
db.commit()
db.close()
