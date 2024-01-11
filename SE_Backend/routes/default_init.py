import uuid
from datetime import datetime

from passlib.context import CryptContext

from SE_Backend import models
from SE_Backend.database import SessionLocal

db = SessionLocal()

person_id = uuid.uuid4()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


payment_type1 = models.PaymentType(
    name="Phí gửi xe máy (tháng)",
    rate=70000,
    active=True,
    id=1,
)

payment_type2 = models.PaymentType(
    name = "Phí gửi ô tô (tháng)",
    rate = 1200000,
    active = True,
    id = 2,
)

payment_type = models.PaymentType(
    name = "Phí gửi xe hàng tháng",
    rate = 0,
    active = True,
    id = 0,
)

payment_type3 = models.PaymentType(
    name = "Phí quản lý tiền dịch vụ",
    rate = 0,
    active = True,
    id = -1,
)

payment_type9 = models.PaymentType(
    name = "Tiền quản lý CC giá rẻ",
    rate = 7000,
    active = True,
    id = 3,
)

payment_type4 = models.PaymentType(
    name = "Tiền quản lý CC thường",
    rate = 10000,
    active = True,
    id = 4,
)

payment_type5 = models.PaymentType(
    name = "Tiền quản lý CC cao cấp",
    rate = 15000,
    active = True,
    id = 5,
)

payment_type6 = models.PaymentType(
    name = "Tiền điện/số",
    rate = 2500,
    active = True,
    id = 6,
)

payment_type7 = models.PaymentType(
    name = "Tiền nước/số",
    rate = 8000,
    active = True,
    id = 7,
)

payment_type8 = models.PaymentType(
    name = "Tiền internet",
    rate = 150000,
    active = True,
    id = 8,
)
db.add(payment_type)
db.add(payment_type1)
db.add(payment_type2)
db.add(payment_type3)
db.add(payment_type4)
db.add(payment_type5)
db.add(payment_type6)
db.add(payment_type7)
db.add(payment_type8)
db.add(payment_type9)
db.commit()
db.refresh(payment_type)
db.refresh(payment_type1)
db.refresh(payment_type2)
db.refresh(payment_type3)
db.refresh(payment_type4)
db.refresh(payment_type5)
db.refresh(payment_type6)
db.refresh(payment_type7)
db.refresh(payment_type8)
db.refresh(payment_type9)
db.close()