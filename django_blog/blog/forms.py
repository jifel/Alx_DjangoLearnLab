from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


#a form to update profile info

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] #fields the user can edit

#form for creating and updating post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Author will be set in the view, not user-editable

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The title must be at least 5 characters long.")
        return title