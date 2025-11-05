from utils_info import retrieve_info
from utils_retrieve_earnings_estimate import retrieve_earnings_estimate
from utils_retrieve_earnings_history import retrieve_earnings_history
from utils_retrieve_price import retrieve_price
import pandas as pd
import numpy as np
import yfinance as yf
from curl_cffi import requests


def build_peg(my_ticker: str) -> pd.DataFrame:

    my_ticker = my_ticker.upper()

    info = retrieve_info(my_ticker)
    sector = info["sector"]
    industry = info["industry"]

    earnings_estimate = retrieve_earnings_estimate(my_ticker)
    earnings_f0 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "0y")
    ]["yearAgoEps"].values[0]
    earnings_f1 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "0y")
    ]["avg"].values[0]
    earnings_f2 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "+1y")
    ]["avg"].values[0]

    growth_f1 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "0y")
    ]["growth"].values[0]
    growth_f2 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "+1y")
    ]["growth"].values[0]

    nb_analysts_f1 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "0y")
    ]["numberOfAnalysts"].values[0]
    nb_analysts_f2 = earnings_estimate[
        (earnings_estimate["Ticker"] == my_ticker)
        & (earnings_estimate["period"] == "+1y")
    ]["numberOfAnalysts"].values[0]

    high_to_low_eps_f1 = (
        earnings_estimate[
            (earnings_estimate["Ticker"] == my_ticker)
            & (earnings_estimate["period"] == "0y")
        ]["high"].values[0]
        / earnings_estimate[
            (earnings_estimate["Ticker"] == my_ticker)
            & (earnings_estimate["period"] == "0y")
        ]["low"].values[0]
        - 1
    )
    high_to_low_eps_f2 = (
        earnings_estimate[
            (earnings_estimate["Ticker"] == my_ticker)
            & (earnings_estimate["period"] == "+1y")
        ]["high"].values[0]
        / earnings_estimate[
            (earnings_estimate["Ticker"] == my_ticker)
            & (earnings_estimate["period"] == "+1y")
        ]["low"].values[0]
        - 1
    )

    price = retrieve_price(my_ticker)
    current_price = price["Close"].iloc[-1]

    pe_f0 = current_price / earnings_f0
    pe_f1 = current_price / earnings_f1
    pe_f2 = current_price / earnings_f2

    peg_f1 = pe_f1 / growth_f1
    peg_f2 = pe_f2 / growth_f2

    earnings_history = retrieve_earnings_history(my_ticker)
    surprise_average = earnings_history[(earnings_history["Ticker"] == my_ticker)][
        "surprisePercent"
    ].mean()

    session = requests.Session(impersonate="chrome")
    balance_sheet = yf.Ticker(my_ticker, session=session).get_balance_sheet()
    fiscal_month = str(np.datetime64(balance_sheet.columns.values[0], "M"))[-2:]

    data = {
        "sector": sector,
        "industry": industry,
        "ticker": my_ticker,
        "earnings_f0": earnings_f0,
        "earnings_f1": earnings_f1,
        "earnings_f2": earnings_f2,
        "growth_f1": growth_f1,
        "growth_f2": growth_f2,
        "pe_f0": pe_f0,
        "pe_f1": pe_f1,
        "pe_f2": pe_f2,
        "peg_f1": peg_f1,
        "peg_f2": peg_f2,
        "surprise_average": surprise_average,
        "nb_analysts_f1": nb_analysts_f1,
        "nb_analysts_f2": nb_analysts_f2,
        "high_to_low_eps_f1": high_to_low_eps_f1,
        "high_to_low_eps_f2": high_to_low_eps_f2,
        "fiscal_month": fiscal_month,
    }
    output = pd.DataFrame(data, index=[0])

    return output
