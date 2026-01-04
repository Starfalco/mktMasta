import pandas as pd
import yfinance as yf
from datetime import date
from utils_const import DOWNLOAD_PRICE_RENAME


def download_price(
    symbol: str, start_date: date = None, end_date: date = None, session=None
) -> pd.DataFrame:
    df_price = (
        yf.download(
            symbol, start=start_date, end=end_date, session=session, group_by="ticker"
        )
        .stack(level=0)
        .reset_index()
        .rename(columns=DOWNLOAD_PRICE_RENAME)
        .astype({"date": str})
    )

    return df_price
