import datetime
from pydantic import BaseModel


class RewardBase(BaseModel):
    reward_type_id: int
    date: datetime.date
    recipient: str
    spending_id: int


class RewardCreate(RewardBase):
    pass


class Reward(RewardBase):
    id: int

    class Config:
        orm_mode = True


class RewardTypeBase(BaseModel):
    name: str
    description: str


class RewardTypeCreate(RewardTypeBase):
    pass


class RewardType(RewardTypeBase):
    id: int

    class Config:
        orm_mode = True
