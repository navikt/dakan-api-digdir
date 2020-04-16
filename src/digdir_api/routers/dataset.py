from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from digdir_api.collections.dataset import DatasetCollection
from digdir_api.collections.catalogs import DatapackageCatalog

router = APIRouter()


@router.get("/dataset")
async def get_all_datasets():
    datasets = await DatasetCollection().create()
    return Response(status_code=status.HTTP_200_OK, content=datasets, media_type="text/turtle")


@router.get("/datapackage")
async def get_all_datapackage():
    datapackage = await DatapackageCatalog().create()
    return Response(status_code=status.HTTP_200_OK, content=datapackage, media_type="text/turtle")
