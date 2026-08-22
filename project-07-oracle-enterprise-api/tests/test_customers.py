from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_invalid_customer():

    response = client.get(
        "/api/v1/customers/0"
    )

    assert response.status_code == 400
