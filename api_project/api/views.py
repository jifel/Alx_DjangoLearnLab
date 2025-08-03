from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
#import generic views from DRF
from rest_framework import generics
from rest_framework import viewsets 


# Create a view that list all books using ListAPIView
#generic views are specific but  viewsets provide all basic crud operations
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()   #the data to return
    serializer_class = BookSerializer #how to serialize the data

    
#extending to use a viewset as well

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer