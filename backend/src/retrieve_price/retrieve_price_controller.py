from fastapi import APIRouter
from .retrieve_price_manager import retrive_price
from .retrieve_price_model import retrieve_price_model
from json import loads

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/retrieve_price/{symbol}")
async def get(symbol: str) -> list[retrieve_price_model]:

    response = loads(retrive_price.get_price(symbol).to_json(orient="records"))

    return response
