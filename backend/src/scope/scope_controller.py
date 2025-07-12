from fastapi import APIRouter
from .scope_manager import scope
from .scope_model import scope_model

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.get("/scope/{symbol}")
async def get(symbol: str) -> list[scope_model]:

    scope_return = scope.get_scope(symbol)

    return scope_return


@router.get("/scope")
async def get() -> list[scope_model]:

    scope_return = scope.get_scope()

    return scope_return
