from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


def _split_csv(value: str) -> List[str]:
    """Split a comma-separated string into a list, stripping whitespace."""
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


class Settings(BaseSettings):
    """Centralized configuration using environment variables with defaults."""

    # CORS settings — accept comma-separated string from env, stored as list
    # Override via FASTAPI_ORIGINS env var for production
    fastapi_origins_raw: str = (
        "http://localhost,"
        "http://localhost:8080,"
        "http://localhost:4200,"
        "http://localhost:8000"
    )
    allow_methods_raw: str = "GET,POST,PUT,DELETE"

    # File paths
    path_utils: str = "/code/utils/"
    path_screener_cache: str = "/code/backend/src/cache/screener_cache.parquet"

    # Frontend config (served via /config.json endpoint)
    frontend_base_url: str = ""  # Empty = use relative paths (recommended for prod)

    @property
    def fastapi_origins(self) -> List[str]:
        return _split_csv(self.fastapi_origins_raw)

    @property
    def allow_methods(self) -> List[str]:
        return _split_csv(self.allow_methods_raw)

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }

    def get_frontend_config(self) -> dict:
        """Generate the frontend config JSON."""
        base_url = self.frontend_base_url
        if not base_url:
            # When empty, frontend should use relative paths
            return {
                "backendApi": {
                    "baseUrl": "",
                    "httpHeader": "Content-Type: application/json",
                    "endpointInitCache": "cache/init_cache",
                    "endpointRetrieveCache": "cache/retrieve_cache",
                    "endpointFilterFieldUniqueValues": "filter/filter_field_unique_values",
                    "endpointFilterStringField": "filter/filter_string_field"
                }
            }
        return {
            "backendApi": {
                "baseUrl": base_url,
                "httpHeader": "Content-Type: application/json",
                "endpointInitCache": "cache/init_cache",
                "endpointRetrieveCache": "cache/retrieve_cache",
                "endpointFilterFieldUniqueValues": "filter/filter_field_unique_values",
                "endpointFilterStringField": "filter/filter_string_field"
            }
        }


@lru_cache()
def get_settings() -> Settings:
    """Cached settings instance — call once at app startup."""
    return Settings()


settings = get_settings()
