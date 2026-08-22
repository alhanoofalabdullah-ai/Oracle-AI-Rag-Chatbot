from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_create_order():

    response = client.post(

        "/api/v1/orders/",

        json={
            "customer_id": 1
        }

    )

    assert response.status_code == 201
