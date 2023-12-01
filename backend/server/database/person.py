import uuid
from sqlalchemy.orm import Session

from .. import models, schemas


def get_person(db: Session, cccd: str):
    return db.query(models.Person).filter(models.Person.cccd == cccd).first()


def get_people(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.person.PersonCreate):
    id = uuid.uuid4()
    db_person = models.Person(
        id=id,
        name=person.name,
        dob=person.dob,
        sex=person.sex,
        religion=person.religion,
        ethnicity=person.ethnicity,
        job=person.job,
        job_location=person.job_location,
        cccd=person.cccd,
    )

    db.add(db_person)
    db.commit()
    db.refresh(db_person)

    return db_person
