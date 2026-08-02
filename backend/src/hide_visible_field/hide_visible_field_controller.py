from fastapi import APIRouter
from .hide_visible_field_manager import hide_visible_field
from json import loads

router = APIRouter(prefix="/filter", tags=["filter"])


@router.post("/hide_visible_field/")
async def get(
    field: str,
    by_values: bool = False,
    fields: list[str] = None,
) -> bool:

    try:
        hide_visible = hide_visible_field()
        hide_visible.get_hide_visible_field(field, by_values, fields)
        response = True
    except:
        response = False

    return response
