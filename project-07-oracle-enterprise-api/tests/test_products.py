from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_products_endpoint():

    response = client.get(
        "/api/v1/products/"
    )

    assert response.status_code == 200
