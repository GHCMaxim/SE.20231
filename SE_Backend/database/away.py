from sqlalchemy.orm import Session

from .. import models, schemas


def get_away(db: Session, id: int):
    return db.query(models.Away).filter(models.Away.id == id).first()


def get_aways(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Away).offset(skip).limit(limit).all()


def get_aways_by_household(db: Session, household_id: str):
    return db.query(models.Away).filter(models.Away.household_id == household_id).all()


def get_aways_by_type(db: Session, away_type_id: int):
    return db.query(models.Away).filter(models.Away.away_type_id == away_type_id).all()


def create_away(db: Session, away: schemas.away.AwayCreate):
    db_away = models.Away(
        household_id=away.household_id,
        cccd=away.cccd,
        away_type_id=away.away_type_id,
        description=away.description,
    )

    db.add(db_away)
    db.commit()
    db.refresh(db_away)

    return db_away


def get_away_type(db: Session, id: int):
    return db.query(models.AwayType).filter(models.AwayType.id == id).first()


def get_away_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AwayType).offset(skip).limit(limit).all()


def create_away_type(db: Session, away_type: schemas.away.AwayTypeCreate):
    db_away_type = models.AwayType(
        name=away_type.name,
        description=away_type.description,
        active=away_type.active,
    )

    db.add(db_away_type)
    db.commit()
    db.refresh(db_away_type)

    return db_away_type


def put_away(id: int, away: schemas.away.AwayModify, db: Session):
    db.query(models.Away).filter(models.Away.id == away.id).update(away.dict())
    db.commit()

    return db.query(models.Away).filter(models.Away.id == away.id).first()
