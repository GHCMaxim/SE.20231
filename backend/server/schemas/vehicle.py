from pydantic import BaseModel


class VehicleBase(BaseModel):
    license_plate: str
    vehicle_type: str
    owner: int


class VehicleCreate(BaseModel):
    pass


class Vehicle(BaseModel):
    pass

    class Config:
        orm_mode = True
