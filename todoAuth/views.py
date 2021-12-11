from django.shortcuts import render
from .serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TokenObtainPairSerializer
from django.contrib import auth

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# class Logout(APIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         token = TokenObtainPairSerializer.get_token(request.user)
#         token['username'] = request.user.username
#
#         return Response(status=status.HTTP_200_OK)