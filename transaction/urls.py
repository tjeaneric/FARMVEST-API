from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TransactionAPIView

urlpatterns = [
    path("transaction", TransactionAPIView.as_view(), name="Transactions"),
    path("transaction/<int:id>", TransactionAPIView.as_view(), name="Transaction_detail"),
]