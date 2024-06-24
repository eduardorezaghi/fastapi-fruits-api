from enum import Enum
from pydantic import BaseModel, ConfigDict

class Status(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"

class FlavorVariation(Enum):
    CITRIC = "Citric"
    SWEET = "Sweet"
    SOUR = "Sour"
    BITTER = "Bitter"
    TANGY = "Tangy"

class FruitBase(BaseModel):
    name: str
    description: str | None = None
    flavor_variation: FlavorVariation

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

