from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

spendings = APIRouter(tags=["spendings"])


@spendings.get("/api/spendings", response_model=list[schemas.spending.Spending])
def get_spendings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    spendings = database.spending.get_spendings(db, skip=skip, limit=limit)
    return spendings


@spendings.get("/api/spendings/{id}", response_model=schemas.spending.Spending)
def get_spending(id: int, db: Session = Depends(get_db)):
    db_spending = database.spending.get_spending(db, id=id)
    if db_spending is None:
        raise HTTPException(status_code=404, detail="spending not found.")
    return db_spending


@spendings.post("/api/spendings", response_model=schemas.spending.Spending)
def post_spending(
    spending: schemas.spending.SpendingCreate, db: Session = Depends(get_db)
):
    return database.spending.create_spending(db, spending=spending)
