import pandas as pd
import yfinance as yf
from curl_cffi import requests
from datetime import date


class extracts_price:

    def get_price(symbol: str = None, start_date: date = None, end_date: date = None):

        try:

            session = requests.Session(impersonate="chrome")

            df = yf.download(
                symbol, start=start_date, end=end_date, session=session, group_by="ticker"
            ).stack(level=0)

            response = pd.DataFrame(df.to_records())

        except Exception as e:

            response = e

        return response
