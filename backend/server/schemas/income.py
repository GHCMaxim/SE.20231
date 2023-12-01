import datetime
from pydantic import BaseModel


class IncomeBase(BaseModel):
    description: str


class IncomeCreate(IncomeBase):
    pass


class Income(IncomeBase):
    id: int
    total: int
    income_time: datetime.datetime
    total_income_id: int

    class Config:
        orm_mode = True


class IncomeTypeCreate(IncomeBase):
    pass


class IncomeType(IncomeBase):
    id: int
    total: int
    calc_date: datetime.datetime

    class Config:
        orm_mode = True
