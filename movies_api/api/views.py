from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.response import Response

from movies_api.api.serializers import MovieSerializer, MovieTitleSerializer, CommentSerializer
from movies_api.api.utils import get_movie_data_from_title, sanitize_external_movie_data
from movies_api.models import Movie, Comment


class MoviesView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    """
    List all movies, or create a new movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieTitleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        find_movie_data = get_movie_data_from_title(serializer.data['title'])

        if 'error' in find_movie_data.keys():
            return Response(find_movie_data, status=status.HTTP_404_NOT_FOUND)
        else:
            movie_data = sanitize_external_movie_data(find_movie_data)
            movie_serializer = MovieSerializer(data=movie_data)
            movie_serializer.is_valid(raise_exception=True)

            self.perform_create(movie_serializer)
            headers = self.get_success_headers(movie_serializer.data)
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentsView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    """
    List all comments, or create a new movie.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieTitleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)