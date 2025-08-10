import os
import pandas as pd
from json import loads


class retrive_price:

    def get_price(symbol: str):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
        # parent_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "..")) #local

        data_path = os.path.join(parent_dir, "extracts", "price.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow")
        df = pd.DataFrame(df.to_records())
        df = df[df["Ticker"] == symbol.upper()]

        # df.rename(columns={'Adj Close' : 'AdjClose'},inplace=True)

        result = df.to_json(orient="records")
        response = loads(result)

        return response
