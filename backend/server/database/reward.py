from sqlalchemy.orm import Session

from .. import models


def get_reward(db: Session, id: int):
    return db.query(models.Reward).filter(models.Reward.id == id).first()


def get_rewards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reward).offset(skip).limit(limit).all()
