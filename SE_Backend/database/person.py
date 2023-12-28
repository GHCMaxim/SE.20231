import uuid
import datetime
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


def update_person(db: Session, person: schemas.person.PersonModify):
    db.query(models.Person).filter(models.Person.cccd == person.cccd).update(
        person.dict()
    )
    db.commit()

    return db.query(models.Person).filter(models.Person.cccd == person.cccd).first()


def count_people(db: Session):
    return db.query(models.Person).count()


def count_age(db: Session):
    # Count by age list: 0-10. 11-18, 19-30, 31-50, 51-70, 71+
    range = [0, 11, 19, 31, 51, 71]
    num = []
    for i in range:
        if range[-1] == i:
            num.append(
                db.query(models.Person)
                .filter(models.Person.dob.year < datetime.now().year - i)
                .count()
            )
        else:
            num.append(
                db.query(models.Person)
                .filter(
                    models.Person.dob.year < datetime.now().year - i,
                    models.Person.dob.year > datetime.now().year - i + 1,
                )
                .count()
            )
    return num


def count_gender(db: Session):
    range = ["M", "F"]
    num = []
    for i in range:
        num.append(db.query(models.Person).folter(models.Person.sex == i).count())
    return num
