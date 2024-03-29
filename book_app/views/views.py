from django.shortcuts import render
from ..models import Book, Borrow
from django.db import connection

def available_book_list(request):
    avail_books = Book.objects.filter(available_copies__gt = 0)
    return render(request, "available_books.html", {"avail_books": avail_books})

def book_list(request):
    books = Book.objects.all()
    all_books = []
    for book in books:
            print(type(book))
            if book.available_copies > 0:
                availability = "Available"
            else:
                # Raw SQL query to get the next return date for the book
                cursor = connection.cursor()
                cursor.execute("""
                    SELECT due_date
                    FROM borrow
                    WHERE book_id = %s
                    ORDER BY due_date
                    LIMIT 1
                """, [book.id])
                row = cursor.fetchone()
                next_return_date = row[0] if row else None
                availability = f"Expected return date: {next_return_date.strftime('%Y-%m-%d')}" if next_return_date else "Unavailable"
            # print(availability)
            book.availability = availability
            # print(book,book.availability)
            all_books.append(book)
    # print(all_books)
    return render(request, "show_all_books.html", {"all_books" : all_books})
