import sys
sys.path.append("/opt/airflow/dags/modules/")
from data_downloader import *

def prices_task():

    price_extract = Prices(get_input(), starting_date='2024-06-01', ending_date='2024-06-30')
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
    file_ticker = '/inputs/sp500_list.csv'
    # file_ticker = 'inputs/sp500_list.csv' # uncomment for ide run
    df_ticker = pd.read_csv(file_ticker,encoding='utf-8',sep=';')['Symbol']
    list_ticker = list(df_ticker)

    return list_ticker

if __name__ == '__main__':

    # prices_task()
    # earnings_estimate_task()
    # earnings_history_task()
    info_task()