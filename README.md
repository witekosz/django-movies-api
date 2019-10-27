# Django Movies REST API

Simple implementation of Django and Django Rest Framework. 

Example: [django-movie-api.herokuapp.com](https://django-movie-api.herokuapp.com/)

Available endpoints: 
- /movies GET - List movies added to database
    * allow ordering for id, title, released, runtime, writer and director fields
- /movies POST - Add movie to database, data from [omdbapi.com](http://www.omdbapi.com/), validation based on movie title
    * required movie title in request body
- /comments GET - List all comments added to movies in db
    * allow ordering for all fields 
    * allow filtering based on commented movie
- /comments POST - Add comment to movies in db, request body params:
    * movie and text are required
    * posting author is optional
    * add_date is default today
 - /top GET - List most commented movies in given date range,
    specifying date range is required,
    query params: 
    * start-date=DD-MM-YYY
    * end-date=DD-MM-YYY

Requirements: **python 3.6+**.

Running app locally(on Linux):
1. Copy git repository.
2. Run: cd django_movies_api
3. Run: docker-compose build
3. Run: docker-compose up -d
4. Server should run on: localhost:8000

