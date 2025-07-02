from fastapi import APIRouter
from .earnings_history_manager import earnings_history
from .earnings_history_model import earnings_history_model

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/earnings_history/{symbol}")
async def get(symbol: str) -> list[earnings_history_model]:

    get_earnings_history = earnings_history.get_earnings_history(symbol)

    return get_earnings_history


@router.get("/earnings_history")
async def get() -> list[earnings_history_model]:

    get_earnings_history = earnings_history.get_earnings_history()

    return get_earnings_history
