from pydantic import BaseModel


class BirthBase(BaseModel):
    book_number: str


class BirthCreate(BirthBase):
    pass


class Birth(BirthBase):
    id: str

    class Config:
        from_attributes = True
