# Create Book Instance

book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)>>> book1.save()

# Expected Output:
# The book "1984" by George Orwell (1949) is successfully created and saved in the database.
# No output is shown unless there is an error.
