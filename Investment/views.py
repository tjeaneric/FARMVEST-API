from rest_framework import generics 
from .serializer import InvestmentSerializer
from .models import Investment
from django.shortcuts import get_object_or_404

# Create your views here.


class InvestmentPostView(generics.CreateAPIView):

    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentGetDetailView(generics.RetrieveAPIView):
    
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    # def get_object(self):
    #     pk = self.kwargs['id']
        # return get_object_or_404(User, id=id)

class AllInvestment(generics.ListAPIView):
    
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    # paginate_by =None

class DeleteInvestmentView(generics.DestroyAPIView):
    
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer