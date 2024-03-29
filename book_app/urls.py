from django.urls import path
from .views.views import available_book_list, book_list
from .views.student_views import my_books

urlpatterns = [
    path('avail-books/', available_book_list, name= 'available_books'),
    path('all-books/', book_list, name= 'all_books'),
    # for student
    path('my-books/',my_books, name= 'my_books'),


]