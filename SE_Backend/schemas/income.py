import datetime
from pydantic import BaseModel


class IncomeBase(BaseModel):
    description: str


class IncomeCreate(IncomeBase):
    total: int
    income_time: datetime.datetime
    total_income_id: int


class Income(IncomeBase):
    id: int
    total: int
    income_time: datetime.datetime
    total_income_id: int

    class Config:
        from_attributes = True


class TotalIncomeCreate(IncomeBase):
    total: int
    calc_date: datetime.datetime


class TotalIncome(IncomeBase):
    id: int
    total: int
    calc_date: datetime.datetime

    class Config:
        from_attributes = True
