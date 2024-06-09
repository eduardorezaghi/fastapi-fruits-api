import http
from fastapi.testclient import TestClient
from src.main import app
from tests.conftest import TestingSessionLocal

client = TestClient(app)

class TestMain:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == http.HTTPStatus.OK
        assert response.json() == {"Hello": "World"}

    def test_create_fruit(self, db_session):
        response = client.post(
            "/fruits/",
            json={"name": "Apple", "description": "A delicious red fruit"},
        )

        assert response.status_code == http.HTTPStatus.CREATED
        assert response.json() == {"name": "Apple", "description": "A delicious red fruit"}

    def test_get_fruit(self, db_session):
        response = client.get("/fruits/1")

        assert response.status_code == http.HTTPStatus.NOT_FOUND
