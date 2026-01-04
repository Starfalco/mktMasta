from fastapi import APIRouter
from .sort_by_fields_manager import sort_by_fields
from .sort_by_fields_model import sort_by_fields_model
from json import loads

router = APIRouter(prefix="/sort", tags=["sort"])


@router.post("/sort_by_fields/")
async def get(
    ascending_sort: bool = True,
    fields: list[str] = None,
) -> list[sort_by_fields_model]:

    response = loads(
        sort_by_fields()
        .get_sort_by_fields(ascending_sort, fields)
        .to_json(orient="records")
    )

    return response
