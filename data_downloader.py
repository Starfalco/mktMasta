import yfinance as yf
import pandas as pd
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from getuseragent import UserAgent
import multitasking
import signal
import utils
import shared

# This is required to handle keyboard interruptions and
# to kill all threads if such an interruption occurs.
multitasking.set_max_threads(multitasking.config['CPU_CORES'])
signal.signal(signal.SIGINT, multitasking.killall)

class Extract(ABC):
    def __init__(self, tickers, output_path, output_type):
        self.tickers = tickers  # expect list of tickers
        self.output_path = output_path
        self.output_type = output_type
    
    @abstractmethod
    def get_data(self):
        pass

class Prices(Extract):
    def __init__(self, tickers, output_path, output_type, starting_date, ending_date):
        super().__init__(tickers, output_path, output_type)
        self.starting_date = starting_date
        self.ending_date = ending_date

    def get_data(self):
        yf.download(self.tickers, start = self.starting_date, end = self.ending_date, group_by = 'ticker').stack(level=0).to_csv(self.output_path + 'price' + self.output_type, encoding = 'utf-8', sep = ';')

class Earnings(Extract):
    def __init__(self, tickers, output_path, output_type):
        super().__init__(tickers, output_path, output_type)
        self.results = []  # list to store all results

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
        
        # wait for all tasks to finish before writing the results to a CSV file
        multitasking.wait_for_tasks()

        # concatenate all dataframes and write to the CSV file
        all_data = pd.concat(self.results)
        all_data.to_csv(self.output_path + 'earnings_estimate' + self.output_type, encoding = 'utf-8', sep = ';')
