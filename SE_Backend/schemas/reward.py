import datetime
import uuid

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
        from_attributes = True


class RewardTypeBase(BaseModel):
    name: str
    description: str
    active: bool


class RewardTypeCreate(RewardTypeBase):
    pass


class RewardType(RewardTypeBase):
    id: int

    class Config:
        from_attributes = True


class RewardTypeModify(RewardTypeBase):
    id: int
    name: str
    description: str
    active: bool

    class Config:
        from_attributes = True


class RewardModify(RewardBase):
    id: int

    class Config:
        from_attributes = True
