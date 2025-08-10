import os
import pandas as pd
from json import loads
from datetime import date
from ..extracts_price.extracts_price_manager import extracts_price


class compute_max_drawn_down:

    def __init__(self,symbol: str = None, start_date: date = None, end_date: date = None):
        self.symbol = symbol
        self.price = extracts_price.get_price(symbol,start_date,end_date)
        self.start_date = start_date
        self.end_date = end_date

    def get_max_drawn_down(self):

        try:

            df_price = pd.DataFrame(self.price)
            df_mdd = self.__build_max_drawn_down(df_price)

            df = pd.DataFrame(df_mdd.to_records())

            result = df.to_json(orient="records")
            response = loads(result)

        except Exception as e:

            response = e

        return response
    
    def __build_max_drawn_down(self,my_df):

        MDD = 0
        data = {} 
        
        for index in range(1, len(my_df)):
            gap = my_df.loc[len(my_df)-1,'Close']/my_df.loc[len(my_df) - index,'Close'] - 1
            if gap < MDD:
                
                MDD = gap
                occurrence = my_df.loc[len(my_df)-index,'Date']
                MaxPrice = my_df.loc[len(my_df)-index,'Close']
                data = {'max_drawn_down':[MDD], 'occurrence':[occurrence], 'max_price':[MaxPrice]} 
        
        output = pd.DataFrame(data, index = [0])
    
        return output