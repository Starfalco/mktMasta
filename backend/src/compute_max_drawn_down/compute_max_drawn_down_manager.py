import pandas as pd
from datetime import date
from ..extracts_price.extracts_price_manager import extracts_price
from ....utils.utils_max_drawn_down import build_max_drawn_down as mdd


class compute_max_drawn_down:

    def __init__(
        self, symbol: str = None, start_date: date = None, end_date: date = None
    ):
        self.symbol = symbol
        self.price = extracts_price.get_price(symbol, start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date

    def get_max_drawn_down(self):

        try:

            df_price = pd.DataFrame(self.price)
            df_mdd = mdd(df_price)

            response = pd.DataFrame(df_mdd.to_records())

        except Exception as e:

            response = e

        return response
