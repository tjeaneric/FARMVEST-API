from rest_framework import generics 
from .serializer import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404


class UserPostView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGetDetailView(generics.RetrieveAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.RetrieveUpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get_object(self):
    #     pk = self.kwargs['id']
        # return get_object_or_404(User, id=id)

class AllUser(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # paginate_by =None

class DeleteUserView(generics.DestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer