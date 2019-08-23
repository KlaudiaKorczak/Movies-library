import datetime
import json
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from movies.models import Movie, Comment
from movies.serializers import MoviesSerializer, CommentsSerializer, TopCommentsSerializer
from movies.utils.prepare_statistics import count_comments, generate_statistics
from urllib.request import urlopen

DEFAULT_DATES = {'FROM': '2019-08-19',
                 'TO': datetime.datetime.utcnow()}


class MoviesList(APIView):
    def get(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MoviesSerializer(movies, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Error": str(e)})

    def post(self, request, format=None):
        try:
            title = request.data.get('title')
            if len(request.data) != 1 or request.data.get('title') is None:
                return Response("Invalid data. Request body must contain only the 'title'.",
                                status=status.HTTP_400_BAD_REQUEST)
            url = "http://www.omdbapi.com/?t={}&apikey=459014fb".format(title)
            json_url = urlopen(url)
            data = json.loads(json_url.read())
            serializer = MoviesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": str(e)})


class TopComments(APIView):
    def get(self, request, **kwargs):
        try:
            date_from = kwargs.get('from', DEFAULT_DATES['FROM'])
            date_to = kwargs.get('to', DEFAULT_DATES['TO'])
            movies = Movie.objects.all()
            comments = Comment.objects
            sorted_numbers = count_comments(movies, comments, date_from, date_to)
            statistics = generate_statistics(sorted_numbers)
            serialized_stats = TopCommentsSerializer(statistics, many=True).data
            return Response(serialized_stats)
        except Exception as e:
            return Response({"Error": str(e)})


class CommentsList(ListCreateAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentsSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_fields = ('movie_id', )
