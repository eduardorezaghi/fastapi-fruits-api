import pytest
from src.models import Fruit
from src.repositories import FruitRepository
from src.schemas import FlavorVariation

@pytest.fixture
def fruit_repo(db_session):
    return FruitRepository(db_session)

class TestFruitRepository:
    def test_create_fruit(self, db_session, fruit_repo: FruitRepository):
        # Arrange
        fruit = Fruit(name="Apple", description="A delicious red fruit", flavor_variation="SWEET")

        # Act
        created_fruit = fruit_repo.create_fruit(fruit)

        # Assert
        assert created_fruit.id is not None
        assert created_fruit.name == "Apple"
        assert created_fruit.description == "A delicious red fruit"
        assert created_fruit.flavor_variation == FlavorVariation.SWEET

    def test_get_fruit(self, db_session, fruit_repo):
        # Arrange
        fruit = Fruit(name="Apple", description="A delicious red fruit", flavor_variation="SWEET")
        db_session.add(fruit)
        db_session.commit()

        # Act
        retrieved_fruit = fruit_repo.get_fruit(fruit.id)

        # Assert
        assert retrieved_fruit is not None
        assert retrieved_fruit.id == fruit.id
        assert retrieved_fruit.name == "Apple"
        assert retrieved_fruit.description == "A delicious red fruit"
        assert retrieved_fruit.flavor_variation == FlavorVariation.SWEET

    def test_get_fruits(self, db_session, fruit_repo):
        # Arrange
        fruit1 = Fruit(name="Apple", description="A delicious red fruit", flavor_variation="SWEET")
        fruit2 = Fruit(name="Orange", description="A juicy orange fruit", flavor_variation="TANGY")
        db_session.add_all([fruit1, fruit2])
        db_session.commit()

        # Act
        fruits = fruit_repo.get_fruits()

        # Assert
        assert len(fruits) == 2
        assert fruits[0].name == "Apple"
        assert fruits[1].name == "Orange"

    def test_update_fruit(self, db_session, fruit_repo):
        # Arrange
        fruit = Fruit(name="Apple", description="A delicious red fruit", flavor_variation="SWEET")
        db_session.add(fruit)
        db_session.commit()

        # Act
        fruit.name = "Green Apple"
        updated_fruit = fruit_repo.update_fruit(fruit)

        # Assert
        assert updated_fruit.name == "Green Apple"

    def test_delete_fruit(self, db_session, fruit_repo):
        # Arrange
        fruit = Fruit(name="Apple", description="A delicious red fruit", flavor_variation="SWEET")
        db_session.add(fruit)
        db_session.commit()

        # Act
        deleted_fruit = fruit_repo.delete_fruit(fruit)

        # Assert
        assert deleted_fruit.id is not None
        assert deleted_fruit.name == "Apple"
        assert deleted_fruit.description == "A delicious red fruit"
        assert deleted_fruit.flavor_variation == FlavorVariation.SWEET