from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app.drf_api.serializers import MovieSerializer
from watchlist_app.models import Movie


# Detail and list endpoint of movie model, created using drf with function base view.
@api_view()
def movie_list(request):
    return Response(MovieSerializer(Movie.objects.all(), many=True).data, status=200)


@api_view()
def movie_detail(request, pk):
    return Response(MovieSerializer(Movie.objects.get(pk=pk)).data, status=200)
