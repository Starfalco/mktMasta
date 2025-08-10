from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class compute_max_drawn_down_model(BaseModel):
    max_drawn_down: Optional[float] = "NA"
    occurrence: Optional[date] = "NA"
    max_price: Optional[float] = "NA"
