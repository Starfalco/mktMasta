import json
from curl_cffi import requests
from datetime import date

config_path = "/code/backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)

import pandas as pd
import sys

# setting path
sys.path.append(config["path_utils"])

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
