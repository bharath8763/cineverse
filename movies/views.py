from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    hero_movie = movies.first()
    return render(request, "movies.html", {
        "movies": movies,
        "hero_movie": hero_movie
    })


def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "movie_detail.html", {
        "movie": movie
    })


def book_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "book_movie.html", {
        "movie": movie
    })


def seat_booking(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, "seat_booking.html", {
        "movie": movie
    })


def payment(request, id):
    movie = get_object_or_404(Movie, id=id)

    seats = request.GET.get("seats")
    amount = request.GET.get("amount")
    date = request.GET.get("date")
    time = request.GET.get("time")

    if request.method == "POST":
        method = request.POST.get("method")
        return render(request, "payment_success.html", {
            "movie": movie,
            "seats": seats,
            "amount": amount,
            "date": date,
            "time": time,
            "method": method
        })

    return render(request, "payment.html", {
        "movie": movie,
        "seats": seats,
        "amount": amount,
        "date": date,
        "time": time
    })


# ✅ THIS FUNCTION WAS MISSING / NOT CONNECTED
def payment_success(request):
    return render(request, "payment_success.html")
