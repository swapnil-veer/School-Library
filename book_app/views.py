from django.shortcuts import render
from .models import Book, Borrow

def available_book_list(request):
    avail_books = Book.objects.filter(available_copies__gt = 0)
    return render(request, "available_books.html", {"avail_books": avail_books})

def book_list(request):
    books = Book.objects.all()
    return render(request, "show_all_books.html", {"all_books" : books})
