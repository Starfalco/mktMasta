from fastapi import APIRouter
from .init_cache_manager import init_cache

router = APIRouter(prefix="/cache", tags=["cache"])


@router.get("/init_cache/")
async def get() -> bool:

    try:
        cache = init_cache()
        cache.get_init_cache()
        response = True
    except:
        response = False

    return response
