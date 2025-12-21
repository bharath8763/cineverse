from django.urls import path
from .views import seat_selection

urlpatterns = [
    path('book/<int:movie_id>/', seat_selection, name='book_movie'),
]
