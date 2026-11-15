import pandas as pd
from datetime import date

from .. import settings


class retrieve_cache:

    def __init__(self):
        self.output_path = settings.path_screener_cache

    def get_retrieve_cache(self):
        df = pd.read_parquet(self.output_path, engine="pyarrow").reset_index()

        # Add the date this data was generated (dd-mm-yyyy format)
        df["value_date_dmy"] = date.today().strftime("%d-%m-%Y")

        return df
