from fastapi import APIRouter
from .extracts_earnings_dates_manager import extracts_earnings_dates
from .extracts_earnings_dates_model import extracts_earnings_dates_model
from datetime import date

router = APIRouter(prefix="/extract", tags=["extract"])


@router.get("/extracts_earnings_dates/{symbol}")
async def get(
    symbol: str
) -> list[extracts_earnings_dates_model]:

    response = extracts_earnings_dates.get_extracts_earnings_dates(symbol)

    return response
