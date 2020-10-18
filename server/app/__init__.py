from fastapi import FastAPI

from app import settings
from app.api import api_router
from app.db import startup_db, shutdown_db

__version__ = "0.1.0"
app = FastAPI(
    debug=settings.DEBUG,
    version=__version__,
    on_startup=[startup_db],
    on_shutdown=[shutdown_db],
)
app.include_router(api_router, prefix=settings.API_V1_STR)
