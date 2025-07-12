from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .earnings_estimate import earnings_estimate_controller
from .earnings_history import earnings_history_controller
from .price import price_controller
from .scope import scope_controller
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

app.include_router(earnings_estimate_controller.router)
app.include_router(earnings_history_controller.router)
app.include_router(price_controller.router)
app.include_router(scope_controller.router)
