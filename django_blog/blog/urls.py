from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentCreateView, CommentDeleteView


urlpatterns = [
    #route for home view
    path('', views.home_view, name='home'),

    # Route for user registration — calls our custom view in views.py
    path('register/', views.register_view, name='register'),

    # Route for login — uses Django’s built-in LoginView
    # The template_name tells Django which HTML file to use for rendering the login page
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Route for logout — uses Django’s built-in LogoutView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #Route for posts
    #path('posts/', views.posts_view, name='posts'),

    #route for profile
    path('profile/', views.profile_view, name='profile'),  # new profile URL

    #route for edit profile page
    #path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    #routes for CRUD operations
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

   

     # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]





