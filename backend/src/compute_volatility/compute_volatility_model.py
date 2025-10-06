from typing import Optional
from pydantic import BaseModel


class volatility_model(BaseModel):
    volatility: Optional[float] = "NA"
