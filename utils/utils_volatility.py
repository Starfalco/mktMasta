import pandas as pd


def build_volatility(my_df: pd.DataFrame) -> pd.DataFrame:

    # initializing daily_perf_df_concat
    daily_perf_df_concat = pd.DataFrame()
    try:
        for index in range(0, len(my_df) - 1):

            daily_perf = my_df.loc[index + 1, "close"] / my_df.loc[index, "close"] - 1
            daily_perf_dict = {"daily_perf": [daily_perf]}
            daily_perf_df = pd.DataFrame(daily_perf_dict, index=[index])

            daily_perf_df_concat = pd.concat(
                [daily_perf_df_concat, daily_perf_df],
            )

        volatility = daily_perf_df_concat["daily_perf"].std()
        volatility_dict = {"volatility": volatility}
    except:
        volatility_dict = {"volatility": None}

    volatility_df = pd.DataFrame(volatility_dict, index=[0])

    return volatility_df
