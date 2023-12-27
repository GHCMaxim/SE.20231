from sqlalchemy.orm import Session

from .. import models, schemas


def get_spending(db: Session, id: int):
    return db.query(models.Spending).filter(models.Spending.id == id).first()


def get_spendings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Spending).offset(skip).limit(limit).all()


def create_spending(db: Session, spending: schemas.spending.SpendingCreate):
    db_spending = models.Spending(
        description=spending.description,
        total=spending.total,
        date=spending.date,
        total_id=spending.total_id,
    )

    db.add(db_spending)
    db.commit()
    db.refresh(db_spending)

    return db_spending
