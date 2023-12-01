import datetime
from pydantic import BaseModel


class PaymentBase(BaseModel):
    name: str


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int
    type_id: int
    creation_date: datetime.datetime
    expiration_date: datetime.datetime
    price: int
    household: str
    income_id: int

    class Config:
        orm_type = True


class PaymentTypeCreate(PaymentBase):
    pass


class PaymentType(PaymentBase):
    id: int

    class Config:
        orm_type = True
