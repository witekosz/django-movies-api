# Django Movies REST API

A simple implementation of Django and Django Rest Framework. 

Example: [django-movie-api.herokuapp.com](https://django-movie-api.herokuapp.com/)

Available endpoints: 
- /**movies** GET - List movies added to the database
    * allow ordering for id, title, released, runtime, writer and director fields
- /**movies** POST - Add movie to database, data from [omdbapi.com](http://www.omdbapi.com/), validation based on the movie title
    * required movie title in the request body
- /**comments** GET - List all comments added to movies in db
    * allow ordering for all fields 
    * allow filtering based on a commented movie
- /**comments** POST - Add comment to movies in db, request body params:
    * movie and text are required
    * posting author is optional
    * add_date is default today
 - /**top** GET - List most commented movies in the given date range,
    specifying date range is required,
    query params: 
    * start-date=DD-MM-YYY
    * end-date=DD-MM-YYY

Requirements:
- latest verison of **docker**
- latest version of **docker compose**

### Development

Uses default SQLite database and Django development server.

Run app by docker compose locally(on Linux):
1. Open terminal
2. Copy git repository
3. Go to the project directory:
    ```sh
    $ cd django_movies_api
    ```
4. Build images:
    ```sh 
   $ docker-compose build
   ```
5. Run containers:
    ```sh
    $ docker-compose up -d
    ```
6. Create a database:
    ```sh
    $ docker-compose exec web python manage.py migrate --noinput
    ```
6. The server should be running on: [localhost:8000](http://localhost:8000/)

### Production

Uses Heroku, PostgreSQL and gunicorn.
For deployment use heroku.yml. 
