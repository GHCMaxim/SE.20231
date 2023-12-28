import datetime
import uuid
from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str
    dob: datetime.date
    sex: str
    phone_number: str
    religion: str
    ethnicity: str
    job: str
    job_location: str
    cccd: str


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: uuid.UUID

    class Config:
        from_attributes = True


class PersonModify(PersonBase):
    pass
