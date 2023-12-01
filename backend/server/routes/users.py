import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

users = APIRouter(tags=["users"])


@users.get("/api/users", response_model=schemas.user.User)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = database.user.get_users(db, skip=skip, limit=limit)
    return users


@users.get("/api/users/{user_id}", response_model=schemas.user.User)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = database.user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found.")
    return db_user
