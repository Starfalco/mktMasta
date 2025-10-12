from fastapi import APIRouter
from .compute_peg_manager import compute_peg
from .compute_peg_model import peg_model
from json import loads

router = APIRouter(prefix="/compute", tags=["compute"])


@router.get("/compute_peg/{symbol}")
async def get(symbol: str) -> list[peg_model]:

    peg = compute_peg(symbol)

    response = loads(peg.get_peg().to_json(orient="records"))

    return response
