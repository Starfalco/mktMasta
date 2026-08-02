import os, json
import pandas as pd

config_path = "/code/backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)


class hide_default_field:

    def __init__(self):
        self.output_path = config["path_screener_cache"]

    def get_hide_default_field(
        self,
    ):

        # To get the directory of the script/file:
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # To get one directory up from the current file
        parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
        data_path = os.path.join(parent_dir, "cache", "screener_cache.parquet")

        df = pd.read_parquet(data_path, engine="pyarrow").reset_index()

        df[
            [
                "earnings_f0",
                "earnings_f1",
                "earnings_f2",
                "growth_f1",
                "growth_f2",
                "pe_f0",
                "pe_f1",
                "pe_f2",
                "nb_analysts_f1",
                "nb_analysts_f2",
                "high_to_low_eps_f1",
                "high_to_low_eps_f2",
                "earnings_f0_industry_bench",
                "earnings_f1_industry_bench",
                "earnings_f2_industry_bench",
                "earnings_f0_sector_bench",
                "earnings_f1_sector_bench",
                "earnings_f2_sector_bench",
                "growth_f1_industry_bench",
                "growth_f2_industry_bench",
                "growth_f1_sector_bench",
                "growth_f2_sector_bench",
                "pe_f0_industry_bench",
                "pe_f1_industry_bench",
                "pe_f2_industry_bench",
                "pe_f0_sector_bench",
                "pe_f1_sector_bench",
                "pe_f2_sector_bench",
                "scoring_f0",
                "scoring_f1",
                "scoring_f2",
                "surprise_average_industry_bench",
                "surprise_average_sector_bench",
            ]
        ] = None

        df.to_parquet(self.output_path)

        return df
