from django.urls import path
from .views import WalletPostView,WalletUpdateView,WalletGetDetailView,AllWallet,DeleteWalletView


urlpatterns = [
    path('create_transactions/', WalletPostView.as_view(),name='your_wallet'),
    path('transaction_details<int:pk>/', WalletGetDetailView.as_view(), name='wallet_details'),
    path('update_transaction/<int:pk>/', WalletUpdateView.as_view(), name='update_wallet'),
    #path('delete_wallet/<int:pk>/', DeleteWalletView.as_view(), name='Delete_Wallet'),
    path('all_wallet/', AllWallet.as_view(), name ='allwallet')
]