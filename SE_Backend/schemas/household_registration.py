from pydantic import BaseModel


class HouseholdRegistrationBase(BaseModel):
    id: str
    name: str
    location: str
    creation_date: str
    owner: str


class HouseholdRegistrationCreate(HouseholdRegistrationBase):
    pass


class HouseholdRegistration(HouseholdRegistrationBase):
    pass

    class Config:
        from_attributes = True


class HouseholdRegistrationModify(HouseholdRegistrationBase):
    pass

    class Config:
        from_attributes = True
