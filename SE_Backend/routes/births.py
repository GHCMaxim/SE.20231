from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

births = APIRouter(tags=["births"])


@births.get("/api/births", response_model=list[schemas.birth.Birth])
def get_births(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    births = database.birth.get_births(db, skip=skip, limit=limit)
    return births


@births.get("/api/births/{id}", response_model=schemas.birth.Birth)
def get_birth(id: int, db: Session = Depends(get_db)):
    db_birth = database.birth.get_birth(db, id=id)
    if db_birth is None:
        raise HTTPException(status_code=404, detail="birth not found.")
    return db_birth


@births.get(
    "/api/births/by_book_number/{book_number}", response_model=schemas.birth.Birth
)
def get_birth_by_book_number(book_number: int, db: Session = Depends(get_db)):
    db_birth = database.birth.get_birth_by_book_number(db, book_number=book_number)
    if db_birth is None:
        raise HTTPException(status_code=404, detail="birth not found.")
    return db_birth


@births.post("/api/births", response_model=schemas.birth.Birth)
def post_birth(birth: schemas.birth.BirthCreate, db: Session = Depends(get_db)):
    return database.birth.create_birth(db, birth=birth)
