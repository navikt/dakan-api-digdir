from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/digdir-api/isAlive", include_in_schema=False)
async def is_alive_status():
    """
    Alive check
    """
    return JSONResponse(status_code=status.HTTP_200_OK, content={})


@router.get("/digdir-api/isReady", include_in_schema=False)
async def is_ready_status():
    """
    Ready check
    """
    return JSONResponse(status_code=status.HTTP_200_OK, content={})
