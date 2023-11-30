from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from movies.models import Movie
from movies.serializers import MovieSerializer


def movie_list_view(request: HttpRequest) -> HttpResponse:
    movies = Movie.objects.all()[:5]
    context = {
        "movies": movies,
    }
    return render(request, "movies/movies_list.html", context=context)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.select_related("certification")
    serializer_class = MovieSerializer

