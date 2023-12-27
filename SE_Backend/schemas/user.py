import uuid
from pydantic import BaseModel


class UserBase(BaseModel):
    address: str
    name: str
    sex: str
    cccd: str
    job: str
    username: str
    permissions: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
