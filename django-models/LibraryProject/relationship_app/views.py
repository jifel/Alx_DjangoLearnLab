from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Book
from .models import Library

# Create your views here.
#function based view
def list_books(request):
    books = Book.objects.all()
    context = {'books':books}


    return render(request, 'relationship_app/list_books.html', context)


#class based view


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = Book.objects.filter(library=library)
        return context


#user registration
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('list_books')
    template_name = 'relationship_app/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)