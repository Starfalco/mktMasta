from abc import ABC, abstractmethod

import yfinance as yf
import pandas as pd

# from deltalake.writer import write_deltalake
# import requests
# from bs4 import BeautifulSoup
# from getuseragent import UserAgent
import multitasking
import signal
import _utils as _utils
import _shared as _shared
from requests_ratelimiter import LimiterSession, RequestRate, Limiter, Duration

import json

config_path = "dags/modules/config.json"

with open(config_path) as stream:
    config = json.load(stream)

# This is required to handle keyboard interruptions and
# to kill all threads if such an interruption occurs.
multitasking.set_max_threads(multitasking.config["CPU_CORES"])
signal.signal(signal.SIGINT, multitasking.killall)


class Extract(ABC):
    def __init__(self, tickers):
        self.tickers = tickers  # expect list of tickers
        self.request_rate = RequestRate(int(config["request_rate"]), Duration.SECOND)
        self.limiter = Limiter(self.request_rate)
        self.session = LimiterSession(limiter=self.limiter)
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        self.folder_path = config["extract_path"]
        # Check config file for IDE path

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
        # write_deltalake(self.output_path, yf.download(self.tickers, start = self.starting_date, end = self.ending_date, group_by = 'ticker').stack(level=0), mode='overwrite')
        yf.download(
            self.tickers,
            start=self.starting_date,
            end=self.ending_date,
            group_by="ticker",
            session=self.session,
        ).stack(level=0).to_parquet(self.output_path)


class Earnings_Estimate(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "earnings_estimate.parquet"

    @multitasking.task
    def get_data_for_ticker(self, ticker, progress=True):
        df = pd.DataFrame(
            yf.Ticker(ticker, session=self.session).get_earnings_estimate()
        )
        df["Ticker"] = ticker  # add a column for ticker name
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
        # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path)


class Earnings_History(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "earnings_history.parquet"

    @multitasking.task
    def get_data_for_ticker(self, ticker, progress=True):
        df = pd.DataFrame(
            yf.Ticker(ticker, session=self.session).get_earnings_history()
        )
        df["Ticker"] = ticker  # add a column for ticker name
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
        # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path)


class Info(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "info.parquet"

    @multitasking.task
    def get_data_for_ticker(self, ticker, progress=True):

        try:
            industry = yf.Ticker(ticker, session=self.session).get_info()["industry"]
        except:
            industry = "unknown"
        try:
            sector = yf.Ticker(ticker, session=self.session).get_info()["sector"]
        except:
            sector = "unknown"
        df = pd.DataFrame.from_records(
            {"Ticker": [ticker], "industry": [industry], "sector": [sector]}
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
        # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path, index=False)
