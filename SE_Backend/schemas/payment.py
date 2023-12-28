import datetime
from pydantic import BaseModel


class PaymentBase(BaseModel):
    name: str


class PaymentCreate(PaymentBase):
    type_id: int
    creation_date: datetime.datetime
    expiration_date: datetime.datetime
    price: int
    household: str
    income_id: int


class Payment(PaymentBase):
    id: int
    type_id: int
    creation_date: datetime.datetime
    expiration_date: datetime.datetime
    price: int
    household: str
    income_id: int

    class Config:
        from_attributes = True


class PaymentTypeCreate(PaymentBase):
    rate: int
    active: bool


class PaymentType(PaymentBase):
    id: int
    rate: int
    active: bool

    class Config:
        from_attributes = True


class PaymentTypeModify(PaymentBase):
    id: int
    rate: int
    active: bool

    class Config:
        from_attributes = True


class PaymentModify(PaymentBase):
    id: int
    type_id: int
    creation_date: datetime.datetime
    expiration_date: datetime.datetime
    price: int
    household: str
    income_id: int

    class Config:
        from_attributes = True
