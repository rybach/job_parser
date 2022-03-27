import pymongo
from fastapi import FastAPI


def connect_to_db(app: FastAPI, db_settings: dict) -> None:
    app.client = pymongo.MongoClient(db_settings['uri'])
    app.db = app.client[db_settings['db_name']]
    app.collection = app.db.vacancies


def close_db_connection(app: FastAPI) -> None:
    app.client.close()
