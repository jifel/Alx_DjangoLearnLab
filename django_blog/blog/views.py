#adding a custom view because of the instruction and the extra email field added

# Import render to display templates and redirect to send users to another URL
from django.shortcuts import render, redirect, get_object_or_404

# Import messages framework to display success or error notifications
from django.contrib import messages

# Import the custom user creation form, profileform we built
from .forms import CustomUserCreationForm, ProfileForm, PostForm, CommentForm


# This decorator ensures only logged-in users can access the view.
# If a user is not logged in, they will be redirected to the login page.
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment

# This view handles user registration
def register_view(request):
    # Check if the request is a POST (form submission)
    if request.method == "POST":
        # Bind submitted form data to our custom form
        form = CustomUserCreationForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # Save the new user to the database
            form.save()
            # Show a success message to the user
            messages.success(request, "Account created successfully!")
            # Redirect to the login page after successful registration
            return redirect('login')
    else:
        # If the request is GET, display an empty registration form
        form = CustomUserCreationForm()
    
    # Render the registration page with the form
    return render(request, 'blog/register.html', {'form': form})

# view for home page
def home_view(request):
    return render(request, 'blog/home.html')


#this view handles posts

def posts_view(request):
    return render(request, 'blog/posts.html')

'''
#this view handles profile page

@login_required
def profile_view(request):
    """
    Handles requests to the user's profile page.
    - Displays the logged-in user's information.
    - Requires authentication (cannot be accessed by anonymous users).
    """
    
    # Render the 'profile.html' template located in 'blog/templates/blog/'
    # Passes the request context automatically, which includes the 'user' object.
    return render(request, 'blog/profile.html', {'user':request.user})


#this view handles the  edit profile page

@login_required
def edit_profile_view(request):
    # If user submitted the form (POST request)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)  # bind form to current user
        if form.is_valid():
            form.save()  # save updates to DB
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')  # go back to profile page after saving
    else:
        # For GET request, load the form with current user data
        form = ProfileForm(instance=request.user)

    return render(request, 'blog/edit_profile.html', {'form': form})
'''

#combined profile_view & edit_profile_view


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')  # after saving, go back to profile
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})

#@login_required → Ensures only logged-in users can see/edit their profile.
#instance=request.user → Pre-fills form with their existing info.
#messages.success → Shows the green "Profile updated!" message in the template.
#redirect('profile') → Avoids resubmitting form if the page is refreshed.

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # <app>/<model>_list.html default
    context_object_name = 'posts'
    ordering = ['-published_date']  # newest first


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        #all comments for this post
        context['comments'] = Comment.objects.filter(post=post)

        #empty form(submission handled by CommentCreateView)
        context['comment_form'] = CommentForm

        return context

    


# Create a new post (only for logged-in users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user #set author automatically
        return super().form_valid(form)


# Update an existing post (only for author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete a post (only for author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    #edit your own comment
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'


    def get_success_url(self):
        #after editing go back to the post the comment belongs to
        return self.object.post.get_absolute_url()
    
    def test_func(self):
        #only the author of the comment can edit it
        return self.request.user == self.get_object().author
    


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
        #delete your own comment (with confirmation)
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'


    def get_success_url(self):
        return self.object.post.get_absolute_url()
        
    def test_func(self):
            #only the author of the comment can edit it
        return self.request.user == self.get_object().author
        


class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Handles creating a new comment.
    Requires the user to be logged in (LoginRequiredMixin).
    """
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        """
        Before saving the comment:
        - Attach the post being commented on (from URL pk).
        - Attach the currently logged-in user as the author.
        """
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        After successfully creating a comment,
        redirect back to the post detail page.
        """
        return self.object.post.get_absolute_url()


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Handles updating an existing comment.
    Only the comment author can edit it.
    """
    model = Comment
    form_class = CommentForm

    def test_func(self):
        """
        Check that the logged-in user is the author of the comment.
        If not, they can’t edit.
        """
        return self.request.user == self.get_object().author

    def get_success_url(self):
        """
        After updating, redirect back to the post detail page.
        """
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Handles deleting a comment.
    Only the comment author can delete it.
    """
    model = Comment

    def test_func(self):
        """
        Check that the logged-in user is the author of the comment.
        If not, they can’t delete.
        """
        return self.request.user == self.get_object().author

    def get_success_url(self):
        """
        After deleting, redirect back to the post detail page.
        """
        return self.object.post.get_absolute_url()

   