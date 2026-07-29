from fastapi import APIRouter
from .hide_default_field_manager import hide_default_field

router = APIRouter(prefix="/filter", tags=["filter"])


@router.get("/hide_default_field/")
async def get() -> bool:

    try:
        hide = hide_default_field()
        hide.get_hide_default_field()
        response = True
    except:
        response = False

    return response
