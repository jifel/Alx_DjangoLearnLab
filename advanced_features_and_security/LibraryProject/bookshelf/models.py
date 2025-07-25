from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


    #including custom permissions for this book model

    class Meta:
        permissions = [
            ("can_view","Can view list of books"),
            ("can_create","Can add a book"),
            ("can_edit","Can edit attributes of a book"),
            ("can_delete","Can delete books"),

        ]
 

#extending the  user to add more fields
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)


#custom manager to control how users and superusers are created

class CustomUserManager(BaseUserManager):

    #method to create a s regular user

    def create_user(self, username, email, password=None, **extra_fields):
        #check that an email is provided(more validation will be added later)
        if not email:
            raise ValueError('Email is required')
        

        #normalize the email (e.g. lowercasing domain part)
        email = self.normalize_email(email)


        #create a user instance(but  dont save yet)
        user = self.model(username=username, email=email, **extra_fields)

        #set the hashed password using django's built in method
        user.set_password(password)

        #save the user to the database using the correct DB alias
        user.save(using=self._db)

        return user
    
    #method to creat esuperuser (admin user)
    def create_superuser(self,username, email, password=None, **extra_fields):

        #ensure is_staff and is_superuser are set to True
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)


        #optional: enforce these values (guard against them being set to False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        

        #call create_user with the necessary flags
        return self.create_user(username, email, password, **extra_fields)
    
#assign the customusermanager to my custom user model

objects = CustomUserManager()    