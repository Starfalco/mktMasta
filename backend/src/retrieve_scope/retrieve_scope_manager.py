import os
import pandas as pd
from json import loads


class scope:

    def get_scope(symbol: str = None):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
        # parent_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "..")) #local

        data_path = os.path.join(parent_dir, "inputs", "sp500_list.csv")

        df = pd.read_csv(data_path, encoding="utf-8", sep=";")

        if symbol != None:
            df = df[df["Symbol"] == symbol.upper()]

        result = df.to_json(orient="records")
        response = loads(result)

        return response
