import json

from django.http import HttpResponse
#                       ^^^^ There is also a JsonResponse that does the trick nicely

def index(request):
    return HttpResponse(
        json.dumps(
            {'hello': 'world'},
            sort_keys=True,
            indent=4,
        )
    )