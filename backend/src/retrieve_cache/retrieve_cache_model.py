from typing import Any, Optional
from pydantic import BaseModel, ConfigDict
from datetime import date


class retrieve_cache_model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    def model_dump(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        kwargs.setdefault("exclude_none", True)
        return super().model_dump(*args, **kwargs)

    def model_dump_json(self, *args: Any, **kwargs: Any) -> str:
        kwargs.setdefault("exclude_none", True)
        return super().model_dump_json(*args, **kwargs)

    sector: Optional[str] = None
    industry: Optional[str] = None
    naics_title: Optional[str] = None
    naics_code: Optional[str] = None
    ticker: Optional[str] = None
    earnings_f0: Optional[float] = None
    earnings_f1: Optional[float] = None
    earnings_f2: Optional[float] = None
    growth_f1: Optional[float] = None
    growth_f2: Optional[float] = None
    pe_f0: Optional[float] = None
    pe_f1: Optional[float] = None
    pe_f2: Optional[float] = None
    peg_f1: Optional[float] = None
    peg_f2: Optional[float] = None
    surprise_average: Optional[float] = None
    nb_analysts_f1: Optional[float] = None
    nb_analysts_f2: Optional[float] = None
    high_to_low_eps_f1: Optional[float] = None
    high_to_low_eps_f2: Optional[float] = None
    fiscal_month: Optional[float] = None
    volatility: Optional[float] = None
    max_drawn_down: Optional[float] = None
    occurrence: Optional[date] = None
    max_price: Optional[float] = None
    earnings_f0_industry_bench: Optional[float] = None
    earnings_f1_industry_bench: Optional[float] = None
    earnings_f2_industry_bench: Optional[float] = None
    earnings_f0_sector_bench: Optional[float] = None
    earnings_f1_sector_bench: Optional[float] = None
    earnings_f2_sector_bench: Optional[float] = None
    earnings_f0_naics_bench: Optional[float] = None
    earnings_f1_naics_bench: Optional[float] = None
    earnings_f2_naics_bench: Optional[float] = None
    earnings_f0_delta_industry: Optional[float] = None
    earnings_f1_delta_industry: Optional[float] = None
    earnings_f2_delta_industry: Optional[float] = None
    earnings_f0_delta_sector: Optional[float] = None
    earnings_f1_delta_sector: Optional[float] = None
    earnings_f2_delta_sector: Optional[float] = None
    earnings_f0_delta_naics: Optional[float] = None
    earnings_f1_delta_naics: Optional[float] = None
    earnings_f2_delta_naics: Optional[float] = None
    growth_f1_industry_bench: Optional[float] = None
    growth_f2_industry_bench: Optional[float] = None
    growth_f1_sector_bench: Optional[float] = None
    growth_f2_sector_bench: Optional[float] = None
    growth_f1_naics_bench: Optional[float] = None
    growth_f2_naics_bench: Optional[float] = None
    growth_f1_delta_industry: Optional[float] = None
    growth_f2_delta_industry: Optional[float] = None
    growth_f1_delta_sector: Optional[float] = None
    growth_f2_delta_sector: Optional[float] = None
    growth_f1_delta_naics: Optional[float] = None
    growth_f2_delta_naics: Optional[float] = None
    pe_f0_industry_bench: Optional[float] = None
    pe_f1_industry_bench: Optional[float] = None
    pe_f2_industry_bench: Optional[float] = None
    pe_f0_sector_bench: Optional[float] = None
    pe_f1_sector_bench: Optional[float] = None
    pe_f2_sector_bench: Optional[float] = None
    pe_f0_naics_bench: Optional[float] = None
    pe_f1_naics_bench: Optional[float] = None
    pe_f2_naics_bench: Optional[float] = None
    pe_f0_delta_industry: Optional[float] = None
    pe_f1_delta_industry: Optional[float] = None
    pe_f2_delta_industry: Optional[float] = None
    pe_f0_delta_sector: Optional[float] = None
    pe_f1_delta_sector: Optional[float] = None
    pe_f2_delta_sector: Optional[float] = None
    pe_f0_delta_naics: Optional[float] = None
    pe_f1_delta_naics: Optional[float] = None
    pe_f2_delta_naics: Optional[float] = None
    pe_f1_vs_f0: Optional[float] = None
    pe_f2_vs_f1: Optional[float] = None
    scoring_f0: Optional[float] = None
    scoring_f1: Optional[float] = None
    scoring_f2: Optional[float] = None
    surprise_average_industry_bench: Optional[float] = None
    surprise_average_sector_bench: Optional[float] = None
    surprise_average_naics_bench: Optional[float] = None
