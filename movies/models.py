from django.db import models


class Ratings(models.Model):
    Source = models.CharField(max_length=100, blank=True)
    Value = models.CharField(max_length=50, blank=True)


class Movie(models.Model):
    Title = models.CharField(max_length=150, blank=True)
    Year = models.CharField(max_length=50, blank=True)
    Rated = models.CharField(max_length=100, blank=True)
    Released = models.CharField(max_length=200, blank=True)
    Runtime = models.CharField(max_length=50, blank=True)
    Genre = models.CharField(max_length=200, blank=True)
    Director = models.CharField(max_length=200, blank=True)
    Writer = models.TextField(max_length=200, blank=True)
    Actors = models.CharField(max_length=200, blank=True)
    Plot = models.CharField(max_length=400, blank=True)
    Language = models.CharField(max_length=50, blank=True)
    Country = models.CharField(max_length=50, blank=True)
    Awards = models.CharField(max_length=150, blank=True)
    Poster = models.CharField(max_length=150, blank=True)
    Ratings = models.ManyToManyField(Ratings)
    Metascore = models.CharField(max_length=50, blank=True)
    imdbRating = models.CharField(max_length=50, blank=True)
    imdbVotes = models.CharField(max_length=50, blank=True)
    imdbID = models.CharField(max_length=50, blank=True)
    Type = models.CharField(max_length=50, blank=True)
    DVD = models.CharField(max_length=50, blank=True)
    BoxOffice = models.CharField(max_length=50, blank=True)
    Production = models.CharField(max_length=200, blank=True)
    Website = models.CharField(max_length=50, blank=True)
    Response = models.CharField(max_length=50, blank=True)


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
