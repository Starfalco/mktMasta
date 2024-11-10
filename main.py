from data_downloader import *

file_ticker = './inputs/sp500_list.csv'
df_ticker = pd.read_csv(file_ticker,encoding='utf-8',sep=';')['Symbol']
list_ticker = list(df_ticker)

# price_extract = Prices(list_ticker, starting_date='2024-06-01', ending_date='2024-06-30')
# price_extract.get_data()

# earnings_estimate_extract = Earnings_Estimate(list_ticker)
# earnings_estimate_extract.get_data()

earnings_estimate_extract = Earnings_History(list_ticker)
earnings_estimate_extract.get_data()

# info_extract = Info(list_ticker)
# info_extract.get_data()