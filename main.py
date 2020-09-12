from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from verifier import handle_verification

# TODO return a form where credential GUID can be pasted for verification
async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def verify(request):
    return await handle_verification(request)


app = Starlette(routes=[Route('/', homepage), Route('/verify/{guid}', verify)])
