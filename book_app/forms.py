from django import forms
from .models import Book, Borrow

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'
