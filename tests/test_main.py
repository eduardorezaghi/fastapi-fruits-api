from http import HTTPStatus as http_status
from fastapi.testclient import TestClient
from src.main import app
from tests.conftest import TestingSessionLocal, test_client

class TestMain:
    def test_root(self, test_client):
        response = test_client.get("/")
        assert response.status_code == http_status.OK
        assert response.json() == {"message": "Welcome to this fantastic app!"}

    def test_create_fruit(self, test_client, db_session):
        response = test_client.post(
            "/fruits/",
            json={"name": "Apple", "description": "A delicious red fruit"},
        )

        assert response.status_code == http_status.CREATED
        assert response.json() == {"id": 1, "name": "Apple", "description": "A delicious red fruit"}

    def test_get_fruit(self, test_client, db_session):
        response = test_client.get("/fruits/1")

        assert response.status_code == http_status.NOT_FOUND


    def test_read_fruit_success(self, test_client, db_session):
        # Arrange
        test_client.post(
            "/fruits/",
            json={"name": "Apple", "description": "A delicious red fruit"},
        )

        # Act
        response = test_client.get("/fruits/1")

        # Assert
        assert response.status_code == http_status.OK
        assert response.json() == {"id": 1, "name": "Apple", "description": "A delicious red fruit"}


    def test_read_fruit_failure(self, test_client, db_session):
        response = test_client.get("/fruits/2")
        assert response.status_code == http_status.NOT_FOUND