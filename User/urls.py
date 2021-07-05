from django.urls import path, include
from .views import UserAPIView, AuthenticationViewSet
from rest_framework.routers import DefaultRouter

routes = DefaultRouter(trailing_slash=False)

routes.register("authentication", AuthenticationViewSet, basename="authentication")


urlpatterns = [
    path("user/all", UserAPIView.as_view(), name="users"),
    path("user/<int:id>", UserAPIView.as_view(), name="user_detail"),
    path("", include(routes.urls)),
]
