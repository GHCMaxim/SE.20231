import datetime
from pydantic import BaseModel


class IncomeBase(BaseModel):
    description: str


class IncomeCreate(IncomeBase):
    total: int
    income_time: datetime.date


class Income(IncomeBase):
    id: int
    total: int
    income_time: datetime.date

    class Config:
        from_attributes = True


class TotalIncomeCreate(IncomeBase):
    total: int
    calc_date: datetime.date


class TotalIncome(IncomeBase):
    id: int
    total: int
    calc_date: datetime.date

    class Config:
        from_attributes = True


class IncomeUpdate(IncomeBase):
    id: int
    total: int
    income_time: datetime.date

    class Config:
        from_attributes = True