import json
from movies.serializers import MoviesSerializer, CommentsSerializer
from movies.models import Comment, Movie

FILE = 'movies/utils/test_utils/test_movie_object.json'
BODY = "base comment"


class BaseTest:
    '''Class for creating base data for tests'''

    def __init__(self):
        with open(FILE) as json_file:
            data = json.load(json_file)
        self.movie_serializer = MoviesSerializer(data=data)
        if self.movie_serializer.is_valid():
            self.movie_serializer.save()

        movie = Movie.objects.get(pk=1)
        if movie:
            self.comment = Comment.objects.create(movie_id=movie, body=BODY)
