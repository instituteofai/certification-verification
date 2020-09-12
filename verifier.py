from starlette.responses import PlainTextResponse
import json
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

async def handle_verification(request):
    certifications = {}
    guid = request.path_params['guid']
    with open('certifications.json') as f:
        certifications = json.load(f)
    
    if guid in certifications:
        return templates.TemplateResponse('certification.html', { 'request': request, 'guid': guid, 'data': certifications[guid] })
    else:
        return templates.TemplateResponse('no-certification.html', { 'request': request, 'guid': guid })
