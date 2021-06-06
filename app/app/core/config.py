import os
from functools import lru_cache
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class GlobalConfig(BaseSettings):
    DESCRIPTION = "App description"
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "UTC"
    SERVICE_NAME = "AppService"
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "DEV")
    API_V1_STR: str = "/api/v1"

    # Database config
    DATABASE_URL: Optional[PostgresDsn] = os.environ.get(
        "DATABASE_URL", "postgres://postgres:postgres@0.0.0.0:5432/postgres"
    )
    DB_MIN_SIZE: int = 2
    DB_MAX_SIZE: int = 15
    DB_FORCE_ROLL_BACK: bool = False


class DevConfig(GlobalConfig):
    DESCRIPTION = "Dev app description"
    DEBUG = True


class TestConfig(GlobalConfig):
    DESCRIPTION = "Dev app description"
    DEBUG = True
    TESTING = True
    DB_FORCE_ROLL_BACK = True


class FactoryConfig:
    """Returns a config instance depends on the ENV_STATE variable."""

    def __init__(self, environment: Optional[str] = "DEV"):
        self.environment = environment

    def __call__(self):
        if self.environment == "TEST":
            return TestConfig()
        return DevConfig()


@lru_cache()
def get_configuration():
    return FactoryConfig(GlobalConfig().ENVIRONMENT)()


config = get_configuration()
