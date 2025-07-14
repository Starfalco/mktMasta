from fastapi import APIRouter
from .retrieve_scope_manager import scope
from .retrieve_scope_model import scope_model

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/scope/{symbol}")
async def get(symbol: str) -> list[scope_model]:

    response = scope.get_scope(symbol)

    return response


@router.get("/scope")
async def get() -> list[scope_model]:

    response = scope.get_scope()

    return response
