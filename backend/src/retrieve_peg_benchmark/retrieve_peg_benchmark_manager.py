from ....utils.utils_retrieve_peg_benchmark import retrieve_peg_benchmark


class peg_benchmark:

    def get_peg_benchmark(symbol: str = None):
        return retrieve_peg_benchmark(symbol)
