import pandas as pd


def build_volatility(my_df: pd.DataFrame) -> pd.DataFrame:

    Vol_Vector = pd.DataFrame()
    try:
        for index in range(0, len(my_df) - 1):

            Dayli_Perf = my_df.loc[index + 1, "Close"] / my_df.loc[index, "Close"] - 1
            Dayli_Perf = {"Dayli_Perf": [Dayli_Perf]}
            Dayli_Perf = pd.DataFrame(Dayli_Perf, index=[index])

            Vol_Vector = pd.concat([Vol_Vector, Dayli_Perf])

        Vol = Vol_Vector["Dayli_Perf"].std()
        data = {"volatility": Vol}
    except:
        data = {"volatility": None}

    output = pd.DataFrame(data, index = [0])

    return output
