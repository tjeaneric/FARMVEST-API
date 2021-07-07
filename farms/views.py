from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import FarmSerializer
from .models import Farm
from rest_framework import viewsets, generics, mixins


# Create your views here.


class FarmAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
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


# class FarmViewSet(viewsets.ModelViewSet):
#     serializer_class = FarmSerializer
#     queryset = Farm.objects.all()
