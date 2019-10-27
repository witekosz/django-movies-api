#Django Movies REST API

Simple implementation of Django and Django Rest Framework. 

https://django-movie-api.herokuapp.com/

Available endpoints: 
- /movies GET - List movies added to database
- /movies POST - Add movie to database, required movie title in request body, 
    data from http://www.omdbapi.com/, validation based on movie title
- /comment GET - List all comments added to movies in db
- /comments POST - Add comment to movies in db, required movie id and text,
    author is optional
 - /top GET - List most commented movies in given data range,
    specifying data range is required

