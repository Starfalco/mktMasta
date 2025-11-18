from typing import Optional
from pydantic import BaseModel, Field


class scope_model(BaseModel):
    company: Optional[str] = Field(validation_alias="Company")
    ticker: Optional[str] = Field(validation_alias="Symbol")
