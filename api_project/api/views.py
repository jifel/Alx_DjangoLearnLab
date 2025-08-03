from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
#import generic views from DRF
from rest_framework import generics
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated, IsAdminUser



# Create a view that list all books using ListAPIView
#generic views are specific but  viewsets provide all basic crud operations
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()   #the data to return
    serializer_class = BookSerializer #how to serialize the data

    
#ModelViewSet gives you full CRUD support for the Book Model

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() # query all books
    serializer_class = BookSerializer #use this serializer

    # 🔐 Protect the endpoint so only logged-in users with valid tokens can access it
    permission_classes = [IsAuthenticated]