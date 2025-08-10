import os
import pandas as pd
from json import loads


class earnings_history:
    path_earnings_history = "extracts/earnings_history.parquet"

    def get_earnings_history(symbol: str = None):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
        # parent_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "..")) #local

        data_path = os.path.join(parent_dir, "extracts", "earnings_history.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow").reset_index()
        df.rename(columns={"index": "date"}, inplace=True)

        if symbol != None:
            df = df[df["Ticker"] == symbol.upper()]

        result = df.to_json(orient="records")
        response = loads(result)

        return response
