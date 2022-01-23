from django.urls import path

from watchlist_app.views import movie_list

urlpatterns = [path("movieList/", movie_list, name="movie_list_api")]
