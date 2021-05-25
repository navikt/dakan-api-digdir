import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from dakan_api_digdir.routers import health, terms, dataset, apis

try:
    os.environ["PRODUCTION"]
except KeyError:
    logging.warning("Getting env variables from .env file")
    load_dotenv()

app = FastAPI()
subapi = FastAPI(docs_url="/docs", openapi_prefix="/digdir-api")

app.mount("/digdir-api", subapi)
subapi.include_router(health.router)
subapi.include_router(terms.router)
subapi.include_router(dataset.router)
subapi.include_router(apis.router)

