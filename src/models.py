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


class FruitRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_fruit(self, fruit: Fruit):
        self.db_session.add(fruit)
        self.db_session.commit()
        self.db_session.refresh(fruit)
        return fruit

    def get_fruit(self, fruit_id: int):
        return self.db_session.query(Fruit) \
            .filter(Fruit.id == fruit_id) \
            .first()

    def get_fruits(self):
        return self.db_session.query(Fruit).all()

    def update_fruit(self, fruit: Fruit):
        self.db_session.add(fruit)
        self.db_session.commit()
        self.db_session.refresh(fruit)
        return fruit

    def delete_fruit(self, fruit: Fruit):
        self.db_session.delete(fruit)
        self.db_session.commit()
        return fruit
