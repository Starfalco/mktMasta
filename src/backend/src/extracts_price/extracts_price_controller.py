from fastapi import APIRouter
from .extracts_price_manager import extracts_price
from .extracts_price_model import extracts_price_model
from datetime import date

router = APIRouter(prefix="/extract", tags=["extract"])


@router.get("/extracts_price/{symbol}")
async def get(
    symbol: str, start_date: date = None, end_date: date = None
) -> list[extracts_price_model]:

    response = extracts_price.get_price(symbol, start_date, end_date)

    return response
