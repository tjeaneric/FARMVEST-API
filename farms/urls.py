from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import FarmAPIView

urlpatterns = [
    path("farms", FarmAPIView.as_view(), name="farm"),
    path("farms/<int:id>", FarmAPIView.as_view(), name="farm_detail"),
]
# routes = DefaultRouter(trailing_slash=False)
# routes.register("farm", views.FarmViewSet)
#
# urlpatterns = [path("", include(routes.urls))]
