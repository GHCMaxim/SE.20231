from pydantic import BaseModel


class HouseholdRegistrationBase(BaseModel):
    id: str
    name: str
    location: str
    creation_date: str


class HouseholdRegistrationCreate(HouseholdRegistrationBase):
    pass


class HouseholdRegistration(HouseholdRegistrationBase):
    pass

    class Config:
        from_attributes = True
