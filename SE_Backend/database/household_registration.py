from sqlalchemy.orm import Session

from .. import models, schemas


def get_household_registration(db: Session, id: str):
    return (
        db.query(models.HouseholdRegistration)
        .filter(models.HouseholdRegistration.id == id)
        .first()
    )


def get_household_registrations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HouseholdRegistration).offset(skip).limit(limit).all()


def create_household_registration(
    db: Session, household: schemas.household_registration.HouseholdRegistrationCreate
):
    db_household = models.HouseholdRegistration(
        id=household.id,
        name=household.name,
        location=household.location,
        creation_date=household.creation_date,
        owner=household.owner,
        size=household.size,
        house_type=household.house_type,
    )

    db.add(db_household)
    db.commit()
    db.refresh(db_household)

    return db_household


def count_households(db: Session):
    return db.query(models.HouseholdRegistration).count()


def modify_household_registrations(
    db: Session,
    id: str,
    household: schemas.household_registration.HouseholdRegistrationModify,
):
    db.query(models.HouseholdRegistration).filter(
        models.HouseholdRegistration.id == id
    ).update(household.model_dump())
    db.commit()
    return (
        db.query(models.HouseholdRegistration)
        .filter(models.HouseholdRegistration.id == household.id)
        .first()
    )
