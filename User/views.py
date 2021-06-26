from rest_framework import generics 
from .serializer import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404


class UserPostRequest(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGetDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AllUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer