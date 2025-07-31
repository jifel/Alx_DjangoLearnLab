from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
#import generic views from DRF
from rest_framework import generics


# Create a view that list all books using ListAPIView

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()   #the data to return
    serializer_class = BookSerializer #how to serialize the data

    
