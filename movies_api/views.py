from django.http import HttpResponse


def index(request):
    message = """
    <h3>Django REST API Movies</h3>
    <p><a href="/api">/api</a></p>
    <p><a href="/admin">/admin</a></p>
    """
    return HttpResponse(message)
