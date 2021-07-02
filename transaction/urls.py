from django.urls import path
from .views import TransactionPostView,TransactionUpdateView,TransactionGetDetailView,AllTransaction,DeleteTransactionView


urlpatterns = [
    path('create_transactions/', TransactionPostView.as_view(),name='create-Transaction'),
    path('transaction_details<int:pk>/', TransactionGetDetailView.as_view(), name='Transaction-details'),
    path('update_transaction/<int:pk>/', TransactionUpdateView.as_view(), name='update_Transaction'),
    path('delete_transaction/<int:pk>/', DeleteTransactionView.as_view(), name='Delete_Transaction'),
    path('all_transactions/', AllTransaction.as_view(), name ='allTransactions')
]