from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import get_db

from .. import schemas, database

vehicles = APIRouter(tags=["vehicles"])


@vehicles.get("/api/vehicles", response_model=list[schemas.vehicle.Vehicle])
def get_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicles = database.vehicle.get_vehicles(db, skip=skip, limit=limit)
    return vehicles


@vehicles.get("/api/vehicles/count", response_model=list[schemas.vehicle.VehicleCount])
def count_vehicles_per_household(db: Session = Depends(get_db)):
    return database.vehicle.count_vehicles_per_household(db)

@vehicles.get("/api/vehicles/find/{license_plate}", response_model=schemas.vehicle.Vehicle)
def get_vehicle(license_plate: str, db: Session = Depends(get_db)):
    db_vehicle = database.vehicle.get_vehicle(db, license_plate=license_plate)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="vehicle not found.")
    return db_vehicle


@vehicles.post("/api/vehicles", response_model=schemas.vehicle.Vehicle)
def post_vehicle(vehicle: schemas.vehicle.VehicleCreate, db: Session = Depends(get_db)):
    return database.vehicle.create_vehicle(db, vehicle=vehicle)
