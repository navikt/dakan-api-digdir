from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from digdir_api.collections.terms import TermCollection

router = APIRouter()


@router.get("/terms")
async def get_all_terms():
    terms = await TermCollection().create()
    return JSONResponse(status_code=status.HTTP_200_OK, content=terms)
