import sys

# sys.path.append("/opt/airflow/dags/modules/")
from metadata import *

import json

config_path = "dags/modules/config.json"

with open(config_path) as stream:
    config = json.load(stream)


def get_input():
    file_ticker = config["path_inputs"]
    df_ticker = pd.read_csv(file_ticker, encoding="utf-8", sep=";")["Symbol"]
    list_ticker = list(df_ticker)

    return list_ticker


def mdd_task():
    mdd_transform = Max_Drawn_Down(
        get_input(), starting_date=config["start_date"], ending_date=config["end_date"]
    )
    mdd_transform.transform_data()


if __name__ == "__main__":

    mdd_task()
