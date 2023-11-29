from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

async def home(request:Request):
    return JSONResponse({"message": "Hello, world!"})

app = Starlette(
    debug = True, 
    routes = [
        Route("/", home)
    ]
)