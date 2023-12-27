from pydantic import BaseModel


class VehicleBase(BaseModel):
    license_plate: str
    vehicle_type: str
    owner: int


class VehicleCreate(VehicleBase):
    pass


class Vehicle(VehicleBase):
    pass

    class Config:
        from_attributes = True
