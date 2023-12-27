from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

relationships = APIRouter(tags=["relationships"])


@relationships.get(
    "/api/relationships", response_model=list[schemas.relationship.Relationship]
)
def get_relationships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    relationships = database.relationship.get_relationships(db, skip=skip, limit=limit)
    return relationships


@relationships.get(
    "/api/relationships/{id}", response_model=schemas.relationship.Relationship
)
def get_relationship(id: int, db: Session = Depends(get_db)):
    db_relationship = database.relationship.get_relationship(db, id=id)
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
