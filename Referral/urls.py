from django.urls import path
from .views import ReferralPostView,ReferralUpdateView,ReferralGetDetailView,AllReferral,DeleteReferralView


urlpatterns = [
    path('create/', ReferralPostView.as_view(),name='create-Referral'),
    path('<int:pk>/', ReferralGetDetailView.as_view(), name='Referral-details'),
    path('update/<int:pk>/', ReferralUpdateView.as_view(), name='update_Referral'),
    path('delete/<int:pk>/', DeleteReferralView.as_view(), name='Delete_Referral'),
    path('all_Referral/', AllReferral.as_view(), name ='allReferral')