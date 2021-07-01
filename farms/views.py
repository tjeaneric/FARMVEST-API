from django.shortcuts import render
from .serializer import FarmSerializer
from .models import Farm
from rest_framework import viewsets

# Create your views here.


class FarmViewSet(viewsets.ModelViewSet):
    serializer_class = FarmSerializer
    queryset = Farm.objects.all()
