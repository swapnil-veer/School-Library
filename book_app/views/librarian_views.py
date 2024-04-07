from ..models import Borrow
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from users.models import CustomUser
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView
from ..models import Book
from ..forms import BookForm, BorrowForm
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.contrib import messages
from time import timezone

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

# @user_passes_test(is_admin)
# @user_passes_test(lambda u: u.is_superuser)
class AddBookView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm  # Make sure this line is correct
    template_name = 'librarian/addbook.html'
    # success_url = '/success-url/'
    success_url = reverse_lazy('add_book')  # Redirect to the same page
    success_message = "Book added successfully."  # Success message to display

    def get_success_url(self):
        return reverse_lazy('add_book') 
    
    def test_func(self):
        return is_admin(self.request.user)

    def handle_no_permission(self):
        return HttpResponseForbidden("You do not have permission to access this page.")
    

@user_passes_test(is_admin)
def add_to_borrow(request):
    if request.method == "GET":
        pass

# class AddToBorrow(UserPassesTestMixin, SuccessMessageMixin, CreateView):
#     model = Borrow
#     form_class = BorrowForm
#     template_name = 'librarian/add_to_borrow.html/'
#     success_url = reverse_lazy('add_to_borrow')
#     success_message = "Student book added successfully."  # Success message to display

#     def get_success_url(self):
#         return reverse_lazy('add_to_borrow') 
    
#     def test_func(self):
#         return is_admin(self.request.user)

#     def handle_no_permission(self):
#         return HttpResponseForbidden("You do not have permission to access this page.")

@user_passes_test(is_admin)
def add_to_borrow(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save()
            # borrow.due_date = timezone.now() + timezone.timedelta(days=30)
            # borrow.save()
            messages.success(request, "Student book added successfully.")
            return redirect(reverse('add_to_borrow'))
    else:
        form = BorrowForm()
    
    context = {'form': form}
    return render(request, 'librarian/add_to_borrow.html', context)
