from ..models import Borrow
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from users.models import CustomUser
from django.core.paginator import Paginator

def is_admin(user):
    return (user.is_authenticated and user.is_superuser)


@user_passes_test(is_admin)
def borrowed_books(request):
    # print(is_admin(request))
    borrowed_books = Borrow.objects.filter(return_date__isnull=True)
    paginator = Paginator(borrowed_books, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,template_name="librarian/borrowed_books.html", context= {"page_obj" : page_obj})
