from fastapi import APIRouter
from .retrieve_peg_benchmark_manager import peg_benchmark
from .retrieve_peg_benchmark_model import peg_benchmark_model
from json import loads

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/peg_benchmark/{symbol}")
async def get(symbol: str) -> list[peg_benchmark_model]:

    response = loads(peg_benchmark.get_peg_benchmark(symbol).to_json(orient="records"))

    return response


@router.get("/peg_benchmark")
async def get() -> list[peg_benchmark_model]:

    response = loads(peg_benchmark.get_peg_benchmark().to_json(orient="records"))

    return response
