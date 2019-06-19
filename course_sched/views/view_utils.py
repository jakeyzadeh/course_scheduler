import json
from django.http import HttpResponse

def render_to_json(request, data):
    ''' renders an http response with json data '''
    return HttpResponse(
        json.dumps(data, ensure_ascii=False),
        mimetype=request.is_ajax() and "application/json" or "text/html"
    )
