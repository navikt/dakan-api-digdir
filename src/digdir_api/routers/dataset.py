from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from digdir_api.collections.dataset import DatasetCollection

router = APIRouter()


@router.get("/digdir-api/dataset")
async def get_all_datasets():
    datasets = await DatasetCollection().create()
    return JSONResponse(status_code=status.HTTP_200_OK, content=datasets)
