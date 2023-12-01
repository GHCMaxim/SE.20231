from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

rewards = APIRouter(tags=["rewards"])


@rewards.get("/api/rewards", response_model=schemas.person.Person)
def get_rewards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rewards = database.reward.get_rewards(db, skip=skip, limit=limit)
    return rewards


@rewards.get("/api/rewards/{id}", response_model=schemas.person.Person)
def get_reward(id: int, db: Session = Depends(get_db)):
    db_reward = database.reward.get_reward(db, id=id)
    if db_reward is None:
        raise HTTPException(status_code=404, detail="reward not found.")
    return db_reward
