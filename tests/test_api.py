from fastapi.testclient import TestClient
from app.main import app 

client=TestClient(app)

def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_list_products_returns_two_products():
    response = client.get("/products")

    assert response.status_code == 200
    assert  len( response.json())== 2

def test_get_product_returns_requested_id():
    response = client.get("/products/7")
    assert response.status_code == 200
    assert response.json()["id"] == 7

def test_product_id_must_be_an_integer():
    response = client.get("/products/abc")

    assert response.status_code == 422


def test_list_products_contains_expected_names():
    response = client.get("/products")

    product_names = [product["name"] for product in response.json()]

    assert "Clavier" in product_names
    assert "Souris" in product_names
