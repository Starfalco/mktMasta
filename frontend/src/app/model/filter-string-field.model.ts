export interface FilterStringFieldModel {
  sector: string;
  industry: string;
  naics_title: string;
  naics_code: string;
  ticker: string;
  earnings_f0: number;
  earnings_f1: number;
  earnings_f2: number;
  growth_f1: number;
  growth_f2: number;
  pe_f0: number;
  pe_f1: number;
  pe_f2: number;
  peg_f1: number;
  peg_f2: number;
  surprise_average: number;
  nb_analysts_f1: number;
  nb_analysts_f2: number;
  high_to_low_eps_f1: number;
  high_to_low_eps_f2: number;
  fiscal_month: number;
  volatility: number;
  max_drawn_down: number;
  occurrence: string;
  max_price: number;
  earnings_f0_industry_bench: number;
  earnings_f1_industry_bench: number;
  earnings_f2_industry_bench: number;
  earnings_f0_sector_bench: number;
  earnings_f1_sector_bench: number;
  earnings_f2_sector_bench: number;
  earnings_f0_naics_bench: number;
  earnings_f1_naics_bench: number;
  earnings_f2_naics_bench: number;
  earnings_f0_delta_industry: number;
  earnings_f1_delta_industry: number;
  earnings_f2_delta_industry: number;
  earnings_f0_delta_sector: number;
  earnings_f1_delta_sector: number;
  earnings_f2_delta_sector: number;
  earnings_f0_delta_naics: number;
  earnings_f1_delta_naics: number;
  earnings_f2_delta_naics: number;
  growth_f1_industry_bench: number;
  growth_f2_industry_bench: number;
  growth_f1_sector_bench: number;
  growth_f2_sector_bench: number;
  growth_f1_naics_bench: number;
  growth_f2_naics_bench: number;
  growth_f1_delta_industry: number;
  growth_f2_delta_industry: number;
  growth_f1_delta_sector: number;
  growth_f2_delta_sector: number;
  growth_f1_delta_naics: number;
  growth_f2_delta_naics: number;
  pe_f0_industry_bench: number;
  pe_f1_industry_bench: number;
  pe_f2_industry_bench: number;
  pe_f0_sector_bench: number;
  pe_f1_sector_bench: number;
  pe_f2_sector_bench: number;
  pe_f0_naics_bench: number;
  pe_f1_naics_bench: number;
  pe_f2_naics_bench: number;
  pe_f0_delta_industry: number;
  pe_f1_delta_industry: number;
  pe_f2_delta_industry: number;
  pe_f0_delta_sector: number;
  pe_f1_delta_sector: number;
  pe_f2_delta_sector: number;
  pe_f0_delta_naics: number;
  pe_f1_delta_naics: number;
  pe_f2_delta_naics: number;
  pe_f1_vs_f0: number;
  pe_f2_vs_f1: number;
  scoring_f0: number;
  scoring_f1: number;
  scoring_f2: number;
  surprise_average_industry_bench: number;
  surprise_average_sector_bench: number;
  surprise_average_naics_bench: number;
  value_date_dmy: string;
}

export interface FilterFieldOption {
  value: keyof FilterStringFieldModel;
  label: string;
}

export const FILTER_STRING_FIELD_OPTIONS: readonly FilterFieldOption[] = [
  { value: 'sector', label: 'Sector' },
  { value: 'industry', label: 'Industry' },
  { value: 'naics_title', label: 'NAICS Title' },
  { value: 'naics_code', label: 'NAICS Code' },
  { value: 'ticker', label: 'Ticker' },
  { value: 'earnings_f0', label: 'Earnings (F0)' },
  { value: 'earnings_f1', label: 'Earnings (F1)' },
  { value: 'earnings_f2', label: 'Earnings (F2)' },

  { value: 'growth_f1', label: 'Growth (F1)' },
  { value: 'growth_f2', label: 'Growth (F2)' },
  { value: 'pe_f0', label: 'P/E (F0)' },
  { value: 'pe_f1', label: 'P/E (F1)' },
  { value: 'pe_f2', label: 'P/E (F2)' },

  { value: 'peg_f1', label: 'PEG (F1)' },
  { value: 'peg_f2', label: 'PEG (F2)' },

  { value: 'surprise_average', label: 'Average Surprise' },
  { value: 'nb_analysts_f1', label: 'Analysts (F1)' },
  { value: 'nb_analysts_f2', label: 'Analysts (F2)' },

  { value: 'high_to_low_eps_f1', label: 'High/Low EPS (F1)' },
  { value: 'high_to_low_eps_f2', label: 'High/Low EPS (F2)' },

  { value: 'fiscal_month', label: 'Fiscal Month' },
  { value: 'volatility', label: 'Volatility' },
  { value: 'max_drawn_down', label: 'Max Drawdown' },
  { value: 'occurrence', label: 'Occurrence' },
  { value: 'max_price', label: 'Maximum Price' },

  { value: 'earnings_f0_industry_bench', label: 'Earnings F0 Industry Benchmark' },
  { value: 'earnings_f1_industry_bench', label: 'Earnings F1 Industry Benchmark' },
  { value: 'earnings_f2_industry_bench', label: 'Earnings F2 Industry Benchmark' },

  { value: 'earnings_f0_sector_bench', label: 'Earnings F0 Sector Benchmark' },
  { value: 'earnings_f1_sector_bench', label: 'Earnings F1 Sector Benchmark' },
  { value: 'earnings_f2_sector_bench', label: 'Earnings F2 Sector Benchmark' },

  { value: 'earnings_f0_naics_bench', label: 'Earnings F0 NAICS Benchmark' },
  { value: 'earnings_f1_naics_bench', label: 'Earnings F1 NAICS Benchmark' },
  { value: 'earnings_f2_naics_bench', label: 'Earnings F2 NAICS Benchmark' },

  { value: 'earnings_f0_delta_industry', label: 'Earnings F0 Δ Industry' },
  { value: 'earnings_f1_delta_industry', label: 'Earnings F1 Δ Industry' },
  { value: 'earnings_f2_delta_industry', label: 'Earnings F2 Δ Industry' },

  { value: 'earnings_f0_delta_sector', label: 'Earnings F0 Δ Sector' },
  { value: 'earnings_f1_delta_sector', label: 'Earnings F1 Δ Sector' },
  { value: 'earnings_f2_delta_sector', label: 'Earnings F2 Δ Sector' },

  { value: 'earnings_f0_delta_naics', label: 'Earnings F0 Δ NAICS' },
  { value: 'earnings_f1_delta_naics', label: 'Earnings F1 Δ NAICS' },
  { value: 'earnings_f2_delta_naics', label: 'Earnings F2 Δ NAICS' },

  { value: 'growth_f1_industry_bench', label: 'Growth F1 Industry Benchmark' },
  { value: 'growth_f2_industry_bench', label: 'Growth F2 Industry Benchmark' },

  { value: 'growth_f1_sector_bench', label: 'Growth F1 Sector Benchmark' },
  { value: 'growth_f2_sector_bench', label: 'Growth F2 Sector Benchmark' },

  { value: 'growth_f1_naics_bench', label: 'Growth F1 NAICS Benchmark' },
  { value: 'growth_f2_naics_bench', label: 'Growth F2 NAICS Benchmark' },

  { value: 'growth_f1_delta_industry', label: 'Growth F1 Δ Industry' },
  { value: 'growth_f2_delta_industry', label: 'Growth F2 Δ Industry' },

  { value: 'growth_f1_delta_sector', label: 'Growth F1 Δ Sector' },
  { value: 'growth_f2_delta_sector', label: 'Growth F2 Δ Sector' },

  { value: 'growth_f1_delta_naics', label: 'Growth F1 Δ NAICS' },
  { value: 'growth_f2_delta_naics', label: 'Growth F2 Δ NAICS' },

  { value: 'pe_f0_industry_bench', label: 'P/E F0 Industry Benchmark' },
  { value: 'pe_f1_industry_bench', label: 'P/E F1 Industry Benchmark' },
  { value: 'pe_f2_industry_bench', label: 'P/E F2 Industry Benchmark' },

  { value: 'pe_f0_sector_bench', label: 'P/E F0 Sector Benchmark' },
  { value: 'pe_f1_sector_bench', label: 'P/E F1 Sector Benchmark' },
  { value: 'pe_f2_sector_bench', label: 'P/E F2 Sector Benchmark' },

  { value: 'pe_f0_naics_bench', label: 'P/E F0 NAICS Benchmark' },
  { value: 'pe_f1_naics_bench', label: 'P/E F1 NAICS Benchmark' },
  { value: 'pe_f2_naics_bench', label: 'P/E F2 NAICS Benchmark' },

  { value: 'pe_f0_delta_industry', label: 'P/E F0 Δ Industry' },
  { value: 'pe_f1_delta_industry', label: 'P/E F1 Δ Industry' },
  { value: 'pe_f2_delta_industry', label: 'P/E F2 Δ Industry' },

  { value: 'pe_f0_delta_sector', label: 'P/E F0 Δ Sector' },
  { value: 'pe_f1_delta_sector', label: 'P/E F1 Δ Sector' },
  { value: 'pe_f2_delta_sector', label: 'P/E F2 Δ Sector' },

  { value: 'pe_f0_delta_naics', label: 'P/E F0 Δ NAICS' },
  { value: 'pe_f1_delta_naics', label: 'P/E F1 Δ NAICS' },
  { value: 'pe_f2_delta_naics', label: 'P/E F2 Δ NAICS' },

  { value: 'pe_f1_vs_f0', label: 'P/E F1 vs F0' },
  { value: 'pe_f2_vs_f1', label: 'P/E F2 vs F1' },

  { value: 'scoring_f0', label: 'Score F0' },
  { value: 'scoring_f1', label: 'Score F1' },
  { value: 'scoring_f2', label: 'Score F2' },

  { value: 'surprise_average_industry_bench', label: 'Average Surprise Industry Benchmark' },
  { value: 'surprise_average_sector_bench', label: 'Average Surprise Sector Benchmark' },
  { value: 'surprise_average_naics_bench', label: 'Average Surprise NAICS Benchmark' },
  { value: 'value_date_dmy', label: 'Value Date' },
] as const;