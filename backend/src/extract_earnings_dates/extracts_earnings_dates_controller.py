from fastapi import APIRouter
from .extracts_earnings_dates_manager import extracts_earnings_dates
from .extracts_earnings_dates_model import extracts_earnings_dates_model
from json import loads

router = APIRouter(prefix="/extract", tags=["extract"])


@router.get("/extracts_earnings_dates/{symbol}")
async def get(
    symbol: str
) -> list[extracts_earnings_dates_model]:

    response = loads(extracts_earnings_dates.get_extracts_earnings_dates(symbol).to_json(orient="records"))

    return response
