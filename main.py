from data_downloader import *

file_ticker = './inputs/sp500_list.csv'
df_ticker = pd.read_csv(file_ticker,encoding='utf-8',sep=';')['Symbol']
list_ticker = list(df_ticker)

price_extract = Prices(list_ticker,'./extracts/price/','.csv', starting_date='2024-06-01', ending_date='2024-06-30')
price_extract.get_data()