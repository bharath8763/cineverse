from django.shortcuts import render, get_object_or_404
from movies.models import Movie

def seat_selection(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'seat_selection.html', {'movie': movie})
