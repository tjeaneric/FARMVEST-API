from django.urls import path
from .views import InvestmentPostView,InvestmentUpdateView,InvestmentGetDetailView,AllInvestment,DeleteInvestmentView


urlpatterns = [
    path('create/', InvestmentPostView.as_view(),name='create-Investment'),
    path('<int:pk>/', InvestmentGetDetailView.as_view(), name='Investment-details'),
    path('update/<int:pk>/', InvestmentUpdateView.as_view(), name='update_Investment'),
    path('delete/<int:pk>/', DeleteInvestmentView.as_view(), name='Delete_Investment'),
    path('all_Investments/', AllInvestment.as_view(), name ='allInvestments')
]
