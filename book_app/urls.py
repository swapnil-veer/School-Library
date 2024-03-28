from django.urls import path
from .views import available_book_list

urlpatterns = [
    path('avail-books/', available_book_list, name= 'available_books'),
]