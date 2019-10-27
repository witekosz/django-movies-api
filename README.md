# Django Movies REST API

Simple implementation of Django and Django Rest Framework. 

Example: [django-movie-api.herokuapp.com](https://django-movie-api.herokuapp.com/)

Available endpoints: 
- /movies GET - List movies added to database
- /movies POST - Add movie to database, required movie title in request body, 
    data from [omdbapi.com](http://www.omdbapi.com/), validation based on movie title
- /comments GET - List all comments added to movies in db
- /comments POST - Add comment to movies in db, required movie id and text,
    author is optional
 - /top GET - List most commented movies in given data range,
    specifying data range is required

Requirements: **python 3.7+**.

Running app locally(on Linux):
1. Copy git repository.
2. Run: cd django_movies_api
3. Run: docker-compose build
3. Run: docker-compose up -d
4. Server should run on: localhost:8000


