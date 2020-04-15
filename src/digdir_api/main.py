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

app = FastAPI(docs_url=None, redoc_url=None, swagger_static={"favicon": "/digdir-api/static/favicon.png"})

app.mount("/digdir-api/static", StaticFiles(directory="src/digdir_api/static"), name="static")


@app.get("/digdir-api/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="/digdir-api/static/swagger-ui-bundle.js",
        swagger_css_url="/digdir-api/static/swagger-ui.css",
    )

app.include_router(health.router)
app.include_router(terms.router)
app.include_router(dataset.router)
