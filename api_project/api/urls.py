from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router instance - DefaultRouter auto-generates URL patterns for ViewSets
router = DefaultRouter()

# 'books_all' is the URL prefix that will be used (e.g., /books_all/, /books_all/1/)
# 'basename' is used to name the URL patterns
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    #route for the BookList view (LISTAPIView)
    path('books/', BookList.as_view(), name='book-list'), #route to list books

    #include the router-generated urls for BookViewSet (all CRUD operations) in the app's URLs
    path('',include(router.urls)), # this incudes all routes registered with the router
]