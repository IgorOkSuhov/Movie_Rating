from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F


def show_all_movie(request):
    movies = Movie.objects.order_by(F ('year').desc(nulls_last=True))
    return render(request, 'movie_app/all_movie.html',{
        'movies': movies
    })
# Create your views here.

def show_one_movie(request, id_movie: int):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'movie_app/one_movie.html',{
        'movie': movie
    })


