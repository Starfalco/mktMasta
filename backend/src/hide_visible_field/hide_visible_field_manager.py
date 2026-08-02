import os, json
import pandas as pd

config_path = "/code/backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)


class hide_visible_field:

    def __init__(self):
        self.output_path = config["path_screener_cache"]

    def get_hide_visible_field(
        self,
        field: str,
        by_values: bool = False,
        fields: list[str] = None,
    ):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
        data_path = os.path.join(parent_dir, "cache", "screener_cache.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow").reset_index()

        if field != None:
            df[field] = None

        if by_values != False:
            df[fields] = None

        df.to_parquet(self.output_path)

        return df
