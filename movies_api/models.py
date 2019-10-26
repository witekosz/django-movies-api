from django.db import models


class TimeModel(models.Model):
    """
    Abstract model for storing instance time data
    """
    mod_date = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Movie(models.Model):
    """
    Model for storing fetched movies
    """
    title = models.CharField(max_length=200, unique=True)
    released = models.DateField(null=True)
    runtime = models.PositiveSmallIntegerField(null=True)

    genre = models.TextField()
    director = models.CharField(max_length=200)
    writer = models.TextField()
    actors = models.TextField()
    plot = models.TextField()

    language = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    awards = models.TextField()
    poster = models.URLField(null=True)

    def __str__(self):
        return "%s %s" % (self.title, self.released if self.released else "")


class Comment(TimeModel):
    """
    Model for movie comments
    """
    movie = models.ForeignKey(Movie, related_name='movies', on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return "%s %s" % (self.movie, self.author if self.author else "")
