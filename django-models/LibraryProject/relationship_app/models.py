from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title =models.CharField()
    author =models.ForeignKey(Author, on_delete= models.CASCADE)


    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name=models.CharField()
    books=models.ManyToManyField(Book)


    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField() 
    library = models.OneToOneField(Library, on_delete=models.CASCADE)   



    def __str__(self):
        return self.name




class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
