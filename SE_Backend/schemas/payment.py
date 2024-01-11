import datetime
from pydantic import BaseModel


class PaymentBase(BaseModel):
    name: str


class PaymentCreate(PaymentBase):
    type_id: int
    creation_date: datetime.date
    expiration_date: datetime.date
    price: int
    household: str
    income_id: int
    paid: bool


class Payment(PaymentBase):
    id: int
    type_id: int
    creation_date: datetime.date
    price: int
    household: str
    income_id: int
    paid: bool

    class Config:
        from_attributes = True


class PaymentTypeCreate(PaymentBase):
    rate: int
    active: bool


class PaymentType(PaymentBase):
    id: int
    name: str
    rate: int
    active: bool

    class Config:
        from_attributes = True


class PaymentTypeModify(PaymentBase):
    id: int
    name: str
    rate: int
    active: bool

    class Config:
        from_attributes = True


class PaymentModify(PaymentBase):
    id: int
    type_id: int
    creation_date: datetime.date
    expiration_date: datetime.date
    price: int
    household: str
    income_id: int

    class Config:
        from_attributes = True

class PaymentVehicle(BaseModel):
    household: str
    vehicle_count_type1: int
    vehicle_count_type2: int
    price: int
    paid: bool

class PaymentHouse(BaseModel):
    household: str
    house_type: int
    size: int
    price: int
    paid: bool

class PaymentHousehold(BaseModel):
    household: str
    vehicle_payment: bool
    house_payment: bool
    service_payment: bool
    total_payment: int
    total_paid: int

class PaymentService(BaseModel):
    household: str
    service_payment: int
    paid: bool
