# retrieve books

all_books = Book.objects.get(title="1984")

# display all books:
>>> print(all_books)


# Expected Output:
<QuerySet [<Book: Book object (1)>]>





