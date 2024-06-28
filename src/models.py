from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src import Base
from src.schemas import FlavorVariation

class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description: str = Column(String)
    flavor_variation: FlavorVariation = Column(Enum(FlavorVariation))



