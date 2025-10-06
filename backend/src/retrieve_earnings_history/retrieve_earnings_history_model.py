from typing import Optional
from pydantic import BaseModel
from datetime import date


class earnings_history_model(BaseModel):
    date: Optional[date]
    epsActual: Optional[float] = None
    epsEstimate: Optional[float] = None
    epsDifference: Optional[float] = None
    surprisePercent: Optional[float] = None
    Ticker: Optional[str] = None
