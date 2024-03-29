from django.urls import path
from .views.views import available_book_list, book_list

urlpatterns = [
    path('avail-books/', available_book_list, name= 'available_books'),
    path('all-books/', book_list, name= 'all_books'),

]