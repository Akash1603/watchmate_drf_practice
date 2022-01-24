from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from watchlist_app.models import Movie


# In Both API we added to much manual code in endpoints, so in next commit (C4) we used django rest framework.
def movie_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse({"Movies": movies}, status=200)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return JsonResponse({"name": movie.name,
                         "description": movie.description,
                         "active": movie.active}, status=200)
