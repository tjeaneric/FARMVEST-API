from django.urls import path
from .views import InvestmentAPIView


urlpatterns = [
    path("investments", InvestmentAPIView.as_view(), name="investments"),
    path("investments/<int:id>", InvestmentAPIView.as_view(), name="investment_detail"),
]
