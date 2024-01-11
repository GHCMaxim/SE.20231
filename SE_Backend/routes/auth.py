from datetime import datetime, timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt

from .. import database, schemas
from ..schemas.auth import Token
from ..config import config
from ..routes import get_db

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

auth = APIRouter(tags=["auth"])


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)
    return encoded_jwt


@auth.post("/api/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    db_user = database.user.get_user_by_username(db, username=form_data.username)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found.")
    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="incorrect username or password.")

    access_token_expires = timedelta(minutes=float(config.access_token_expire_minutes))
    access_token = create_access_token(
        {"sub": db_user.username, "role": db_user.permissions, "name": db_user.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth.post("/api/users", response_model=schemas.user.User)
async def register(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    return database.user.create_user(db, user=user)
