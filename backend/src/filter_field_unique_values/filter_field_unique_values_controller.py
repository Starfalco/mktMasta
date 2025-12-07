from fastapi import APIRouter
from .filter_field_unique_values_manager import filter_field_unique_values
from json import loads

router = APIRouter(prefix="/filter", tags=["filter"])


@router.get("/filter_field_unique_values/")
async def get(field: str) -> list[str]:

    response = loads(
        filter_field_unique_values()
        .get_filter_field_unique_values(field)
        .to_json(orient="records")
    )

    return response
