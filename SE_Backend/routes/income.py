from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from .. import schemas, database

incomes = APIRouter(tags=["incomes"])


@incomes.get("/api/incomes", response_model=list[schemas.income.Income])
def get_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_incomes = database.income.get_incomes(db, skip=skip, limit=limit)
    return db_incomes


@incomes.get("/api/incomes/{id}", response_model=schemas.income.Income)
def get_income(id: int, db: Session = Depends(get_db)):
    db_income = database.income.get_income(db, id=id)
    if db_income is None:
        raise HTTPException(status_code=404, detail="income not found.")
    return db_income


@incomes.post("/api/incomes", response_model=schemas.income.Income)
def post_income(income: schemas.income.IncomeCreate, db: Session = Depends(get_db)):
    return database.income.create_income(db, income=income)


@incomes.put("/api/incomes/{id}", response_model=schemas.income.Income)
def put_income(
    id: int, income: schemas.income.IncomeUpdate, db: Session = Depends(get_db)
):
    db_total_income = database.income.get_income(db, id=id)
    if db_total_income is None:
        raise HTTPException(status_code=404, detail="income not found.")
    return database.income.update_income(db, id, income=income)
