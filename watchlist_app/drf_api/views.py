from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app.drf_api.serializers import MovieSerializer
from watchlist_app.models import Movie


# Perform CRUD endpoint of movie model, created using drf with function base view.
@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        return Response(MovieSerializer(Movie.objects.all(), many=True).data, status=200)
    serial_data = MovieSerializer(data=request.data)
    if serial_data.is_valid():  # Here we can also use raise_exception= True,
        serial_data.save()
        return Response(serial_data.data, status=201)
    else:
        return Response(
            serial_data.errors,
            status=400)  # we don't need to write this line code when we use raise_exception in is_valid() method.


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "GET":
        return Response(MovieSerializer(movie).data, status=200)
    if request.method == "PUT":
        serial_data = MovieSerializer(movie, data=request.data)
        if serial_data.is_valid(raise_exception=True):
            serial_data.save()
            return Response(serial_data.data, status=200)
    else:
        movie.delete()
        return Response({"Message": "Object deleted success"}, status=200)
