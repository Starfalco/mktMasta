from fastapi import APIRouter
from .retrieve_cache_manager import retrieve_cache
from .retrieve_cache_model import retrieve_cache_model
from json import loads

router = APIRouter(prefix="/cache", tags=["cache"])


@router.get("/retrieve_cache")
async def get() -> list[retrieve_cache_model]:

    cache = retrieve_cache()
    response = loads(cache.get_retrieve_cache().to_json(orient="records"))

    return response
