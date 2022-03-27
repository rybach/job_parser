from typing import Callable
from fastapi import FastAPI

from api.db import connect_to_db, close_db_connection


def create_start_app_handler(app: FastAPI, db_settings: dict) -> Callable:
    def start_app() -> None:
        connect_to_db(app, db_settings)

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    def stop_app() -> None:
        close_db_connection(app)

    return stop_app
