from fastapi import APIRouter
from .filter_numeric_field_manager import filter_numeric_field
from .filter_numeric_field_model import filter_numeric_field_model
from json import loads

router = APIRouter(prefix="/filter", tags=["filter"])


@router.post("/filter_numeric_field/")
async def get(
    field: str,
    min: float = None,
    max: float = None,
    by_values: bool = False,
    values: list[float] = None,
) -> list[filter_numeric_field_model]:

    response = loads(
        filter_numeric_field()
        .get_filter_numeric_field(field, min, max, by_values, values)
        .to_json(orient="records")
    )

    return response
