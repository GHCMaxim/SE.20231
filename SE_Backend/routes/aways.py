from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

aways = APIRouter(tags=["aways"])


@aways.get("/api/aways", response_model=list[schemas.away.Away])
def get_aways(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    aways = database.away.get_aways(db, skip=skip, limit=limit)
    return aways


@aways.get("/api/aways/{id}", response_model=schemas.away.Away)
def get_away(id: int, db: Session = Depends(get_db)):
    db_away = database.away.get_away(db, id=id)
    if db_away is None:
        raise HTTPException(status_code=404, detail="away not found.")
    return db_away


@aways.get("/api/aways/by_household/{household_id}", response_model=schemas.away.Away)
def get_aways_by_household(household_id: str, db: Session = Depends(get_db)):
    db_aways = database.away.get_aways_by_household(db, household_id=household_id)
    return db_aways


@aways.get("/api/aways/by_household/{household_id}", response_model=schemas.away.Away)
def get_aways_by_type(away_type_id: int, db: Session = Depends(get_db)):
    db_aways = database.away.get_aways_by_type(db, away_type_id=away_type_id)
    return db_aways


@aways.post("/api/aways", response_model=schemas.away.Away)
def post_away(away: schemas.away.AwayCreate, db: Session = Depends(get_db)):
    return database.away.create_away(db, away=away)


@aways.get("/api/away_types", response_model=list[schemas.away.AwayType])
def get_away_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    away_types = database.away.get_away_types(db, skip=skip, limit=limit)
    return away_types


@aways.get("/api/away_types/{id}", response_model=schemas.away.AwayType)
def get_away_type(id: int, db: Session = Depends(get_db)):
    db_away_type = database.away.get_away_type(db, id=id)
    if db_away_type is None:
        raise HTTPException(status_code=404, detail="away type not found.")
    return db_away_type


@aways.post("/api/aways", response_model=schemas.away.AwayType)
def post_away_type(
    away_type: schemas.away.AwayTypeCreate, db: Session = Depends(get_db)
):
    return database.away.create_away_type(db, away_type=away_type)

@aways.put("/api/aways/{id}", response_model=schemas.away.Away)
def put_away(id: int, away: schemas.away.AwayModify, db: Session = Depends(get_db)):
    db_away = database.away.get_away(db, id=away.id)
    if db_away is None:
        raise HTTPException(status_code=404, detail="away not found.")
    return database.away.put_away(db, away=away)