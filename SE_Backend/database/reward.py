import datetime

from sqlalchemy.orm import Session

from .. import models, schemas


def get_reward(db: Session, id: int):
    return db.query(models.Reward).filter(models.Reward.id == id).first()


def get_rewards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reward).offset(skip).limit(limit).all()


def create_reward(db: Session, reward: schemas.reward.RewardCreate):
    db_reward = models.Reward(
        reward_type_id=reward.reward_type_id,
        date=reward.date,
        recipient=reward.recipient,
        spending_id=reward.spending_id,
    )

    db.add(db_reward)
    db.commit()
    db.refresh(db_reward)

    return db_reward


def get_reward_type(db: Session, id: int):
    return db.query(models.RewardType).filter(models.RewardType.id == id).first()


def get_reward_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RewardType).offset(skip).limit(limit).all()


def create_reward_type(db: Session, reward_type: schemas.reward.RewardTypeCreate):
    db_reward_type = models.RewardType(
        name=reward_type.name,
        description=reward_type.description,
        active=reward_type.active,
    )

    db.add(db_reward_type)
    db.commit()
    db.refresh(db_reward_type)

    return db_reward_type


def update_reward_type(db: Session, reward_type: schemas.reward.RewardTypeModify):
    db.query(models.RewardType).filter(models.RewardType.id == reward_type.id).update(
        reward_type.dict()
    )
    db.commit()
    return (
        db.query(models.RewardType)
        .filter(models.RewardType.id == reward_type.id)
        .first()
    )


def update_reward(db: Session, reward: schemas.reward.RewardModify):
    db.query(models.Reward).filter(models.Reward.id == reward.id).update(reward.dict())
    db.commit()
    return db.query(models.Reward).filter(models.Reward.id == reward.id).first()


def count_rewards(db: Session):
    # Returns the number of rewards in the current year
    return (
        db.query(models.Reward)
        .filter(models.Reward.date.year == datetime.now().year)
        .count()
    )
