from datetime import datetime

from django.db.models import Count
from rest_framework import filters
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters import rest_framework as django_filters

from movies_api.api.serializers import MovieSerializer, MovieTitleSerializer, CommentSerializer
from movies_api.api.utils import get_movie_data_from_title, sanitize_external_movie_data
from movies_api.models import Movie, Comment


class MoviesView(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 generics.GenericAPIView):
    """
    List all movies or add a new movie
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    ordering_fields = ['id', 'title', 'released', 'runtime', 'writer', 'director']

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
    List all comments or comment a movie
    For API testing purposes add_date can be also specified
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_fields = ('movie',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view()
def get_top_movies(request):
    """
    List movies rating based of comments in given date range
    ---
    parameters:
    - name: start-date
        description: Date in format DD-MM-YYYY
        required: true
        type: string
    - name: end-date
        description: Date in format DD-MM-YYYY
        required: true
        type: string
    """

    if ('start-date' not in request.query_params) or ('end-date' not in request.query_params):
        return Response({"error": "Please provide start-date and end-date params."}, status=status.HTTP_400_BAD_REQUEST)

    start_date = request.query_params['start-date']
    end_date = request.query_params['end-date']

    try:
        start_date_obj = datetime.strptime(start_date, '%d-%m-%Y').date()
        end_date_obj = datetime.strptime(end_date, '%d-%m-%Y').date()

    except Exception as e:
        return Response(
            {"error": "Please provide correct date params, format: dd-mm-yyyy."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if start_date >= end_date or end_date <= start_date:
        return Response(
            {"error": "Please provide correct date range."},
            status=status.HTTP_400_BAD_REQUEST
        )

    queryset = Comment.objects.filter(add_date__range=[start_date_obj, end_date_obj])
    if queryset:
        movies_queryset = queryset \
            .values('movie', 'movie__title') \
            .annotate(total_comments=Count('*')) \
            .order_by('-total_comments')

        rank = 0
        for i, q in enumerate(movies_queryset):
            if i == 0:
                rank += 1
            else:
                if movies_queryset[i-1]['total_comments'] == q['total_comments']:
                    rank = movies_queryset[i-1]['rank']
                else:
                    rank += 1
            q['rank'] = rank

        return Response(movies_queryset, status=status.HTTP_200_OK)

    return Response({"message": "No data for provided date range."}, status=status.HTTP_204_NO_CONTENT)
