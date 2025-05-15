import os
import requests
from fastapi import HTTPException
from app.config import settings


API_ENDPOINT = "https://api.freecurrencyapi.com/v1"

if os.getenv("ENV") != "CI":
    API_KEY = settings.api_key
else:
    API_KEY = os.getenv("API_KEY")


if not API_KEY:
    raise EnvironmentError("API_KEY is not set")


def get_conversion_rate():
    response = requests.get(f"{API_ENDPOINT}/latest?apikey={API_KEY}")
    response = response.json()["data"]
    return response


def get_currencies():
    response = requests.get(f"{API_ENDPOINT}/currencies?apikey={API_KEY}")
    try:
        data = response.json()
        print("data", data)
        if "data" not in data:
            raise HTTPException(status_code=502, detail=f"API Error: {data}")
        return data["data"]
    except Exception as e:
        raise HTTPException(
            status_code=502, detail=f"Failed to fetch currencies: {str(e)}"
        )


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
