from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
from digdir_api.collections.dataset import DatasetCollection

router = APIRouter()


@router.get("/dataset")
async def get_all_datasets():
    datasets = await DatasetCollection().create()
    return Response(status_code=status.HTTP_200_OK, content=datasets, media_type="text/turtle")
