import os
import pandas as pd


def build_peg_benchmark(my_ticker: str = None) -> pd.DataFrame:

    # To get the directory of the script/file:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # To get one directory up from the current file
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    peg_path = os.path.join(parent_dir, "metadata", "peg.parquet")
    mdd_path = os.path.join(parent_dir, "metadata", "max_drawn_down.parquet")
    vol_path = os.path.join(parent_dir, "metadata", "volatility.parquet")

    df_peg = pd.read_parquet(peg_path, engine="pyarrow").reset_index()
    df_mdd = pd.read_parquet(mdd_path, engine="pyarrow").reset_index()
    df_vol = pd.read_parquet(vol_path, engine="pyarrow").reset_index()

    df_peg_mdd = df_peg.merge(df_mdd, how="inner", on="ticker", right_index=False)
    df = df_peg_mdd.merge(df_vol, how="inner", on="ticker", right_index=False)

    df["earnings_f0_industry_bench"] = (
        df["earnings_f0"].groupby(df["industry"]).transform("mean")
    )
    df["earnings_f1_industry_bench"] = (
        df["earnings_f1"].groupby(df["industry"]).transform("mean")
    )
    df["earnings_f2_industry_bench"] = (
        df["earnings_f2"].groupby(df["industry"]).transform("mean")
    )
    df["earnings_f0_sector_bench"] = (
        df["earnings_f0"].groupby(df["sector"]).transform("mean")
    )
    df["earnings_f1_sector_bench"] = (
        df["earnings_f1"].groupby(df["sector"]).transform("mean")
    )
    df["earnings_f2_sector_bench"] = (
        df["earnings_f2"].groupby(df["sector"]).transform("mean")
    )

    df["earnings_f0_delta_industry"] = (
        df["earnings_f0"] - df["earnings_f0_industry_bench"]
    )
    df["earnings_f1_delta_industry"] = (
        df["earnings_f1"] - df["earnings_f1_industry_bench"]
    )
    df["earnings_f2_delta_industry"] = (
        df["earnings_f2"] - df["earnings_f2_industry_bench"]
    )
    df["earnings_f0_delta_sector"] = df["earnings_f0"] - df["earnings_f0_sector_bench"]
    df["earnings_f1_delta_sector"] = df["earnings_f1"] - df["earnings_f1_sector_bench"]
    df["earnings_f2_delta_sector"] = df["earnings_f2"] - df["earnings_f2_sector_bench"]

    # df['growth_f0_industry_bench'] = df['growth_f0'].groupby(df['industry']).transform('mean')
    df["growth_f1_industry_bench"] = (
        df["growth_f1"].groupby(df["industry"]).transform("mean")
    )
    df["growth_f2_industry_bench"] = (
        df["growth_f2"].groupby(df["industry"]).transform("mean")
    )
    # df['growth_f0_sector_bench'] = df['growth_f0'].groupby(df['sector']).transform('mean')
    df["growth_f1_sector_bench"] = (
        df["growth_f1"].groupby(df["sector"]).transform("mean")
    )
    df["growth_f2_sector_bench"] = (
        df["growth_f2"].groupby(df["sector"]).transform("mean")
    )

    # df['growth_f0_delta_industry'] = df['growth_f0'] - df['growth_f0_industry_bench']
    df["growth_f1_delta_industry"] = df["growth_f1"] - df["growth_f1_industry_bench"]
    df["growth_f2_delta_industry"] = df["growth_f2"] - df["growth_f2_industry_bench"]
    # df['growth_f0_delta_sector'] = df['growth_f0'] - df['growth_f0_sector_bench']
    df["growth_f1_delta_sector"] = df["growth_f1"] - df["growth_f1_sector_bench"]
    df["growth_f2_delta_sector"] = df["growth_f2"] - df["growth_f2_sector_bench"]

    df["pe_f0_industry_bench"] = df["pe_f0"].groupby(df["industry"]).transform("mean")
    df["pe_f1_industry_bench"] = df["pe_f1"].groupby(df["industry"]).transform("mean")
    df["pe_f2_industry_bench"] = df["pe_f2"].groupby(df["industry"]).transform("mean")
    df["pe_f0_sector_bench"] = df["pe_f0"].groupby(df["sector"]).transform("mean")
    df["pe_f1_sector_bench"] = df["pe_f1"].groupby(df["sector"]).transform("mean")
    df["pe_f2_sector_bench"] = df["pe_f2"].groupby(df["sector"]).transform("mean")

    df["pe_f0_delta_industry"] = df["pe_f0"] - df["pe_f0_industry_bench"]
    df["pe_f1_delta_industry"] = df["pe_f1"] - df["pe_f1_industry_bench"]
    df["pe_f2_delta_industry"] = df["pe_f2"] - df["pe_f2_industry_bench"]
    df["pe_f0_delta_sector"] = df["pe_f0"] - df["pe_f0_sector_bench"]
    df["pe_f1_delta_sector"] = df["pe_f1"] - df["pe_f1_sector_bench"]
    df["pe_f2_delta_sector"] = df["pe_f2"] - df["pe_f2_sector_bench"]

    df["pe_f1_vs_f0"] = df["pe_f1"] - df["pe_f0"]
    df["pe_f2_vs_f1"] = df["pe_f2"] - df["pe_f1"]

    df["scoring_f0"] = (
        df["earnings_f0_delta_industry"]
        + df["earnings_f0_delta_sector"]
        + df["pe_f0_delta_industry"]
        + df["pe_f0_delta_sector"]
    )

    df["scoring_f1"] = (
        df["earnings_f1_delta_industry"]
        + df["earnings_f1_delta_sector"]
        + df["pe_f1_delta_industry"]
        + df["pe_f1_delta_sector"]
    )
    +df["growth_f1_delta_industry"] + df["growth_f1_delta_sector"] + df["pe_f1_vs_f0"]

    df["scoring_f2"] = (
        df["earnings_f2_delta_industry"]
        + df["earnings_f2_delta_sector"]
        + df["pe_f2_delta_industry"]
        + df["pe_f2_delta_sector"]
    )
    +df["growth_f2_delta_industry"] + df["growth_f2_delta_sector"] + df["pe_f2_vs_f1"]

    # surprise average
    df["surprise_average_industry_bench"] = (
        df["surprise_average"].groupby(df["industry"]).transform("mean")
    )
    df["surprise_average_sector_bench"] = (
        df["surprise_average"].groupby(df["sector"]).transform("mean")
    )

    if my_ticker != None:
        df = df[df["ticker"] == my_ticker.upper()]

    return df
