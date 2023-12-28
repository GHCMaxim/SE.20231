from pydantic import BaseModel


class RelationshipBase(BaseModel):
    cccd: str
    relationship: str
    birth_id: int
    alive: bool
    death_paper_id: int
    household_id: str


class RelationshipCreate(RelationshipBase):
    pass


class Relationship(RelationshipBase):
    pass

    class Config:
        from_attributes = True

class RelationshipModify(RelationshipBase):
    pass

    class Config:
        from_attributes = True