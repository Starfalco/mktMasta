from ....utils.utils_retrieve_earnings_history import retrieve_earnings_history


class earnings_history:

    def get_earnings_history(symbol: str):
        return retrieve_earnings_history(symbol)
