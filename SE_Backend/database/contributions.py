from sqlalchemy.orm import Session
import time
from sqlalchemy.sql.functions import func
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
    db: Session, contribution: schemas.contributions.ContributionsCreate, contribution_event: schemas.contributions.ContributionEventBase
):
    id = int(time.time()*1000)
    db_contribution = models.Contributions(
        id=id,
        contributor=contribution.contributor,
        amount=contribution.amount,
        description=contribution.description,
        contribution_time=contribution.contribution_time,
        contribution_event=contribution.contribution_event,
    )

    event = db.query(models.ContributionEvent).filter(models.ContributionEvent.id == contribution.contribution_event).first()
    event.total_amount += contribution.amount
    db.query(models.ContributionEvent).filter(models.ContributionEvent.id == contribution.contribution_event).update(event.model_dump())
    db.add(db_contribution)
    db.commit()
    db.refresh(db_contribution)

    return db_contribution


def update_contributions(db: Session, id: str, contribution: schemas.contributions.ContributionsModify):
    db.query(models.Contributions).filter(models.Contributions.id == id).update(contribution.model_dump())
    db.commit()
    return db.query(models.Contributions).filter(models.Contributions.id == contribution.id).first()


def get_contribution_event(db: Session, id: int):
    return db.query(models.ContributionEvent).filter(models.ContributionEvent.id == id).first()

def get_contribution_events(db: Session, skip: int=0, limit: int=100):
    return db.query(models.ContributionEvent).offset(skip).limit(limit).all()

def create_contribution_event(db: Session, contribution_event: schemas.contributions.ContributionEventCreate):
    db_contribution_event = models.ContributionEvent(
        id = contribution_event.id,
        total_amount=0,
        description=contribution_event.description,
        event_time=contribution_event.event_time,
    )

    db.add(db_contribution_event)
    db.commit()
    db.refresh(db_contribution_event)

    return db_contribution_event

def modify_contribution_event(db: Session, id: int, contribution_event: schemas.contributions.ContributionEventModify):
    db.query(models.ContributionEvent).filter(models.ContributionEvent.id == id).update(contribution_event.model_dump())
    db.commit()
    return db.query(models.ContributionEvent).filter(models.ContributionEvent.id == contribution_event.id).first()

def get_contribution_events_info(db:Session, contribution_event: schemas.contributions.ContributionEventBase):
    return db.query(models.ContributionEvent.event_time,
                    models.ContributionEvent.id,
                    models.ContributionEvent.description,
                    func.count(models.Contributions.contributor).label("number_of_contributors"),
                    func.sum(models.Contributions.amount).label("total_amount")).filter(models.Contributions.contribution_event == contribution_event.id).group_by(models.Contributions.contribution_event).all()


