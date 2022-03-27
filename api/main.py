from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.events import create_start_app_handler, create_stop_app_handler
from api.routes.api import router as api_router

from settings import MONGO_DB as db_settings


def get_application() -> FastAPI:
    application = FastAPI()

    # Allow everything for connection
    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    # Basically create db connection
    application.add_event_handler(
        'startup', create_start_app_handler(application, db_settings),
    )
    # Basically close db connection
    application.add_event_handler(
        'shutdown', create_stop_app_handler(application),
    )

    application.include_router(api_router, prefix='/api')

    return application


app = get_application()
