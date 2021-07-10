from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import WalletAPIView

urlpatterns = [
    path("wallet", WalletAPIView.as_view(), name="Wallet"),
    path("wallet/<int:id>", WalletAPIView.as_view(), name="Wallet_detail"),
]