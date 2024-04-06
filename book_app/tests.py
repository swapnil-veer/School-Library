from django.test import TestCase
from django.urls import reverse
from .models import Book,Borrow
from datetime import datetime, timedelta
from users.models import CustomUser

class BookListViewTests(TestCase):
    def setUp(self):
        # Create dummy books
        self.book1 = Book.objects.create(title="Available Book", author="Author A", total_copies=5, available_copies=3)
        self.book2 = Book.objects.create(title="Unavailable Book", author="Author B", total_copies=3, available_copies=0)
        self.superuser = CustomUser.objects.create_superuser(email='superuser@example.com', password='adminpassword')
        self.user1 = CustomUser.objects.create_user(email="lennon@thebeatles.com", password="johnpassword", is_student=True)
        self.user2 = CustomUser.objects.create_user(email="lennohn@thebeatles.com", password="johnjjpassword", is_student=False)
        # self.user3 = CustomUser.objects.create
 
        self.due_date_book1 = datetime.now() + timedelta(days=10)
        self.due_date_book2 = datetime.now() + timedelta(days=15)
        self.borrower1 = Borrow.objects.create(borrower = self.user1, book = self.book1, due_date = self.due_date_book1)
        self.borrower2 = Borrow.objects.create(borrower = self.user2, book = self.book2, due_date = self.due_date_book2) 
        # print(self.borrower2)


    def atest_available_books_list(self):
        response = self.client.get(reverse('available_books'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.book1.title)

        self.assertNotContains(response, self.book2.title)

    def atest_all_books_list(self):
        response = self.client.get(reverse('all_books'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)

    def atest_book_availability(self):
        response = self.client.get(reverse('all_books'))
        self.assertEqual(response.status_code, 200)

        # Check if book 1 is available
        self.assertContains(response, "Available")

        # Check if book 2 is unavailable
        # self.assertContains(response, "Unavailable")

        expected_date_str = self.due_date_book2.strftime('%Y-%m-%d')
        self.assertContains(response, f"Expected return date: {expected_date_str}")

    def atest_my_books(self):
        self.client.login(email="lennon@thebeatles.com", password="johnpassword")
        response = self.client.get(reverse('my_books'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "Book1")

    def atest_non_student_access_my_books(self):
        response=self.client.get(reverse('my_books'))
        self.assertEqual(response.status_code, 403)

    def test_borrowed_bokks(self):
        self.client.login(email="superuser@example.com", password = "adminpassword")
        self.client.session['_auth_user_id']
        response=self.client.get(reverse('borrow_books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "user1")


