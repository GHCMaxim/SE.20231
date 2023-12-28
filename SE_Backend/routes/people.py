from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from .. import schemas, database

people = APIRouter(tags=["people"])


@people.get("/api/people", response_model=list[schemas.person.Person])
def get_people(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    people = database.person.get_people(db, skip=skip, limit=limit)
    return people


@people.get("/api/people/{cccd}", response_model=schemas.person.Person)
def get_person(cccd: str, db: Session = Depends(get_db)):
    db_person = database.person.get_person(db, cccd=cccd)
    if db_person is None:
        raise HTTPException(status_code=404, detail="person not found.")
    return db_person


@people.post("/api/people", response_model=schemas.person.Person)
def post_person(person: schemas.person.PersonCreate, db: Session = Depends(get_db)):
    db_user = database.person.get_person(db, cccd=person.cccd)
    if db_user:
        raise HTTPException(status_code=400, detail="person already registered.")
    return database.person.create_person(db, person=person)


@people.put("/api/people/{cccd}", response_model=schemas.person.Person)
def put_person(
    cccd: str, person: schemas.person.PersonModify, db: Session = Depends(get_db)
):
    db_user = database.person.get_person(db, cccd=cccd)
    if not db_user:
        raise HTTPException(status_code=404, detail="person not found.")
    return database.person.update_person(db, cccd, person=person)
