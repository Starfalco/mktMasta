from fastapi import APIRouter
from .compute_peg_benchmark_manager import compute_peg_benchmark
from .compute_peg_benchmark_model import peg_benchmark_model
from json import loads

router = APIRouter(prefix="/compute", tags=["compute"])


@router.get("/compute_peg_benchmark/{symbol}")
async def get(symbol: str) -> list[peg_benchmark_model]:

    peg_benchmark = compute_peg_benchmark(symbol)

    try:
        response = loads(peg_benchmark.get_peg_benchmark().to_json(orient="records"))
    except:
        response = peg_benchmark.get_peg_benchmark()

    return response


@router.get("/compute_peg_benchmark")
async def get() -> list[peg_benchmark_model]:

    peg_benchmark = compute_peg_benchmark()

    try:
        response = loads(peg_benchmark.get_peg_benchmark().to_json(orient="records"))
    except:
        response = peg_benchmark.get_peg_benchmark()

    return response
