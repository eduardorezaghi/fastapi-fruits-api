from enum import Enum
from pydantic import BaseModel, ConfigDict

class Status(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"

class FruitBase(BaseModel):
    name: str
    description: str | None = None

class FruitCreate(FruitBase):
    pass

class FruitCreatedResponse(FruitBase):
    model_config: dict = ConfigDict(from_attributes=True)
    
    id: int
    Status: Status

class GetFruitResponse(FruitBase):
    model_config: dict = ConfigDict(from_attributes=True)

    Status: Status
    id: int


class Fruit(FruitBase):
    model_config: dict = ConfigDict(from_attributes=True)

    id: int

