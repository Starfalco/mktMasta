import pandas as pd
import sys

from .. import settings

# setting path
sys.path.append(settings.path_utils)

from utils_peg_benchmark import build_peg_benchmark as peg_benchmark


class compute_peg_benchmark:

    def __init__(self, symbol: str = None):
        self.symbol = symbol

    def get_peg_benchmark(self):
        return peg_benchmark(self.symbol)
