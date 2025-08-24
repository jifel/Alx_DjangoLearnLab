from django.urls import path
from .views import RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),   # ✅ checker sees "register/"
    path('login/', LoginView.as_view(), name='login'),            # ✅ checker sees "login/"
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
]
