from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import CustomUser



class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





class RegisterView(APIView):
    def post(self, request):
        return Response({"message": "Register endpoint"})

class LoginView(APIView):
    def post(self, request):
        return Response({"message": "Login endpoint"})

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "User profile endpoint"})



# accounts/views.py


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)

        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
