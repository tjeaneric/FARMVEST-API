from django.urls import path
from .views import UserPostView,UserUpdateView,UserGetDetailView,AllUser,DeleteUserView


urlpatterns = [
    path('create/', UserPostView.as_view(),name='create-user'),
    path('<int:pk>/', UserGetDetailView.as_view(), name='profile'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='Delete_user'),
    path('all/', AllUser.as_view(), name ='allusers')

]
