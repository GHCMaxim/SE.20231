import datetime

from pydantic import BaseModel


class ContributionsBase(BaseModel):
    id: str
    contributor: str
    amount: int
    description: str
    contribution_time: datetime.date
    contribution_event: int


class ContributionsCreate(ContributionsBase):
    contributor: str
    amount: int
    description: str
    contribution_time: datetime.date
    contribution_event: int


class ContributionsModify(ContributionsBase):
    pass

    class Config:
        from_attributes = True

class ContributionEventBase(BaseModel):
    id: int
    total_amount: int
    description: str
    event_time: datetime.date

class ContributionEventCreate(ContributionEventBase):
    pass

class ContributionEventModify(ContributionEventBase):
    pass

    class Config:
        from_attributes = True

class ContributionEventCount(BaseModel):
    event_time: datetime.date
    id: int
    description: str
    number_of_contributors: int
    total_amount: int
