import os
import pandas as pd


def retrieve_naics(symbol: str) -> pd.DataFrame:

    # To get the directory of the script/file:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # To get one directory up from the current file
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    data_path = os.path.join(parent_dir, "inputs", "sp500_list.csv")

    df = pd.read_csv(
        data_path,
        dtype={
            "Company": str,
            "Symbol": str,
            "NAICS_Level_2_Code": str,
            "NAICS_Level_2_Subsector_Title": str,
        },
        sep=";",
        encoding="utf-8"
    )
    df = pd.DataFrame(df.to_records())
    df = df[df["Symbol"] == symbol.upper()].reset_index()

    return df
