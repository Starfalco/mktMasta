import json

config_path = "/code/backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)

import pandas as pd


class retrieve_cache:

    def __init__(self):
        self.output_path = config["path_screener_cache"]

    def get_retrieve_cache(self):
        df = pd.read_parquet(self.output_path, engine="pyarrow").reset_index()

        return df
