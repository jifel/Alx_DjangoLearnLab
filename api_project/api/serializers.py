from rest_framework import serializers
from .models import Book


# Define a serializer class for the Book model

class BookSerializer(serializers.ModelSerializer):
    # Meta class tells Django how to map the model to the serializer
    class Meta:
        model = Book  # Specify the model to serialize
        fields = '__all__'  # Include all model fields in the serialized output