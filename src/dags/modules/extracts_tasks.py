import sys, os
import json

# sys.path.append("/opt/airflow/dags/modules/")
from data_downloader import *


# To get the directory of the script/file:
current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_dir, "config.json")

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


def earnings_dates_task():

    earnings_dates_extract = Earnings_Dates(get_input())
    earnings_dates_extract.get_data()


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
