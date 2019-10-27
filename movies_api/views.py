from django.http import HttpResponse


def index(request):
    message = "<h3>Django REST API Movies</h3>"
    return HttpResponse(message)
