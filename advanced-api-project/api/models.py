from django.db import models
from django.utils import timezone

# Author model: Represents a writer who can have multiple books
# One Author can be linked to many Book objects (One-to-Many relationship)
class Author(models.Model):
    name = models.CharField(max_length=255)  # Stores the name of the author

    def __str__(self):
        return self.name  # Display author's name in admin and shell


# Book model: Represents a book written by an author
# The ForeignKey field creates a one-to-many relationship with Author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published

    # ForeignKey: Each book is linked to a single author
    # related_name='books' allows us to access all books by an author via author.books.all()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

   
