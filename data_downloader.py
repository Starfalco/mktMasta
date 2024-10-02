import yfinance as yf
import pandas as pd
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from getuseragent import UserAgent

class Extract(ABC):
    def __init__(self, ticker, output_path, output_type):
        self.ticker = ticker
        self.output_path = output_path
        self.output_type = output_type

    @abstractmethod
    def get_data(self):
        pass

class Prices(Extract):
    def __init__(self, ticker, output_path, output_type, starting_date, ending_date):
        super().__init__(ticker, output_path, output_type)
        self.starting_date = starting_date
        self.ending_date = ending_date

    def get_data(self):
        yf.download(self.ticker, start = self.starting_date, end = self.ending_date, group_by = 'ticker').stack(level=0).to_csv(self.output_path + 'price' + self.output_type, encoding = 'utf-8', sep = ';')

class Earnings(Extract):
    def __init__(self, ticker, output_path, output_type):
        super().__init__(ticker, output_path, output_type)

    def get_data(self):
        yf.download(self.ticker, start = self.starting_date, end = self.ending_date, group_by = 'ticker').stack(level=0).to_csv(self.output_path + 'price' + self.output_type, encoding = 'utf-8', sep = ';')
