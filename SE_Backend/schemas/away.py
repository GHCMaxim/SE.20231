from pydantic import BaseModel


class AwayBase(BaseModel):
    description: str


class AwayCreate(AwayBase):
    household_id: str
    away_type_id: int


class Away(AwayBase):
    id: int
    household_id: str
    away_type_id: int

    class Config:
        from_attributes = True


class AwayTypeCreate(AwayBase):
    name: str
    active: bool


class AwayModify(AwayBase):
    id: int
    household_id: str
    away_type_id: int
    class Config:
        from_attributes = True

class AwayType(AwayBase):
    id: int
    name: str
    active: bool

    class Config:
        from_attributes = True
