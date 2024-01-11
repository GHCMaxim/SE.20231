from sqlalchemy import func, select
from sqlalchemy.sql import label
from sqlalchemy.orm import Session


from .. import models, schemas


def get_vehicle(db: Session, license_plate: str):
    return (
        db.query(models.Vehicle)
        .filter(models.Vehicle.license_plate == license_plate)
        .first()
    )


def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicle).offset(skip).limit(limit).all()


def create_vehicle(db: Session, vehicle: schemas.vehicle.VehicleCreate):
    db_vehicle = models.Vehicle(
        license_plate=vehicle.license_plate,
        vehicle_type=vehicle.vehicle_type,
        owner=vehicle.owner,
    )

    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle

def delete_vehicle(db: Session, license_plate: str):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.license_plate == license_plate).first()
    db.delete(db_vehicle)

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def modify_vehicle(db: Session, license_plate: str, vehicle: schemas.vehicle.VehicleModify):
    db_vehicle = db.query(models.Vehicle).filter(models.Vehicle.license_plate == license_plate).first()
    db_vehicle.license_plate = vehicle.license_plate
    db_vehicle.vehicle_type = vehicle.vehicle_type
    db_vehicle.owner = vehicle.owner

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def count_vehicles_per_household(db: Session):
    return db.query(
        models.vehicle.Vehicle.owner,
        label("count_type_1", func.count(models.vehicle.Vehicle.vehicle_type == "1")),
        label("count_type_2", func.count(models.vehicle.Vehicle.vehicle_type == "2"))
    ).group_by(models.vehicle.Vehicle.owner).all()
