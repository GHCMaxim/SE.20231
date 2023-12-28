from datetime import datetime

from dateutil.relativedelta import relativedelta
from sqlalchemy import extract
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
    )

    db.add(db_income)
    db.commit()
    db.refresh(db_income)

    return db_income


def update_income(db: Session, id: int, income: schemas.income.IncomeUpdate):
    db.query(models.Income).filter(models.Income.id == id).update(income.model_dump())
    db.commit()

    return db.query(models.Income).filter(models.Income.id == income.id).first()


def count_income(db: Session):
    # Returns the total amount of Income last month, in millions, and percentage increase/decrease since the month before
    last_month = (
        db.query(models.TotalIncome)
        .filter(
            extract("month", models.TotalIncome.calc_date)
            == datetime.today() + relativedelta(months=-1)
        )
        .count()
    )
    last_last_month = (
        db.query(models.TotalIncome)
        .filter(
            extract("month", models.TotalIncome.calc_date)
            == datetime.today() + relativedelta(months=-2)
        )
        .count()
    )

    return [last_month, last_last_month]
