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

class VehicleCount(BaseModel):
    owner : str
    count_type_1 : int
    count_type_2 : int

class VehicleModify(VehicleBase):
    pass 
    class Config:
        orm_mode = True