from rest_framework import serializers

from movies.models import Movie, Comment


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
                  'Language', 'Country', 'Awards', 'Poster', 'Ratings', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type',
                  'DVD', 'BoxOffice', 'Production', 'Website', 'Response']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['movie_id', 'body']


class TopCommentsSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    total_comments = serializers.IntegerField()
    rank = serializers.IntegerField()
