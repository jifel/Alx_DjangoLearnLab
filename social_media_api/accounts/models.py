from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # self-referential many-to-many for followers
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    followers = models.ManyToManyField(
    'self',
    symmetrical=False,
    related_name='following',
    blank=True
)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username still required, but login uses email

    def __str__(self):
        return self.email
