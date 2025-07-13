# CREATE
# Create a Book instance
book1 = Book(title="1984", author="George Orwell", publication_year=1949)
book1.save()
# Expected output: Book object saved successfully with id=1 (no direct output unless printed)

# RETRIEVE
# Retrieve and display all attributes of the book
all_books = Book.objects.all()
print(all_books)
# Expected output: <QuerySet [<Book: Book object (1)>]>


# UPDATE
# Update the title of "1984" to "Nineteen Eighty-Four"
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Expected output: Title updated successfully (no direct output unless printed)

# Confirm update
updated_book = Book.objects.get(id=1)
print(updated_book.title)
# Expected output: Nineteen Eighty-Four

# DELETE
# Delete the book
book = Book.objects.get(id=1)
book.delete()
# Expected output: (1, {'bookshelf.Book': 1})

# Confirm deletion
all_books = Book.objects.all()
print(all_books)
# Expected output: <QuerySet []>
