from fastapi import APIRouter
from .filter_string_field_manager import filter_string_field
from .filter_string_field_model import filter_string_field_model
from json import loads

router = APIRouter(prefix="/filter", tags=["filter"])


@router.post("/filter_string_field/")
async def get(
    field: str,
    contains: str = None,
    not_contains: str = None,
    by_values: bool = False,
    values: list[str] = None,
) -> list[filter_string_field_model]:

    response = loads(
        filter_string_field()
        .get_filter_string_field(field, contains, not_contains, by_values, values)
        .to_json(orient="records")
    )

    return response
