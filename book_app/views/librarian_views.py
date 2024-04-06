from ..models import Borrow
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from users.models import CustomUser

def is_admin(user):
    return (user.is_authenticated and user.is_superuser)


@user_passes_test(is_admin)
def borrowed_books(request):
    # print(is_admin(request))
    borrowed_books = Borrow.objects.filter(return_date__isnull=True)
    return render(request,template_name="librarian/borrowed_books.html", context= {borrowed_books : borrowed_books})
