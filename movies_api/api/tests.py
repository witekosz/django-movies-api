from rest_framework.test import APIRequestFactory, APITestCase

from movies_api.api import views
from movies_api.models import Movie


class TestMovies(APITestCase):
    """
    Tests for movies endpoint
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.MoviesView.as_view()
        self.uri = '/movies/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'
            .format(response.status_code)
        )

    def test_post_false_movie(self):
        request = self.factory.post(self.uri, {'title': 'kjlsdfslijfds'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 404,
            'Expected Response Code 404, received {0} instead.'
            .format(response.status_code)
        )

    def test_post_good_movie(self):
        request = self.factory.post(self.uri, {'title': 'Terminator'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 201,
            'Expected Response Code 201, received {0} instead.'
            .format(response.status_code)
        )


class TestComments(APITestCase):
    """
    Tests for movies endpoint
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.CommentsView.as_view()
        self.uri = '/comments/'
        Movie.objects.create(title='Terminator', id=1)

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            'Expected Response Code 200, received {0} instead.'
            .format(response.status_code)
        )

    def test_post_false_comment(self):
        """
        Check posting comment to non existing movie
        """
        request = self.factory.post(self.uri, {'movie': 5, 'text': 'Nice movie.', 'author': 'tester'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 400,
            'Expected Response Code 400, received {0} instead.'
            .format(response.status_code)
        )

    def test_post_good_comment(self):
        request = self.factory.post(self.uri, {'movie': 1, 'text': 'Nice movie.', 'author': 'tester'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 201,
            'Expected Response Code 201, received {0} instead.'
            .format(response.status_code)
        )


class TestTop(APITestCase):
    """
    Tests for top endpoint
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.get_top_movies
        self.uri = '/top/'

    def test_list_top_correct_dates(self):
        request = self.factory.get(self.uri, {'start-date': '20-10-2019', 'end-date': '25-10-2019'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 204,
            'Expected Response Code 204, received {0} instead.'
            .format(response.status_code)
        )

    def test_list_top_no_dates(self):
        """
        Check request with no given params
        """
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 400,
            'Expected Response Code 400, received {0} instead.'
            .format(response.status_code)
        )

    def test_list_top_error_dates_format(self):
        """
        Check error in dates format
        """
        request = self.factory.get(self.uri, {'start-date': '20-10-19', 'end-date': '20-2019'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 400,
            'Expected Response Code 400, received {0} instead.'
            .format(response.status_code)
        )

    def test_list_top_mixed_dates(self):
        """
        Check invalid date range
        """
        request = self.factory.get(self.uri, {'start-date': '21-10-2019', 'end-date': '19-10-2019'})
        response = self.view(request)
        self.assertEqual(
            response.status_code, 400,
            'Expected Response Code 400, received {0} instead.'
            .format(response.status_code)
        )
