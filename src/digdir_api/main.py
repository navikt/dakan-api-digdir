import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from digdir_api.routers import health, terms, dataset
from fastapi.openapi.docs import get_swagger_ui_html

try:
    os.environ["PRODUCTION"]
except KeyError:
    logging.warning("Getting env variables from .env file")
    load_dotenv()

app = FastAPI(docs_url="/digdir-api/docs")

app.include_router(health.router)
app.include_router(terms.router)
app.include_router(dataset.router)
