import json

from django.http import HttpResponse
#                       ^^^^ There is also a JsonResponse that does the trick nicely
from internetOfSwings import models


def index(request):
    return HttpResponse(
        json.dumps(
            {'hello': 'world'},
            sort_keys=True,
            indent=4,
        )
    )


def plot_swing(request, swing_uuid):
    swing = models.Swing.objects.all()[0]
    response = HttpResponse(content_type="image/png")
    swing.plot_to_file(response)
    return response
