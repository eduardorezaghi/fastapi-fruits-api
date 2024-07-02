from enum import Enum
from pydantic import BaseModel, ConfigDict, Field

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
    model_config: dict = ConfigDict(
        from_attributes=True,
        json_schema_extra= dict(
            example={
                "name": "Apple",
                "description": "A fruit that is red or green in color",
                "flavor_variation": FlavorVariation.SWEET
            }
        )
    )

    name: str
    description: str | None = None
    flavor_variation: FlavorVariation

class Fruit(FruitBase):
    model_config: dict = ConfigDict(from_attributes=True)

    id: int

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

class GetFruitsResponse(BaseModel):
    model_config: dict = ConfigDict(
        from_attributes=True,
        json_schema_extra= dict(
            example={
                "Status": "Success",
                "fruits": [
                    {
                        "name": "Apple",
                        "description": "A fruit that is red or green in color",
                        "flavor_variation": FlavorVariation.SWEET
                    },
                    {
                        "name": "Orange",
                        "description": "A fruit that is orange in color",
                        "flavor_variation": FlavorVariation.CITRIC
                    }
                ]
            }
        )
    )

    Status: Status
    fruits: list[FruitBase] | None = None


class GetFruitsResponse(BaseModel):
    model_config: dict = ConfigDict(from_attributes=True)

    Status: Status
    fruits: list[FruitBase] | None = None
