from django.contrib import admin
from .models import Author, Book

# Registering Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display these columns in admin list view

# Registering Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')  # Display these columns
