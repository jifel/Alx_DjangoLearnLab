from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin #base admin for user models
from django.utils.translation import gettext_lazy as _  #marks strings for translations..just safe to have it here for now
from .models import CustomUser #Import your custom user model

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')  # enable search bar
    list_filter = ('publication_year',)  # enable filters by year

admin.site.register(Book, BookAdmin)



#define a custom admin class for the customuser model
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
