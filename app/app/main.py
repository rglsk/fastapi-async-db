from fastapi import FastAPI

from app.core.app_events import create_start_app_handler, create_stop_app_handler
from app.core.config import config
from app.api.routes import api


def get_application() -> FastAPI:
    application = FastAPI(
        title=config.SERVICE_NAME,
        description=config.DESCRIPTION,
        debug=config.DEBUG,
    )
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.include_router(api.api_router, prefix=config.API_V1_STR)
    application.include_router(api.articles_router, prefix=config.API_V1_STR)

    return application


app = get_application()
