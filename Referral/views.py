from rest_framework import generics 
from .serializer import ReferralSerializer
from .models import Referral
from django.shortcuts import get_object_or_404

# Create your views here.

class ReferralPostView(generics.CreateAPIView):

    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class ReferralGetDetailView(generics.RetrieveAPIView):
    
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

class ReferralUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

    # def get_object(self):
    #     pk = self.kwargs['id']
        # return get_object_or_404(User, id=id)

class AllReferral(generics.ListAPIView):
    
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer
    # paginate_by =None

class DeleteReferralView(generics.DestroyAPIView):
    
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer