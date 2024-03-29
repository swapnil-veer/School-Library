from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from ..models import Book, Borrow
from django.contrib.auth.models import User

@login_required
def my_books(request):
    current_user = request.user
    borrowed_books = Borrow.objects.filter(borrower=current_user)
    
    # Check if the user is authenticated and is a student
    if not current_user.groups.filter(name='Student').exists():
        return HttpResponseForbidden("You do not have permission to access this page.")

    return render(request, "student/my_books.html", {borrowed_books: borrowed_books})
