from rest_framework import serializers

from movies.models import Movie, Comment, Ratings


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):
    Ratings = RatingsSerializer(many=True)

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


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['movie_id', 'body']


class TopCommentsSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    total_comments = serializers.IntegerField()
    rank = serializers.IntegerField()
