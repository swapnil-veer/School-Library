from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookListViewTests(TestCase):
    def setUp(self):
        # Create dummy books
        self.book1 = Book.objects.create(title="Available Book", author="Author A", total_copies=5, available_copies=3)
        self.book2 = Book.objects.create(title="Unavailable Book", author="Author B", total_copies=3, available_copies=0)

    def test_available_books_list(self):
        response = self.client.get(reverse('available_books'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.book1.title)

        self.assertNotContains(response, self.book2.title)

