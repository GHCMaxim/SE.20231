from sqlalchemy.orm import Session
import uuid

from .. import models, schemas


def get_contribution(db: Session, id: str):
    return(
        db.query(models.Contributions)
        .filter(models.Contributions.contributor == id)
        .first()
    )


def get_contributions(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Contributions).offset(skip).limit(limit).all()


def create_contributions(
    db: Session, contribution: schemas.contributions.ContributionsCreate
):
    id = uuid.uuid4()
    db_contribution = models.Contributions(
        id=id,
        contributor=contribution.contributor,
        amount=contribution.amount,
        description=contribution.description,
        contribution_time=contribution.contribution_time,
    )

    db.add(db_contribution)
    db.commit()
    db.refresh(db_contribution)

    return db_contribution


def update_contributions(db: Session, id: str, contribution: schemas.contributions.ContributionsModify):
    db.query(models.Contributions).filter(models.Contributions.id == id).update(contribution.model_dump())
    db.commit()
    return db.query(models.Contributions).filter(models.Contributions.id == contribution.id).first()
