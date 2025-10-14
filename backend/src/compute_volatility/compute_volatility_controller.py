from fastapi import APIRouter
from .compute_volatility_manager import compute_volatility
from .compute_volatility_model import volatility_model
from datetime import date
from json import loads

router = APIRouter(prefix="/compute", tags=["compute"])


@router.get("/compute_volatility/{symbol}")
async def get(
    symbol: str, start_date: date = None, end_date: date = None
) -> list[volatility_model]:

    volatility = compute_volatility(symbol, start_date, end_date)

    response = loads(volatility.get_volatility().to_json(orient="records"))

    return response
