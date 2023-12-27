import uuid
from argon2 import PasswordHasher
from sqlalchemy.orm import Session

from .. import models, schemas


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.user.UserCreate):
    ph = PasswordHasher()
    hashed_password = ph.hash(user.password)
    db_user = models.User(
        address=user.address,
        name=user.name,
        sex=user.sex,
        cccd=user.cccd,
        job=user.job,
        username=user.username,
        password=hashed_password,
        permissions=user.permissions,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
