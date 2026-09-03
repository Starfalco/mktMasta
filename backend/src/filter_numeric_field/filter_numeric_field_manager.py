import os
import pandas as pd

from .. import settings


class filter_numeric_field:

    def __init__(self):
        self.output_path = settings.path_screener_cache

    def get_filter_numeric_field(
        self,
        field: str,
        min: float = None,
        max: float = None,
        by_values: bool = False,
        values: list[float] = None,
    ):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
        data_path = os.path.join(parent_dir, "cache", "screener_cache.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow").reset_index()

        if min != None:
            df = df[df[field] >= min]

        if max != None:
            df = df[df[field] <= max]

        if by_values != False:
            df = df[df[field].isin(values)]

        df.to_parquet(self.output_path,engine="pyarrow")

        return df
