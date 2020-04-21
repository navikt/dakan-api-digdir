from fastapi import APIRouter
from fastapi.responses import Response
from fastapi import status
from digdir_api.models.model import ResponseModel
from digdir_api.collections.terms import collection

router = APIRouter()


@router.get("/terms", response_class=ResponseModel)
def get_all_terms():
    terms = collection.create_collection()
    return Response(status_code=status.HTTP_200_OK, content=terms.decode(), media_type="text/turtle")
