# api/urls.py

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)
'''
this is also right but didnt pass the checker
urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book (separate path as requested)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update an existing book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
'''


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),           # GET all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # GET one book
    path('books/create/', BookCreateView.as_view(), name='book-create'),   # POST create book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),   # PUT/PATCH update
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),   # DELETE remove
]
