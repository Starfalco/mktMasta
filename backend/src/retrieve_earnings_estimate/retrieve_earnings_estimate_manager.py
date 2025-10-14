from ....utils.utils_retrieve_earnings_estimate import retrieve_earnings_estimate


class earnings_estimate:

    def get_earnings_estimate(symbol: str = None):
        return retrieve_earnings_estimate(symbol)
