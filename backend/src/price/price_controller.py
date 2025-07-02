from fastapi import APIRouter
from .price_manager import price
from .price_model import price_model

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/price/{symbol}")
async def get(symbol: str) -> list[price_model]:

    get_price = price.get_price(symbol)

    return get_price
