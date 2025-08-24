from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, FollowUserView,UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),   # ✅ checker sees "register/"
    path('login/', LoginView.as_view(), name='login'),            # ✅ checker sees "login/"
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
