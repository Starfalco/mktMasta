import sys, os, json
from datetime import date

sys.path.append("/opt/airflow/dags/modules/")
from metadata import *
from rate_limiter import default_rate_limiter

# To get the directory of the script/file:
current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_dir, "config.json")

with open(config_path) as stream:
    config = json.load(stream)


def _get_date_range():
    """Return (starting_date, ending_date) as YYYY-MM-DD strings.

    ending_date = today
    starting_date = 6 months before ending_date
    """
    today = date.today()
    # Subtract 6 months (handle year boundary correctly)
    month = today.month - 6
    year = today.year
    if month <= 0:
        month += 12
        year -= 1
    starting = today.replace(year=year, month=month)
    return starting.isoformat(), today.isoformat()


def get_input():
    file_ticker = config["path_inputs"]
    df_ticker = pd.read_csv(file_ticker, encoding="utf-8", sep=";")["Symbol"]
    list_ticker = list(df_ticker)

    return list_ticker


def mdd_task():
    starting_date, ending_date = _get_date_range()
    mdd_transform = Max_Drawn_Down(
        get_input(), starting_date=starting_date, ending_date=ending_date
    )
    mdd_transform.transform_data()


def volatility_task():
    starting_date, ending_date = _get_date_range()
    volatility_transform = Volatility(
        get_input(), starting_date=starting_date, ending_date=ending_date
    )
    volatility_transform.transform_data()


def peg_task():
    peg_transform = peg(get_input())
    peg_transform.transform_data()


def peg_benchmark_task():
    peg_transform = peg_benchmark(get_input())
    peg_transform.transform_data()


if __name__ == "__main__":

    mdd_task()
