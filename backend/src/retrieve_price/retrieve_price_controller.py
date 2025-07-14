from fastapi import APIRouter
from .retrieve_price_manager import price
from .retrieve_price_model import price_model

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/price/{symbol}")
async def get(symbol: str) -> list[price_model]:

    response = price.get_price(symbol)

    return response
