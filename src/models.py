from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src import Base

class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description: str = Column(String)


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