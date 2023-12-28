from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import get_db
from .. import schemas, database

rewards = APIRouter(tags=["rewards"])


@rewards.get("/api/rewards", response_model=list[schemas.reward.Reward])
def get_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rewards = database.reward.get_rewards(db, skip=skip, limit=limit)
    return rewards


@rewards.get("/api/rewards/{id}", response_model=schemas.reward.Reward)
def get_reward(id: int, db: Session = Depends(get_db)):
    db_reward = database.reward.get_reward(db, id=id)
    if db_reward is None:
        raise HTTPException(status_code=404, detail="reward not found.")
    return db_reward


@rewards.post("/api/rewards", response_model=schemas.reward.Reward)
def post_reward(reward: schemas.reward.RewardCreate, db: Session = Depends(get_db)):
    return database.reward.create_reward(db, reward=reward)


@rewards.get("/api/reward_types", response_model=list[schemas.reward.RewardType])
def get_reward_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reward_types = database.reward.get_reward_types(db, skip=skip, limit=limit)
    return reward_types


@rewards.get("/api/reward_types/{id}", response_model=schemas.reward.RewardType)
def get_reward_type(id: int, db: Session = Depends(get_db)):
    db_reward_type = database.reward.get_reward_type(db, id=id)
    if db_reward_type is None:
        raise HTTPException(status_code=404, detail="reward type not found.")
    return db_reward_type


@rewards.post("/api/rewards_types", response_model=schemas.reward.RewardType)
def post_reward_type(
    reward_type: schemas.reward.RewardTypeCreate, db: Session = Depends(get_db)
):
    return database.reward.create_reward_type(db, reward_type=reward_type)


@rewards.put("/api/rewards/{id}", response_model=schemas.reward.Reward)
def put_reward(
    id: int, reward: schemas.reward.RewardModify, db: Session = Depends(get_db)
):
    db_reward = database.reward.get_reward(db, id=id)
    if db_reward is None:
        raise HTTPException(status_code=404, detail="reward not found.")
    return database.reward.update_reward(db, reward=reward)


@rewards.put("/api/reward_types/{id}", response_model=schemas.reward.RewardType)
def put_reward_type(
    id: int, reward_type: schemas.reward.RewardTypeModify, db: Session = Depends(get_db)
):
    db_reward_type = database.reward.get_reward_type(db, id=id)
    if db_reward_type is None:
        raise HTTPException(status_code=404, detail="reward type not found.")
    return database.reward.update_reward_type(db, reward_type=reward_type)
