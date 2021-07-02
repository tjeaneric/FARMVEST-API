from rest_framework import generics 
from .serializer import TransactionSerializer
from .models import Transaction
from django.shortcuts import get_object_or_404

class TransactionPostView(generics.CreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionGetDetailView(generics.RetrieveAPIView):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # def get_object(self):
    #     pk = self.kwargs['id']
        # return get_object_or_404(User, id=id)

class AllTransaction(generics.ListAPIView):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # paginate_by =None

class DeleteTransactionView(generics.DestroyAPIView):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
# Create your views here.
