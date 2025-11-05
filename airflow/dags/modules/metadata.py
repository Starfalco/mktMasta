import json

config_path = "/opt/airflow/dags/modules/config.json"

with open(config_path) as stream:
    config = json.load(stream)

from abc import ABC, abstractmethod
import pandas as pd

# from deltalake.writer import write_deltalake
import multitasking
import signal
import sys

# setting path
sys.path.append(config["path_modules"])

import _utils
import _shared

# setting path
sys.path.append(config["path_utils"])

# importing
from utils_max_drawn_down import build_max_drawn_down as mdd
from utils_volatility import build_volatility as vol
from utils_retrieve_price import retrieve_price
from utils_peg import build_peg

# This is required to handle keyboard interruptions and
# to kill all threads if such an interruption occurs.
multitasking.set_max_threads(multitasking.config["CPU_CORES"])
signal.signal(signal.SIGINT, multitasking.killall)


class Metadata(ABC):
    def __init__(self, tickers):
        self.tickers = tickers  # expect list of tickers
        self.folder_path = config["metadata_path"]
        # Check config file for IDE path

    @abstractmethod
    def transform_data(self):
        pass


class Max_Drawn_Down(Metadata):
    def __init__(self, tickers, starting_date, ending_date):
        super().__init__(tickers)
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "max_drawn_down.parquet"

    @multitasking.task
    def transform_data_for_ticker(self, ticker, progress=True):
        self.price = retrieve_price(ticker)
        df = mdd(self.price)
        df["Ticker"] = ticker  # add a column for ticker name
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def transform_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.transform_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        try:
            # concatenate all dataframes and write to the delta_lake file
            all_data = pd.concat(self.results)
        except:
            all_data = pd.DataFrame(self.results)
            # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path)


class Volatility(Metadata):
    def __init__(self, tickers, starting_date, ending_date):
        super().__init__(tickers)
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "volatility.parquet"

    @multitasking.task
    def transform_data_for_ticker(self, ticker, progress=True):
        self.price = retrieve_price(ticker)
        df = vol(self.price)
        df["Ticker"] = ticker  # add a column for ticker name
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def transform_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.transform_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        try:
            # concatenate all dataframes and write to the delta_lake file
            all_data = pd.concat(self.results)
        except:
            all_data = pd.DataFrame(self.results)
            # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path)


class peg(Metadata):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "peg.parquet"

    @multitasking.task
    def transform_data_for_ticker(self, ticker, progress=True):
        # self.price = retrieve_price(ticker)
        df = build_peg(ticker)
        self.results.append(df)

        if progress:
            _shared._PROGRESS_BAR.animate()

    def transform_data(self, progress=True):

        if progress:
            _shared._PROGRESS_BAR = _utils.ProgressBar(len(self.tickers), "completed")

        for ticker in self.tickers:
            self.transform_data_for_ticker(ticker, progress=(progress))

        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        try:
            # concatenate all dataframes and write to the delta_lake file
            all_data = pd.concat(self.results)
        except:
            all_data = pd.DataFrame(self.results)
            # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path)
