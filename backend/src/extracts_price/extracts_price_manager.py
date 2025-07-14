import os
import pandas as pd
from json import loads
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

            df = pd.DataFrame(df.to_records())

            result = df.to_json(orient="records")
            response = loads(result)

        except Exception as e:

            response = e

        return response
