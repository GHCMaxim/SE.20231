from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

contributions = APIRouter(tags=["contributions"])


@contributions.get("/api/contributions", response_model=list[schemas.contributions.ContributionsBase])
def get_contributions(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    contributions = database.contributions.get_contributions(db, skip=skip, limit=limit)
    return contributions

    
@contributions.get("/api/contributions/{cccd}", response_model=schemas.contributions.ContributionsBase)
def get_contribution(cccd: str, db: Session=Depends(get_db)):
    db_contribution = database.contributions.get_contribution(db, cccd=cccd)
    if db_contribution is None:
        raise HTTPException(status_code=404, detail="contribution not found.")
    return db_contribution


@contributions.put("/api/contributions/{id}", response_model=schemas.contributions.ContributionsModify)
def put_contribution(
    id: str,
    contribution: schemas.contributions.ContributionsModify,
    db: Session=Depends(get_db)
):
    db_contribution = database.contributions.get_contribution(db, id=id)
    if db_contribution is None:
        raise HTTPException(status_code=404, detail="contribution not found.")
    return database.contributions.update_contributions(db, id=id, contribution=contribution)


@contributions.post("/api/contributions", response_model=schemas.contributions.ContributionsBase)
def post_contribution(contribution: schemas.contributions.ContributionsCreate, db: Session=Depends(get_db)):
    return database.contributions.create_contributions(db, contribution=contribution)

@contributions.post("/api/contribution_events", response_model=schemas.contributions.ContributionEventBase)
def post_contribution_event(contribution_event: schemas.contributions.ContributionEventCreate, db: Session=Depends(get_db)):
    return database.contributions.create_contribution_event(db, contribution_event=contribution_event)

@contributions.get("/api/contribution_events", response_model=list[schemas.contributions.ContributionEventBase])
def get_contribution_events(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return database.contributions.get_contribution_events(db, skip=skip, limit=limit)

@contributions.get("/api/contribution_events/{id}", response_model=schemas.contributions.ContributionEventBase)
def get_contribution_event(id: int, db: Session=Depends(get_db)):
    db_contribution_event = database.contributions.get_contribution_event(db, id=id)
    if db_contribution_event is None:
        raise HTTPException(status_code=404, detail="contribution event not found.")
    return db_contribution_event

@contributions.put("/api/contribution_events/{id}", response_model=schemas.contributions.ContributionEventModify)
def put_contribution_event(id: int, contribution_event: schemas.contributions.ContributionEventModify, db: Session=Depends(get_db)):
    db_contribution_event = database.contributions.get_contribution_event(db, id=id)
    if db_contribution_event is None:
        raise HTTPException(status_code=404, detail="contribution event not found.")
    return database.contributions.update_contribution_event(db, id=id, contribution_event=contribution_event)

@contributions.get("/api/contribution_events_count",response_model=schemas.contributions.ContributionEventCount)
def get_contribution_events_count(db: Session=Depends(get_db)):
    return database.contributions.get_contribution_events_info(db)