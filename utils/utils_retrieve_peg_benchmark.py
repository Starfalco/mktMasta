import os
import pandas as pd


def retrieve_peg_benchmark(symbol: str = None) -> pd.DataFrame:

    # To get the directory of the script/file:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # To get one directory up from the current file
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    data_path = os.path.join(parent_dir, "metadata", "peg_benchmark.parquet")

    df = pd.read_parquet(data_path, engine="pyarrow").reset_index()
    df.rename(columns={"index": "period"}, inplace=True)

    if symbol != None:
        df = df[df["ticker"] == symbol.upper()]

    return df
