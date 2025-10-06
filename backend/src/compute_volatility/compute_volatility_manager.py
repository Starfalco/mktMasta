import pandas as pd
from datetime import date
from ..extracts_price.extracts_price_manager import extracts_price
from ....utils.utils_volatility import build_volatility as volatility


class compute_volatility:

    def __init__(
        self, symbol: str = None, start_date: date = None, end_date: date = None
    ):
        self.symbol = symbol
        self.price = extracts_price.get_price(symbol, start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date

    def get_volatility(self):

        try:

            df_price = pd.DataFrame(self.price)
            df_volatility = volatility(df_price)

            response = pd.DataFrame(df_volatility.to_records())

        except Exception as e:

            response = e

        return response
