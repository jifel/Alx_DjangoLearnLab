from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user and authenticate
        self.author = Author.objects.create(name="John Doe")
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Create a sample book
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2024)

        # Define endpoints
        self.list_url = reverse("book-list")     # for GET (list) and POST (create)
        self.detail_url = reverse("book-detail", args=[self.book.id])  # for GET, PUT, DELETE


#. Creating a Book
#Simulate a POST request to /api/books/ with valid data.
#Check:
#Status code is 201 CREATED.
#Response JSON contains the correct book data.
#Book exists in the database with the same details.

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Jane Doe",
            "published_year": 2025
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")

#Create a book in setUp().
#Send a PUT or PATCH request to update a field.
#Verify:
#Status code is 200 OK.
#The updated field is reflected in the database.

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": "John Doe",
            "published_year": 2023
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

#3. Deleting a Book
#Create a book.
#Send a DELETE request.
#Verify:
#Status code is 204 NO CONTENT.
#Book is no longer in the database.

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)
    

    def test_authentication_required(self):
        # Remove any authenticated user
        self.client.logout()
        response = self.client.post(self.create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
