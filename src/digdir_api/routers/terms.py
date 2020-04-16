from fastapi import APIRouter
from fastapi.responses import Response
from fastapi import status
from digdir_api.models.model import ResponseModel
from digdir_api.collections.terms import TermCollection

router = APIRouter()


@router.get("/terms", response_class=ResponseModel)
async def get_all_terms():
    terms = await TermCollection().create()
    return Response(status_code=status.HTTP_200_OK, content=terms, media_type="text/turtle")
