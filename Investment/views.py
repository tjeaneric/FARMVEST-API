from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import InvestmentSerializer
from .models import Investment
from django.shortcuts import get_object_or_404


class InvestmentAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = "id"

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
