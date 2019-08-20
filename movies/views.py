from django.shortcuts import render

from movies.forms import CommentForm
from movies.models import Movie
# from .forms import MoviesForm


def home(request):
    return render(request, 'home.html')

def comments(request):
    return render(request, 'home.html')


def movies(request):
    movies_list = Movie.objects.all()
    if request.method == 'GET':
        columns = [field.name for field in Movie._meta.fields]
        return render(request, 'movies_list.html', {'movies_list': movies_list, 'columns': columns})
    else:
        external_object = {'title':'titanic'}
        comments_form = CommentForm()
        return render(request, 'movie_detail.html', {'external_object': external_object,
                                                     'comments_form': comments_form})
