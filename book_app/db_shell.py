from book_app.models import Book 
# exec(open(r"C:\Users\DELL\open_source\School-Library\book_app\db_shell.py").read())

book1 = Book.objects.create(title="Lorem Ipsum", author="Lorem Ipsum", total_copies=5, available_copies=3)
book2 = Book.objects.create(title="Dolor Sit Amet", author="Lorem Ipsum", total_copies=3, available_copies=0)
book3 = Book.objects.create(title="Consectetur Adipiscing", author="Lorem Ipsum", total_copies=7, available_copies=7)
book4 = Book.objects.create(title="Sed Do Eiusmod", author="Lorem Ipsum", total_copies=4, available_copies=4)
book5 = Book.objects.create(title="Tempor Incididunt", author="Lorem Ipsum", total_copies=2, available_copies=1)