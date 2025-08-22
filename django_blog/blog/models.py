from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):

        """
        Returns the canonical URL for this Post instance.
        Django uses this to know where the "detail page" of the object is.
        """
    # Import reverse here (instead of at the top of the file) 
    # to avoid circular import issues with urls.py
        from django.urls import reverse


    # Use reverse() to look up the URL pattern named 'post-detail'
    # and pass the current object's id as the argument.
    # Example: if self.id = 7 and the URL pattern is:
    # path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail')
    # This will return "/posts/7/"
        return reverse('post-detail', args=[str(self.id)])



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True) #set once, when created
    updated_at = models.DateTimeField(auto_now= True) #auto-update on save


    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"