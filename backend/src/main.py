from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .retrieve_earnings_estimate import retrieve_earnings_estimate_controller
from .retrieve_earnings_history import retrieve_earnings_history_controller
from .retrieve_price import retrieve_price_controller
from .retrieve_scope import retrieve_scope_controller
from .extracts_price import extracts_price_controller
from .extract_earnings_dates import extracts_earnings_dates_controller
from .compute_max_drawn_down import compute_max_drawn_down_controller
from .compute_volatility import compute_volatility_controller
from .compute_peg import compute_peg_controller
from .compute_peg_benchmark import compute_peg_benchmark_controller
import json

config_path = "backend/src/config.json"

with open(config_path) as stream:
    config = json.load(stream)

app = FastAPI()

origins = config["fastapi_origins"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=config["allow_methods"],
    allow_headers=[],
)

app.include_router(retrieve_earnings_estimate_controller.router)
app.include_router(retrieve_earnings_history_controller.router)
app.include_router(retrieve_price_controller.router)
app.include_router(retrieve_scope_controller.router)
app.include_router(extracts_price_controller.router)
app.include_router(extracts_earnings_dates_controller.router)
app.include_router(compute_max_drawn_down_controller.router)
app.include_router(compute_volatility_controller.router)
app.include_router(compute_peg_controller.router)
app.include_router(compute_peg_benchmark_controller.router)
