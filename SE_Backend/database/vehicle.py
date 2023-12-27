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
