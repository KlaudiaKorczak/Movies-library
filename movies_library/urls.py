import movies.api_views
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movies', movies.api_views.Movies, basename='movies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/', movies.api_views.CommentsList.as_view()),
    path('top/', movies.api_views.Top.as_view()),  # parameters for top/ endpoint are optional
]
urlpatterns += router.urls
