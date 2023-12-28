import uuid
from datetime import datetime

from sqlalchemy import extract
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
        phone_number=person.phone_number,
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


def update_person(db: Session, cccd: str, person: schemas.person.PersonModify):
    db.query(models.Person).filter(models.Person.cccd == cccd).update(
        person.model_dump()
    )
    db.commit()

    return db.query(models.Person).filter(models.Person.cccd == person.cccd).first()


def count_people(db: Session):
    return db.query(models.Person).count()


def count_age(db: Session):
    # Count by age list: 0-10. 11-18, 19-30, 31-50, 51-70, 71+
    age_range = [0, 11, 19, 31, 51, 71]
    num = []
    for i, n in enumerate(age_range):
        if age_range[-1] == n:
            num.append(
                db.query(models.Person)
                .filter(extract("year", models.Person.dob) < datetime.now().year - n)
                .count()
            )
        else:
            num.append(
                db.query(models.Person)
                .filter(
                    (
                        extract("year", models.Person.dob)
                        < datetime.now().year - age_range[i]
                    )
                    & (
                        extract("year", models.Person.dob)
                        > datetime.now().year - age_range[i + 1]
                    )
                )
                .count()
            )
    return num


def count_gender(db: Session):
    num = [
        db.query(models.Person)
        .filter((models.Person.sex == "M") | (models.Person.sex == "F"))
        .count()
    ]
    return num
