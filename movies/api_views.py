from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from movies.models import Movie, Comment
from movies.serializers import MoviesSerializer, CommentsSerializer, TopCommentsSerializer
import urllib, json
from urllib.request import urlopen
from django_filters import rest_framework as filters
import collections

# Api view renders data into the json format.


class MoviesList(APIView):
    # queryset = Movie.objects.all()
    # serializer_class = MoviesSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('Title',)

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        title = request.data.get('title')
        url = "http://www.omdbapi.com/?t={}&apikey=459014fb".format(title)
        json_url = urlopen(url)
        data = json.loads(json_url.read())
        serializer = MoviesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('movie_id', )


class TopComments(APIView):
    def get(self, request, **kwargs):
        date_from = kwargs.get('from', '2019-08-19')
        date_to = kwargs.get('to', '2019-09-30')
        print(request.data)
        # date_from = "2011-01-01"
        # date_to ="2019-08-21"
        movies = Movie.objects.all()
        sorted_numbers = count_comments(movies,  date_from, date_to)
        results_list = generate_statistics(sorted_numbers)
        # print(results_list)
        ser = TopCommentsSerializer(results_list, many=True).data
        # date_from = request.date_from
        return Response(results_list)


def count_comments(movies, date_from, date_to):
    movies_comments = {}
    for movie in movies:
        comments_count = Comment.objects.filter(created__range=[date_from, date_to], movie_id=movie.id).count()
        movies_comments[movie.id] = comments_count
    sorted_numbers = sorted(movies_comments.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_numbers


def generate_statistics(sorted_numbers):
    rank = 1
    current_value = sorted_numbers[0][1]
    results_list = []

    for pair in sorted_numbers:
        if pair[1] < current_value:
            current_value = pair[1]
            rank += 1
        results_list.append({'movie_id': pair[0], 'total_comments': pair[1], 'rank': rank})

    return results_list