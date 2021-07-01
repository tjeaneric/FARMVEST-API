from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

routes = DefaultRouter(trailing_slash=False)
routes.register("farm", views.FarmViewSet)

urlpatterns = [path("", include(routes.urls))]
