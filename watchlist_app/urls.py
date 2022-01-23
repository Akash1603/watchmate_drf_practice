from django.urls import path

from watchlist_app.views import movie_list, movie_detail

urlpatterns = [
    path("movieList/", movie_list, name="movie_list_api"),
    path("movieDetail/<int:pk>/", movie_detail, name="movie_detail_api"),
]
