from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .retrieve_earnings_estimate import retrieve_earnings_estimate_controller
from .retrieve_earnings_history import retrieve_earnings_history_controller
from .retrieve_price import retrieve_price_controller
from .retrieve_scope import retrieve_scope_controller
from .extracts_price import extracts_price_controller
import json

config_path = "src/config.json"

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
