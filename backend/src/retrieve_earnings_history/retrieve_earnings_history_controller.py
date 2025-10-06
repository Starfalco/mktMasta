from fastapi import APIRouter
from .retrieve_earnings_history_manager import earnings_history
from .retrieve_earnings_history_model import earnings_history_model
from json import loads

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/earnings_history/{symbol}")
async def get(symbol: str) -> list[earnings_history_model]:

    response = earnings_history.get_earnings_history(symbol)
    response = response.to_json(orient="records")
    response = loads(response)

    return response


@router.get("/earnings_history")
async def get() -> list[earnings_history_model]:

    response = earnings_history.get_earnings_history()
    response = response.to_json(orient="records")
    response = loads(response)

    return response
