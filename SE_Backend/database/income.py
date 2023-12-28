import datetime
from sqlalchemy.orm import Session

from .. import models, schemas


def get_income(db: Session, id: int):
    return db.query(models.Income).filter(models.Income.id == id).first()


def get_incomes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Income).offset(skip).limit(limit).all()


def create_income(db: Session, income: schemas.income.IncomeCreate):
    db_income = models.income.Income(
        total=income.total,
        income_time=income.income_time,
        total_income_id=income.total_income_id,
    )

    db.add(db_income)
    db.commit()
    db.refresh(db_income)

    return db_income


def get_total_income(db: Session, id: int):
    return db.query(models.TotalIncome).filter(models.TotalIncome.id == id).first()


def get_total_incomes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TotalIncome).offset(skip).limit(limit).all()


def create_total_income(db: Session, total_income: schemas.income.TotalIncomeCreate):
    db_total_income = models.income.Income(
        total=total_income.total,
        calc_date=total_income.calc_date,
    )

    db.add(db_total_income)
    db.commit()
    db.refresh(db_total_income)

    return db_total_income

def update_income(db: Session, income: schemas.income.IncomeUpdate):
    db.query(models.Income).filter(models.Income.id == income.id).update(income.dict())
    db.commit()
    
    return db.query(models.Income).filter(models.Income.id == income.id).first()

def count_income(db: Session):
    # Returns the total amount of Income last month, in millions, and percentage increase/decrease since the month before
    return list(db.query(models.TotalIncome).filter(models.TotalIncome.calc_date.month == datetime.now() - datetime.timedelta(months=1))/1000000,
                db.query(models.TotalIncome).filter(models.TotalIncome.calc_date.month == datetime.now() - datetime.timedelta(months=1))/db.query(models.TotalIncome).filter(models.TotalIncome.calc_date.month == datetime.now() - datetime.timedelta(months=2))-1)
