from rest_framework.generics import ListAPIView

from movies.models import Movie
from movies.serializers import MoviesSerializer
# Api view renders data into the json format.

class MoviesList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
