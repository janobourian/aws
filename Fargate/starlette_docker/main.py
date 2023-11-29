from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse
import asyncio
import random


async def home(request: Request):
    return JSONResponse({"message": "Hello, world!"})


async def rabbit(request: Request):
    number = random.choice([i for i in range(15)])
    await asyncio.sleep(number)
    return JSONResponse({"message": "Follow the rabbit!", "time_awaited": number})


routes = [
    Route("/", home),
    Route("/rabbit", rabbit),
]

app = Starlette(debug=True, routes=routes)
