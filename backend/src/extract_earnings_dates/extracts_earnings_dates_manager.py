import pandas as pd
import yfinance as yf
from curl_cffi import requests
from datetime import date


class extracts_earnings_dates:


    def get_extracts_earnings_dates(symbol: str = None):

        try:

            session = requests.Session(impersonate="chrome")

            df = pd.DataFrame(yf.Ticker(symbol, session=session).get_calendar())

            response = pd.DataFrame(df.to_records())

        except Exception as e:

            response = e

        return response
