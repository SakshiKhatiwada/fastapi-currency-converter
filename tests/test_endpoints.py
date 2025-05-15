from fastapi.testclient import TestClient
from app.main import app
from app.utils import currency_converter

client = TestClient(app)


def test_site_check():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_converter_api():
    payload = {"from_curr": "USD", "to_curr": "GBP", "amount": 100}

    response = client.post("/api/convert", json=payload)
    assert response.status_code == 200

    converted_output = currency_converter(payload)
    assert response.json() == converted_output
