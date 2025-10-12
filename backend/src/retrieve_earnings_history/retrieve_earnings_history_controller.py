from fastapi import APIRouter
from .retrieve_earnings_history_manager import earnings_history
from .retrieve_earnings_history_model import earnings_history_model
from json import loads

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/earnings_history/{symbol}")
async def get(symbol: str) -> list[earnings_history_model]:

    response = loads(
        earnings_history.get_earnings_history(symbol).to_json(orient="records")
    )

    return response


@router.get("/earnings_history")
async def get() -> list[earnings_history_model]:

    response = loads(earnings_history.get_earnings_history().to_json(orient="records"))

    return response
