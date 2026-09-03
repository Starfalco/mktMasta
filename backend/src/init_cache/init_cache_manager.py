from .. import settings
from ....utils.utils_retrieve_peg_benchmark import retrieve_peg_benchmark


class init_cache:

    def __init__(self):
        self.output_path = settings.path_screener_cache

    def get_init_cache(self):
        df = retrieve_peg_benchmark(None)
        df.drop("level_0",axis="columns").to_parquet(self.output_path,engine="pyarrow")
