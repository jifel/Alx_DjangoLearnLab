from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


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

