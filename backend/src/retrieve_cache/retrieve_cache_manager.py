import pandas as pd

from .. import settings


class retrieve_cache:

    def __init__(self):
        self.output_path = settings.path_screener_cache

    def get_retrieve_cache(self):
        df = pd.read_parquet(self.output_path, engine="pyarrow").reset_index()

        return df
