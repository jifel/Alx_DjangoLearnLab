# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the changes
book.save()

# Confirm the update
print(book)
# Expected output: <Book: Nineteen Eighty-Four by George Orwell