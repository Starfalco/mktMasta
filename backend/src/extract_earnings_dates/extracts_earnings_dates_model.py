from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class extracts_earnings_dates_model(BaseModel):
    divendendDate: Optional[date] = Field(validation_alias="Dividend Date")
    exDivendendDate: Optional[date] = Field(validation_alias="Ex-Dividend Date")
    earningsDate: Optional[date] = Field(validation_alias="Earnings Date")
    earningsHigh: Optional[float] = Field(validation_alias="Earnings High")
    earningsLow: Optional[float] = Field(validation_alias="Earnings Low")
    earningsAvg: Optional[float] = Field(validation_alias="Earnings Average")
    revenueHigh: Optional[int] = Field(validation_alias="Revenue High")
    revenueLow: Optional[int] = Field(validation_alias="Revenue Low")
    revenueAvg: Optional[int] = Field(validation_alias="Revenue Average")