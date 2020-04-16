from starlette.responses import Response


class ResponseModel(Response):
    media_type = "text/turtle"
