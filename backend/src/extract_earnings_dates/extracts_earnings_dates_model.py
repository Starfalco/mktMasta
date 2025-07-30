from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class extracts_earnings_dates_model(BaseModel):
    # index: Optional[int] = Field(alias="index")
    divendendDate: Optional[date] = Field(alias="Dividend Date")
    exDivendendDate: Optional[date] = Field(alias="Ex-Dividend Date")
    earningsDate: Optional[date] = Field(alias="Earnings Date")
    earningsHigh: Optional[float] = Field(alias="Earnings High")
    earningsLow: Optional[float] = Field(alias="Earnings Low")
    earningsAvg: Optional[float] = Field(alias="Earnings Average")
    revenueHigh: Optional[int] = Field(alias="Revenue High")
    revenueLow: Optional[int] = Field(alias="Revenue Low")
    revenueAvg: Optional[int] = Field(alias="Revenue Average")