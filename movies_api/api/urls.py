from django.urls import path

from movies_api import views
from movies_api.api import views as api_views


urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('movies/', api_views.MoviesView.as_view(), name='movies'),
    path('comments/', api_views.CommentsView.as_view(), name='comments'),
    path('top/', api_views.get_top_movies, name='top'),
]
