from abc import ABC, abstractmethod

import yfinance as yf
import pandas as pd
# from deltalake.writer import write_deltalake
# import requests
# from bs4 import BeautifulSoup
# from getuseragent import UserAgent
import multitasking
import signal
import utils
import shared

# This is required to handle keyboard interruptions and
# to kill all threads if such an interruption occurs.
multitasking.set_max_threads(multitasking.config['CPU_CORES'])
signal.signal(signal.SIGINT, multitasking.killall)

class Extract(ABC):
    def __init__(self, tickers):
        self.tickers = tickers  # expect list of tickers
    
    @abstractmethod
    def get_data(self):
        pass

class Prices(Extract):
    def __init__(self, tickers, starting_date, ending_date):
        super().__init__(tickers)
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.output_path = 'extracts/price.parquet'

    def get_data(self):
        # write_deltalake(self.output_path, yf.download(self.tickers, start = self.starting_date, end = self.ending_date, group_by = 'ticker').stack(level=0), mode='overwrite')
        yf.download(self.tickers, start = self.starting_date, end = self.ending_date, group_by = 'ticker').stack(level=0).to_parquet(self.output_path)

class Earnings_Estimate(Extract):
    def __init__(self, tickers):
        super().__init__(tickers)
        self.results = []  # list to store all results
        self.output_path = 'extracts/earnings_estimate.parquet'

    @multitasking.task
    def get_data_for_ticker(self, ticker, progress=True):
        df = pd.DataFrame(yf.Ticker(ticker).get_earnings_estimate())
        df['Ticker'] = ticker  # add a column for ticker name
        self.results.append(df)

        if progress:
            shared._PROGRESS_BAR.animate()

    def get_data(self, progress=True):

        if progress:
            shared._PROGRESS_BAR = utils.ProgressBar(len(self.tickers), 'completed')

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
        self.output_path = 'extracts/info.parquet'

    @multitasking.task
    def get_data_for_ticker(self, ticker, progress=True):

        try:
            industry = yf.Ticker(ticker).get_info()['industry']
        except:
            industry = 'unknown'
        try:
            sector = yf.Ticker(ticker).get_info()['sector']
        except:
            sector = 'unknown'
        df = pd.DataFrame.from_records({"Ticker": [ticker], "industry": [industry], "sector": [sector]})
        self.results.append(df)

        if progress:
            shared._PROGRESS_BAR.animate()

    def get_data(self, progress=True):

        if progress:
            shared._PROGRESS_BAR = utils.ProgressBar(len(self.tickers), 'completed')

        for ticker in self.tickers:
            self.get_data_for_ticker(ticker, progress=(progress))
        
        # wait for all tasks to finish before writing the results to a delta_lake file
        multitasking.wait_for_tasks()

        # concatenate all dataframes and write to the delta_lake file
        all_data = pd.concat(self.results)
        # write_deltalake(self.output_path, all_data, mode='overwrite')
        all_data.to_parquet(self.output_path,index=False)
