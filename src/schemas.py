from pydantic import BaseModel

class FruitBase(BaseModel):
    name: str
    description: str | None = None

class FruitCreate(FruitBase):
    pass

class Fruit(FruitBase):
    id: int

    class Config:
        orm_mode = True
