import pandas as pd
from ....utils.utils_peg import build_peg as peg


class compute_peg:

    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_peg(self):

        try:

            df_peg = peg(self.symbol)
            response = pd.DataFrame(df_peg.to_records())

        except Exception as e:

            response = e

        return response
