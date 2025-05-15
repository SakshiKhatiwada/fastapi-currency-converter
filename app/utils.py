import requests
from app.config import settings
from fastapi import HTTPException


API_ENDPOINT = "https://api.freecurrencyapi.com/v1"


def get_conversion_rate():
    response = requests.get(f"{API_ENDPOINT}/latest?apikey={settings.api_key}")
    response = response.json()["data"]
    return response


def get_currencies():
    response = requests.get(f"{API_ENDPOINT}/currencies?apikey={settings.api_key}")
    return response.json()["data"]


def currency_converter(data) -> float:
    rates = get_conversion_rate()

    try:
        rate_from = rates[data["from_curr"].upper()]
        rate_to = rates[data["to_curr"].upper()]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=e)

    amount_in_usd = data["amount"] / rate_from
    converted_amount = amount_in_usd * rate_to

    return round(converted_amount, 2)
