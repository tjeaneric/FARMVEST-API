from django.urls import path
from .views import UserPostRequest,UserGetDetail,AllUser


urlpatterns = [
    path('create/', UserPostRequest.as_view(),name='create-user'),
    path('<int:pk>/', UserGetDetail.as_view(), name='profile'),
    path('all/', AllUser.as_view(), name ='allusers')

]
