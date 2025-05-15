from fastapi import APIRouter, HTTPException, status
from app.schemas import ConverterPayload, CurrencyResponse
from app.utils import currency_converter, get_currencies

router = APIRouter(prefix="/api", tags=["converter"])


@router.post("/convert", response_model=float)
async def convert_currency(payload: ConverterPayload):
    data = dict(payload)
    currencies = list(get_currencies().keys())

    if data["from_curr"] not in currencies or data["to_curr"] not in currencies:
        raise HTTPException(
            detail="Invalid Currency code", status_code=status.HTTP_400_BAD_REQUEST
        )

    return currency_converter(data)


@router.get("/currencies", response_model=CurrencyResponse)
async def get_currency():
    return get_currencies()
