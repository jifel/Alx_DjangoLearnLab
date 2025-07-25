from django.urls import path
from . import views

app_name = 'bookshelf' #helps with namespacing URLS in templates

urlpatterns = [
    #view: list of books (requires can_view permission)
    path('',views.book_list, name='book_list'),

       # View: create a new book (requires can_create permission)
    path('create/', views.book_create, name='book_create'),

    # View: edit an existing book by its primary key (requires can_edit permission)
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),

    # View: delete an existing book by its primary key (requires can_delete permission)
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]