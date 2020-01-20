
from dateutil.relativedelta import relativedelta
from django.utils.datetime_safe import datetime
from rest_framework import serializers

from movies.models import Movie, Comment, Ratings


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['movie_id', 'body']


class MoviesSerializer(serializers.ModelSerializer):
    Ratings = RatingsSerializer(many=True, required=False)
    Title = serializers.CharField(required=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        ratings_data = validated_data.pop('Ratings')
        movie = Movie.objects.create(**validated_data)
        for rating_data in ratings_data:
            rating, created = Ratings.objects.get_or_create(**rating_data)
            movie.Ratings.add(rating)
        return movie


class DateFormatSerializer(serializers.Serializer):
    start = serializers.DateField(format="%Y-%m-%d",  default=datetime.now() - relativedelta(weeks=6))
    end = serializers.DateField(format="%Y-%m-%d", default=datetime.now())


class TopCommentsSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    total_comments = serializers.IntegerField()
    rank = serializers.IntegerField()
