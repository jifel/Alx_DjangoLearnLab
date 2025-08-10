

# DRF generic view classes and permission helpers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# local imports
from .models import Book
from .serializers import BookSerializer

#for filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# ----------------------------------------------------------------
# ListView: GET /books/  -> returns list of all books
# ----------------------------------------------------------------
class BookListView(generics.ListAPIView):
    """
    List all Book instances.
    GET only (returns a list). Anyone can read; writes are restricted.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow read for everyone, require authentication for write actions.
    # (ListAPIView doesn't write, but we set this for consistency/readability.)
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Define which backends to use for filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Specify the model fields allowed for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Specify the model fields allowed for searching
    search_fields = ['title','author']

    #field for ordering
    ordering = ['title', 'publication_year']



# ----------------------------------------------------------------
# DetailView: GET /books/<pk>/  -> retrieve one book by id
# ----------------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single Book by primary key.
    GET only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ----------------------------------------------------------------
# CreateView: POST /books/create/  -> create a new book
# ----------------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Create a new Book instance.
    POST only. Requires authentication (because of IsAuthenticatedOrReadOnly).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ----------------------------------------------------------------
# UpdateView: PUT/PATCH /books/<pk>/update/  -> update an existing book
# ----------------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing Book (PUT = full update, PATCH = partial update).
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ----------------------------------------------------------------
# DeleteView: DELETE /books/<pk>/delete/  -> delete a book
# ----------------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a single Book instance.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
