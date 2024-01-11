from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from .. import schemas, database

relationships = APIRouter(tags=["relationships"])


@relationships.get(
    "/api/relationships", response_model=list[schemas.relationship.Relationship]
)
def get_relationships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_relationships = database.relationship.get_relationships(
        db, skip=skip, limit=limit
    )
    return db_relationships


@relationships.get(
    "/api/relationships/{cccd}", response_model=schemas.relationship.Relationship
)
def get_relationship(cccd: str, db: Session = Depends(get_db)):
    db_relationship = database.relationship.get_relationship(db, cccd=cccd)
    if db_relationship is None:
        raise HTTPException(status_code=404, detail="relationship not found.")
    return db_relationship


@relationships.post(
    "/api/relationships", response_model=schemas.relationship.Relationship
)
def post_relationship(
    relationship: schemas.relationship.RelationshipCreate, db: Session = Depends(get_db)
):
    return database.relationship.create_relationship(db, relationship=relationship)


@relationships.put(
    "/api/relationships/{cccd}", response_model=schemas.relationship.RelationshipModify
)
def update_relationship(
    cccd: str,
    relationship: schemas.relationship.RelationshipModify,
    db: Session = Depends(get_db),
):
    db_relationship = database.relationship.get_relationship(db, cccd=cccd)
    if db_relationship is None:
        raise HTTPException(status_code=404, detail="relationship not found.")
    return database.relationship.put_relationship(db, cccd, relationship=relationship)

@relationships.get("/api/relationships/household/{household_id}", response_model=list[schemas.relationship.Relationship])
def get_people_in_household(household_id: str, db: Session = Depends(get_db)):
    db_people = database.relationship.get_people_in_household(db, household_id=household_id)
    if db_people is None:
        raise HTTPException(status_code=404, detail="household not found.")
    return db_people