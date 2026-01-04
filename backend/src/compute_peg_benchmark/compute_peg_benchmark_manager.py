import json

config_path = "/code/backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)

import pandas as pd
import sys

# setting path
sys.path.append(config["path_utils"])

from utils_peg_benchmark import build_peg_benchmark as peg_benchmark


class compute_peg_benchmark:

    def __init__(self, symbol: str = None):
        self.symbol = symbol

    def get_peg_benchmark(self):
        return peg_benchmark(self.symbol)
