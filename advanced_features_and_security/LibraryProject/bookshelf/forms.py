from django import forms
from .models import Book




#defining exampleform for checker
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

# Define a form for the Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
