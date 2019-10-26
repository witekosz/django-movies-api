from django.urls import path, include
from rest_framework import routers

from movies_api.api import views


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('movies/', views.MoviesView.as_view(), name='movies'),
    path('comments/', views.CommentsView.as_view(), name='movies'),
    # path('top', views.index, name='index'),
]