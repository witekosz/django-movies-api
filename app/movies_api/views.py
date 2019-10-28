from django.http import HttpResponse


def index(request):
    message = """
    <h3>Django REST API Movies</h3>
    <p><a href="/api">/api</a></p>
    <p><a href="/admin">/admin</a></p>
    """
    return HttpResponse(message)


def api_root(request):
    message = """
    <h3>API Root</h3>
    <p><a href="/api/movies">/movies</a></p>
    <p><a href="/api/comments">/comments</a></p>
    <p><a href="/api/top">/top</a></p>
    <br>
    <p><a href="/">&lArr; return</a></p>
    """
    return HttpResponse(message)
