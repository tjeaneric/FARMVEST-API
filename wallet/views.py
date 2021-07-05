from rest_framework import generics 
from .serializer import WalletSerializer
from .models import Wallet
from django.shortcuts import get_object_or_404

class WalletPostView(generics.CreateAPIView):

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletGetDetailView(generics.RetrieveAPIView):
    
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    # def get_object(self):
    #     pk = self.kwargs['id']
        # return get_object_or_404(User, id=id)

class AllWallet(generics.ListAPIView):
    
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    # paginate_by =None

class DeleteWalletView(generics.DestroyAPIView):
    
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
# Create your views here.




