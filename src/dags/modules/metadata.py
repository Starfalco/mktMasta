from abc import ABC, abstractmethod

import yfinance as yf
import pandas as pd

# from deltalake.writer import write_deltalake
import multitasking
import signal
import _utils as _utils
import _shared as _shared
import json

from ...backend.src.compute_max_drawn_down.compute_max_drawn_down_manager import (
    compute_max_drawn_down as mdd,
)
from ...backend.src.retrieve_price.retrieve_price_manager import retrive_price

config_path = "dags/modules/config.json"

with open(config_path) as stream:
    config = json.load(stream)

# This is required to handle keyboard interruptions and
# to kill all threads if such an interruption occurs.
multitasking.set_max_threads(multitasking.config["CPU_CORES"])
signal.signal(signal.SIGINT, multitasking.killall)


class Metadata(ABC):
    def __init__(self, tickers):
        self.tickers = tickers  # expect list of tickers
        self.folder_path = config["Metadata_path"]
        # Check config file for IDE path

    @abstractmethod
    def transform_data(self):
        pass


class Max_Drawn_Down(Metadata, mdd):
    def __init__(self, tickers, starting_date, ending_date):
        super().__init__(tickers)
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.results = []  # list to store all results
        self.output_path = self.folder_path + "max_drawn_down.parquet"

    @multitasking.task
    def transform_data_for_ticker(self, ticker, progress=True):
        self.price = retrive_price.get_price(ticker, self.start_date, self.end_date)
        df = pd.DataFrame(
            mdd(ticker, self.starting_date, self.ending_date).get_max_drawn_down()
        )
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

        # concatenate all dataframes and write to the delta_lake file
        all_data = pd.concat(self.results)
        # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path)
