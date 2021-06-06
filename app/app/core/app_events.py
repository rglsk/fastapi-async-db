import logging
from typing import Callable

from fastapi import FastAPI


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        from app.db.base import database

        logging.info("connecting to a database")
        await database.connect()
        logging.info("Database connection - successful")

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        from app.db.base import database

        logging.info("Closing connection to database")
        await database.disconnect()
        logging.info("Database connection - closed")

    return stop_app
