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


@contributions.put("/api/contributions/{cccd}", response_model=schemas.contributions.ContributionsModify)
def put_contribution(
    cccd: str,
    contribution: schemas.contributions.ContributionsModify,
    db: Session=Depends(get_db)
):
    db_contribution = database.contributions.get_contribution(db, cccd=cccd)
    if db_contribution is None:
        raise HTTPException(status_code=404, detail="contribution not found.")
    return database.contributions.update_contributions(db, id=cccd, contribution=contribution)


@contributions.post("/api/contributions", response_model=schemas.contributions.ContributionsBase)
def post_contribution(contribution: schemas.contributions.ContributionsCreate, db: Session=Depends(get_db)):
    return database.contributions.create_contributions(db, contribution=contribution)
