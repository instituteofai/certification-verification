import os

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from app.verifier import handle_verification
from starlette.staticfiles import StaticFiles


# TODO return a form where credential GUID can be pasted for verification
async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def verify(request):
    return await handle_verification(request)


app = Starlette(routes=[
    Route('/', homepage),
    Route('/verify/{guid}', verify),
    Mount('/static', app=StaticFiles(
        directory=os.path.join(os.path.dirname(__file__), 'static')),
        name="static"
    )
])
