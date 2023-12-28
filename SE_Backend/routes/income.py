from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

incomes = APIRouter(tags=["incomes"])


@incomes.get("/api/incomes", response_model=list[schemas.income.Income])
def get_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    incomes = database.income.get_incomes(db, skip=skip, limit=limit)
    return incomes


@incomes.get("/api/incomes/{id}", response_model=schemas.income.Income)
def get_income(id: int, db: Session = Depends(get_db)):
    db_income = database.income.get_income(db, id=id)
    if db_income is None:
        raise HTTPException(status_code=404, detail="income not found.")
    return db_income


@incomes.post("/api/incomes", response_model=schemas.income.Income)
def post_income(income: schemas.income.IncomeCreate, db: Session = Depends(get_db)):
    return database.income.create_income(db, income=income)


@incomes.get("/api/total_income", response_model=list[schemas.income.TotalIncome])
def get_total_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    total_income = database.income.get_total_incomes(db, skip=skip, limit=limit)
    return total_income


@incomes.get("/api/total_income/{cccd}", response_model=schemas.income.TotalIncome)
def get_total_income(id: int, db: Session = Depends(get_db)):
    db_total_income = database.income.get_total_income(db, id=id)
    if db_total_income is None:
        raise HTTPException(status_code=404, detail="total_income not found.")
    return db_total_income


@incomes.post("/api/total_income", response_model=schemas.income.TotalIncome)
def post_total_income(
    total_income: schemas.income.TotalIncomeCreate, db: Session = Depends(get_db)
):
    return database.income.create_total_income(db, total_income=total_income)


@incomes.put("/api/total_income/{id}", response_model=schemas.income.TotalIncome)
def put_income(
    id: int, total_income: schemas.income.IncomeUpdate, db: Session = Depends(get_db)
):
    db_total_income = database.income.get_total_income(db, id=id)
    if db_total_income is None:
        raise HTTPException(status_code=404, detail="total_income not found.")
    return database.income.update_total_income(db, total_income=total_income)
