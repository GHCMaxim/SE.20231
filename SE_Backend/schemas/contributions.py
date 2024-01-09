import datetime

from pydantic import BaseModel


class ContributionsBase(BaseModel):
    id: str
    contributor: str
    amount: int
    description: str
    contribution_time: datetime.date


class ContributionsCreate(ContributionsBase):
    pass


class ContributionsModify(ContributionsBase):
    pass

    class Config:
        from_attributes = True
