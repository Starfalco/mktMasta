from typing import Optional
from pydantic import BaseModel


class earnings_estimate_model(BaseModel):
    period: Optional[str] = None
    avg: Optional[float] = None
    low: Optional[float] = None
    high: Optional[float] = None
    yearAgoEps: Optional[float] = None
    numberOfAnalysts: Optional[float] = None
    growth: Optional[float] = None
    Ticker: Optional[str] = None
