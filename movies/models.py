from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50, blank=True)


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
