from typing import Optional
from pydantic import BaseModel


class peg_model(BaseModel):
    sector: Optional[str] = "NA"
    industry: Optional[str] = "NA"
    ticker: Optional[str] = "NA"
    earnings_f0: Optional[float] = "NA"
    earnings_f1: Optional[float] = "NA"
    earnings_f2: Optional[float] = "NA"
    growth_f1: Optional[float] = "NA"
    growth_f2: Optional[float] = "NA"
    pe_f0: Optional[float] = "NA"
    pe_f1: Optional[float] = "NA"
    pe_f2: Optional[float] = "NA"
    peg_f1: Optional[float] = "NA"
    peg_f2: Optional[float] = "NA"
    surprise_average: Optional[float] = "NA"
    nb_analysts_f1: Optional[float] = "NA"
    nb_analysts_f2: Optional[float] = "NA"
    high_to_low_eps_f1: Optional[float] = "NA"
    high_to_low_eps_f2: Optional[float] = "NA"
    fiscal_month: Optional[float] = "NA"
