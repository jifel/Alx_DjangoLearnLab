from django.shortcuts import render #renders HTML templates..connects view logic with the frontend
from django.contrib.auth.decorators import permission_required #restrict access to views based on permissions
from .models import Book
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404 #retreives an object from the db or returns 404 if not found
from .forms import BookForm
from .forms import ExampleForm
# Create your views here.
#(can_view)

#view to display a list of books
#only users with 'can_view' permission can access
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all() #retrieve all books from the database
    return render(request, 'bookshelf/book_list.html', {'books':books})



#view to allow creating a book
#only users with 'can_create' permission can access
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # If the request is a POST (i.e. the user submitted the form)
    if request.method == 'POST':
        # Bind the submitted data to the form
        form = BookForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            # Save the new book to the database
            form.save()

            # Redirect to the book list page after successful creation
            return redirect('bookshelf:book_list')

    else:
        # If the request is a GET, instantiate an empty form
        form = BookForm()

    # Render the book creation form template with the form context
    return render(request, 'bookshelf/book_form.html', {'form': form})


#view to edit an existing book
#only users wirh can_edit permission can access
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk = pk) #get the book or return 404 if not found

    if request.method == 'POST':
        
        #update book fields with submitted form data
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST['publication_year']
        book.save()


        #redirect to book list after editing
        return redirect('book_list')
    
    #if request method is GET, render the form template with book data
    return render(request, 'bookshelf/book_form.html', {'book': book})



#view to delete an existing book
#only users with can_delete permission can access
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk = pk)

    if request.method == 'POST':

        #deleete the books and redirect
        book.delete()
        return redirect('book_list')
    

    #if GET, show confirmation page
    return render(request,'bookshelf/book_confirm_delete.html', {'book': book})