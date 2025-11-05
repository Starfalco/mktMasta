import json

config_path = "/code/backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)

import pandas as pd
import sys

# setting path
sys.path.append(config["path_utils"])

from utils_peg import build_peg as peg


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
