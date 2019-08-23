import movies.api_views
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movies.api_views.MoviesList.as_view()),
    path('comments/', movies.api_views.CommentsList.as_view()),
    re_path('^top/(?P<from>\d{4}-\d{2}-\d{2})/(?P<to>\d{4}-\d{2}-\d{2})/$', movies.api_views.TopComments.as_view()),
    re_path('^top/(?P<from>\d{4}-\d{2}-\d{2})/$', movies.api_views.TopComments.as_view()),
    path('top/', movies.api_views.TopComments.as_view()),  # parameters for top/ endpoint are optional
]
