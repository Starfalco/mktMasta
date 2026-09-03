import json
from curl_cffi import requests
from datetime import date
import pandas as pd
import sys

from .. import settings

# setting path
sys.path.append(settings.path_utils)

from utils_yfinance import download_price


class extracts_price:

    def get_price(symbol: str = None, start_date: date = None, end_date: date = None):

        try:

            session = requests.Session(impersonate="chrome")

            df = download_price(
                symbol,
                start_date,
                end_date,
                session,
            )

            response = pd.DataFrame(df.to_records())

        except Exception as e:

            response = e

        return response
