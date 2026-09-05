from abc import ABC, abstractmethod
import json, os, sys

import yfinance as yf
import pandas as pd

import multitasking
import signal
import _utils
import _shared
from curl_cffi import requests

# To get the directory of the script/file:
current_dir = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(current_dir, "config.json")

with open(config_path) as stream:
    config = json.load(stream)

# setting path
sys.path.append(config["path_utils"])

# importing
from utils_yfinance import download_price
from rate_limiter import RateLimiter

# Create rate limiter from config
rate_limiter = RateLimiter(
    request_delay=1.0 / int(config.get("request_rate", 2)),
    max_retries=int(config.get("max_retries", 3)),
    base_delay=float(config.get("base_delay", 2.0)),
    max_delay=float(config.get("max_delay", 60.0)),
)

# This is required to handle keyboard interruptions and
# to kill all threads if such an interruption occurs.
multitasking.set_max_threads(int(config.get("cpu_cores", 4)))
signal.signal(signal.SIGINT, multitasking.killall)


class Extract(ABC):
    def __init__(self, tickers):
        self.tickers = tickers  # expect list of tickers
        self.session = rate_limiter.get_session()
        self.folder_path = config["extract_path"]

    @abstractmethod
    def get_data(self):
        pass


class Prices(Extract):
    def __init__(self, tickers, starting_date, ending_date):
        super().__init__(tickers)
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.output_path = self.folder_path + "price.parquet"

    def get_data(self):
        download_price(
            self.tickers,
            self.starting_date,
            self.ending_date,
            self.session,
        ).to_parquet(self.output_path,engine="pyarrow")


class Earnings_Estimate(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "earnings_estimate.parquet"

    @multitasking.task
    @rate_limiter.retry_on_rate_limit()
    def get_data_for_ticker(self, ticker, progress=True):
        df = pd.DataFrame(
            yf.Ticker(ticker, session=self.session).get_earnings_estimate()
        )
        df["ticker"] = ticker  # add a column for ticker name
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def get_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.get_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        # concatenate all dataframes and write to the delta_lake file
        all_data = pd.concat(self.results)
        all_data.to_parquet(self.output_path,engine="pyarrow")


class Earnings_Dates(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "earnings_dates.parquet"

    @multitasking.task
    @rate_limiter.retry_on_rate_limit()
    def get_data_for_ticker(self, ticker, progress=True):
        df = pd.DataFrame(yf.Ticker(ticker, session=self.session).get_calendar())
        df["ticker"] = ticker  # add a column for ticker name
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def get_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.get_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        # concatenate all dataframes and write to the delta_lake file
        all_data = pd.concat(self.results)
        all_data.to_parquet(self.output_path,engine="pyarrow")


class Earnings_History(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "earnings_history.parquet"

    @multitasking.task
    @rate_limiter.retry_on_rate_limit()
    def get_data_for_ticker(self, ticker, progress=True):
        df = pd.DataFrame(
            yf.Ticker(ticker, session=self.session).get_earnings_history()
        )
        df["ticker"] = ticker  # add a column for ticker name
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def get_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.get_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        # concatenate all dataframes and write to the delta_lake file
        all_data = pd.concat(self.results)
        all_data.to_parquet(self.output_path,engine="pyarrow")


class Info(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "info.parquet"

    @multitasking.task
    @rate_limiter.retry_on_rate_limit()
    def get_data_for_ticker(self, ticker, progress=True):

        # try:
        industry = yf.Ticker(ticker, session=self.session).get_info()["industry"]
        # except:
        #     industry = "unknown"
        # try:
        sector = yf.Ticker(ticker, session=self.session).get_info()["sector"]
        # except:
        #     sector = "unknown"
        df = pd.DataFrame.from_records(
            {"ticker": [ticker], "industry": [industry], "sector": [sector]}
        )
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def get_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.get_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        # concatenate all dataframes and write to the delta_lake file
        all_data = pd.concat(self.results)
        all_data.to_parquet(self.output_path, index=False)
