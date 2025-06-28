import sys

sys.path.append("/opt/airflow/dags/modules/")
from data_downloader import *

import json

config_path = "dags/modules/config.json"

with open(config_path) as stream:
    config = json.load(stream)


def prices_task():

    price_extract = Prices(
        get_input(), starting_date=config["start_date"], ending_date=config["end_date"]
    )
    price_extract.get_data()


def earnings_estimate_task():

    earnings_estimate_extract = Earnings_Estimate(get_input())
    earnings_estimate_extract.get_data()


def earnings_history_task():

    earnings_history_extract = Earnings_History(get_input())
    earnings_history_extract.get_data()


def info_task():

    info_extract = Info(get_input())
    info_extract.get_data()


def get_input():
    file_ticker = config["path_inputs"]
    df_ticker = pd.read_csv(file_ticker, encoding="utf-8", sep=";")["Symbol"]
    list_ticker = list(df_ticker)

    return list_ticker


if __name__ == "__main__":

    prices_task()
    # earnings_estimate_task()
    # earnings_history_task()
    # info_task()
