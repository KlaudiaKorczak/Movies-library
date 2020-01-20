import json
from rank import DenseRank
from django.db.models import Count, F, Q
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import viewsets
from movies.models import Movie, Comment
from movies.serializers import MoviesSerializer, CommentsSerializer, TopCommentsSerializer, DateFormatSerializer
from urllib.request import urlopen


class Movies(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer

    def create(self, request, *args, **kwargs):
        title_serializer = self.get_serializer(data=request.data)
        title_serializer.is_valid(raise_exception=True)

        title = request.data['Title']
        url = "http://www.omdbapi.com/?t={}&apikey=459014fb".format(title)
        json_url = urlopen(url)
        data = json.loads(json_url.read())

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Top(ListAPIView):
    serializer_class = TopCommentsSerializer

    def get_queryset(self):
        date_serializer = DateFormatSerializer(data=self.request.query_params)
        date_serializer.is_valid(raise_exception=True)

        date_from = date_serializer.validated_data['start']
        date_to = date_serializer.validated_data['end']

        qs = (
            Movie.objects.filter(
                Q(comments__created__date__gte=date_from, comments__created__date__lte=date_to) |
                Q(comments__isnull=True)
            )
            .annotate(total_comments=Count('comments'))
            .annotate(movie_id=F('id'))
            .annotate(rank=DenseRank('total_comments'))
            .values('movie_id', 'total_comments', 'rank'))
        return qs


class CommentsList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('movie_id', )
