import os
import pandas as pd


def retrieve_info(symbol: str) -> pd.DataFrame:

    # To get the directory of the script/file:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # To get one directory up from the current file
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    data_path = os.path.join(parent_dir, "extracts", "info.parquet")

    df = pd.read_parquet(data_path, engine="pyarrow")
    df = pd.DataFrame(df.to_records())
    df = df[df["Ticker"] == symbol.upper()].reset_index()

    return df
