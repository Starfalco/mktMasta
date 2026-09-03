import os
import pandas as pd

from .. import settings


class sort_by_fields:

    def __init__(self):
        self.output_path = settings.path_screener_cache

    def get_sort_by_fields(
        self,
        ascending_sort: bool = True,
        fields: list[str] = None,
    ):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
        data_path = os.path.join(parent_dir, "cache", "screener_cache.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow")

        df.sort_values(by=fields, ascending=ascending_sort, inplace=True)

        df.to_parquet(self.output_path,engine="pyarrow")

        return df
