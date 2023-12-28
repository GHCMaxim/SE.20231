import datetime

from pydantic import BaseModel


class IncomeBase(BaseModel):
    description: str


class IncomeCreate(IncomeBase):
    total: int
    income_time: datetime.datetime


class Income(IncomeBase):
    id: int
    total: int
    income_time: datetime.datetime

    class Config:
        from_attributes = True


class IncomeUpdate(IncomeBase):
    id: int
    total: int
    income_time: datetime.datetime

    class Config:
        from_attributes = True
