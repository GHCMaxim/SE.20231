from sqlalchemy.orm import Session

from .. import models, schemas


def get_birth(db: Session, id: int):
    return db.query(models.Birth).filter(models.Birth.id == id).first()


def get_births(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Birth).offset(skip).limit(limit).all()


def get_birth_by_book_number(db: Session, book_number: int):
    return (
        db.query(models.Birth).filter(models.Birth.book_number == book_number).first()
    )


def create_birth(db: Session, birth: schemas.birth.BirthCreate):
    db_birth = models.birth.Birth(book_number=birth.book_number)

    db.add(db_birth)
    db.commit()
    db.refresh(db_birth)

    return db_birth
