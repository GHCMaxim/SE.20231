from pydantic import BaseModel


class AwayBase(BaseModel):
    description: str


class AwayCreate(AwayBase):
    pass


class Away(AwayBase):
    id: int
    household_id: str
    away_type_id: int

    class Config:
        orm_mode = True


class AwayTypeCreate(AwayBase):
    pass


class AwayType(AwayBase):
    id: int
    name: str

    class Config:
        orm_mode = True
