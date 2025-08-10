from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


# BookSerializer: Serializes all fields of the Book model
# Includes custom validation for publication_year to ensure it's not set in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields (title, publication_year, author)

    def validate_publication_year(self, value):
        # Validation to ensure publication_year is not in the future
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: Serializes author name and nested books
# Uses BookSerializer to show all books related to an author dynamically
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer: Serializes related books automatically using the 'books' related_name from the model
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']  # Only include name and the list of related books

    # Documentation:
    # - The 'books' field is populated by the related_name='books' in the Book model's ForeignKey.
    # - Since books are read-only here, they can't be created/edited directly via AuthorSerializer.
    # - This setup allows clients to see all books for a given author in one API response.
