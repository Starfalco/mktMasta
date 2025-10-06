from fastapi import APIRouter
from .retrieve_earnings_estimate_manager import earnings_estimate
from .retrieve_earnings_estimate_model import earnings_estimate_model
from json import loads

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/earnings_estimate/{symbol}")
async def get(symbol: str) -> list[earnings_estimate_model]:

    response = earnings_estimate.get_earnings_estimate(symbol)
    response = response.to_json(orient="records")
    response = loads(response)

    return response


@router.get("/earnings_estimate")
async def get() -> list[earnings_estimate_model]:

    response = earnings_estimate.get_earnings_estimate()
    response = response.to_json(orient="records")
    response = loads(response)

    return response
