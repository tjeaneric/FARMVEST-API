from django.urls import path
from .views import ReferralAPIView


urlpatterns = [
    path("referrals", ReferralAPIView.as_view(), name="referrals"),
    path("referrals/<int:id>", ReferralAPIView.as_view(), name="referral_detail"),
]
