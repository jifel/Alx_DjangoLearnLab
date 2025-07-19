from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')  # enable search bar
    list_filter = ('publication_year',)  # enable filters by year


admin.site.register(Book, BookAdmin)
