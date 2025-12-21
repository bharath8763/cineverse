from django.urls import path
from .views import (
    movie_list,
    movie_detail,
    book_movie,
    seat_booking,
    payment,
    payment_success
)

urlpatterns = [
    path("", movie_list, name="movies"),
    path("movie/<int:id>/", movie_detail, name="movie_detail"),
    path("book/<int:id>/", book_movie, name="book_movie"),
    path("seats/<int:id>/", seat_booking, name="seat_booking"),
    path("payment/<int:id>/", payment, name="payment"),
    path("payment/success/", payment_success, name="payment_success"),
]
