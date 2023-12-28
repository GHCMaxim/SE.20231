from sqlalchemy.orm import Session

from .. import models, schemas


def get_relationship(db: Session, id: int):
    return db.query(models.Relationship).filter(models.Relationship.id == id).first()


def get_relationships(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Relationship).offset(skip).limit(limit).all()


def create_relationship(
    db: Session, relationship: schemas.relationship.RelationshipCreate
):
    db_relationship = models.Relationship(
        cccd=relationship.cccd,
        relationship=relationship.relationship,
        birth_id=relationship.birth_id,
        alive=relationship.alive,
        death_paper_id=relationship.death_paper_id,
        household_id=relationship.household_id,
    )

    db.add(db_relationship)
    db.commit()
    db.refresh(db_relationship)

    return db_relationship

def put_relationship(cccd: int, relationship: schemas.relationship.RelationshipModify, db: Session):
    db.query(models.Relationship).filter(models.Relationship.cccd == cccd).update(relationship.dict())
    db.commit()
    return db.query(models.Relationship).filter(models.Relationship.cccd == cccd).first()