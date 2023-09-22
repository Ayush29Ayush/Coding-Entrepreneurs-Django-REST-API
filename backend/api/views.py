import json
from django.http import JsonResponse


# def api_home(request, *args, **kwargs):
#     return JsonResponse({"message": "Hi there, this is your Django API response!!"})

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET) # url query params
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    # print(data.keys())
    # data['headers'] = request.headers # request.META ->
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)

{'query': 'Hello world', 'params': {'abc': ['123']}, 'headers': {'Content-Length': '24', 'Content-Type': 'application/json', 'Host': 'localhost:8000', 'User-Agent': 'python-requests/2.31.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}, 'content_type': 'application/json'}