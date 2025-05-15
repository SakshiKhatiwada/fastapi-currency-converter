from pydantic import BaseModel, RootModel
from typing import Dict


class CurrencyDetail(BaseModel):
    symbol: str
    name: str
    symbol_native: str
    decimal_digits: int
    rounding: int
    code: str
    name_plural: str
    type: str


class CurrencyResponse(RootModel[Dict[str, CurrencyDetail]]):
    pass


class ConverterPayload(BaseModel):
    from_curr: str
    to_curr: str
    amount: float
