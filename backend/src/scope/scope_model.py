from typing import Optional
from pydantic import BaseModel


class scope_model(BaseModel):
    Company: Optional[str] = None
    Symbol: Optional[str] = None
