import datetime

from pydantic import BaseModel


class SpendingBase(BaseModel):
    description: str
    total: int
    date: datetime.date
    household_id: str
    total_id: int


class SpendingCreate(SpendingBase):
    pass


class Spending(SpendingBase):
    id: int

    class Config:
        from_attributes = True
