from rest_framework import serializers
from .models import Farm
from django_countries.serializers import CountryFieldMixin


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = "__all__"
