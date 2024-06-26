from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "book"

class Borrow(models.Model):
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.borrower.username} - {self.book.title} - {self.due_date}"
    
    class Meta:
        db_table = "borrow"

