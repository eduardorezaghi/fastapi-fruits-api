from sqlalchemy.orm import Session
from src.models import Fruit


class FruitRepository:
    def __init__(self, db_session: Session):
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