# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})  # Indicates 1 object deleted from the Book model

# Confirm the deletion by retrieving all books
all_books = Book.objects.all()
print(all_books)
# Expected output: <QuerySet []>  # No books in the database, confirming deletion
