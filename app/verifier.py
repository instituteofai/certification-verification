from starlette.responses import PlainTextResponse
import json
from starlette.templating import Jinja2Templates
import os

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), 'templates'))

async def handle_verification(request):
    certifications = {}
    guid = request.path_params['guid']
    certification_file = os.path.join(os.path.dirname(__file__), 'certifications.json')
    print(certification_file)
    with open(certification_file) as f:
        certifications = json.load(f)
    
    if guid in certifications:
        return templates.TemplateResponse('certification.html', { 'request': request, 'guid': guid, 'data': certifications[guid] })
    else:
        return templates.TemplateResponse('no-certification.html', { 'request': request, 'guid': guid })
