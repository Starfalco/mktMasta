from typing import Optional
from pydantic import BaseModel, Field
from datetime import date as dt


class earnings_history_model(BaseModel):
    date: Optional[dt] = Field(validation_alias="quarter")
    epsActual: Optional[float] = None
    epsEstimate: Optional[float] = None
    epsDifference: Optional[float] = None
    surprisePercent: Optional[float] = None
    Ticker: Optional[str] = None
