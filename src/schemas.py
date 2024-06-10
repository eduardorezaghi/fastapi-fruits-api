from enum import Enum
from pydantic import BaseModel

class Status(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"

class FruitBase(BaseModel):
    name: str
    description: str | None = None

class FruitCreate(FruitBase):
    pass

class FruitCreatedResponse(FruitBase):
    id: int
    Status: Status

    class Config:
        orm_mode = True

class GetFruitResponse(FruitBase):
    Status: Status
    id: int
    
    class Config:
        orm_mode = True

class Fruit(FruitBase):
    id: int

    class Config:
        orm_mode = True
