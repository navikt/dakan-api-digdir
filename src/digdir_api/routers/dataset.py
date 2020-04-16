from typing import Type

from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from digdir_api.collections.dataset import DatasetCollection
from digdir_api.collections.catalogs import DatapackageCatalog
from digdir_api.models.model import ResponseModel

router = APIRouter()


@router.get("/dataset", response_class=ResponseModel)
async def get_all_datasets():
    datasets = await DatasetCollection().create()
    return Response(status_code=status.HTTP_200_OK, content=datasets, media_type="text/turtle")


@router.get("/datapackages", response_class=ResponseModel)
async def get_all_datapackage():
    datapackages = await DatapackageCatalog().create()
    return Response(status_code=status.HTTP_200_OK, content=datapackages, media_type="text/turtle")
