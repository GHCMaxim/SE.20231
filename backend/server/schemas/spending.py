import datetime
from pydantic import BaseModel


class SpendingBase(BaseModel):
    description: str
    total: int
    date: datetime.date
    total_id: int


class SpendingCreate(SpendingBase):
    pass


class Spending(SpendingBase):
    id: int

    class Config:
        orm_mode = True
